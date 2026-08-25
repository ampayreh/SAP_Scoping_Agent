# SAP Scoping Agent — Evaluation Results

System model (under test): `us.anthropic.claude-sonnet-4-6`
Judge model: `us.anthropic.claude-opus-4-6-v1`
Judge independence: ✅ different model line from the system under test
Runs per scenario: 3


The judge is blinded to method on every call: it is never told whether it is
grading the pipeline or the baseline, and the pairwise comparison below
anonymizes and randomizes which output is "Response A" vs "Response B".

## Absolute Scores (0-5, judge blinded to method)

| Scenario | Method | Completeness | Accuracy | Actionability | SAP Grounding | Cost | Latency |
|----------|--------|:---:|:---:|:---:|:---:|------:|--------:|
| scenario-a-agribusiness | pipeline | 5 | 5 | 5 | 4 | $1.6953 | 486.7s |
| scenario-a-agribusiness | baseline | 5 | 5 | 5 | 4 | $0.1749 | 220.5s |
| scenario-a-agribusiness | pipeline | 5 | 5 | 5 | 4 | $1.6794 | 430.0s |
| scenario-a-agribusiness | baseline | 5 | 5 | 5 | 4 | $0.2482 | 293.4s |
| scenario-a-agribusiness | pipeline | 5 | 5 | 5 | 5 | $1.6763 | 461.5s |
| scenario-a-agribusiness | baseline | 5 | 5 | 5 | 4 | $0.2087 | 261.2s |
| scenario-b-high-tech | pipeline | 5 | 5 | 5 | 5 | $1.7279 | 475.5s |
| scenario-b-high-tech | baseline | 5 | 5 | 5 | 5 | $0.2500 | 302.6s |
| scenario-b-high-tech | pipeline | 5 | 5 | 5 | 5 | $1.7577 | 518.0s |
| scenario-b-high-tech | baseline | 5 | 5 | 5 | 5 | $0.2500 | 279.7s |
| scenario-b-high-tech | pipeline | 5 | 5 | 5 | 5 | $1.7316 | 487.0s |
| scenario-b-high-tech | baseline | 5 | 5 | 5 | 5 | $0.2500 | 278.3s |

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
| scenario-a-agribusiness | baseline | 3 | 4.75 | 0.0 | 5 |
| scenario-a-agribusiness | pipeline | 3 | 4.833 | 0.118 | 4 |
| scenario-b-high-tech | baseline | 3 | 5.0 | 0.0 | 5 |
| scenario-b-high-tech | pipeline | 3 | 5.0 | 0.0 | 5 |

## Blinded Pairwise Comparison

For each run where both pipeline and baseline outputs exist, the judge saw both
anonymized as "Response A" / "Response B" (order randomized per call, never
revealed) and picked a winner or a tie per dimension, with a mandatory quoted
excerpt. Counts below are aggregated across every scenario and run.

| Dimension | Pipeline preferred | Baseline preferred | Tie | Errors |
|-----------|:---:|:---:|:---:|:---:|
| completeness | 3 | 3 | 0 | 0 |
| accuracy | 2 | 3 | 1 | 0 |
| actionability | 1 | 4 | 1 | 0 |
| sap_grounding | 3 | 3 | 0 | 0 |

**Example quoted evidence (spot-check):**

- *scenario-a-agribusiness / completeness* — winner: **baseline** — "EU Deforestation Regulation (EUDR) 2023/1115 — Operators must demonstrate commodity not linked to deforestation; geolocation of plots required"
- *scenario-a-agribusiness / accuracy* — winner: **pipeline** — "This is distinct from EUDR (which does not cover cashew nuts as of 2026)."
- *scenario-a-agribusiness / actionability* — winner: **baseline** — "SAP Business One (Cloud Edition) or SAP S/4HANA Cloud Public Edition (GROW with SAP) — 65-employee company does not justify full SAP S/4HANA Private Cloud or On-Premise"
- *scenario-a-agribusiness / sap_grounding* — winner: **baseline** — "GROW with SAP (S/4HANA Public Cloud) is a viable alternative if agribusiness add-ons and multi-currency depth are prioritized. Full S/4HANA enterprise would be over-engineered and over-budget for this"

## Adversarial Cases

| Case | Name | Result |
|------|------|--------|
| adv-01 | refusal-on-insufficient-input | ✅ PASS |
| adv-02 | refusal-on-non-sap-request | ✅ PASS |
