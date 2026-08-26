"""Cap-calibration probe: does the tool-round budget actually buy quality?

Generates the SAME scenario twice -- once at _MAX_TOOL_ROUNDS=2, once at 8 --
then judges both. Generation is the expensive part (~$5 total) and happens
ONCE per cap; the judge calls are Haiku and cost pennies, so the blinded
pairwise comparison is repeated N times on the identical pair. That directly
answers the reliability problem DECISIONS.md #13 measured (a single pairwise
verdict flips ~1-in-5), for almost no extra money.

Writes evals/cap_probe.json. Makes no changes to committed results.
"""
import json, sys, time
sys.path.insert(0, ".")
import anthropic
import orchestrator as orch
import eval as ev

SCENARIO = "scenario-a-agribusiness"   # the scenario that showed score variance
CAPS = [2, 8]
N_PAIRWISE = 5

client = anthropic.AnthropicBedrock(aws_region="us-east-1")
scenarios = {s["id"]: s for s in ev.discover_scenarios()}
scen = scenarios[SCENARIO]

runs = {}
for cap in CAPS:
    orch._MAX_TOOL_ROUNDS = cap
    print(f"\n{'='*60}\nGenerating pipeline at cap={cap}\n{'='*60}")
    t0 = time.monotonic()
    result = ev.run_pipeline_for_eval(client, scen["input_text"])
    combined = "\n\n---\n\n".join(
        f"## Skill {k} Output\n\n{orch._skill_output_text(v)}"
        for k, v in sorted(result["outputs"].items())
    )
    per_skill_chars = {k: len(orch._skill_output_text(v)) for k, v in sorted(result["outputs"].items())}
    runs[cap] = {
        "cap": cap,
        "text": combined,
        "total_chars": len(combined),
        "per_skill_chars": per_skill_chars,
        "cost_usd": result["total_cost_usd"],
        "latency_s": round(result["total_latency_ms"] / 1000, 1),
        "tool_calls": sum(m.get("tool_calls", 0) for m in result["metrics"]),
        "confidence": {k: v.get("confidence") for k, v in sorted(result["outputs"].items())},
    }
    print(f"  cap={cap}: {len(combined)} chars, ${result['total_cost_usd']}, "
          f"{runs[cap]['tool_calls']} tool calls, {runs[cap]['latency_s']}s")
    print(f"  per-skill chars: {per_skill_chars}")

# Absolute scores, one judge call each
print(f"\n{'='*60}\nAbsolute scoring\n{'='*60}")
for cap in CAPS:
    runs[cap]["absolute"] = ev.judge_output(client, SCENARIO, runs[cap]["text"])
    scores = {d: runs[cap]["absolute"].get(d, {}).get("score") for d in ev.DIMENSIONS}
    print(f"  cap={cap}: {scores}")

# Blinded pairwise, repeated on the IDENTICAL pair (cheap, addresses judge noise).
# NOTE: judge_pairwise's arg names are (text_pipeline, text_baseline); here they
# carry cap-2 and cap-8 respectively, so a "pipeline" winner means cap2 won.
print(f"\n{'='*60}\nBlinded pairwise, {N_PAIRWISE}x on the identical pair\n{'='*60}")
verdicts = []
for i in range(N_PAIRWISE):
    pw = ev.judge_pairwise(client, SCENARIO, runs[2]["text"], runs[8]["text"])
    if "error" in pw:
        print(f"  call {i+1}: ERROR {pw['error'][:80]}")
        continue
    decoded = {d: ("cap2" if v["winner"] == "pipeline" else "cap8" if v["winner"] == "baseline" else v["winner"])
               for d, v in pw["dimensions"].items()}
    verdicts.append(decoded)
    print(f"  call {i+1}: {decoded}")

from collections import Counter
print(f"\n{'='*60}\nPAIRWISE TALLY ({len(verdicts)} valid calls)\n{'='*60}")
tally = {}
for d in ev.DIMENSIONS:
    c = Counter(v[d] for v in verdicts if d in v)
    tally[d] = dict(c)
    print(f"  {d}: {dict(c)}")

out = {
    "scenario": SCENARIO,
    "caps": CAPS,
    "n_pairwise": N_PAIRWISE,
    "judge_model": ev.JUDGE_MODEL,
    "system_model": ev.MODEL_ID,
    "runs": {str(c): {k: v for k, v in runs[c].items() if k != "text"} for c in CAPS},
    "pairwise_verdicts": verdicts,
    "pairwise_tally": tally,
}
with open("evals/cap_probe.json", "w") as f:
    json.dump(out, f, indent=2)

print(f"\n--- COST ---")
for c in CAPS:
    print(f"  cap={c}: ${runs[c]['cost_usd']}  ({runs[c]['tool_calls']} tool calls, {runs[c]['latency_s']}s)")
print(f"  probe total (generation only): ${round(sum(runs[c]['cost_usd'] for c in CAPS), 2)}")
print("\nWrote evals/cap_probe.json")
