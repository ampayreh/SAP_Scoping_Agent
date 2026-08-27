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
for a genuinely intentional difference.

**A bug in this guardrail itself, found before being trusted:** the first
version used a strict `<` comparison, which — because the real historical
bug sits EXACTLY on the 0.5 ratio boundary (8192 / 16384 = 0.5 precisely)
— would have silently let the one concrete case this check exists to catch
pass through uncaught. Found by testing against the exact historical
values, not by inspection. Fixed to `<=`. 8 test cases run before commit,
all passing. See `DECISIONS.md` #14.

---

## ⚠️ 2026-08-26 — READ BEFORE CITING ANY PIPELINE NUMBER ABOVE

**Every pipeline quality, cost, and latency figure in this file and in
`DECISIONS.md` #8 through #14 was measured on runs where Skills 02 and 03
contributed EMPTY output.** Found while verifying Step 4's confidence/trace
instrumentation — the instrumentation's first real run surfaced it.

`call_claude_with_retry()` capped tool-use at 5 rounds. On this task the
model never self-terminates (it always wants another scope-item lookup),
so the loop routinely exited with `stop_reason` still `"tool_use"` —
leaving a response containing only `tool_use` blocks and **no text block**.
Text extraction then produced `""` from a response the model was never
given the chance to finish. No error, no warning; the empty string was
stored and billed as if it were valid output. Verified across historical
runs: Skills 02/03 output files are 0 bytes on the large majority of every
run in this session, going back to the first.

**Why it went unnoticed:** the judge graded the *concatenation* of all four
skills. Skills 01 and 04 each produced 40k+ characters, so the combined
text always looked substantial. Nothing compared per-skill output length to
zero. Every pipeline-vs-baseline number was computed against what was
effectively a two-skill pipeline.

**What this does and does not change, stated honestly:**

- **The "pipeline does not beat baseline" conclusion is not overturned —
  if anything it is reinforced.** A pipeline missing real content from two
  of its four steps would plausibly score *worse*, not better. But the
  comparison was not measuring what it claimed to measure.
- **The cost figures were UNDERSTATED, not overstated.** Skill 02 logged
  $0.67 while returning nothing; with the fix it costs $1.35 and returns a
  real 72k-character analysis. The headline "pipeline costs 8.4× the
  baseline" is therefore a floor, not the true multiple.
- **Every number above needs a full rerun before it can be trusted.** Not
  done here — this commit fixes the defect and flags the data; it does not
  regenerate it. **The n=3 tables above are retained deliberately, marked
  rather than deleted**, so the record shows what was believed and why it
  was wrong.

**Three fixes, in the order they were actually needed:**

1. **The forced-synthesis fallback is what fixes the bug** — not the round
   cap. If the loop exhausts with the model still requesting tools, the
   harness answers the pending tool calls and makes one final call with
   `tools` removed and an explicit instruction to stop and write the answer.
   **Removing `tools` alone was verified insufficient:** a first version did
   exactly that and the model returned `stop_reason='end_turn'` with zero
   content blocks and 8 output tokens — a genuinely empty response. The
   explicit instruction is the load-bearing part.
2. **`_MAX_TOOL_ROUNDS` 5 → 8, now a cost dial, not a correctness
   threshold.** Measured: at 20 rounds the model made 123 tool calls, cost
   $2.45 for one skill, and *still* returned empty text before the fallback
   existed. **Not empirically optimized** — no A/B across cap values was
   run. Measured: 2 rounds → 16 calls/$0.69; 8 rounds → 45 calls/$1.35;
   20 rounds → 123 calls/$2.45.
3. **Empty text is now always reported as a defect**, never returned
   silently: the harness prints `stop_reason`, block types, and output-token
   count so the next person gets a diagnosis instead of a mystery.

**A newly-surfaced issue this fix exposes but does NOT resolve:** Skill 02's
synthesis output is genuinely truncated — `final_stop_reason: "max_tokens"`,
`final_output_tokens: 16384/16384`, proven not inferred. Deliberately not
fixed here: raising one skill's `max_tokens` would trip Step 3's own
config-outlier guardrail (correctly — it would make the other three skills
outliers), so it is a deliberate config decision, not a one-line change.
Step 4's `confidence` field now reports `low` with that exact basis on every
affected run, which is precisely the job it was added to do.

**Process hazard found the hard way, recorded so it doesn't recur:** running
`eval.py` for verification **overwrites `evals/results.json` and
`evals/RESULTS.md` unconditionally**. A single-scenario verification run
during this work silently clobbered the committed n=3 dataset (12 results,
6 pairwise → 1 result, 0 pairwise) and wiped previously-committed notes from
this file. Both were recovered from git. Anyone running `eval.py` to verify
a code change on a branch carrying committed results should expect this and
restore afterward — or better, the harness should refuse to overwrite
committed results without an explicit flag. **Not fixed here** (out of this
step's scope); named so the next person is not surprised by it.

See `DECISIONS.md` #15 for the full account.

---

## 2026-08-26 — Cap-calibration probe: does the tool-round budget buy quality?

`_MAX_TOOL_ROUNDS` was set to 8 as an explicitly un-optimized middle ground
(#15). Before spending on a full rerun, this probe measured whether the
budget actually pays for itself. Method: generate the same scenario twice
(cap 2 vs cap 8), judge both absolutely, then run the blinded pairwise
comparison **5× on the identical pair** — generation is the expensive part
and happens once per cap, while judge calls are cheap, so repeating the
comparison directly addresses the ~1-in-5 verdict instability measured in
#13. Reproducible via `scripts/cap_probe.py`; raw data in
`evals/cap_probe.json`.

| | cap 2 | cap 8 |
|---|---|---|
| Cost (1 pipeline run) | **$2.06** | **$3.63** (+76%) |
| Tool calls | 24 | 54 |
| Latency | 1143s | 1156s (no real difference) |
| Total output | 225,838 chars | 224,207 chars |
| Absolute score (mean of 4) | 3.75 | **4.25** |
| Blinded pairwise (5 calls × 4 dims) | 6 wins | **12 wins** (2 ties) |

**The probe did not support the cheaper option, which is the opposite of
the hypothesis it was run to test.** Cap 8 leads on both grading modes.

**Two findings that make the result interpretable rather than just a
number:**

1. **Output volume is identical (within 0.2% per skill) because both caps
   are limited by `max_tokens`, not by the tool budget.** Skills 02 and 03
   hit `16384/16384` and report `confidence: low` under *both* caps. So the
   extra lookups do not buy *more* output — they buy better-grounded
   content inside the same fixed budget.
2. **The clearest gap is on SAP grounding (cap 8 wins 4–1)** — precisely the
   dimension the scope-item lookup tool exists to support. That mechanistic
   coherence is why this reads as signal rather than noise: the dimension
   that improved is the one more lookups should improve.

**Honest limits.** Generation is **n=1 per cap** on **one scenario** — the
5× repetition covers judge noise, not generation variance. One of the five
pairwise calls flipped to cap 2 on all four dimensions, a live reminder of
#13's instability. And this compares 2 vs 8 only; whether 8 is better than
12 or 20 is untested, and cost grows steeply (20 rounds → 123 calls on a
single skill, #15). **The probe is sufficient to reject the cheap option,
which is what it was run to decide — it is not a claim that 8 is optimal.**

**Decision: keep `_MAX_TOOL_ROUNDS = 8` for the full rerun.** The delta
across a full n=3 matrix is roughly $9 (~$15 vs ~$24), which is not worth
knowingly running a configuration the evidence says is worse.

---

## 2026-08-26 — Full rerun ATTEMPTED and BLOCKED: daily token quota

**The retraction above stands unresolved. No new numbers were produced.**
The full n=3 rerun decided on in #16 was attempted twice and blocked both
times by an account-level constraint, not a code defect.

**The blocker:** `429 - Too many tokens per day`. Sonnet 4.6's per-day
token quota on this account is **10,800,000** and is **not adjustable**
(Service Quotas `L-B29C9321`, doubled to `L-248E47B7` for the `us.`
cross-region profile). Only per-minute limits can be raised, and
per-minute was never the binding constraint.

**Measured, not guessed:** `state/*-metrics.json` shows **9,162,662 Sonnet
tokens consumed across 16 pipeline runs that day — 84.8% of the cap** —
before baselines. The cap-calibration probe, the Step 4 verification runs,
and the first rerun attempt had already spent the day's budget. The 429 was
arithmetic.

**Feasibility, now quantified:** one cap-8 pipeline run = 995,230 tokens; a
full n=3 matrix plus baselines ≈ **6.5M tokens, ~60% of a fresh day's
allowance**. Feasible with ~40% headroom for a retry — but only on a day
not already spent on other work. Judge calls draw on Haiku's separate 27M
budget and are not a constraint.

**Three fixes came out of the two failed attempts** (all tested, none
producing eval numbers):

1. **Rate-limit backoff separated from generic API-error backoff.** They
   had shared one schedule, so a throttled call waited 2s/4s/8s — 14
   seconds total — and gave up. Rate limits now get `[30, 60, 90, 120, 150]`
   (450s) and deliberately do not consume the general retry budget.
2. **Fast-fail on daily quota.** Fix #1 made this case *worse*: it spent 7.5
   minutes retrying an error the first response had already made certain.
   The harness now inspects the 429 body and raises in seconds, printing the
   quota-check command. Fails safe — anything not positively identified as
   per-day is still retried as per-minute.
3. **Checkpointing.** Attempt 1 lost all spend because results only reached
   disk at the very end. `evals/results.checkpoint.json` is now written
   after each completed iteration, on a **separate path** from
   `results.json` so a partial run can never overwrite a committed dataset.

**To confirm quota headroom before retrying:**

```
aws service-quotas list-service-quotas --service-code bedrock --region us-east-1
```

Do **not** pass `--no-paginate` — it silently returns only the first page
(6 quotas instead of 1,179), which briefly produced a confidently wrong
"no matching quotas" reading during this investigation.

---

## 2026-08-27 — CORRECTION to the note above, and attempt 3

**The quota is a ROLLING 24-HOUR WINDOW, not a calendar-day reset.** The
note above left this open; it was then asserted to be UTC-midnight-based.
That was wrong. Correcting it here rather than editing the earlier note, so
the mistake stays visible.

**Evidence.** Attempt 3 (02:17 UTC, 08-27) failed after 2 of 6 pipelines
with the same `429 Too many tokens per day`:

| Hypothesis | Tokens in window | Explains the failure? |
|---|---|---|
| Calendar day (08-27 only) | 2,038,209 — 18.9% of cap | **No** |
| **Rolling 24h** | **8,065,971 — 74.7% of cap** | **Yes** |

Requests had briefly succeeded 6.7 hours after the previous failure, which
looked like a reset. It was partial recovery: earlier runs aging out of the
rolling window freed just enough headroom for about two runs.

**Attempt 3 outcome:** 2 of 6 iterations completed. Zero per-minute
throttling. The daily-quota fast-fail worked — failed in seconds, not 450s.

**Checkpointing worked on its first real failure.** Four scored results and
two blinded pairwise comparisons (`scenario-a-agribusiness`, runs 0 and 1)
preserved in `evals/results.checkpoint.json`. Committed `results.json`
untouched. Attempt 1 had lost everything; attempt 3 lost nothing.

**No conclusions are drawn from that fragment.** Two runs on one scenario
is not a result. The scores are kept for provenance only — not analysed,
not compared, and they do **not** lift the retraction above.

**Structural finding, independent of any eventual quality number:** at
~1.0M tokens per pipeline run against a 10.8M rolling cap, this account
supports **about ten pipeline runs per 24 hours, total** — and one n=3
matrix needs ~60% of that. Input tokens are ~94% of consumption (8.66M of
9.16M measured on 08-26) because Skills 02/03 re-send an accumulating
conversation every tool round. **The pipeline is costly enough that
evaluating it is itself rate-limited.**

**When a full run fits** (needs prior-24h use ≤ 4.29M): first viable around
**18:30 UTC 08-27**; window fully clear **04:30 UTC 08-28**.

**Status: the retraction stands. Three attempts, no citable numbers.**
