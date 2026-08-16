#!/usr/bin/env python3
"""
SAP S/4HANA Scoping Agent — Evaluation Harness

Runs the orchestrator pipeline against benchmark scenarios and compares
output quality between the agentic pipeline and a single-prompt baseline.
Grades using both deterministic assertions and LLM-judge scoring.

Usage:
    python eval.py                                # all scenarios, 1 run each
    python eval.py --runs 3                       # 3 runs per scenario (variance)
    python eval.py --scenario scenario-a          # one scenario only
    python eval.py --baseline-only                # single-prompt baseline only

Environment:
    ANTHROPIC_API_KEY  — required
    MODEL_ID           — model for the system under test (default: claude-sonnet-4-20250514)
    JUDGE_MODEL        — model for the LLM judge (default: claude-sonnet-4-20250514)

Output:
    evals/results.json   — machine-readable results
    evals/RESULTS.md     — human-readable summary table
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path
from typing import Any

import anthropic

BENCHMARKS_DIR = Path(__file__).parent / "benchmarks"
EVALS_DIR = Path(__file__).parent / "evals"
RESULTS_JSON = EVALS_DIR / "results.json"
RESULTS_MD = EVALS_DIR / "RESULTS.md"

MODEL_ID = os.environ.get("MODEL_ID", "claude-sonnet-4-20250514")
JUDGE_MODEL = os.environ.get("JUDGE_MODEL", "claude-sonnet-4-20250514")


# ── Scenario Discovery ─────────────────────────────────────

def discover_scenarios() -> list[dict]:
    """Find benchmark scenarios with input files."""
    scenarios = []
    for d in sorted(BENCHMARKS_DIR.iterdir()):
        if not d.is_dir() or d.name.startswith("."):
            continue
        input_file = d / "input.md"
        if input_file.exists():
            scenarios.append({
                "id": d.name,
                "input_path": str(input_file),
                "input_text": input_file.read_text(),
                "reference_outputs": {
                    f"skill-{i:02d}": (d / f"skill-{i:02d}-output.md").read_text()
                    for i in range(1, 6)
                    if (d / f"skill-{i:02d}-output.md").exists()
                },
            })
    return scenarios


# ── Pipeline Execution ─────────────────────────────────────

def run_pipeline_for_eval(client: anthropic.Anthropic, input_text: str) -> dict:
    """Run the full orchestrator pipeline and capture outputs + metrics."""
    from orchestrator import run_pipeline, PipelineState

    t0 = time.monotonic()
    state = run_pipeline(input_text, skip_gate=True)
    total_ms = (time.monotonic() - t0) * 1000

    return {
        "method": "pipeline",
        "outputs": state.outputs,
        "metrics": state.metrics,
        "total_latency_ms": round(total_ms),
        "total_cost_usd": round(sum(m["cost_usd"] for m in state.metrics), 4),
    }


def run_baseline_for_eval(client: anthropic.Anthropic, input_text: str) -> dict:
    """Run a single-prompt baseline: give all info in one prompt, ask for complete output."""
    system_prompt = """You are an expert SAP S/4HANA implementation consultant. Given a client brief,
produce a complete scoping deliverable that includes:

1. A structured discovery brief (JSON format)
2. Module fit analysis with relevance ratings and fit scores
3. An implementation roadmap with phases, timelines, resources, and budget
4. An executive proposal summary

Produce all four sections in a single response. Be thorough and specific."""

    t0 = time.monotonic()
    response = client.messages.create(
        model=MODEL_ID,
        max_tokens=16384,
        system=system_prompt,
        messages=[{"role": "user", "content": f"## Client Brief\n\n{input_text}"}],
    )
    latency_ms = (time.monotonic() - t0) * 1000

    text = "\n".join(b.text for b in response.content if b.type == "text")

    return {
        "method": "baseline",
        "outputs": {"combined": text},
        "metrics": [{
            "skill": "combined",
            "input_tokens": response.usage.input_tokens,
            "output_tokens": response.usage.output_tokens,
            "latency_ms": round(latency_ms),
            "cost_usd": round(
                response.usage.input_tokens * 3e-6 + response.usage.output_tokens * 15e-6, 4
            ),
            "tool_calls": 0,
            "retries": 0,
        }],
        "total_latency_ms": round(latency_ms),
        "total_cost_usd": round(
            response.usage.input_tokens * 3e-6 + response.usage.output_tokens * 15e-6, 4
        ),
    }


# ── LLM Judge ──────────────────────────────────────────────

JUDGE_RUBRIC = """You are evaluating SAP S/4HANA implementation scoping deliverables.
Score each dimension from 0 to 5 using these criteria:

COMPLETENESS (0-5): Does the output cover all critical scoping dimensions?
  5=Comprehensive, no significant gaps. 3=~70% coverage. 1=<40% coverage.

ACCURACY (0-5): Are module recommendations, timeline estimates, and SAP references correct?
  5=Expert-level accuracy. 3=Mostly reasonable. 1=Major errors.

ACTIONABILITY (0-5): Could a real SAP consultant use this as a starting point?
  5=Ready to present with formatting only. 3=Usable with significant rework. 1=Generic/vague.

SAP_GROUNDING (0-5): Are recommendations grounded in SAP methodology (Activate, scope items, Clean Core)?
  5=Specific scope item references, correct Activate phases. 3=General SAP awareness. 1=No SAP specifics.

Respond with ONLY a JSON object:
{
  "completeness": {"score": 0-5, "reasoning": "..."},
  "accuracy": {"score": 0-5, "reasoning": "..."},
  "actionability": {"score": 0-5, "reasoning": "..."},
  "sap_grounding": {"score": 0-5, "reasoning": "..."}
}"""


def judge_output(client: anthropic.Anthropic, scenario_id: str, method: str, output_text: str) -> dict:
    """Grade an output using the LLM judge."""
    try:
        response = client.messages.create(
            model=JUDGE_MODEL,
            max_tokens=1000,
            system=JUDGE_RUBRIC,
            messages=[{
                "role": "user",
                "content": f"Scenario: {scenario_id}\nMethod: {method}\n\nOUTPUT TO EVALUATE:\n\n{output_text[:30000]}",
            }],
        )
        text = response.content[0].text.strip()
        return json.loads(text)
    except Exception as e:
        return {"error": str(e)}


# ── Adversarial Cases ──────────────────────────────────────

ADVERSARIAL_CASES = [
    {
        "id": "adv-01",
        "name": "refusal-on-insufficient-input",
        "input": "We want SAP.",
        "assertions": {
            "must_contain_any": ["clarifying", "question", "more information", "tell me more", "details"],
            "must_not_contain_any": ["Phase 1", "timeline", "budget", "$"],
        },
        "rationale": "With minimal input, the agent should ask clarifying questions, not hallucinate a full roadmap.",
    },
    {
        "id": "adv-02",
        "name": "refusal-on-non-sap-request",
        "input": "Help me build a marketing campaign for our new product launch in Q3.",
        "assertions": {
            "must_contain_any": ["SAP", "S/4HANA", "implementation", "scoping", "ERP"],
            "must_not_contain_any": ["marketing campaign", "product launch", "advertising"],
        },
        "rationale": "The agent should stay within its SAP scoping domain and redirect.",
    },
]


def run_adversarial(client: anthropic.Anthropic) -> list[dict]:
    """Run adversarial test cases against Skill 01."""
    from orchestrator import load_skill_prompt, call_claude_with_retry

    results = []
    skill_prompt = load_skill_prompt("01-client-discovery-intake.md")

    for case in ADVERSARIAL_CASES:
        print(f"  Adversarial: {case['id']} ({case['name']})...", end=" ", flush=True)

        text, metrics = call_claude_with_retry(
            client,
            system=skill_prompt,
            user_message=f"## Client Brief\n\n{case['input']}",
            max_tokens=4096,
        )

        # Grade deterministically
        text_lower = text.lower()
        failures = []

        for v in case["assertions"].get("must_contain_any", []):
            if not any(val.lower() in text_lower for val in case["assertions"]["must_contain_any"]):
                failures.append(f"must_contain_any: none of {case['assertions']['must_contain_any']} found")
                break

        for v in case["assertions"].get("must_not_contain_any", []):
            if v.lower() in text_lower:
                failures.append(f"must_not_contain: '{v}' found")

        passed = len(failures) == 0
        print("PASS" if passed else f"FAIL ({failures})")

        results.append({
            "case_id": case["id"],
            "name": case["name"],
            "passed": passed,
            "failures": failures,
            "reply_excerpt": text[:500],
            "metrics": metrics,
        })

    return results


# ── Report ─────────────────────────────────────────────────

def write_results(all_results: list[dict], adversarial: list[dict], runs: int):
    """Write results.json and RESULTS.md."""
    EVALS_DIR.mkdir(exist_ok=True)

    output = {
        "model": MODEL_ID,
        "judge_model": JUDGE_MODEL,
        "runs_per_scenario": runs,
        "results": all_results,
        "adversarial": adversarial,
    }

    with open(RESULTS_JSON, "w") as f:
        json.dump(output, f, indent=2)

    # Build markdown report
    lines = [
        "# SAP Scoping Agent — Evaluation Results\n",
        f"Model: `{MODEL_ID}` | Judge: `{JUDGE_MODEL}` | Runs per scenario: {runs}\n",
        "",
        "## Pipeline vs Baseline\n",
        "| Scenario | Method | Completeness | Accuracy | Actionability | SAP Grounding | Cost | Latency |",
        "|----------|--------|:---:|:---:|:---:|:---:|------:|--------:|",
    ]

    for r in all_results:
        scores = r.get("judge_scores", {})
        c = scores.get("completeness", {}).get("score", "—")
        a = scores.get("accuracy", {}).get("score", "—")
        act = scores.get("actionability", {}).get("score", "—")
        sg = scores.get("sap_grounding", {}).get("score", "—")
        cost = f"${r.get('total_cost_usd', 0):.4f}"
        lat = f"{r.get('total_latency_ms', 0) / 1000:.1f}s"
        lines.append(f"| {r['scenario']} | {r['method']} | {c} | {a} | {act} | {sg} | {cost} | {lat} |")

    lines += [
        "",
        "## Adversarial Cases\n",
        "| Case | Name | Result |",
        "|------|------|--------|",
    ]
    for a in adversarial:
        status = "✅ PASS" if a["passed"] else f"❌ FAIL: {a['failures']}"
        lines.append(f"| {a['case_id']} | {a['name']} | {status} |")

    with open(RESULTS_MD, "w") as f:
        f.write("\n".join(lines) + "\n")

    print(f"\nResults: {RESULTS_JSON}")
    print(f"Report:  {RESULTS_MD}")


# ── Main ───────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="SAP Scoping Agent — Evaluation Harness")
    parser.add_argument("--runs", type=int, default=1, help="Runs per scenario (default: 1)")
    parser.add_argument("--scenario", type=str, help="Run a specific scenario only")
    parser.add_argument("--baseline-only", action="store_true", help="Run baseline only")
    parser.add_argument("--pipeline-only", action="store_true", help="Run pipeline only")
    parser.add_argument("--skip-adversarial", action="store_true", help="Skip adversarial cases")
    args = parser.parse_args()

    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("Error: ANTHROPIC_API_KEY must be set.", file=sys.stderr)
        sys.exit(1)

    client = anthropic.Anthropic()
    scenarios = discover_scenarios()

    if args.scenario:
        scenarios = [s for s in scenarios if args.scenario in s["id"]]
    if not scenarios:
        print("No matching scenarios found.", file=sys.stderr)
        sys.exit(1)

    print(f"Scenarios: {len(scenarios)} | Runs: {args.runs} | Model: {MODEL_ID}\n")

    all_results = []

    for scenario in scenarios:
        for run_idx in range(args.runs):
            print(f"\n{'='*60}")
            print(f"Scenario: {scenario['id']} | Run {run_idx + 1}/{args.runs}")
            print(f"{'='*60}")

            # Pipeline run
            if not args.baseline_only:
                print("\n--- Pipeline ---")
                pipeline_result = run_pipeline_for_eval(client, scenario["input_text"])

                # Combine outputs for judging
                combined_pipeline = "\n\n---\n\n".join(
                    f"## Skill {k} Output\n\n{v}"
                    for k, v in sorted(pipeline_result["outputs"].items())
                )
                judge_scores = judge_output(client, scenario["id"], "pipeline", combined_pipeline)

                all_results.append({
                    "scenario": scenario["id"],
                    "run": run_idx,
                    "method": "pipeline",
                    "total_cost_usd": pipeline_result["total_cost_usd"],
                    "total_latency_ms": pipeline_result["total_latency_ms"],
                    "per_skill_metrics": pipeline_result["metrics"],
                    "judge_scores": judge_scores,
                })

            # Baseline run
            if not args.pipeline_only:
                print("\n--- Baseline ---")
                baseline_result = run_baseline_for_eval(client, scenario["input_text"])

                judge_scores = judge_output(
                    client, scenario["id"], "baseline",
                    baseline_result["outputs"].get("combined", "")
                )

                all_results.append({
                    "scenario": scenario["id"],
                    "run": run_idx,
                    "method": "baseline",
                    "total_cost_usd": baseline_result["total_cost_usd"],
                    "total_latency_ms": baseline_result["total_latency_ms"],
                    "per_skill_metrics": baseline_result["metrics"],
                    "judge_scores": judge_scores,
                })

    # Adversarial cases
    adversarial_results = []
    if not args.skip_adversarial:
        print(f"\n{'='*60}")
        print("Adversarial Cases")
        print(f"{'='*60}")
        adversarial_results = run_adversarial(client)

    write_results(all_results, adversarial_results, args.runs)


if __name__ == "__main__":
    main()
