# Architectural Decisions

Non-obvious choices in this codebase, with rationale.

---

## 1. Progressive disclosure vs. monolithic context

**Chosen:** Each skill's full prompt (~50–80KB of Markdown) is loaded into the
system prompt only when that step runs. Prior steps' *outputs* are passed in the
user message; prior steps' *prompts* are not.

**Rejected:** Loading all four skill prompts into a single system prompt and
asking the model to execute them sequentially in one pass.

**Why:** The five skill files total ~340KB / ~4,800 lines. Loading them all at
once would:

1. **Saturate the context window.** With four skill prompts plus a detailed
   client brief, the combined system prompt alone would consume 80–100K tokens,
   leaving little room for generation and making the model more likely to
   lose track of task-specific instructions buried in the middle.

2. **Prevent targeted cost control.** Skills 01 and 04 need different max_tokens
   limits and different tool configurations. Progressive loading lets each step
   use exactly the context it needs.

3. **Break resumability.** If step 3 fails (rate limit, network error), the
   monolithic approach requires re-running steps 1 and 2. Progressive loading
   with JSON state persistence after each step means a failure at step 3 resumes
   from step 3, not from scratch.

The tradeoff: each step's model call re-processes the client brief and prior
outputs, paying input-token cost for the overlap. At current Sonnet pricing
(~$3/M input), the added cost for a typical scenario is $0.05–0.10 — far less
than the cost of wasted generation from a context-window overrun.

---

## 2. Scope-item lookup as a tool, not as inline context

**Chosen:** A `lookup_scope_items` tool that the model calls via Claude's
tool-use capability during Skills 02 and 03.

**Rejected:** Embedding the full scope-item catalogue in the system prompt.

**Why:**

1. **Selective retrieval.** The curated catalogue has 20 entries now but would
   grow to 200+ in a production deployment. The model calls the tool with a
   query ("FI", "export", "batch management") and gets back only the relevant
   items, not the full list.

2. **Demonstrable tool use.** The orchestrator's tool-use loop — send tools,
   handle tool_use stop reason, execute the tool, send results back — is a
   real, running implementation of the pattern. It is not a mock or a stub.

3. **Upgrade path.** The tool's implementation (`search_scope_items`) currently
   searches a hardcoded dictionary. Replacing it with an API call to the SAP
   Best Practice Explorer or an MCP server connection requires changing one
   function, not restructuring the pipeline. See `skills/05-sap-best-practices-fetcher.md`
   for the MCP tool specification this would implement.

---

## 3. Human-approval gate before proposal generation

**Chosen:** The pipeline pauses before Skill 04 (Executive Proposal Drafter)
and asks for human confirmation. In non-interactive mode (eval runs, CI),
the gate is skipped via `--no-gate`.

**Why:** The first three skills produce structured analysis (discovery brief,
module fit, roadmap). These are internal working documents — if a module
score is wrong, it is easy to spot and correct. The proposal, however, is a
narrative deliverable addressed to a client's C-suite. Generating it without
review risks compounding errors from earlier steps into a polished document
that *looks* authoritative but contains bad recommendations.

The gate is not a safety guardrail (the model does not generate harmful
content here). It is a workflow design choice: the human reviews the analysis
before the system invests tokens in synthesizing it into prose. The eval
harness skips the gate by design — its purpose is to measure quality, not to
require human interaction.

---

## 4. Eval design: pipeline vs. baseline, not pipeline vs. human

**Chosen:** The eval compares the agentic pipeline (4-step, tool-augmented)
against a single-prompt baseline (same model, same client brief, one shot).

**Rejected:** Comparing against human consultant output.

**Why:** A human-baseline comparison is more interesting but methodologically
fraught: who is the human, how much time did they spend, what tools did they
use? The pipeline-vs-baseline comparison isolates the variable that matters:
does breaking the task into structured steps with tool use produce better
output than giving the model everything at once?

The benchmark methodology (`benchmarks/benchmark-methodology.md`) specifies
5 evaluation dimensions scored on a 0–5 rubric: Completeness, Accuracy,
Actionability, Consistency, and SAP Grounding. The LLM judge uses a
different model instance than the system under test (or at minimum, a
separate call with a grading-only prompt) to avoid self-evaluation bias.

The Consistency dimension requires ≥3 runs per scenario. The existing
benchmark files contain 1 run each. The eval harness closes this gap by
supporting `--runs N`, producing per-run scores and cross-run variance in
the results table.

---

## 5. State persistence: JSON files, not a database

**Chosen:** Pipeline state is written to `state/<run-id>.json` after each
step. Individual skill outputs are saved as separate files. All are plain
JSON or Markdown.

**Rejected:** SQLite, a database, or in-memory-only state.

**Why:** The pipeline runs infrequently (once per client engagement in a real
deployment, a few times per eval run in development). The state is small
(under 1MB per run). JSON files are:

- **Inspectable** — `cat state/run-xxx.json | jq .completed_steps` shows
  exactly where a failed run stopped.
- **Diffable** — two runs can be compared with standard text tools.
- **Portable** — no database driver, no schema migration, no connection
  string. The orchestrator runs from a clean clone with one dependency
  (`anthropic` SDK) and one env var.

The tradeoff: no concurrent-write safety. This is acceptable because the
pipeline is single-threaded by design — each step depends on the prior
step's output.

---

## 6. MCP server: thin wrapper over the same catalogue

**Chosen:** `mcp_server.py` exposes exactly two tools (`lookup_scope_items`,
`list_all_scope_items`) over stdio transport using the MCP Python SDK v2.0.
The scope-item catalogue is a literal copy of the one in `orchestrator.py`.

**Rejected:**

1. **MCP as the only access path** — making the orchestrator connect as an
   MCP client for every scope-item lookup would add a subprocess dependency
   and startup latency to every eval run, for no improvement in lookup quality.

2. **Embedding the catalogue in a vector store** — 20 items is a structured
   lookup problem, not a semantic search problem. Trigram matching (`query in
   field.lower()`) is exact, deterministic, and has zero infrastructure cost.

**Why a real MCP server matters despite the small catalogue:**

- The server implements the full MCP protocol (initialize handshake, tools/list,
  tools/call) — any MCP client (Claude Desktop, another agent, a test harness)
  can connect with zero code changes.
- It proves the MCP integration path documented in Skill 05's specification
  actually works end-to-end. The spec said "this is how it would work"; the
  server shows it does work.
- The `--test` mode lets someone verify the catalogue without installing an MCP
  client or the full SDK.

**Upgrade path:** Replacing the hardcoded `SCOPE_ITEMS` dict with an API call
to SAP's Best Practice Explorer requires changing `search_scope_items()` only.
The MCP server's tool interface and the orchestrator's tool-use interface both
stay unchanged.


---

## 7. Adversarial eval fix: root-caused as a test-design bug, not an agent bug

**Context:** The two committed adversarial cases (adv-01, adv-02) had been
failing since the eval was first run with --runs 3. Investigating by
reproducing both cases directly against Skill 01 showed the agent's actual
behavior was already correct in both cases — the assertions were wrong.

**adv-01 (insufficient input):** Skill 01 explicitly instructs flagging
missing budget/timeline as gaps when completeness is under 30% (see the
"Insufficient input" row in Skill 01's edge-case table). The agent does
exactly that — e.g. "CRITICAL: Timeline or go-live target not provided."
The original assertion banned the words "timeline"/"budget"/"$" outright,
which fails a well-behaved response for using those words to say they're
*missing*. Fixed by testing for the actual failure mode instead: a
fabricated dollar figure (`\$[\d,]`) or a fabricated "Phase 1:" roadmap
heading — i.e., the agent inventing numbers/plans it has no basis for.

**adv-02 (off-topic request):** The agent already declined and explained
why, but had to quote the off-topic request ("marketing campaign") to
explain the decline — a good refusal necessarily references what it's
refusing. The original assertion banned those exact phrases, which fails
any refusal that explains itself. Fixed by testing for actual marketing
deliverable content instead (a target-audience section, a creative
concept, a call-to-action) — the agent producing the thing it was asked
for, not the agent naming what it's declining.

**Also fixed, not just the test:** Skill 01 had no explicit instruction
for genuinely off-topic requests — only for "client using non-SAP
terminology" (a different case: SAP-relevant input in unfamiliar words,
not input with no SAP connection at all). Added a dedicated "Off-topic /
non-SAP request" row instructing a concise 2-3 sentence decline. This
measurably improved the actual response — before, the model hedged with
a long "possibility A / possibility B" branch; after, it's a clean
two-sentence decline. Not just passing a better test — genuinely better
behavior, verified by direct reproduction before and after the change.

**Why this matters for the eval harness's own credibility:** an eval
that fails a correctly-behaving agent teaches the wrong lesson — either
someone "fixes" the agent to game a bad assertion (worse behavior, better
score), or the failure gets shrugged off as noise (real regressions get
lost in known-flaky test noise). Root-causing to the actual failure mode
before touching either the agent or the test is the same discipline
applied to the LMMSmartClinicAI robustness fixes in the same audit pass.
