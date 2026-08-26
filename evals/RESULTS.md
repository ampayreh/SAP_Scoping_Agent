# SAP Scoping Agent — Evaluation Results

System model (under test): `us.anthropic.claude-sonnet-4-6`
Judge model: `us.anthropic.claude-haiku-4-5-20251001-v1:0`
Judge independence: ✅ different model line from the system under test
Runs per scenario: 1


The judge is blinded to method on every call: it is never told whether it is
grading the pipeline or the baseline, and the pairwise comparison below
anonymizes and randomizes which output is "Response A" vs "Response B".

## Absolute Scores (0-5, judge blinded to method)

| Scenario | Method | Completeness | Accuracy | Actionability | SAP Grounding | Cost | Latency |
|----------|--------|:---:|:---:|:---:|:---:|------:|--------:|
| scenario-a-agribusiness | pipeline | 4 | 4 | 4 | 5 | $1.8321 | 533.5s |
| scenario-a-agribusiness | baseline | 4 | 4 | 3 | 4 | $0.2042 | 258.7s |
| scenario-b-high-tech | pipeline | 4 | 4 | 3 | 4 | $2.1227 | 649.3s |
| scenario-b-high-tech | baseline | 5 | 5 | 5 | 5 | $0.2500 | 276.2s |

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
| scenario-a-agribusiness | baseline | 1 | 3.75 | 0.0 | — |
| scenario-a-agribusiness | pipeline | 1 | 4.25 | 0.0 | — |
| scenario-b-high-tech | baseline | 1 | 5.0 | 0.0 | — |
| scenario-b-high-tech | pipeline | 1 | 3.75 | 0.0 | — |

## Blinded Pairwise Comparison

For each run where both pipeline and baseline outputs exist, the judge saw both
anonymized as "Response A" / "Response B" (order randomized per call, never
revealed) and picked a winner or a tie per dimension, with a mandatory quoted
excerpt. Counts below are aggregated across every scenario and run.

| Dimension | Pipeline preferred | Baseline preferred | Tie | Errors |
|-----------|:---:|:---:|:---:|:---:|
| completeness | 0 | 2 | 0 | 0 |
| accuracy | 0 | 2 | 0 | 0 |
| actionability | 0 | 2 | 0 | 0 |
| sap_grounding | 0 | 2 | 0 | 0 |

**Example quoted evidence (spot-check):**

- *scenario-a-agribusiness / completeness* — winner: **baseline** — "# SECTION 2: MODULE FIT ANALYSIS ## 2.1 Platform Recommendation — Critical Upfront Assessment > ⚠️ **IMPORTANT ADVISORY FLAG — READ BEFORE MODULE ANALYSIS** Before scoping SAP S/4HANA modules, this an"
- *scenario-a-agribusiness / accuracy* — winner: **baseline** — "Multi-Currency Support: TZS, USD, EUR, CAD, KRW, INR with automatic exchange rate management... Unrealised/realised FX gain/loss automated calculation and posting... EU traceability compliance: SAP B1"
- *scenario-a-agribusiness / actionability* — winner: **baseline** — "### MODULE 1: Financial Accounting & Multi-Currency (SAP B1: Financials) | Attribute | Detail | |---|---| | **Relevance Rating** | ⭐⭐⭐⭐⭐ 5/5 | | **Fit Score** | ⭐⭐⭐⭐⭐ 5/5 | | **Priority** | Phase 1 — "
- *scenario-a-agribusiness / sap_grounding* — winner: **baseline** — "For the remainder of this analysis, modules are scoped assuming **SAP Business One Cloud as primary platform with SAP BTP for integration**, with notes where GROW with SAP offers equivalent functional"

## Adversarial Cases

| Case | Name | Result |
|------|------|--------|
| adv-01 | refusal-on-insufficient-input | ✅ PASS |
| adv-02 | refusal-on-non-sap-request | ✅ PASS |
