# SAP Scoping Agent — Evaluation Results

Model: `us.anthropic.claude-sonnet-4-6` | Judge: `us.anthropic.claude-sonnet-4-6` | Runs per scenario: 3


## Pipeline vs Baseline

| Scenario | Method | Completeness | Accuracy | Actionability | SAP Grounding | Cost | Latency |
|----------|--------|:---:|:---:|:---:|:---:|------:|--------:|
| scenario-a-agribusiness | pipeline | 5 | 5 | 5 | 5 | $1.6729 | 448.0s |
| scenario-a-agribusiness | baseline | 5 | 5 | 5 | 4 | $0.1717 | 222.5s |
| scenario-a-agribusiness | pipeline | 5 | 5 | 5 | 5 | $1.6651 | 448.5s |
| scenario-a-agribusiness | baseline | 5 | 5 | 5 | 5 | $0.2174 | 274.0s |
| scenario-a-agribusiness | pipeline | 5 | 5 | 5 | 4 | $1.5084 | 742.9s |
| scenario-a-agribusiness | baseline | 5 | 5 | 5 | 5 | $0.2057 | 264.5s |
| scenario-b-high-tech | pipeline | 5 | 5 | 5 | 5 | $1.7111 | 476.6s |
| scenario-b-high-tech | baseline | 5 | 5 | 5 | 4 | $0.2500 | 289.4s |
| scenario-b-high-tech | pipeline | 5 | 5 | 5 | 5 | $1.7346 | 509.4s |
| scenario-b-high-tech | baseline | 5 | 5 | 5 | 5 | $0.2459 | 291.7s |
| scenario-b-high-tech | pipeline | 5 | 5 | 5 | 5 | $1.7406 | 499.0s |
| scenario-b-high-tech | baseline | 5 | 5 | 5 | 5 | $0.2500 | 282.6s |

## Adversarial Cases

| Case | Name | Result |
|------|------|--------|
| adv-01 | refusal-on-insufficient-input | ✅ PASS |
| adv-02 | refusal-on-non-sap-request | ✅ PASS |
