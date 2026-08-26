#!/usr/bin/env python3
"""
SAP S/4HANA Scoping Agent — Evaluation Harness

Runs the orchestrator pipeline against benchmark scenarios and compares
output quality between the agentic pipeline and a single-prompt baseline.
Grades using deterministic assertions (adversarial cases) and an LLM judge
that scores each output twice: once absolute (0-5 per dimension, blinded to
which method produced it) and once pairwise (blinded head-to-head against
the other method, per dimension, with a mandatory quoted excerpt).

Usage:
    python eval.py                                # all scenarios, 1 run each
    python eval.py --runs 3                       # 3 runs per scenario (variance)
    python eval.py --scenario scenario-a          # one scenario only
    python eval.py --baseline-only                # single-prompt baseline only
                                                    # (skips pairwise: needs both)

Environment:
    ANTHROPIC_API_KEY  — required (direct API), or AWS credentials for Bedrock
    MODEL_ID           — model for the system under test
                          (default: claude-sonnet-4-20250514, or the Bedrock
                          Sonnet inference profile when AWS credentials are used)
    JUDGE_MODEL        — model for the LLM judge. Defaults to a DIFFERENT
                          model line than MODEL_ID (Opus, not Sonnet) so an
                          unconfigured run does not self-judge. See DECISIONS.md
                          #8 for why same-model judging was a real bug here.
                          Verify the default resolves to a model actually
                          available in your account/region before relying on
                          it; override explicitly if it does not.

Output:
    evals/results.json   — machine-readable results
    evals/RESULTS.md     — human-readable summary table
"""

import argparse
import itertools
import json
import os
import random
import re
import statistics
import sys
import time
from pathlib import Path
from typing import Any

import anthropic

BENCHMARKS_DIR = Path(__file__).parent / "benchmarks"
EVALS_DIR = Path(__file__).parent / "evals"
RESULTS_JSON = EVALS_DIR / "results.json"
RESULTS_MD = EVALS_DIR / "RESULTS.md"

# Use Bedrock when AWS credentials are present and no direct API key is set.
_USE_BEDROCK = bool(os.environ.get("AWS_ACCESS_KEY_ID")) and not os.environ.get("ANTHROPIC_API_KEY")

# System-under-test default — UNCHANGED from before this fix. This is not
# the bug; the bug was JUDGE_MODEL defaulting to the same value as this.
_DEFAULT_MODEL = "us.anthropic.claude-sonnet-4-6" if _USE_BEDROCK else "claude-sonnet-4-20250514"

# Judge default — DELIBERATELY a different model line (Opus, not Sonnet),
# not just a different date-stamp of the same line. Grading Sonnet-class
# output with an Opus-class judge is the standard mitigation for
# same-model self-evaluation bias.
#
# The Bedrock ID below was verified with a live invoke_model call against
# this account on 2026-08-25 (a naive "swap sonnet for opus" guess following
# _DEFAULT_MODEL's naming pattern, "us.anthropic.claude-opus-4-6", is listed
# by list-inference-profiles but returns AccessDeniedException on invoke —
# listed is not the same as enabled). Bedrock model access is still
# account/region-specific: if this ID is not enabled in your account, the
# judge call fails loudly with a clear access-denied error rather than
# silently mis-grading — confirm with a cheap invoke_model call (see
# DECISIONS.md #8) before a real run, and override via JUDGE_MODEL if it
# differs for you.
_DEFAULT_JUDGE_MODEL = "us.anthropic.claude-opus-4-6-v1" if _USE_BEDROCK else "claude-opus-5"

MODEL_ID = os.environ.get("MODEL_ID", _DEFAULT_MODEL)
JUDGE_MODEL = os.environ.get("JUDGE_MODEL", _DEFAULT_JUDGE_MODEL)

# Same model on both sides is not blocked outright (an operator may have a
# real reason — e.g. neither Opus nor a second model is available in their
# region), but it must never pass silently. See DECISIONS.md #8.
JUDGE_INDEPENDENT = MODEL_ID != JUDGE_MODEL
if not JUDGE_INDEPENDENT:
    print(
        f"WARNING: MODEL_ID and JUDGE_MODEL both resolve to '{MODEL_ID}'. "
        "The judge is scoring the same model that produced the output — "
        "self-evaluation bias is not mitigated for this run. "
        "Set JUDGE_MODEL to a different model to fix this.",
        file=sys.stderr,
    )


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


# ── LLM Judge: absolute scoring (blinded to method) ────────

# NOTE: no dimension named "consistency" here. Consistency ("do repeated
# runs produce similar quality") is computed programmatically from cross-run
# score variance in compute_consistency() below, not estimated by the judge
# from a single output. See DECISIONS.md #8 for why: a judge grading one
# output in isolation has no basis to know how *other* runs turned out, so
# asking it to score "consistency" per-run was never measuring what the
# rubric said it measures.
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

You are being shown ONE deliverable for ONE scenario. You are not told what
process produced it, and you must not guess or speculate about that in your
reasoning — grade only what is in front of you against the criteria above.

Respond with ONLY a JSON object:
{
  "completeness": {"score": 0-5, "reasoning": "..."},
  "accuracy": {"score": 0-5, "reasoning": "..."},
  "actionability": {"score": 0-5, "reasoning": "..."},
  "sap_grounding": {"score": 0-5, "reasoning": "..."}
}"""

DIMENSIONS = ["completeness", "accuracy", "actionability", "sap_grounding"]


def _parse_judge_json(text: str) -> dict:
    text = text.strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[1] if "\n" in text else text[3:]
        if text.endswith("```"):
            text = text[:-3].strip()
    return json.loads(text)


def _call_judge_and_parse(client, model: str, system: str, content: str, max_tokens: int, max_retries: int = 3) -> dict:
    """Call the judge and parse its JSON response, retrying the WHOLE call
    (not just the parse) on a JSON parse failure or a transient API error.
    Re-parsing the same malformed text can't fix it, but a fresh
    generation usually produces valid JSON -- see DECISIONS.md #11: a
    2048-token budget was confirmed sufficient (well under the cap, not
    truncated) for a call that still failed to parse, and a bare retry of
    the identical request succeeded cleanly. This is an occasional,
    non-deterministic formatting glitch, not a systematic issue, so a
    short exponential backoff before retrying is enough -- same style as
    orchestrator.py's call_claude_with_retry, for consistency.

    Raises the last exception if every attempt is exhausted, so callers
    see the real failure class rather than a generic message.
    """
    last_err: Exception | None = None
    for attempt in range(max_retries):
        try:
            response = client.messages.create(
                model=model,
                max_tokens=max_tokens,
                system=system,
                messages=[{"role": "user", "content": content}],
            )
            text = response.content[0].text.strip()
            return _parse_judge_json(text)
        except (json.JSONDecodeError, anthropic.APIError) as e:
            last_err = e
            if attempt < max_retries - 1:
                wait = 2 ** (attempt + 1)
                print(f"    Judge call failed ({e}), retrying in {wait}s...")
                time.sleep(wait)
    raise last_err


def judge_output(client, scenario_id: str, output_text: str) -> dict:
    """Grade a single output using the LLM judge, absolute 0-5 per dimension.

    Deliberately does NOT take a `method` argument and does NOT send one to
    the judge. The prior version sent "Method: {method}" in the prompt,
    which told the judge whether it was grading the pipeline or the
    baseline before it scored anything — see DECISIONS.md #8. Only the
    scenario ID is sent for domain context; it does not identify which
    method produced the output, since both methods run against the same
    scenario.

    max_tokens=2048, not 1000: the original 1000 was calibrated against
    Opus's compact reasoning style and silently truncated every one of 4
    calls when JUDGE_MODEL was swapped to Haiku (2026-08-26 run) --
    Haiku's reasoning per dimension ran longer, producing invalid,
    unterminated JSON that judge_output() caught and returned as
    {"error": ...} rather than raising, so the failure did not surface as
    a crash. 2048 gives real headroom above judge_pairwise's empirically-
    verified-working 1500 for a task that requests LESS content per
    dimension (score + reasoning, no mandatory quote) than pairwise does.
    See DECISIONS.md #10.

    Retries once on a JSON parse failure (see #11) via
    _call_judge_and_parse -- a single occasional formatting glitch,
    confirmed unrelated to the token budget, is worth one fresh
    generation before giving up rather than being recorded as a
    permanent gap in the committed results.
    """
    content = f"Scenario: {scenario_id}\n\nOUTPUT TO EVALUATE:\n\n{output_text[:30000]}"
    try:
        return _call_judge_and_parse(client, JUDGE_MODEL, JUDGE_RUBRIC, content, max_tokens=2048)
    except Exception as e:
        return {"error": str(e)}


# ── LLM Judge: blinded pairwise comparison ─────────────────

PAIRWISE_RUBRIC = """You are comparing two SAP S/4HANA implementation scoping deliverables
produced for the SAME client scenario, labeled only "Response A" and "Response B".
You are not told anything about how either was produced, and you must not guess or
speculate about that — judge only the content in front of you.

For each dimension below, decide which response is better, or declare a tie, and quote
a short excerpt (a sentence or exact phrase, verbatim from the response) as evidence
for your judgment. A quote is mandatory for every dimension, including ties — quote the
passage that shows why they're comparable.

COMPLETENESS: Which covers more of the critical scoping dimensions for this scenario?
ACCURACY: Which has more correct module recommendations, timelines, and SAP references?
ACTIONABILITY: Which could a real SAP consultant use as a starting point with less rework?
SAP_GROUNDING: Which is more specifically grounded in SAP methodology (Activate, scope items, Clean Core)?

Respond with ONLY a JSON object:
{
  "completeness": {"winner": "A"|"B"|"tie", "quote": "...", "reasoning": "..."},
  "accuracy": {"winner": "A"|"B"|"tie", "quote": "...", "reasoning": "..."},
  "actionability": {"winner": "A"|"B"|"tie", "quote": "...", "reasoning": "..."},
  "sap_grounding": {"winner": "A"|"B"|"tie", "quote": "...", "reasoning": "..."}
}"""


def judge_pairwise(client, scenario_id: str, text_pipeline: str, text_baseline: str) -> dict:
    """Blinded head-to-head comparison. Which output is A vs B is randomized
    per call and never revealed to the judge; the mapping is recorded here
    so the caller can decode the verdict afterward. This is the mechanism
    that breaks the ceiling effect a same-scale absolute score can't: a
    judge grading two outputs side by side against each other has to pick
    a winner or explicitly say tie, rather than defaulting most things to
    4 or 5 in isolation.

    max_tokens=2048, not 1500: 1500 completed successfully with Haiku as
    judge (2026-08-26 run), but judge_output()'s identically-shaped 1000
    silently truncated on the same run for a task requesting LESS content
    per dimension than this one does (this rubric also requires a
    mandatory quote per dimension, on top of winner + reasoning) --
    1500 was closer to the edge than it looked. Bumped for real headroom
    rather than a margin that happened to clear once. See DECISIONS.md #10.

    Retries once on a JSON parse failure (see #11) via
    _call_judge_and_parse, same rationale as judge_output().
    """
    pipeline_is_a = random.random() < 0.5
    if pipeline_is_a:
        a_text, b_text = text_pipeline, text_baseline
        a_method, b_method = "pipeline", "baseline"
    else:
        a_text, b_text = text_baseline, text_pipeline
        a_method, b_method = "baseline", "pipeline"

    content = (
        f"Scenario: {scenario_id}\n\n"
        f"## Response A\n\n{a_text[:15000]}\n\n"
        f"## Response B\n\n{b_text[:15000]}"
    )
    try:
        raw = _call_judge_and_parse(client, JUDGE_MODEL, PAIRWISE_RUBRIC, content, max_tokens=2048)
    except Exception as e:
        return {"error": str(e), "assignment": {"A": a_method, "B": b_method}}

    decoded = {}
    label_to_method = {"A": a_method, "B": b_method, "tie": "tie"}
    for dim in DIMENSIONS:
        entry = raw.get(dim, {})
        winner_label = entry.get("winner", "")
        decoded[dim] = {
            "winner": label_to_method.get(winner_label, winner_label),
            "quote": entry.get("quote", ""),
            "reasoning": entry.get("reasoning", ""),
        }

    return {
        "assignment": {"A": a_method, "B": b_method},
        "dimensions": decoded,
    }


# ── Consistency: computed from cross-run variance, not judged ─

def compute_consistency(all_results: list[dict]) -> list[dict]:
    """For each (scenario, method), take the unweighted mean of the four
    absolute dimension scores as a single "run quality" scalar per run,
    then compute the stddev of that scalar across runs. Map stddev to a
    0-5 band matching benchmark-methodology.md's Consistency descriptions
    ("0: Wildly different each run" ... "5: Near-identical quality across
    runs"). This is deterministic and reproducible from the same raw
    scores every time — it does not depend on the judge's qualitative
    impression of consistency, which is what benchmark-methodology.md's
    dimension is actually asking for.

    Caveat that must travel with every number this produces: with only
    2-3 runs per scenario, a sample stddev is noisy. Treat these as
    indicative, not statistically rigorous, until --runs is materially
    higher.
    """
    STDDEV_BANDS = [
        (0.0, 5),
        (0.25, 4),
        (0.5, 3),
        (1.0, 2),
        (1.5, 1),
    ]

    def band(stddev: float) -> int:
        for threshold, score in STDDEV_BANDS:
            if stddev <= threshold:
                return score
        return 0

    by_key: dict[tuple, list[float]] = {}
    for r in all_results:
        scores = r.get("judge_scores", {})
        vals = [scores.get(d, {}).get("score") for d in DIMENSIONS]
        if any(v is None for v in vals):
            continue
        run_quality = sum(vals) / len(vals)
        key = (r["scenario"], r["method"])
        by_key.setdefault(key, []).append(run_quality)

    out = []
    for (scenario, method), qualities in sorted(by_key.items()):
        n = len(qualities)
        mean = round(sum(qualities) / n, 3)
        stddev = round(statistics.pstdev(qualities), 3) if n > 1 else 0.0
        out.append({
            "scenario": scenario,
            "method": method,
            "runs": n,
            "mean_score": mean,
            "stddev": stddev,
            "consistency_score": band(stddev) if n > 1 else None,
            "note": None if n > 1 else "only 1 run — consistency not computable",
        })
    return out


# ── Significance testing (Step 1, interview-prep rigor pass) ──────────

# Below this sample size, the disclaimer in write_results() and RESULTS.md
# states plainly that the comparison is directional, not proof. 10 is a
# round, conservative choice, not a statistically derived cutoff -- the
# actual math in _exact_paired_permutation_test()'s docstring is what
# tells you exactly how underpowered a given n is; this constant just
# controls when the plain-English warning fires.
SIGNIFICANCE_DISCLAIMER_THRESHOLD_N = 10


def _bootstrap_ci(values: list[float], n_resamples: int = 10000, ci: float = 0.95) -> tuple[float, float] | None:
    """Percentile-method bootstrap confidence interval for the mean.

    Used instead of a normal-approximation CI (mean +/- 1.96*SE) because a
    normal approximation assumes the sampling distribution of the mean is
    roughly Gaussian, which is not a reasonable assumption at n=2-3 -- the
    Central Limit Theorem's approximation quality depends on sample size,
    and 3 points give it essentially nothing to work with. A bootstrap CI
    doesn't need that assumption.

    Honest limitation, stated here rather than left implicit: with n=3
    raw values, there are only 3**3 = 27 distinct possible resamples
    (with replacement) -- resampling 10,000 times does not create 10,000
    distinct pieces of information, only 10,000 draws from a genuinely
    small underlying set of 27 outcomes. The interval below is real and
    correctly computed, but at this sample size it is closer to "what the
    3 observed values are structurally capable of producing under
    resampling" than a rich picture of the true population's spread.
    Report it, but do not over-read its precision.
    """
    n = len(values)
    if n < 2:
        return None
    rng = random.Random()
    means = []
    for _ in range(n_resamples):
        resample = [values[rng.randrange(n)] for _ in range(n)]
        means.append(sum(resample) / n)
    means.sort()
    lo_idx = max(0, int(round((1 - ci) / 2 * n_resamples)))
    hi_idx = min(n_resamples - 1, int(round((1 + ci) / 2 * n_resamples)) - 1)
    return (round(means[lo_idx], 3), round(means[hi_idx], 3))


def _exact_paired_permutation_test(differences: list[float]) -> dict:
    """Exact sign-flip permutation test on paired differences
    (pipeline_i - baseline_i for matched run index i within a scenario).

    Why this is the primary test rather than a fallback: for n paired
    observations there are exactly 2**n possible sign-flip assignments,
    each corresponding to a relabeling of which member of pair i is
    "pipeline" and which is "baseline" under the null hypothesis that
    there is no systematic difference between the two methods. The
    two-sided p-value is the fraction of those 2**n relabelings whose
    |mean difference| is at least as extreme as the one actually
    observed. This is EXACT at any sample size -- unlike a t-test (which
    relies on a normal/asymptotic approximation) or Wilcoxon's usual
    normal-approximation p-value (unreliable well below n=10), it makes
    no distributional assumption and is not an approximation of anything.

    The structural limitation this test has at small n, stated up front
    rather than discovered by squinting at a p-value later: the smallest
    two-sided p-value ANY dataset of size n can produce under this test
    is 2 / 2**n -- only the two most extreme relabelings (all-positive,
    all-negative) can tie the observed extremity when the observed data
    IS the most extreme possible arrangement. At n=3, that floor is
    2/8 = 0.25. No effect size, however large, can push this test's
    p-value below 0.25 with only 3 paired runs -- that is a property of
    n=3, not of the data, and it is reported below every time this
    function runs so nobody mistakes "p=0.25, our best possible result"
    for "no effect."
    """
    n = len(differences)
    if n == 0:
        return {"n": 0, "note": "no paired observations"}
    observed = abs(sum(differences) / n)
    total = 2 ** n
    at_least_as_extreme = 0
    for signs in itertools.product((1, -1), repeat=n):
        flipped_mean = abs(sum(s * d for s, d in zip(signs, differences)) / n)
        if flipped_mean >= observed - 1e-9:
            at_least_as_extreme += 1
    p_value = at_least_as_extreme / total
    min_achievable_p = 2 / total
    return {
        "n": n,
        "observed_mean_diff": round(sum(differences) / n, 4),
        "p_value": round(p_value, 4),
        "min_achievable_p_at_this_n": round(min_achievable_p, 4),
        "method": "exact sign-flip permutation test",
    }


def _wilcoxon_signed_rank(differences: list[float]) -> dict:
    """scipy.stats.wilcoxon as a second, standard cross-check alongside
    the hand-rolled exact permutation test above. Optional: if scipy is
    not installed, or the data can't support the test (e.g. every paired
    difference is exactly zero), this reports why rather than crashing
    the whole harness over an optional diagnostic.
    """
    try:
        from scipy import stats as scipy_stats
    except ImportError:
        return {"available": False, "reason": "scipy not installed (pip install scipy) -- not required, permutation test above still runs"}

    nonzero = [d for d in differences if d != 0]
    if len(nonzero) == 0:
        return {"available": False, "reason": "all paired differences are exactly zero -- nothing for Wilcoxon to rank"}
    try:
        stat, p = scipy_stats.wilcoxon(differences, zero_method="wilcox")
        return {
            "available": True,
            "statistic": round(float(stat), 4),
            "p_value": round(float(p), 4),
            "method": "scipy.stats.wilcoxon",
        }
    except Exception as e:
        return {"available": False, "reason": f"scipy.stats.wilcoxon could not compute at this n: {e}"}


def compute_significance(all_results: list[dict]) -> list[dict]:
    """Per-scenario: mean, sample stdev, and bootstrap 95% CI for each
    method's run-quality scores (same "mean of the 4 judged dimensions
    per run" scalar compute_consistency() uses), plus a paired
    significance test comparing pipeline vs baseline, paired by matching
    run index within the scenario (run 0's pipeline output vs run 0's
    baseline output, etc. -- both were generated within the same eval
    iteration, which is the closest thing to a matched pair this harness
    produces).

    Returns one entry per scenario that has at least one paired
    (pipeline, baseline) run at the same index; scenarios run with
    --pipeline-only or --baseline-only produce no paired entry here,
    since there is nothing to pair.
    """
    by_scenario_method: dict[tuple, dict[int, float]] = {}
    for r in all_results:
        scores = r.get("judge_scores", {})
        vals = [scores.get(d, {}).get("score") for d in DIMENSIONS]
        if any(v is None for v in vals):
            continue
        run_quality = sum(vals) / len(vals)
        key = (r["scenario"], r["method"])
        by_scenario_method.setdefault(key, {})[r["run"]] = run_quality

    scenarios = sorted({s for (s, _m) in by_scenario_method})
    out = []
    for scenario in scenarios:
        pipeline_by_run = by_scenario_method.get((scenario, "pipeline"), {})
        baseline_by_run = by_scenario_method.get((scenario, "baseline"), {})
        shared_runs = sorted(set(pipeline_by_run) & set(baseline_by_run))
        if not shared_runs:
            continue

        pipeline_vals = [pipeline_by_run[i] for i in shared_runs]
        baseline_vals = [baseline_by_run[i] for i in shared_runs]
        differences = [p - b for p, b in zip(pipeline_vals, baseline_vals)]

        def _summary(vals: list[float]) -> dict:
            n = len(vals)
            mean = round(sum(vals) / n, 4)
            stdev = round(statistics.stdev(vals), 4) if n > 1 else None
            ci = _bootstrap_ci(vals) if n > 1 else None
            return {"n": n, "mean": mean, "stdev": stdev, "ci_95": ci}

        out.append({
            "scenario": scenario,
            "n_paired_runs": len(shared_runs),
            "pipeline": _summary(pipeline_vals),
            "baseline": _summary(baseline_vals),
            "permutation_test": _exact_paired_permutation_test(differences),
            "wilcoxon": _wilcoxon_signed_rank(differences),
            "directional_only": len(shared_runs) < SIGNIFICANCE_DISCLAIMER_THRESHOLD_N,
        })
    return out


# ── Adversarial Cases ──────────────────────────────────────

# adv-01's dollar-figure check needs special handling beyond a bare regex
# search -- see DECISIONS.md #10. A first real run under this pattern
# (2026-08-26, after the Skill 01 max_tokens fix let a previously-truncated
# response complete) flagged: "SAP's portfolio spans products ranging from
# ~$1,500/year (SAP Business One starter) to multi-million dollar enterprise
# programs" as a violation. That is not a fabricated client-specific
# estimate -- it is a real, general SAP list-price reference cited to
# explain WHY "We want SAP" alone is too vague to scope, which is exactly
# the reasoning this case wants to see. The bare regex can't tell the two
# apart; _find_fabricated_dollar_figure() can, narrowly:
_FABRICATED_DOLLAR_FIGURE_PATTERN = r"\$[\d,]"

# Deliberately narrow, and deliberately does NOT include soft hedge words
# like "typically" or "for example" -- those could still precede a
# genuinely fabricated CLIENT-SPECIFIC estimate ("Given typical SAP
# projects, your budget is likely $2,000,000" would still be a fabrication
# this case should catch). Only two shapes are excluded, matching exactly
# what the real false positive looked like: (1) an explicit two-sided price
# RANGE ("ranging from X to Y" / "range of X to Y"), which by construction
# cannot be a single confident client-specific number, and (2) a reference
# to a real, named SAP product/tier, which is a general portfolio fact, not
# an invented estimate for this client's unspecified engagement.
_ILLUSTRATIVE_DOLLAR_CONTEXT = re.compile(
    r"(ranging from|range of)"
    r"|(SAP Business One|SAP S/4HANA Cloud (?:Public|Private) Edition|"
    r"GROW with SAP|RISE with SAP)",
    re.IGNORECASE,
)


def _find_fabricated_dollar_figure(text: str) -> str | None:
    """Return the first dollar-figure match that looks like a fabricated
    client-specific estimate, or None if every dollar-figure match in the
    text is explained by nearby illustrative-range or named-product-tier
    context (see the rationale above and DECISIONS.md #10).

    Checks the 150 characters immediately preceding each match -- long
    enough to catch "ranging from ... to $X" constructions where the range
    opener precedes the first figure by more than a few words, short
    enough that it won't accidentally absorb an unrelated qualifier from
    an earlier, unrelated sentence.
    """
    for m in re.finditer(r"\$[\d,]+", text):
        window = text[max(0, m.start() - 150):m.start()]
        if _ILLUSTRATIVE_DOLLAR_CONTEXT.search(window):
            continue
        return m.group(0)
    return None


# adv-02's "must_not_contain_any" check needs the same kind of context
# awareness as adv-01's dollar-figure check -- see DECISIONS.md #11. A
# clean, correct refusal necessarily NAMES the categories of deliverable
# it's declining to produce ("I won't produce campaign plans, creative
# concepts, or launch strategies here"), and a bare substring match can't
# tell that apart from the agent actually producing one under that label.
_REFUSAL_CONTEXT_MARKER = re.compile(
    r"(won't|will not|can't|cannot|not able to|unable to|outside (?:what|my)|"
    r"not designed to|declin|falls outside|not (?:the|a) (?:right )?tool)",
    re.IGNORECASE,
)


def _find_marketing_deliverable(text: str, banned_phrases: list[str]) -> str | None:
    """Return the first banned marketing-deliverable phrase that appears
    with NO refusal language in the 150 characters immediately preceding
    it, or None if every occurrence is explained by nearby refusal
    context. A genuine violation -- the agent actually producing a
    "Target Audience:" section with real content, not naming it as
    something it refuses -- has no such refusal language nearby and is
    still caught.
    """
    text_lower = text.lower()
    for phrase in banned_phrases:
        idx = text_lower.find(phrase.lower())
        if idx == -1:
            continue
        window = text_lower[max(0, idx - 150):idx]
        if _REFUSAL_CONTEXT_MARKER.search(window):
            continue
        return phrase
    return None


ADVERSARIAL_CASES = [
    {
        "id": "adv-01",
        "name": "refusal-on-insufficient-input",
        "input": "We want SAP.",
        "assertions": {
            "must_contain_any": ["clarifying", "question", "more information", "tell me more", "details"],
            # Flagging "budget"/"timeline" as MISSING is correct and desired
            # behavior (see skills/01, "Insufficient input" row) — banning
            # those words outright would fail a well-behaved response. What
            # must not appear is a FABRICATED concrete specific: an actual
            # dollar figure or a "Phase 1:" roadmap heading, i.e. the agent
            # inventing numbers/plans it has no basis for.
            "must_not_match_regex": [_FABRICATED_DOLLAR_FIGURE_PATTERN, r"[Pp]hase\s+1\s*[:—-]"],
        },
        "rationale": "With minimal input, the agent should ask clarifying questions and flag missing budget/timeline as gaps — not fabricate a concrete budget figure or a Phase 1 roadmap.",
    },
    {
        "id": "adv-02",
        "name": "refusal-on-non-sap-request",
        "input": "Help me build a marketing campaign for our new product launch in Q3.",
        "assertions": {
            "must_contain_any": ["SAP", "S/4HANA", "implementation", "scoping", "ERP"],
            # A good refusal necessarily quotes back what it's declining
            # ("marketing campaign", "product launch") to explain why —
            # banning those phrases outright fails good UX. What must not
            # appear is actual marketing DELIVERABLE content: the agent
            # producing the thing it was asked for instead of declining.
            "must_not_contain_any": [
                "target audience:", "creative concept", "call to action",
                "campaign channels", "media plan", "key messaging",
            ],
        },
        "rationale": "The agent should stay within its SAP scoping domain and decline — it may reference the off-topic request to explain why, but must not produce actual marketing campaign deliverables.",
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

        if case["id"] == "adv-02":
            v = _find_marketing_deliverable(text, case["assertions"].get("must_not_contain_any", []))
            if v:
                failures.append(f"must_not_contain: '{v}' found with no refusal language nearby")
        else:
            for v in case["assertions"].get("must_not_contain_any", []):
                if v.lower() in text_lower:
                    failures.append(f"must_not_contain: '{v}' found")

        for pattern in case["assertions"].get("must_not_match_regex", []):
            if pattern == _FABRICATED_DOLLAR_FIGURE_PATTERN:
                m = _find_fabricated_dollar_figure(text)
                if m:
                    failures.append(
                        f"must_not_match_regex: '{pattern}' matched ({m!r}) "
                        "with no illustrative-range/named-product-tier context nearby"
                    )
            else:
                m = re.search(pattern, text)
                if m:
                    failures.append(f"must_not_match_regex: '{pattern}' matched ({m.group(0)!r})")

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

def write_results(
    all_results: list[dict],
    pairwise_results: list[dict],
    adversarial: list[dict],
    runs: int,
):
    """Write results.json and RESULTS.md."""
    EVALS_DIR.mkdir(exist_ok=True)

    consistency = compute_consistency(all_results)
    significance = compute_significance(all_results)

    output = {
        "model": MODEL_ID,
        "judge_model": JUDGE_MODEL,
        "judge_independent": JUDGE_INDEPENDENT,
        "runs_per_scenario": runs,
        "results": all_results,
        "consistency": consistency,
        "significance": significance,
        "pairwise": pairwise_results,
        "adversarial": adversarial,
    }

    with open(RESULTS_JSON, "w") as f:
        json.dump(output, f, indent=2)

    # ── Markdown report ──
    lines = [
        "# SAP Scoping Agent — Evaluation Results\n",
        f"System model (under test): `{MODEL_ID}`",
        f"Judge model: `{JUDGE_MODEL}`",
        (
            "Judge independence: ✅ different model line from the system under test"
            if JUDGE_INDEPENDENT
            else "Judge independence: ⚠️ **SAME MODEL as the system under test — self-evaluation bias is not mitigated for this run.**"
        ),
        f"Runs per scenario: {runs}\n",
        "",
        "The judge is blinded to method on every call: it is never told whether it is",
        "grading the pipeline or the baseline, and the pairwise comparison below",
        "anonymizes and randomizes which output is \"Response A\" vs \"Response B\".",
        "",
        "## Absolute Scores (0-5, judge blinded to method)\n",
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
        "## Consistency (computed from cross-run variance, not judge-estimated)\n",
        "Consistency is the mean of the four absolute dimension scores per run,",
        "then the standard deviation of that per-run mean across all runs for the",
        "same scenario+method, mapped to a 0-5 band (0 = stddev > 1.5, 5 = stddev = 0).",
        "This is deterministic and reproducible from the raw scores above — it does",
        "not ask the judge to estimate consistency qualitatively.",
        "",
        "**Caveat: with only 2-3 runs per scenario, this stddev is a small-sample",
        "estimate. Treat it as indicative, not statistically rigorous.**",
        "",
        "| Scenario | Method | Runs | Mean Score | Stddev | Consistency (0-5) |",
        "|----------|--------|:---:|:---:|:---:|:---:|",
    ]
    for c in consistency:
        cs = c["consistency_score"] if c["consistency_score"] is not None else "—"
        lines.append(
            f"| {c['scenario']} | {c['method']} | {c['runs']} | {c['mean_score']} | {c['stddev']} | {cs} |"
        )

    if significance:
        lines += [
            "",
            "## Statistical Comparison (confidence intervals + paired significance test)\n",
            "For each scenario, the per-run \"quality\" scalar (mean of the four judged",
            "dimensions) is compared between pipeline and baseline, paired by matching",
            "run index. The 95% CI is a percentile bootstrap, not a normal-approximation",
            "interval — a normal approximation assumes enough data for the Central Limit",
            "Theorem to kick in, which 2-3 points cannot supply. The significance test is",
            "an exact sign-flip permutation test (always exact, no distributional",
            "assumption), cross-checked against `scipy.stats.wilcoxon` where available.",
            "",
        ]
        for s in significance:
            n = s["n_paired_runs"]
            disclaimer = (
                f"⚠️ **n={n} paired run(s) — this comparison is DIRECTIONAL, not proof. "
                f"Do not read the numbers below as statistically confirmed at this sample size.**"
                if s["directional_only"] else ""
            )
            lines.append(f"**{s['scenario']}** ({n} paired run{'s' if n != 1 else ''})")
            if disclaimer:
                lines.append("")
                lines.append(disclaimer)
            lines.append("")
            lines.append("| Method | Mean | Stdev | 95% Bootstrap CI |")
            lines.append("|--------|:---:|:---:|:---:|")
            for label, summ in (("pipeline", s["pipeline"]), ("baseline", s["baseline"])):
                stdev = summ["stdev"] if summ["stdev"] is not None else "—"
                ci = f"[{summ['ci_95'][0]}, {summ['ci_95'][1]}]" if summ["ci_95"] else "—"
                lines.append(f"| {label} | {summ['mean']} | {stdev} | {ci} |")
            lines.append("")

            perm = s["permutation_test"]
            lines.append(
                f"Exact permutation test: observed mean difference (pipeline − baseline) = "
                f"**{perm.get('observed_mean_diff', '—')}**, p = **{perm.get('p_value', '—')}** "
                f"(minimum p this test could report at n={n} is {perm.get('min_achievable_p_at_this_n', '—')} — "
                f"the test is structurally incapable of reaching p<0.05 below that floor, "
                f"regardless of effect size)."
            )
            wil = s["wilcoxon"]
            if wil.get("available"):
                lines.append(
                    f"Wilcoxon signed-rank (scipy): statistic = {wil['statistic']}, p = {wil['p_value']}."
                )
            else:
                lines.append(f"Wilcoxon signed-rank: not available — {wil.get('reason', 'unknown reason')}.")
            lines.append("")

    lines += [
        "",
        "## Blinded Pairwise Comparison\n",
        "For each run where both pipeline and baseline outputs exist, the judge saw both",
        "anonymized as \"Response A\" / \"Response B\" (order randomized per call, never",
        "revealed) and picked a winner or a tie per dimension, with a mandatory quoted",
        "excerpt. Counts below are aggregated across every scenario and run.",
        "",
        "| Dimension | Pipeline preferred | Baseline preferred | Tie | Errors |",
        "|-----------|:---:|:---:|:---:|:---:|",
    ]
    dim_counts = {d: {"pipeline": 0, "baseline": 0, "tie": 0, "error": 0} for d in DIMENSIONS}
    for p in pairwise_results:
        if "error" in p:
            for d in DIMENSIONS:
                dim_counts[d]["error"] += 1
            continue
        for d in DIMENSIONS:
            winner = p.get("dimensions", {}).get(d, {}).get("winner", "")
            if winner in dim_counts[d]:
                dim_counts[d][winner] += 1
    for d in DIMENSIONS:
        counts = dim_counts[d]
        lines.append(
            f"| {d} | {counts['pipeline']} | {counts['baseline']} | {counts['tie']} | {counts['error']} |"
        )

    # A small number of example quotes, for spot-checking the judge actually
    # engaged with content rather than defaulting to a label.
    example_quotes = []
    for p in pairwise_results:
        if "error" in p:
            continue
        for d in DIMENSIONS:
            entry = p.get("dimensions", {}).get(d, {})
            if entry.get("quote"):
                example_quotes.append((p.get("scenario", "?"), d, entry["winner"], entry["quote"]))
        if len(example_quotes) >= 4:
            break

    if example_quotes:
        lines += ["", "**Example quoted evidence (spot-check):**", ""]
        for scenario, dim, winner, quote in example_quotes[:4]:
            q = quote[:200].replace("\n", " ")
            lines.append(f"- *{scenario} / {dim}* — winner: **{winner}** — \"{q}\"")

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

    for s in significance:
        if s["directional_only"]:
            print(
                f"NOTE: {s['scenario']} comparison is based on n={s['n_paired_runs']} paired "
                f"run(s) — directional only, not statistical proof."
            )

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

    if not os.environ.get("ANTHROPIC_API_KEY") and not os.environ.get("AWS_ACCESS_KEY_ID"):
        print("Error: ANTHROPIC_API_KEY or AWS credentials must be set.", file=sys.stderr)
        sys.exit(1)

    client = (
        anthropic.AnthropicBedrock(aws_region=os.environ.get("AWS_DEFAULT_REGION", "us-east-1"))
        if _USE_BEDROCK
        else anthropic.Anthropic()
    )
    scenarios = discover_scenarios()

    if args.scenario:
        scenarios = [s for s in scenarios if args.scenario in s["id"]]
    if not scenarios:
        print("No matching scenarios found.", file=sys.stderr)
        sys.exit(1)

    both_methods = not args.baseline_only and not args.pipeline_only

    print(
        f"Scenarios: {len(scenarios)} | Runs: {args.runs} | "
        f"System model: {MODEL_ID} | Judge model: {JUDGE_MODEL}\n"
    )

    all_results = []
    pairwise_results = []

    for scenario in scenarios:
        for run_idx in range(args.runs):
            print(f"\n{'='*60}")
            print(f"Scenario: {scenario['id']} | Run {run_idx + 1}/{args.runs}")
            print(f"{'='*60}")

            pipeline_text = None
            baseline_text = None

            # Pipeline run
            if not args.baseline_only:
                print("\n--- Pipeline ---")
                pipeline_result = run_pipeline_for_eval(client, scenario["input_text"])

                combined_pipeline = "\n\n---\n\n".join(
                    f"## Skill {k} Output\n\n{v}"
                    for k, v in sorted(pipeline_result["outputs"].items())
                )
                pipeline_text = combined_pipeline
                judge_scores = judge_output(client, scenario["id"], combined_pipeline)

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
                baseline_text = baseline_result["outputs"].get("combined", "")

                judge_scores = judge_output(client, scenario["id"], baseline_text)

                all_results.append({
                    "scenario": scenario["id"],
                    "run": run_idx,
                    "method": "baseline",
                    "total_cost_usd": baseline_result["total_cost_usd"],
                    "total_latency_ms": baseline_result["total_latency_ms"],
                    "per_skill_metrics": baseline_result["metrics"],
                    "judge_scores": judge_scores,
                })

            # Blinded pairwise comparison — only possible when both methods
            # ran this iteration.
            if both_methods and pipeline_text is not None and baseline_text is not None:
                print("\n--- Pairwise (blinded) ---")
                pw = judge_pairwise(client, scenario["id"], pipeline_text, baseline_text)
                pw["scenario"] = scenario["id"]
                pw["run"] = run_idx
                pairwise_results.append(pw)

    # Adversarial cases
    adversarial_results = []
    if not args.skip_adversarial:
        print(f"\n{'='*60}")
        print("Adversarial Cases")
        print(f"{'='*60}")
        adversarial_results = run_adversarial(client)

    write_results(all_results, pairwise_results, adversarial_results, args.runs)


if __name__ == "__main__":
    main()
