#!/usr/bin/env python3
"""
SAP S/4HANA Scoping Agent — Pipeline Orchestrator

Chains the five skills sequentially via the Claude Messages API,
persisting typed state to JSON after each step for resumability.

Architecture decisions:
  - Progressive disclosure: each skill's full prompt is loaded only when
    its step runs, not all at once. See DECISIONS.md §1.
  - The scope-item lookup tool is available to Skills 02 and 03 via
    Claude's tool-use capability.
  - A human-approval gate pauses before Skill 04 (executive proposal)
    so the user can review the module fit and roadmap before committing
    to proposal generation.

Usage:
    python orchestrator.py --input benchmarks/scenario-a-agribusiness/input.md
    python orchestrator.py --resume state/run-20260816T120000.json  # resume from step 3
    python orchestrator.py --input input.md --step 2                # run only step 2

Environment:
    ANTHROPIC_API_KEY  — required
    MODEL_ID           — optional (default: claude-sonnet-4-20250514)

Output:
    state/<run-id>.json            — persisted pipeline state
    state/<run-id>-skill-01.json   — Skill 01 output
    state/<run-id>-skill-02.json   — Skill 02 output
    state/<run-id>-skill-03.json   — Skill 03 output
    state/<run-id>-skill-04.md     — Skill 04 output (narrative proposal)
    state/<run-id>-metrics.json    — per-step token/latency/cost log
"""

import argparse
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import anthropic

# ── Configuration ──────────────────────────────────────────

# Use Bedrock model IDs when AWS credentials are present, direct API otherwise.
# Override with MODEL_ID env var for either backend.
_USE_BEDROCK = bool(os.environ.get("AWS_ACCESS_KEY_ID")) and not os.environ.get("ANTHROPIC_API_KEY")
_DEFAULT_MODEL = "us.anthropic.claude-sonnet-4-6" if _USE_BEDROCK else "claude-sonnet-4-20250514"
MODEL_ID = os.environ.get("MODEL_ID", _DEFAULT_MODEL)

# Tool-use round cap for call_claude_with_retry(). Was 5, hardcoded
# inline. Found (DECISIONS.md #15) when Step 4's confidence/trace
# instrumentation exposed that Skills 02/03 had been silently producing
# EMPTY text on most runs across an entire session: the loop exited with
# stop_reason still "tool_use", leaving a response with no text block.
#
# Critically, raising this number is NOT what fixed that bug -- measured
# directly: at 20 rounds the model made 123 tool calls, cost $2.45 for a
# single skill, and STILL returned empty text, because on this task the
# model never self-terminates; it always wants another lookup. The actual
# fix is the forced-synthesis fallback in call_claude_with_retry(), which
# guarantees real text at ANY cap value.
#
# So this constant is now purely a cost/thoroughness dial, not a
# correctness threshold. Measured data points, both with the fallback
# working: 2 rounds -> 16 tool calls, $0.69, a complete 72k-char analysis;
# 20 rounds -> 123 tool calls, $2.45 (3.7x the cost of the original 5-round
# setting). 8 is a deliberate middle ground -- real headroom over the
# original 5, well short of the 123-call pathology -- and is NOT
# empirically optimized: no A/B eval across cap values has been run, so
# treat it as a reasonable default, not a tuned one.
_MAX_TOOL_ROUNDS = 8

SKILLS_DIR = Path(__file__).parent / "skills"
STATE_DIR = Path(__file__).parent / "state"

# Approximate per-token costs (USD) for cost logging
# Update these when changing models
TOKEN_COSTS = {
    "claude-sonnet-4-20250514": {"input": 3.0 / 1_000_000, "output": 15.0 / 1_000_000},
    "claude-sonnet-5-20260101": {"input": 3.0 / 1_000_000, "output": 15.0 / 1_000_000},
    "us.anthropic.claude-sonnet-4-6": {"input": 3.0 / 1_000_000, "output": 15.0 / 1_000_000},
}

SKILLS = [
    {"id": "01", "name": "Client Discovery Intake", "file": "01-client-discovery-intake.md", "max_tokens": 16384},
    {"id": "02", "name": "Module Fit Analyzer", "file": "02-module-fit-analyzer.md", "max_tokens": 16384},
    {"id": "03", "name": "Implementation Roadmap", "file": "03-implementation-roadmap.md", "max_tokens": 16384},
    {"id": "04", "name": "Executive Proposal Drafter", "file": "04-executive-proposal-drafter.md", "max_tokens": 16384, "gate": True},
]


# ── Config validation (Step 3, interview-prep rigor pass) ─────

def validate_skill_config(skills: list[dict], field: str = "max_tokens", outlier_ratio: float = 0.5) -> None:
    """Startup guardrail: flag any SKILLS entry whose `field` value sits
    far outside its siblings' values, BEFORE any API call is made. This
    is the check that would have caught the real, shipped Skill 01
    max_tokens=8192-vs-16384 bug (see DECISIONS.md #10) automatically --
    instead of it running silently truncated on every one of 6 runs
    until someone happened to read a raw output file by hand.

    DESIGN DECISION, stated here rather than left implicit: this FAILS
    (raises), it does not just print a warning and continue. A printed
    warning is easy to miss in scrolling terminal output -- that is, in
    fact, exactly what already happened once with the real bug this
    guardrail targets: the truncation produced silently wrong output on
    every single run for an unknown period, and nothing in the harness
    itself ever surfaced it. This check runs at startup, before any API
    call, so failing costs nothing (zero wasted spend, zero wasted time)
    and forces a deliberate decision instead of a scroll-past-able line.
    An escape hatch exists (env var ALLOW_CONFIG_OUTLIERS=1) for a
    genuinely intentional per-skill difference, so this is a locked door
    with a key, not a wall -- but the default is fail-closed.

    field: which per-skill config key to check. Only "max_tokens" is
    wired into run_pipeline() today, but the parameter and the comparison
    logic below are generic (any numeric per-skill value works) so a
    future field doesn't need a second copy of this function.
    outlier_ratio: an entry's value is flagged if it is at or below
    outlier_ratio * max(all values in the group). 0.5 is a deliberate,
    literal match to the shape of the real bug this guardrail exists to
    catch (8192 is exactly half of 16384) -- not a value derived from any
    independent statistical reasoning, an intentional match to the known
    failure case.
    """
    entries = [(s["id"], s["name"], s.get(field)) for s in skills]
    numeric = [(sid, name, val) for sid, name, val in entries if isinstance(val, (int, float))]
    if len(numeric) < 2:
        return  # nothing to compare an outlier against

    group_max = max(val for _sid, _name, val in numeric)
    # <= not <: the real bug this guardrail targets (8192 vs 16384) sits
    # EXACTLY on the ratio boundary (8192 / 16384 == 0.5). A strict "<"
    # comparison would silently exclude the one concrete case this check
    # exists to catch -- caught by testing against that exact historical
    # value before trusting this function, not by reasoning about it.
    outliers = [(sid, name, val) for sid, name, val in numeric if val <= outlier_ratio * group_max]
    if not outliers:
        return

    lines = [
        f"CONFIG VALIDATION FAILED: {len(outliers)} of {len(numeric)} skill(s) have "
        f"'{field}' at or below {outlier_ratio:.0%} of the group max ({group_max}), "
        f"caught BEFORE any API call was made:",
    ]
    for sid, name, val in outliers:
        lines.append(f"  - Skill {sid} ({name}): {field}={val}  (group max={group_max}, ratio={val / group_max:.2f})")
    lines.append(
        "This is the exact shape of a real bug that shipped before: Skill 01 at "
        "max_tokens=8192 while Skills 02-04 used 16384 (DECISIONS.md #10), which "
        "silently truncated output on every run until caught by hand. Fix the "
        "outlier, or set ALLOW_CONFIG_OUTLIERS=1 if this difference is genuinely "
        "intentional."
    )
    message = "\n".join(lines)

    if os.environ.get("ALLOW_CONFIG_OUTLIERS") == "1":
        print(f"WARNING (ALLOW_CONFIG_OUTLIERS=1 set, proceeding anyway):\n{message}", file=sys.stderr)
        return

    raise ValueError(message)


# ── Scope Item Lookup Tool ─────────────────────────────────

# A curated subset of SAP S/4HANA scope items relevant to common
# mid-market implementations. The same catalogue is exposed as an
# MCP server in mcp_server.py (stdio transport, MCP SDK v2.0).
# In production, both this tool and the MCP server would front
# SAP's Best Practice Explorer API.

SCOPE_ITEMS = {
    "1YB": {"name": "General Ledger Accounting", "module": "FI", "area": "Finance", "edition": "Cloud/OP"},
    "2WB": {"name": "Accounts Payable", "module": "FI-AP", "area": "Finance", "edition": "Cloud/OP"},
    "1F7": {"name": "Accounts Receivable", "module": "FI-AR", "area": "Finance", "edition": "Cloud/OP"},
    "4GR": {"name": "Asset Accounting", "module": "FI-AA", "area": "Finance", "edition": "Cloud/OP"},
    "1NZ": {"name": "Bank Account Management", "module": "FI", "area": "Finance", "edition": "Cloud/OP"},
    "J58": {"name": "Cost Center Accounting", "module": "CO", "area": "Controlling", "edition": "Cloud/OP"},
    "1SO": {"name": "Profitability Analysis", "module": "CO-PA", "area": "Controlling", "edition": "Cloud/OP"},
    "BMD": {"name": "Purchase Order Processing", "module": "MM", "area": "Procurement", "edition": "Cloud/OP"},
    "2NM": {"name": "Supplier Evaluation", "module": "MM", "area": "Procurement", "edition": "Cloud/OP"},
    "BD2": {"name": "Sales Order Management", "module": "SD", "area": "Sales", "edition": "Cloud/OP"},
    "BKP": {"name": "Billing and Invoicing", "module": "SD", "area": "Sales", "edition": "Cloud/OP"},
    "1E6": {"name": "Foreign Trade / Export", "module": "GTS", "area": "Trade Compliance", "edition": "OP"},
    "3EN": {"name": "Batch Management", "module": "MM/PP", "area": "Logistics", "edition": "Cloud/OP"},
    "2QH": {"name": "Quality Inspection", "module": "QM", "area": "Quality", "edition": "Cloud/OP"},
    "1YW": {"name": "Warehouse Management", "module": "EWM", "area": "Logistics", "edition": "Cloud/OP"},
    "4DV": {"name": "Production Planning", "module": "PP", "area": "Manufacturing", "edition": "Cloud/OP"},
    "2V4": {"name": "Material Requirements Planning", "module": "PP-MRP", "area": "Manufacturing", "edition": "Cloud/OP"},
    "1O3": {"name": "Plant Maintenance", "module": "PM", "area": "Asset Management", "edition": "Cloud/OP"},
    "BJ0": {"name": "Predictive Maintenance", "module": "PM", "area": "Asset Management", "edition": "Cloud"},
    "3OP": {"name": "Integration with SAP Analytics Cloud", "module": "BTP", "area": "Analytics", "edition": "Cloud"},
}

SCOPE_ITEM_TOOL = {
    "name": "lookup_scope_items",
    "description": (
        "Look up SAP S/4HANA best practice scope items by module code, functional area, "
        "or keyword. Returns scope item IDs, names, modules, and deployment editions. "
        "Use this to ground module recommendations in SAP's official scope item catalogue."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "Search term: module code (e.g., 'FI', 'MM'), area (e.g., 'Finance'), or keyword (e.g., 'batch', 'export')",
            },
        },
        "required": ["query"],
    },
}


def search_scope_items(query: str) -> list[dict]:
    """Search scope items by module, area, or keyword."""
    q = query.lower()
    results = []
    for item_id, item in SCOPE_ITEMS.items():
        if (
            q in item["module"].lower()
            or q in item["area"].lower()
            or q in item["name"].lower()
            or q in item_id.lower()
        ):
            results.append({"id": item_id, **item})
    return results


# ── Pipeline State ─────────────────────────────────────────

class PipelineState:
    """Typed state object persisted to JSON after each step."""

    def __init__(self, run_id: str, input_text: str):
        self.run_id = run_id
        self.input_text = input_text
        self.completed_steps: list[str] = []
        self.outputs: dict[str, Any] = {}
        self.metrics: list[dict] = []

    def to_dict(self) -> dict:
        return {
            "run_id": self.run_id,
            "input_text": self.input_text,
            "completed_steps": self.completed_steps,
            "outputs": self.outputs,
            "metrics": self.metrics,
        }

    @classmethod
    def from_dict(cls, d: dict) -> "PipelineState":
        state = cls(d["run_id"], d["input_text"])
        state.completed_steps = d.get("completed_steps", [])
        state.outputs = d.get("outputs", {})
        state.metrics = d.get("metrics", [])
        return state

    def save(self):
        STATE_DIR.mkdir(exist_ok=True)
        path = STATE_DIR / f"{self.run_id}.json"
        with open(path, "w") as f:
            json.dump(self.to_dict(), f, indent=2)
        return path


# ── Skill Execution ────────────────────────────────────────

def load_skill_prompt(skill_file: str) -> str:
    """Load a skill's full prompt from its Markdown file."""
    path = SKILLS_DIR / skill_file
    if not path.exists():
        raise FileNotFoundError(f"Skill file not found: {path}")
    return path.read_text()


def _upstream_skills_for(skill_id: str) -> list[str]:
    """Single source of truth for which prior skills' outputs feed into a
    given skill's prompt. Used both to assemble the prompt
    (build_user_message) and to record it explicitly in the trace field
    (Step 4, interview-prep rigor pass) -- one function, not two
    hand-maintained copies of the same dependency list that could drift
    apart.
    """
    return {"01": [], "02": ["01"], "03": ["01", "02"], "04": ["01", "02", "03"]}.get(skill_id, [])


def _skill_output_text(output: Any) -> str:
    """Extract the actual generated text from a skill's stored output.

    state.outputs[skill_id] changed shape in Step 4 (interview-prep rigor
    pass): it used to be a bare string, and is now
    {"text": ..., "confidence": {...}, "trace": {...}}. This accessor
    handles BOTH shapes, so state/*.json files saved before this change
    keep working (isinstance check, not a hard assumption about which
    format is on disk) rather than breaking on load.
    """
    return output["text"] if isinstance(output, dict) else output


_SKILL_OUTPUT_LABELS = {"01": "Discovery Brief", "02": "Module Fit Analysis", "03": "Implementation Roadmap"}


def build_user_message(skill_id: str, state: PipelineState) -> str:
    """Build the user message for a skill step, including prior outputs."""
    if skill_id == "01":
        return f"## Client Brief\n\n{state.input_text}"

    parts = [f"## Client Brief\n\n{state.input_text}"]
    for upstream_id in _upstream_skills_for(skill_id):
        if upstream_id in state.outputs:
            label = _SKILL_OUTPUT_LABELS[upstream_id]
            text = _skill_output_text(state.outputs[upstream_id])
            parts.append(f"\n\n## Skill {upstream_id} Output: {label}\n\n{text}")

    return "\n".join(parts)


def call_claude_with_retry(
    client: anthropic.Anthropic,
    system: str,
    user_message: str,
    max_tokens: int,
    tools: list[dict] | None = None,
    max_retries: int = 3,
) -> tuple[str, dict]:
    """
    Call Claude with exponential backoff retry. Handles tool-use loops.
    Returns (response_text, metrics_dict). metrics_dict["tool_call_log"]
    (Step 4, interview-prep rigor pass) is the actual query/result-count
    for every tool call made, not just a count -- this already existed
    implicitly (the query and the result were both computed to build the
    next message) but was discarded once the loop moved on; now it's
    captured and returned instead of only ever being visible in a live
    terminal's scrollback.
    """
    t0 = time.monotonic()
    total_input_tokens = 0
    total_output_tokens = 0
    tool_calls = 0
    tool_call_log: list[dict] = []

    messages = [{"role": "user", "content": user_message}]

    for attempt in range(max_retries):
        try:
            kwargs: dict[str, Any] = {
                "model": MODEL_ID,
                "max_tokens": max_tokens,
                "system": system,
                "messages": messages,
            }
            if tools:
                kwargs["tools"] = tools

            response = client.messages.create(**kwargs)
            total_input_tokens += response.usage.input_tokens
            total_output_tokens += response.usage.output_tokens

            # Handle tool use loop
            max_tool_rounds = _MAX_TOOL_ROUNDS
            while response.stop_reason == "tool_use" and max_tool_rounds > 0:
                max_tool_rounds -= 1
                tool_results = []

                for block in response.content:
                    if block.type == "tool_use" and block.name == "lookup_scope_items":
                        tool_calls += 1
                        results = search_scope_items(block.input["query"])
                        tool_call_log.append({
                            "tool": "lookup_scope_items",
                            "query": block.input["query"],
                            "result_count": len(results),
                            "result_ids": [r["id"] for r in results][:10],  # capped, not a full data dump
                        })
                        tool_results.append({
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": json.dumps(results) if results else json.dumps({"message": "No matching scope items found", "query": block.input["query"]}),
                        })

                if not tool_results:
                    break

                messages = [
                    {"role": "user", "content": user_message},
                    {"role": "assistant", "content": [b.model_dump() for b in response.content]},
                    {"role": "user", "content": tool_results},
                ]

                response = client.messages.create(**kwargs | {"messages": messages})
                total_input_tokens += response.usage.input_tokens
                total_output_tokens += response.usage.output_tokens

            # Real, previously-silent bug (DECISIONS.md #15): if the loop
            # above exits with response.stop_reason STILL "tool_use" --
            # either the round budget ran out while the model still
            # wanted to call tools, or a defensive edge case left
            # tool_results empty -- `response.content` holds ONLY
            # tool_use blocks and zero text blocks. The extraction below
            # would then silently produce "" from a response the model
            # never got to finish, and nothing before this fix ever
            # noticed. Structural fix, not just a bigger round cap (which
            # could someday be exhausted again): answer whatever tool_use
            # blocks are pending for real, then make ONE final call with
            # `tools` removed from the request -- the API cannot return
            # another tool_use turn with no tools offered, so this call
            # is guaranteed to return text.
            if response.stop_reason == "tool_use":
                print(
                    f"    WARNING: tool-use round budget ({_MAX_TOOL_ROUNDS} rounds) exhausted "
                    "while the model still wanted to call tools -- forcing a final "
                    "text-only synthesis call so this does not silently return empty text."
                )
                pending_tool_results = []
                for block in response.content:
                    if block.type == "tool_use" and block.name == "lookup_scope_items":
                        tool_calls += 1
                        results = search_scope_items(block.input["query"])
                        tool_call_log.append({
                            "tool": "lookup_scope_items",
                            "query": block.input["query"],
                            "result_count": len(results),
                            "result_ids": [r["id"] for r in results][:10],
                        })
                        pending_tool_results.append({
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": json.dumps(results) if results else json.dumps({"message": "No matching scope items found", "query": block.input["query"]}),
                        })
                # Removing `tools` alone is NOT sufficient, verified against
                # the real API: a first version of this fallback did exactly
                # that and the model returned stop_reason='end_turn' with
                # ZERO content blocks and 8 output tokens -- a genuinely
                # empty response. Cutting a mid-task model off from its tools
                # without telling it what to do instead leaves it with no
                # directive, and it produces nothing. The explicit
                # stop-and-synthesize instruction below is the part that
                # actually makes this work. Appended as a text block in the
                # same user turn as the tool_results (rather than a second
                # consecutive user message, which the API does not accept).
                _SYNTHESIS_INSTRUCTION = (
                    "You have now used all available tool-lookup rounds for this step. "
                    "Do not request any further tool calls -- no tools are available on this turn. "
                    "Using only the information already gathered above, write your complete "
                    "final response for this skill now, in full, following the output format "
                    "specified in your instructions. If some lookups returned no match, state "
                    "that plainly in your output rather than omitting the item or inventing a value."
                )
                if pending_tool_results:
                    synthesis_turn = pending_tool_results + [{"type": "text", "text": _SYNTHESIS_INSTRUCTION}]
                    messages = [
                        {"role": "user", "content": user_message},
                        {"role": "assistant", "content": [b.model_dump() for b in response.content]},
                        {"role": "user", "content": synthesis_turn},
                    ]
                else:
                    # No pending tool_use blocks to answer (defensive edge
                    # case): still must not send the model into a turn with
                    # no directive, so append the instruction to whatever
                    # message list the loop left behind.
                    messages = list(messages) + [{"role": "user", "content": _SYNTHESIS_INSTRUCTION}]
                synthesis_kwargs = {k: v for k, v in kwargs.items() if k != "tools"}
                synthesis_kwargs["messages"] = messages
                response = client.messages.create(**synthesis_kwargs)
                total_input_tokens += response.usage.input_tokens
                total_output_tokens += response.usage.output_tokens

            # Extract text
            text = "\n".join(b.text for b in response.content if b.type == "text")

            # Empty text is ALWAYS a defect, never a valid result -- this is
            # the exact failure that went unnoticed across an entire session
            # (DECISIONS.md #15): a skill billed real tokens and returned "",
            # and nothing anywhere said so. Never silently return it: surface
            # what the response actually contained so the next person gets a
            # diagnosis instead of a mystery.
            if not text.strip():
                print(
                    f"    ERROR: model returned NO text. "
                    f"stop_reason={response.stop_reason!r}, "
                    f"block types={[b.type for b in response.content]}, "
                    f"output_tokens={response.usage.output_tokens}. "
                    f"This skill's output would be empty -- treating as a failure, not a result."
                )

            latency_ms = (time.monotonic() - t0) * 1000
            costs = TOKEN_COSTS.get(MODEL_ID, {"input": 3e-6, "output": 15e-6})
            cost_usd = total_input_tokens * costs["input"] + total_output_tokens * costs["output"]

            metrics = {
                "input_tokens": total_input_tokens,
                "output_tokens": total_output_tokens,
                # The single final call that actually produced `text` --
                # the only one truncation can affect. Distinct from the
                # cumulative total above, which sums the whole tool-use
                # loop. _estimate_confidence() needs this one.
                "final_output_tokens": response.usage.output_tokens,
                "final_stop_reason": response.stop_reason,
                "latency_ms": round(latency_ms),
                "cost_usd": round(cost_usd, 4),
                "tool_calls": tool_calls,
                "retries": attempt,
                "tool_call_log": tool_call_log,
            }

            return text, metrics

        except anthropic.RateLimitError:
            wait = 2 ** (attempt + 1)
            print(f"    Rate limited, waiting {wait}s...")
            time.sleep(wait)
        except anthropic.APIError as e:
            if attempt == max_retries - 1:
                raise
            wait = 2 ** (attempt + 1)
            print(f"    API error ({e}), retrying in {wait}s...")
            time.sleep(wait)

    raise RuntimeError("Max retries exceeded")


# ── Confidence estimation (Step 4, interview-prep rigor pass) ─

def _estimate_confidence(skill_id: str, metrics: dict, max_tokens: int) -> dict:
    """Estimate a confidence level for one skill's output from OBJECTIVE
    signals available from its own execution -- never by asking the model
    to self-report a confidence score in its own generated text. An LLM's
    own stated confidence is well known to be poorly calibrated, and
    trusting it here would be exactly the kind of unverified claim this
    entire audit has been pushing back on everywhere else. Every input to
    this heuristic is something measured about the call, not something
    the model asserted about itself.

    THE HEURISTIC, IN ORDER (so it's not a black box -- read this before
    trusting a "low"/"medium"/"high" value):

    1. TRUNCATION PROXIMITY (applies to every skill, checked first and
       overrides everything else). If output_tokens lands within 5% of
       max_tokens, the output is plausibly truncated or rushed regardless
       of what it says -- this is a direct, deliberate callback to the
       real Skill 01 bug (DECISIONS.md #10): a skill silently hitting its
       ceiling is exactly the failure mode this project has already
       shipped once. Forces "low" no matter what else is true.
    2. TOOL-GROUNDING MATCH RATE (Skills 02/03 only, which are the only
       skills given the scope-item lookup tool). If the skill made tool
       calls, confidence is the fraction of those calls that returned at
       least one real scope-item match, not empty-handed fallback
       reasoning: >=80% match rate -> "high", >=40% -> "medium", below
       that -> "low". A skill that had the tool available but never
       called it at all is treated as "low" -- ungrounded by choice is
       not better than ungrounded by bad luck.
    3. NO SIGNAL AVAILABLE (Skills 01/04, which have no tool to ground
       against, when not near the token ceiling). Reported honestly as
       "medium" with a basis string that says plainly this reflects only
       "not truncated," not "independently verified" -- there is no
       real signal to call this "high," and calling it "low" with
       nothing wrong detected would be equally dishonest in the other
       direction.
    """
    # Use the FINAL response's output tokens, not the cumulative total.
    # metrics["output_tokens"] sums every call in the tool-use loop, so for
    # a tool-using skill it can exceed a per-call max_tokens ceiling and
    # make this check fire on runs that were never truncated. Caught on
    # this heuristic's first real run (Skill 02 reported "17377/16384",
    # comparing a cumulative total against a per-call cap -- the verdict
    # happened to be right, but the arithmetic was comparing two
    # different quantities). final_output_tokens is the single call that
    # actually produced `text`, which is the only one truncation can
    # affect. Falls back to the cumulative value only if the newer field
    # is absent (e.g. re-reading an older state file).
    output_tokens = metrics.get("final_output_tokens", metrics.get("output_tokens", 0))
    if max_tokens and output_tokens >= 0.95 * max_tokens:
        return {
            "level": "low",
            "basis": (
                f"final response landed at {output_tokens}/{max_tokens} tokens (within 5% of the "
                f"max_tokens ceiling) -- plausibly truncated, regardless of content"
            ),
        }

    tool_call_log = metrics.get("tool_call_log", [])
    if skill_id in ("02", "03"):
        if not tool_call_log:
            return {
                "level": "low",
                "basis": "scope-item lookup tool was available but never called -- output is not grounded in the catalogue at all",
            }
        matched = sum(1 for c in tool_call_log if c.get("result_count", 0) > 0)
        match_rate = matched / len(tool_call_log)
        if match_rate >= 0.8:
            level = "high"
        elif match_rate >= 0.4:
            level = "medium"
        else:
            level = "low"
        return {
            "level": level,
            "basis": f"{matched}/{len(tool_call_log)} scope-item lookups returned a real match ({match_rate:.0%})",
        }

    return {
        "level": "medium",
        "basis": "no tool-grounding signal available for this skill (Skill 01/04 are not given the scope-item tool); reflects only that output was not truncated, not that content was independently verified",
    }


# ── Human Approval Gate ────────────────────────────────────

def request_approval(state: PipelineState) -> bool:
    """
    Pause for human review before generating the executive proposal.
    In non-interactive mode (--no-gate), this is skipped.
    """
    print("\n" + "=" * 60)
    print("HUMAN APPROVAL GATE — Review before proposal generation")
    print("=" * 60)
    print(f"\nCompleted steps: {', '.join(f'Skill {s}' for s in state.completed_steps)}")
    print(f"State file: state/{state.run_id}.json")
    print("\nReview the module fit analysis (Skill 02) and roadmap (Skill 03)")
    print("outputs before proceeding to proposal generation.")

    while True:
        try:
            answer = input("\nProceed with proposal generation? [y/n/q]: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            return False
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no", "q", "quit"):
            return False
        print("Please enter 'y' to proceed or 'n' to stop.")


# ── Main Pipeline ──────────────────────────────────────────

def run_pipeline(
    input_text: str,
    resume_state: PipelineState | None = None,
    single_step: str | None = None,
    skip_gate: bool = False,
) -> PipelineState:
    """Execute the scoping pipeline end-to-end or from a resume point."""

    # Guardrail: catch a config outlier (e.g. the real, previously-shipped
    # Skill 01 max_tokens=8192-vs-16384 bug -- DECISIONS.md #10) before a
    # single API call is made, rather than after someone happens to
    # notice truncated output. See validate_skill_config()'s docstring
    # for why this fails rather than warns.
    validate_skill_config(SKILLS)

    client = (
        anthropic.AnthropicBedrock(aws_region=os.environ.get("AWS_DEFAULT_REGION", "us-east-1"))
        if _USE_BEDROCK
        else anthropic.Anthropic()
    )

    if resume_state:
        state = resume_state
        print(f"Resuming run {state.run_id} from step after {state.completed_steps[-1] if state.completed_steps else 'start'}")
    else:
        run_id = f"run-{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S')}"
        state = PipelineState(run_id, input_text)
        print(f"Starting new run: {state.run_id}")

    for skill in SKILLS:
        skill_id = skill["id"]

        # Skip completed steps (resume)
        if skill_id in state.completed_steps:
            print(f"\n  Skill {skill_id} ({skill['name']}): already completed, skipping")
            continue

        # Single-step mode
        if single_step and skill_id != single_step:
            continue

        # Human approval gate
        if skill.get("gate") and not skip_gate:
            if not request_approval(state):
                print("\nPipeline paused by user. Resume with:")
                saved = state.save()
                print(f"  python orchestrator.py --resume {saved}")
                return state

        print(f"\n  Skill {skill_id} ({skill['name']})")
        print(f"    Loading skill prompt from {skill['file']}...")

        # Progressive disclosure: load skill prompt only when needed
        skill_prompt = load_skill_prompt(skill["file"])
        user_message = build_user_message(skill_id, state)

        # Skills 02 and 03 get the scope-item lookup tool
        tools = [SCOPE_ITEM_TOOL] if skill_id in ("02", "03") else None

        print(f"    Calling Claude ({MODEL_ID})...")
        text, metrics = call_claude_with_retry(
            client,
            system=skill_prompt,
            user_message=user_message,
            max_tokens=skill["max_tokens"],
            tools=tools,
        )

        # tool_call_log belongs in this skill's trace, not the flat
        # numeric metrics log (state.metrics keeps its original
        # token/cost/latency-only shape -- pop it out here rather than
        # having the same data live in two places for no reason).
        tool_call_log = metrics.pop("tool_call_log", [])

        # Record results. Output is now a structured object -- text plus
        # a confidence estimate and an explainability trace (Step 4,
        # interview-prep rigor pass) -- not a bare string. See
        # _estimate_confidence()'s docstring for exactly how confidence
        # is set; it is never the model self-reporting on itself.
        state.outputs[skill_id] = {
            "text": text,
            "confidence": _estimate_confidence(skill_id, {**metrics, "tool_call_log": tool_call_log}, skill["max_tokens"]),
            "trace": {
                "upstream_skills": _upstream_skills_for(skill_id),
                "tool_calls": tool_call_log,
            },
        }
        state.completed_steps.append(skill_id)
        state.metrics.append({"skill": skill_id, "name": skill["name"], **metrics})

        # Persist after each step
        saved = state.save()

        # Save individual skill output
        ext = "md" if skill_id == "04" else "json"
        output_path = STATE_DIR / f"{state.run_id}-skill-{skill_id}.{ext}"
        output_path.write_text(text)

        print(f"    Done: {metrics['input_tokens']} in / {metrics['output_tokens']} out / "
              f"{metrics['latency_ms']}ms / ${metrics['cost_usd']:.4f} / "
              f"{metrics['tool_calls']} tool calls")
        print(f"    Output: {output_path}")

    # Save final metrics
    metrics_path = STATE_DIR / f"{state.run_id}-metrics.json"
    with open(metrics_path, "w") as f:
        json.dump(state.metrics, f, indent=2)

    print(f"\n  Pipeline complete. State: state/{state.run_id}.json")
    print(f"  Metrics: {metrics_path}")

    total_cost = sum(m["cost_usd"] for m in state.metrics)
    total_tokens = sum(m["input_tokens"] + m["output_tokens"] for m in state.metrics)
    print(f"  Total: {total_tokens:,} tokens, ${total_cost:.4f}")

    return state


# ── CLI ────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="SAP S/4HANA Scoping Agent — Pipeline Orchestrator"
    )
    parser.add_argument(
        "--input", type=str, help="Path to client brief (Markdown file)"
    )
    parser.add_argument(
        "--resume", type=str, help="Path to a saved state JSON to resume from"
    )
    parser.add_argument(
        "--step", type=str, choices=["01", "02", "03", "04"],
        help="Run only a specific skill step"
    )
    parser.add_argument(
        "--no-gate", action="store_true",
        help="Skip the human approval gate before proposal generation"
    )
    args = parser.parse_args()

    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("Error: ANTHROPIC_API_KEY must be set.", file=sys.stderr)
        sys.exit(1)

    if args.resume:
        with open(args.resume) as f:
            state = PipelineState.from_dict(json.load(f))
        run_pipeline(state.input_text, resume_state=state, single_step=args.step, skip_gate=args.no_gate)
    elif args.input:
        input_text = Path(args.input).read_text()
        run_pipeline(input_text, single_step=args.step, skip_gate=args.no_gate)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
