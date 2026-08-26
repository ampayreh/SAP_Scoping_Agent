# SAP Scoping Agent — Evaluation Results

System model (under test): `us.anthropic.claude-sonnet-4-6`
Judge model: `us.anthropic.claude-haiku-4-5-20251001-v1:0`
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
