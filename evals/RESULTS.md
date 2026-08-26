# SAP Scoping Agent — Evaluation Results

System model (under test): `claude-sonnet-4-20250514`
Judge model: `claude-opus-5`
Judge independence: ✅ different model line from the system under test
Runs per scenario: 3


The judge is blinded to method on every call: it is never told whether it is
grading the pipeline or the baseline, and the pairwise comparison below
anonymizes and randomizes which output is "Response A" vs "Response B".

## Absolute Scores (0-5, judge blinded to method)

| Scenario | Method | Completeness | Accuracy | Actionability | SAP Grounding | Cost | Latency |
|----------|--------|:---:|:---:|:---:|:---:|------:|--------:|
| scenario-a-agribusiness | pipeline | 5 | 5 | 5 | 5 | $1.7637 | 541.2s |
| scenario-a-agribusiness | baseline | 4 | 4 | 4 | 4 | $0.2253 | 288.0s |
| scenario-a-agribusiness | pipeline | 4 | 4 | 4 | 4 | $1.6989 | 453.2s |
| scenario-a-agribusiness | baseline | 4 | 4 | 4 | 3 | $0.2104 | 264.0s |
| scenario-a-agribusiness | pipeline | 4 | 4 | 3 | 4 | $1.8567 | 600.9s |
| scenario-a-agribusiness | baseline | 5 | 5 | 5 | 5 | $0.1561 | 193.2s |
| scenario-b-high-tech | pipeline | 5 | 5 | 5 | 5 | $1.9437 | 594.0s |
| scenario-b-high-tech | baseline | 5 | 5 | 5 | 5 | $0.2500 | 284.9s |
| scenario-b-high-tech | pipeline | 5 | 5 | 5 | 5 | $1.9257 | 571.9s |
| scenario-b-high-tech | baseline | 5 | 5 | 5 | 5 | $0.2500 | 289.2s |
| scenario-b-high-tech | pipeline | 5 | 5 | 5 | 5 | $2.0804 | 617.3s |
| scenario-b-high-tech | baseline | 5 | 5 | 5 | 5 | $0.2500 | 287.0s |

## Consistency (computed from cross-run variance, not judge-estimated)

Consistency is the mean of the four absolute dimension scores per run,
then the standard deviation of that per-run mean across all runs for the
same scenario+method, mapped to a 0-5 band (0 = stddev > 1.5, 5 = stddev = 0).
This is deterministic and reproducible from the raw scores above — it does
not ask the judge to estimate consistency qualitatively.

**Caveat: with only 2-3 runs per scenario, this stddev is a small-sample
estimate. Treat it as indicative, not statistically rigorous.**

| Scenario | Method | Runs | Mean Score | Stddev | Consistency (0-5) |
|----------|--------|:---:|:---:|:---:|:---:|
| scenario-a-agribusiness | baseline | 3 | 4.25 | 0.54 | 2 |
| scenario-a-agribusiness | pipeline | 3 | 4.25 | 0.54 | 2 |
| scenario-b-high-tech | baseline | 3 | 5.0 | 0.0 | 5 |
| scenario-b-high-tech | pipeline | 3 | 5.0 | 0.0 | 5 |

## Statistical Comparison (confidence intervals + paired significance test)

For each scenario, the per-run "quality" scalar (mean of the four judged
dimensions) is compared between pipeline and baseline, paired by matching
run index. The 95% CI is a percentile bootstrap, not a normal-approximation
interval — a normal approximation assumes enough data for the Central Limit
Theorem to kick in, which 2-3 points cannot supply. The significance test is
an exact sign-flip permutation test (always exact, no distributional
assumption), cross-checked against `scipy.stats.wilcoxon` where available.

**scenario-a-agribusiness** (3 paired runs)

⚠️ **n=3 paired run(s) — this comparison is DIRECTIONAL, not proof. Do not read the numbers below as statistically confirmed at this sample size.**

| Method | Mean | Stdev | 95% Bootstrap CI |
|--------|:---:|:---:|:---:|
| pipeline | 4.25 | 0.6614 | [3.75, 5.0] |
| baseline | 4.25 | 0.6614 | [3.75, 5.0] |

Exact permutation test: observed mean difference (pipeline − baseline) = **0.0**, p = **1.0** (minimum p this test could report at n=3 is 0.25 — the test is structurally incapable of reaching p<0.05 below that floor, regardless of effect size).
Wilcoxon signed-rank (scipy): statistic = 3.0, p = 1.0.

**scenario-b-high-tech** (3 paired runs)

⚠️ **n=3 paired run(s) — this comparison is DIRECTIONAL, not proof. Do not read the numbers below as statistically confirmed at this sample size.**

| Method | Mean | Stdev | 95% Bootstrap CI |
|--------|:---:|:---:|:---:|
| pipeline | 5.0 | 0.0 | [5.0, 5.0] |
| baseline | 5.0 | 0.0 | [5.0, 5.0] |

Exact permutation test: observed mean difference (pipeline − baseline) = **0.0**, p = **1.0** (minimum p this test could report at n=3 is 0.25 — the test is structurally incapable of reaching p<0.05 below that floor, regardless of effect size).
Wilcoxon signed-rank: not available — all paired differences are exactly zero -- nothing for Wilcoxon to rank.


## Blinded Pairwise Comparison

For each run where both pipeline and baseline outputs exist, the judge saw both
anonymized as "Response A" / "Response B" (order randomized per call, never
revealed) and picked a winner or a tie per dimension, with a mandatory quoted
excerpt. Counts below are aggregated across every scenario and run.

| Dimension | Pipeline preferred | Baseline preferred | Tie | Errors |
|-----------|:---:|:---:|:---:|:---:|
| completeness | 2 | 4 | 0 | 0 |
| accuracy | 2 | 3 | 1 | 0 |
| actionability | 1 | 5 | 0 | 0 |
| sap_grounding | 2 | 4 | 0 | 0 |

**Example quoted evidence (spot-check):**

- *scenario-a-agribusiness / completeness* — winner: **baseline** — "Response A: 'Pain Points' section identifies 6 specific numbered pain points (PP-01 through PP-06) each with id, title, description, business_impact, regulatory_driver, and priority rating. Response B"
- *scenario-a-agribusiness / accuracy* — winner: **baseline** — "Response A: 'SAP Business One Cloud Edition as primary; SAP GROW S/4HANA Public Cloud as escalation path' with explicit platform comparison table showing cost estimates ($80K–160K for B1, $400K–800K+ "
- *scenario-a-agribusiness / actionability* — winner: **baseline** — "Response A: Section 2.2 'Module Fit Analysis' begins immediately with structured module-by-module fit scores (Relevance Rating, Fit Score 0–100, Recommendation). For Financial Accounting: '⭐⭐⭐⭐⭐ (5/5 "
- *scenario-a-agribusiness / sap_grounding* — winner: **baseline** — "Response A: 'Platform Recommendation: SAP Business One Cloud Edition as primary; SAP GROW S/4HANA Public Cloud as escalation path' with explicit rationale: 'SAP Business One delivers 90%+ of Highland "

## Adversarial Cases

| Case | Name | Result |
|------|------|--------|
| adv-01 | refusal-on-insufficient-input | ✅ PASS |
| adv-02 | refusal-on-non-sap-request | ✅ PASS |

---

## Harness Changelog

Short, dated notes on changes to the eval harness itself (not to a run's
numbers). Full rationale for each lives in `DECISIONS.md`; this is the
one-line pointer.

**2026-08-26 — Step 1 of 4, interview-rigor pass: confidence intervals +
paired significance test.** Added `compute_significance()`: per-scenario
mean/stdev/95%-bootstrap-CI for both methods, plus a paired comparison
(matched by run index) using an exact sign-flip permutation test
(always exact, no distributional assumption) cross-checked against
`scipy.stats.wilcoxon` where installed. A directional-only disclaimer
prints to stdout and into this file whenever a scenario has fewer than
10 paired runs — currently every scenario, since `--runs 3` is what's
been run so far. The permutation test's own math states its floor
plainly: at n=3, the minimum p-value it can ever report is 0.25 — no
effect size can cross p<0.05 at this sample size. This does not close
the "not enough runs for real power" gap; it makes the size of that gap
explicit and computed, rather than asserted in prose. See `DECISIONS.md`
#12.

**2026-08-26 — Step 2 of 4, interview-rigor pass: judge test-retest
reliability check.** Added `--judge-reliability-check` (opt-in, `--reliability-n`
controls call count, default 5): calls the judge N times on one FIXED, real
(pipeline, baseline) pair — cached once under `evals/fixtures/` on first
run so every future invocation makes zero system-under-test calls, isolating
the judge's own variance from the pipeline's — using both the absolute-scoring
prompt and the blinded pairwise prompt.

**Real result, run against `scenario-b-high-tech`, N=5, judge = Haiku:**
absolute scoring is fairly stable (pipeline: 4 identical calls scored
5/5/5/5, 1 call scored 4/4/4/4 uniformly lower — consistent with one call
being marginally harsher across the board, not per-dimension noise;
baseline: perfectly stable, 5/5/5/5 on every one of 5 calls, zero variance).
**Blinded pairwise verdicts are markedly less stable.** Completeness and
actionability each flipped 1/5 times from a real 4/5 majority. SAP grounding
flipped 2/5 from a weaker 3/5 majority. **Accuracy showed NO stable majority
at all across 5 identical calls — votes split pipeline/pipeline/baseline/tie/baseline,
a genuine 2-2-1 tie.** The judge is not converging on one answer for this
dimension on identical input.

**A bug in this new code, found and fixed before being trusted:** the first
version used `statistics.mode()` to pick a "majority" verdict, which
silently tie-breaks a genuine split (picks whichever value appears first in
the list) rather than reporting that no majority exists — this would have
mislabeled accuracy's real 2-2-1 tie as "3 of 5 disagreed with the
majority," implying a majority that does not exist. Fixed to detect ties
explicitly via `Counter` and report `has_stable_majority: false` with the
full vote distribution when there is one, rather than asserting a winner.
See `DECISIONS.md` #13.

**What this means for every comparison in this file so far:** #9-#11's
findings were built from independent judge calls (different runs, never
the identical input judged twice), so this doesn't invalidate them — but
it does mean a *single* pairwise verdict, especially on accuracy, carries
real judge noise on top of whatever true quality difference exists. This
is not fixed by this step; it is measured by it. See DECISIONS.md #13 for
the full honest account of what this does and does not close.

**2026-08-26 — Step 3 of 4, interview-rigor pass: a preventive guardrail,
not another after-the-fact discovery.** Every bug in this file so far —
including the Skill 01 `max_tokens: 8192` vs 16384 bug (#10) — was caught
by re-reading output after a run, never by anything the harness itself
checked before running. Added `validate_skill_config()` in
`orchestrator.py`, called once at the top of `run_pipeline()`, before any
API call: flags any `SKILLS` entry whose `max_tokens` is at or below 50%
of the group's maximum, naming the skill and the outlier value.
**Design decision, chosen deliberately: it FAILS (raises `ValueError`),
not just warns.** A printed warning is exactly what would NOT have caught
the real bug — that bug ran silently truncated for an unknown number of
runs with no warning anywhere. Failing at startup costs nothing (zero API
spend before the check runs) and forces a decision instead of a
scroll-past-able line; an escape hatch (`ALLOW_CONFIG_OUTLIERS=1`) exists
for a genuinely intentional difference, so it's a locked door with a key,
not a wall.

**A bug in this guardrail itself, found before being trusted:** the first
version used a strict `<` comparison (`val < 0.5 * max`), which — because
the real historical bug sits EXACTLY on the 0.5 ratio boundary
(8192 / 16384 = 0.5 precisely) — would have silently let the one concrete
case this check exists to catch pass through uncaught. Found by testing
the function against the exact historical values before trusting it, not
by inspection. Fixed to `<=`. 8 test cases run before commit, including
the exact bug shape, the boundary itself, one step past the boundary, a
single-skill config, a config with a non-numeric field value, and the
escape hatch — all pass. See `DECISIONS.md` #14.
