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


---

## 8. Eval harness fix: same-model judging, unblinded method label, missing Consistency dimension, ceiling-effect scoring

**Context:** The committed `evals/results.json` showed `"model"` and
`"judge_model"` as the identical value (`us.anthropic.claude-sonnet-4-6`),
and `JUDGE_MODEL`'s default in `eval.py` was literally `_DEFAULT_MODEL` —
the same variable used for the system under test. An unconfigured run
self-judged. Separately, `judge_output()`'s prompt to the judge included
`"Method: {method}"` before the output to grade, so the judge always knew
whether it was scoring the pipeline or the baseline before scoring
anything. And `benchmarks/benchmark-methodology.md` specifies five scored
dimensions including Consistency ("do repeated runs produce similar
quality"), but `JUDGE_RUBRIC` only asked for four — Consistency was
documented but never actually measured. Finally, the committed absolute
0-5 scores clustered almost entirely at 4 and 5 for both methods, which
is a ceiling effect: a same-scale judge with no comparison point tends to
default high, and a scale that can't spread scores apart can't tell you
which method is actually better.

**Why each of these is a real methodological problem, not a nitpick:**

- **Same-model judging is not evaluation, it's the model re-stating its
  own preferences.** A model grading its own output (or a same-family
  output) has no independent check on its blind spots — if it
  systematically over- or under-weights something, the judge shares that
  bias with the system under test. This is the textbook argument for an
  independent judge model, and this repo's own README asserted the judge
  was "separately configurable... to avoid self-evaluation bias" without
  the default actually doing that.
- **An unblinded method label lets the judge's prior about "agentic
  pipelines are more thorough" do the scoring instead of the content.**
  Once the judge is told `Method: pipeline`, any score it assigns is
  confounded with whatever expectation "pipeline" carries — there is no
  way to tell from the resulting number whether the pipeline actually
  produced better content or the judge expected it to.
- **A documented dimension nobody computes is worse than no dimension.**
  Anyone reading `benchmark-methodology.md` and then `results.json` would
  reasonably assume Consistency was being measured somewhere. It never
  was.
- **A 0-5 absolute scale a judge defaults to 4-5 on cannot discriminate.**
  If every response — good or mediocre — gets scored near the ceiling,
  the number stops carrying information about which is better. This is a
  known failure mode of single-output absolute-scale LLM judging, and the
  committed data shows exactly this pattern.

**Fixes, one per problem:**

1. **`JUDGE_MODEL`'s default is now a different model line than
   `MODEL_ID`'s default (Opus vs. Sonnet), not just an independently
   overridable variable that happened to default to the same value.**
   `JUDGE_INDEPENDENT = MODEL_ID != JUDGE_MODEL` is computed at import
   time and, if false, the harness prints a loud stderr warning before
   doing anything else — same-model judging is still permitted (an
   operator may have a real reason, e.g. only one model line available in
   their region), but it can never happen silently again. `results.json`
   now carries `"judge_independent": true/false` and `RESULTS.md` states
   it plainly in the header, so independence is verifiable at a glance
   instead of requiring someone to compare two JSON fields by hand.

2. **`judge_output()` no longer takes or sends a `method` argument.** The
   prompt now sends only the scenario ID (for domain context — it does
   not identify which method produced the output, since both methods run
   against the same scenario) and the output text. `JUDGE_RUBRIC` was
   also given an explicit instruction not to guess or speculate about
   what process produced the output.

3a. **Consistency is now computed programmatically in
    `compute_consistency()`, not judged.** For each (scenario, method), the
    four absolute dimension scores per run are averaged into one "run
    quality" scalar, and the standard deviation of that scalar across runs
    is mapped to a 0-5 band matching `benchmark-methodology.md`'s own
    descriptions (stddev 0 → 5, "near-identical"; stddev > 1.5 → 0,
    "wildly different"). This is deterministic and reproducible from the
    same raw scores every time, which is a stronger match to what the
    methodology doc is actually asking than a judge's one-shot qualitative
    guess would ever be. **Honest limitation, stated in both the code and
    `RESULTS.md`:** with only 2-3 runs per scenario, the sample standard
    deviation is noisy — these numbers are indicative, not statistically
    rigorous, until run counts are materially higher.

3b. **Added a blinded pairwise comparison mode (`judge_pairwise()`),
    run alongside the absolute scoring, not instead of it.** For every
    run where both methods produced output, both are shown to the judge
    anonymized as "Response A" / "Response B", with which one is A
    randomized per call via `random.random()` and never revealed to the
    judge. The judge picks a winner or declares a tie per dimension and
    must quote a verbatim excerpt as evidence for every judgment,
    including ties. The A/B assignment is recorded (for our own
    bookkeeping, never sent to the judge) so the winner can be decoded
    back to "pipeline" / "baseline" / "tie" after the call returns.
    `RESULTS.md` reports aggregate win/tie counts per dimension across all
    scenarios and runs, plus a handful of the actual quoted excerpts so a
    reader can spot-check that the judge engaged with content rather than
    defaulting to a label.

**Verification method, honestly stated:** the new code was validated with
a stubbed Anthropic client that returns canned JSON and records every
prompt sent, run as an offline self-test (not committed — it exercises
internal functions directly, not a public contract). It confirms: (a) no
`Method:` label or the words "pipeline"/"baseline" appear in either the
absolute or pairwise judge prompts; (b) the pairwise A/B assignment is
actually randomized across trials, not fixed; (c) the pairwise decode
maps a canned "A" verdict back to whichever method was actually assigned
to A in that trial, correctly, every time; (d) the consistency computation
gives a zero-stddev, score-5 result for identical repeated scores and a
lower score for varied ones; (e) `write_results()` produces valid JSON and
Markdown containing all three new sections without crashing. **This
confirms the code's logic is correct. It does not confirm what the model
actually says when asked these blinded questions for real** — that
requires a live API run, which this fix's authoring session did not have
credentials to perform. See the open item in `evals/RESULTS.md` and this
repo's `README.md`.

**Why this is the same discipline as #7:** #7 root-caused an eval failure
to the test being wrong, not the agent, and fixed the test rather than
guessing at the agent. This entry does the same thing one level up: the
eval *harness itself* — not any scenario, not the orchestrator, not the
skills — was measuring the wrong thing in three independent ways, and all
three are now fixed at the layer that actually caused them.


---

## 9. First real run under the #8 fix: honest result, and one new finding

**Context:** #8 fixed the eval harness (independent judge, blinded absolute
scoring, blinded pairwise comparison, computed consistency) but could not
be run for real in that session — no API credentials were available. This
entry records the first actual run under the fixed harness: 2 scenarios ×
3 runs, `us.anthropic.claude-sonnet-4-6` as the system under test,
`us.anthropic.claude-opus-4-6-v1` as the independently-verified judge
(confirmed with a live `invoke_model` call before the run — the naive
`us.anthropic.claude-opus-4-6` guess in #8's first draft did not exist and
was corrected to the `-v1` suffix after checking `list-inference-profiles`
against the actual account).

**The result, stated plainly, as instructed: the pipeline does not beat
the baseline on quality in this run.** Absolute scores still cluster at
4-5 for both methods on every dimension — the ceiling effect #8 named is
real and confirmed, absolute scoring alone still can't discriminate. The
blinded pairwise comparison, which exists specifically to break that
ceiling, shows the **baseline winning or tying more often than the
pipeline on every dimension**: across 6 runs × 4 dimensions (24
judgments), baseline was preferred 13 times, pipeline 9 times, 2 ties.
The gap is worst on **actionability** (baseline preferred 4 of 6,
pipeline 1, tie 1) — the dimension most directly about whether a
consultant could use the output as-is, and the one most plausibly hurt by
the truncation finding below. Completeness and SAP grounding were split
close to even (3-3 each); accuracy leaned baseline (3-2, 1 tie).

**Cost and latency are not close.** Pipeline runs averaged $1.71 versus
$0.23 for baseline — **about 7.4× the cost** — and 476s versus 273s
latency — **about 1.75× the time**. Combined with the quality result
above: on these two scenarios, the orchestrated pipeline costs roughly
7× more, runs roughly 1.75× slower, and is not judged better on any
dimension in blinded head-to-head comparison. **This is the honest
number, not a hedged one.** It is also, per the discipline #8 argued for,
a stronger applied-AI story than a fabricated win would have been: the
harness was built to actually discriminate, and when it did, it found a
result the author didn't get to pick.

**One caveat that cuts the other way, stated with equal honesty:** n=3
runs per scenario on 2 scenarios is a small sample, and the
`Consistency` band above (computed, not judge-estimated) shows both
methods scoring 4-5 — i.e. both are reasonably stable, so the pairwise
split is unlikely to be pure noise, but it is not a large-sample result
either. A materially higher `--runs` count would sharpen this, not soften
it — the honest expectation given this data is that more runs would
likely confirm the same direction, not reverse it, but that is an
expectation, not a re-run result.

**New finding, verified with direct evidence, NOT fixed here (in scope
for a future PR, not this one):** Skill 01 (Client Discovery Intake) hits
its `max_tokens` ceiling (8192) on **6 out of 6 runs**, in both scenarios,
with zero variance in output token count — the textbook signature of
truncation, not content that happens to land exactly at a limit.
Confirmed directly by inspecting a raw output file
(`state/run-20260825T232632-skill-01.json`): the file ends mid-sentence,
mid-string, with no closing braces — `"...ranged from $18M to $40M` and
then nothing. This is a real defect in `orchestrator.py`'s `SKILLS` config
(`01-client-discovery-intake.md`'s `max_tokens: 8192`), not in the eval
harness, and per this fix's own scope boundary
(`orchestrator.py`/`skills/` untouched) it is documented here rather than
patched. It plausibly explains some of the actionability and completeness
losses above, since Skill 01's output feeds every downstream skill — but
that is a hypothesis, not verified by this entry, and should not be
overstated.

**Why this belongs in DECISIONS.md rather than only in RESULTS.md's
tables:** the raw tables are generated deterministically and carry no
interpretation. The interpretation — that the negative result is real,
that it should be reported as the honest number, and that a new,
separately-scoped defect was found in the same pass — is exactly the kind
of judgment call this file exists to record, per #6, #7, and #8's
established convention.


---

## 10. Skill 01's max_tokens fix, verified; an interim Haiku-judged re-check;
    two new bugs found and fixed along the way

**The fix (Step 1).** Skill 01 ("Client Discovery Intake") was configured
with `max_tokens: 8192` while Skills 02-04 all use 16384 — the exact
truncation signature #9 confirmed by reading a raw output file directly
(ended mid-sentence, no closing braces, on 6 of 6 prior runs with zero
variance). Changed to 16384 to match the other three skills. Nothing
else in `orchestrator.py` was touched.

**Verified against the actual system under test, not a stand-in.** A
cheap sanity check first used Haiku (fast, near-free) per the original
plan, and it was still truncated — at the *new* 16384 ceiling this time,
with zero variance again. That result was correctly not treated as proof
the fix failed: Haiku is a different model with different verbosity on
this exact prompt, not the model this bug was diagnosed against or the
model Step 3 actually uses. Re-run against Sonnet (the real system under
test): both scenarios produced complete output well under the new ceiling
(10,814 and 11,765 tokens, neither pinned to 16384), and both files were
read directly and confirmed to end on a complete sentence or a closed
table row, not mid-word. The fix is real for the model it needed to be
real for.

**Bug found #1: judge_output()'s max_tokens=1000 silently truncated with
Haiku as judge.** The first live rerun under the fixed Skill 01 (Sonnet
system-under-test, Haiku judge, n=1 x 2 scenarios) produced an Absolute
Scores table that was entirely empty placeholders — every one of the 4
`judge_output()` calls returned `{"error": "Unterminated string..."}`
rather than crashing loudly, so the failure did not surface as an
exception; it surfaced as missing data in the generated report. Root
cause: `max_tokens=1000` was calibrated against Opus's more compact
reasoning style (the original harness fix in #8 was verified with Opus as
judge) and was too tight for Haiku's longer per-dimension reasoning on
this identical rubric shape. `judge_pairwise()`'s `max_tokens=1500`
completed successfully in the same run — but investigating *why* showed
1500 was closer to the edge than it looked, since pairwise's rubric asks
for strictly *more* content per dimension (a mandatory quote, on top of
winner + reasoning) than the absolute rubric does (score + reasoning
only), yet had 50% more budget and still barely cleared. Both budgets are
now 2048, with the reasoning for each documented inline at the call site.

**Recovery method, and its one honest limitation.** Rather than re-pay
for the expensive pipeline-generation calls (~$1.8-2.1/scenario, already
spent and still valid — only the *judge* call on top of them had failed),
the pipeline text was reconstructed for free from the already-saved
`state/run-*.json` files (the orchestrator's own full state persistence,
loaded via `PipelineState.from_dict()`) and re-judged with the fixed
budget. Baseline text was not persisted anywhere on disk in the original
run, so it was regenerated fresh (~$0.20-0.25/scenario) and judged. **The
limitation this creates, stated plainly:** the recovered ABSOLUTE
baseline score and the EXISTING PAIRWISE baseline comparison are judged
against two different baseline generations, not the same one — baseline
generation is not deterministic, and the original text used for pairwise
no longer exists to re-judge absolute against. This is acceptable for an
interim, cost-minimized check; it would not be acceptable for the full
n=3 rerun, which should generate once and judge every mode against that
same generation.

**Bug found #2: adv-01's dollar-figure regex flagged a legitimate
citation as fabrication.** The same rerun that surfaced bug #1 also
flipped a previously-passing adversarial case (#7's 32/32) to failing:
`must_not_match_regex: '\$[\d,]' matched ('$5')`. Investigated by
reproducing the case and reading the full output, not the 500-character
excerpt results.json stores — the match was
`"SAP's portfolio spans products ranging from ~$1,500/year (SAP Business
One starter) to multi-million dollar enterprise programs"`, cited to
explain *why* "We want SAP" alone is too vague to scope. That is the
correct reasoning this case wants to see, not a fabricated client-specific
estimate, and the plausible connection to the Skill 01 fix is real: at
the old 8192 ceiling this explanatory passage may never have been reached
before truncation; with it removed, the model's now-complete answer
includes content a narrow regex hadn't been tested against.

Fixed narrowly, not by loosening the check generally:
`_find_fabricated_dollar_figure()` excludes a dollar-figure match only
when the ~150 characters preceding it contain an explicit two-sided price
range ("ranging from" / "range of") or a named real SAP product/tier
(SAP Business One, S/4HANA Cloud Public/Private Edition, GROW with SAP,
RISE with SAP). Deliberately does NOT include soft hedge words like
"typically" or "for example" — those could still precede a genuinely
fabricated client-specific number ("Given typical SAP projects, your
budget is likely $2,000,000" must still be caught). Verified with 5
targeted cases before spending any more API calls: the real false
positive is excused; a bare fabricated figure, a hedge-worded
fabrication, and a second named product tier all behave correctly in
both directions. Then verified live: both adversarial cases pass
(32/32 restored).

**The honest result of this interim check, stated plainly: the pipeline
still does not beat the baseline, and this run is the most lopsided
result against it yet.** Blinded pairwise: baseline preferred on **8 of
8** dimension-judgments (both scenarios x all 4 dimensions), 0 pipeline
wins, 0 ties — more one-sided than #9's n=3/Opus-judged 13-9-2. Absolute
scores (now real, Haiku-judged, not placeholders) show a more mixed
picture worth naming rather than smoothing over: scenario-a's pipeline
mean (4.25: 4/4/4/5) edges its baseline mean (3.75: 4/4/3/4), diverging
from that same scenario's pairwise verdict (baseline swept all 4
dimensions); scenario-b's baseline mean (5.0) clearly beats its pipeline
mean (3.75: 4/4/3/4), consistent with its pairwise sweep. Cost and
latency are unchanged in direction: pipeline ran $1.83-2.12/scenario
against baseline's $0.20-0.25, and 534-649s against 259-276s.

**This is n=1 per scenario — an interim, cost-minimized check, exactly as
scoped, not a replacement for the full n=3 rerun.** The pending full
rerun (both scenarios, 3 runs each, Sonnet system-under-test, Haiku
judge, single baseline generation per run judged both ways to avoid this
entry's one limitation) should replace these numbers when it runs, per
the same standing rule #9 established: whatever it shows, including if
the pipeline still doesn't beat the baseline, replaces the number here —
not a rewritten version of this entry.


---

## 11. The full n=3 rerun: the pending number from #10, now real —
    plus one more test bug found and a retry mechanism added

**This is the full rerun #9 and #10 both flagged as pending. It replaces
their interim numbers, per the standing rule: whatever it shows,
including if the pipeline still doesn't beat the baseline, replaces the
number here — not a rewritten version of either entry.** 2 scenarios x 3
runs, `us.anthropic.claude-sonnet-4-6` system under test,
`us.anthropic.claude-haiku-4-5-20251001-v1:0` judge (independence
confirmed), both grading modes, blinded pairwise, adversarial cases.

**The honest result, stated plainly: the pipeline does not beat the
baseline, on either grading mode.**

- **Absolute scoring shows a dead tie.** Scenario-a: pipeline mean 4.25,
  baseline mean 4.25 — identical. Scenario-b: pipeline mean 5.0, baseline
  mean 5.0 — identical. Consistency (computed, not judge-estimated) is
  also identical between methods per scenario: 2/5 for both methods on
  scenario-a (real run-to-run variation — scores ranged 3-5 across the 3
  runs for both), 5/5 for both on scenario-b (perfectly stable at 5,5,5,5
  regardless of method or run). Absolute scoring cannot tell these two
  methods apart on this data, at all.
- **Blinded pairwise — the mechanism built specifically to break that
  tie — shows baseline clearly preferred.** Across 6 comparisons x 4
  dimensions (24 judgments): baseline preferred **16**, pipeline
  preferred **7**, tie **1**. Worst on actionability (baseline 5,
  pipeline 1) — the dimension most directly about whether a consultant
  could use the output with less rework. Completeness and SAP grounding
  both lean baseline (4-2 each); accuracy is closest (3-2, 1 tie).
- **Cost and latency are unambiguous.** Pipeline averaged $1.88/run
  against baseline's $0.22 — **8.4x the cost**. Pipeline averaged 563s
  against baseline's 268s — **2.1x the latency**. Combined with the
  quality result above: the orchestrated pipeline costs roughly 8x more,
  runs roughly 2x slower, is tied with the baseline on absolute scoring,
  and is preferred less often than the baseline in blinded head-to-head
  comparison. **On these two scenarios, at this sample size, there is no
  quality basis for the added cost.** This is the honest number, not a
  hedged one, and it is now the full-sample result, not an interim
  smaller-n check.

**One more test-design bug found and fixed, same pattern as #10's
adv-01 fix.** This run's adversarial pass initially failed adv-02
("refusal-on-non-sap-request") on `must_not_contain: 'creative concept'
found`. Reproduced and read the full output, not the excerpt: the agent
gave a clean, correct refusal that explicitly named the categories of
deliverable it was declining --- *"I won't be able to produce campaign
plans, creative concepts, or launch strategies here."* That is the
correct behavior this case wants to see (declining, while explaining
what it's declining, is good UX), not a fabricated marketing deliverable
-- a bare substring match can't tell "the agent named this as something
it refuses" from "the agent produced this." Same root cause as adv-01,
different case.

Fixed narrowly, mirroring adv-01's fix: `_find_marketing_deliverable()`
excuses a banned phrase (`"creative concept"`, `"target audience:"`,
etc.) only when refusal language ("won't", "can't", "declin...", "not
designed to", "outside what/my", "not the/a right tool") appears in the
150 characters immediately preceding it. A genuine violation -- the
agent actually producing a "Target Audience:" section with real content
and no refusal language anywhere nearby -- is still caught; verified
with 4 targeted cases (the real false positive excused; a genuine
violation caught; a refusal naming a *different* banned phrase excused;
bare deliverable content with no refusal nearby caught) before spending
any API calls, then live: 32/32 restored.

**A second, different-shaped failure: one absolute-judge call failed to
parse, unrelated to truncation.** `scenario-b-high-tech` pipeline run 2
of 3 returned `{"error": "Expecting ',' delimiter..."}` from
`judge_output()` despite the #10 fix. Investigated before assuming the
2048-token budget was still insufficient: reconstructed the exact same
pipeline output from its saved state file and re-invoked the judge
directly, capturing the raw response this time instead of only the parse
error. Result: 1,194 output tokens (well under the 2048 cap -- not
truncated) and a clean, valid, complete JSON response on the very next
call. This is an occasional, non-deterministic JSON-formatting glitch
from the judge model, not a systematic budget problem, and needed a
different fix than #10's.

**Fix: `_call_judge_and_parse()`, a shared retry wrapper used by both
`judge_output()` and `judge_pairwise()`.** Retries the *whole* API call
(not just the parse -- re-parsing identical malformed text can't fix it)
on `json.JSONDecodeError` or a transient `anthropic.APIError`, with the
same exponential backoff style as `orchestrator.py`'s existing
`call_claude_with_retry` (`2 ** (attempt+1)` seconds), up to 3 attempts,
raising the last error if every attempt is exhausted so a genuine,
persistent failure still surfaces rather than looping forever or hiding
the failure class. Verified with 3 mocked-client unit tests before
spending any API calls: recovers cleanly after one bad call and one
retry; raises (does not silently swallow) after exhausting all retries;
`judge_output()`'s outer wrapper still correctly turns an exhausted
retry into `{"error": ...}` for the harness's existing reporting flow.
The one gap this run produced was then filled live using the new
retry-enabled path -- succeeded on the first attempt, no retry needed.

**Why this is the right layer for this fix, and #10's token-budget fix
was the right layer for that one.** Two different failure modes got two
different fixes: #10's was systematic (every call under a given budget
with a given model failed the same way, every time) and needed a bigger
budget; this one is occasional and non-deterministic (the exact same
request succeeds nearly every time) and needed a retry, not a bigger
budget -- bumping tokens further would not have prevented an occasional
malformed delimiter. Matching the fix to the actual failure mode, not
applying the same fix reflexively to every judge-call problem, is the
same discipline #7 and #10 already established.

**All twelve absolute-score cells and all six pairwise comparisons in
`evals/RESULTS.md` are now real data from real API calls -- no
placeholders, no `{"error": ...}` entries, no interim/smaller-n caveats
remaining.** This entry is the terminal state of the eval-harness fix
that began at #8: judge independence, blinding, computed consistency,
pairwise comparison, two root-caused test-design bugs, a token-budget
fix, and a retry mechanism, all verified against real committed data
rather than asserted.


---

## 12. Interview-prep rigor pass, Step 1 of 4: confidence intervals and a
    real significance test on the final comparison

**Context.** Prepping to talk about this work honestly in an interview
surfaced a real gap #11's headline numbers had been quietly resting on:
"pipeline mean 4.25, baseline mean 4.25" and "16 of 24 baseline-preferred"
were reported as means and counts with no stated uncertainty, no test of
whether the observed difference (or lack of one) could plausibly be noise,
and no explicit statement of how much statistical weight n=3 can actually
bear. Every number in #11 was real, computed correctly, and honestly
reported — but "honestly reported" and "statistically characterized" are
not the same claim, and an interviewer asking "how confident are you in
that tie?" deserved a computed answer, not a shrug.

**What was added, in `eval.py`:**

- `_bootstrap_ci()` — a percentile bootstrap 95% CI, used instead of a
  normal-approximation interval (`mean +/- 1.96*SE`) because the normal
  approximation's validity depends on the Central Limit Theorem having
  enough data to approximate a Gaussian sampling distribution, which n=2-3
  cannot supply. Documented honestly in its own docstring: with n=3, there
  are only `3**3 = 27` distinct bootstrap resamples, so 10,000 resamples is
  10,000 draws from a genuinely small set of 27 outcomes, not 10,000
  independent pieces of information. The CI is real and correctly computed;
  it is not a rich picture of the true population spread at this n, and the
  docstring says so rather than letting the large resample count imply more
  precision than the underlying data can support.
- `_exact_paired_permutation_test()` — the primary significance test,
  exact at any sample size (no normal/asymptotic approximation, unlike a
  t-test or Wilcoxon's usual p-value). Its docstring works out the actual
  floor: for n paired observations there are `2**n` possible sign-flip
  relabelings, so the smallest two-sided p-value any dataset of that size
  can ever produce is `2 / 2**n`. **At n=3, that floor is 0.25 — this test
  cannot reach conventional significance (p<0.05) at this sample size,
  regardless of how large the true effect is.** This is stated in the code
  comment, computed and printed with every result (`min_achievable_p_at_this_n`),
  and repeated in `RESULTS.md` so it can never be silently missed by a
  reader skimming past a p-value to a mean.
- `_wilcoxon_signed_rank()` — `scipy.stats.wilcoxon` as a second, standard
  cross-check when scipy is installed (now optional in `requirements.txt`);
  reports why it's unavailable rather than crashing when it isn't, or when
  every paired difference is exactly zero (scenario-b-high-tech's case —
  every one of 3 runs scored identically for both methods, leaving nothing
  for a rank-based test to rank).
- `compute_significance()` — per scenario, pairs pipeline and baseline
  runs by matching run index (run 0's pipeline vs. run 0's baseline, etc.
  — the closest thing this harness produces to a matched pair, since both
  were generated within the same eval iteration), and reports mean/stdev/CI
  for each method plus both significance tests on the paired differences.
  Scenarios run with `--pipeline-only`/`--baseline-only` correctly produce
  no entry, since there is nothing to pair.
- A directional-only disclaimer, printed to stdout and written into
  `RESULTS.md`, fires automatically whenever a scenario has fewer than 10
  paired runs (`SIGNIFICANCE_DISCLAIMER_THRESHOLD_N`) — currently every
  scenario on file, since `--runs 3` is the largest run so far.

**Applied against the real, already-committed n=3 data (#11) at zero
additional API cost** — this is pure recomputation over existing judge
scores, no new model calls. Result: permutation test observed mean
difference = 0.0 for both scenarios (an exact match to #11's "dead tie"
finding, now with a computed p-value of 1.0 attached, at the test's own
stated floor of p=0.25 either way), Wilcoxon agrees where it can run.
Verified with three hand-built edge cases before trusting the real output:
n=1 correctly reports a min-achievable-p of 1.0 (a single paired run can
never show significance at all, the most extreme possible statement of
"underpowered"); a pipeline-only scenario correctly produces no paired
entry; mismatched run indices (pipeline has runs 0-1, baseline only has
run 0) correctly pair only the shared index.

**What this does NOT close, stated plainly rather than papered over.**
This makes the size of the "not enough runs" gap explicit and computed
instead of asserted in prose — it does not, and cannot, make n=3 into a
statistically powered comparison. The permutation test's own floor
(p≥0.25 at n=3) is the honest ceiling on what this comparison can ever
claim until `--runs` is materially higher (the docstring's math applies
identically at n=5, n=10, wherever the next real run lands — the floor is
`2/2**n`, so it improves fast: n=5 → 0.0625, n=7 → 0.0156, both below the
conventional 0.05 line). The bootstrap CI has the same underlying-data
limitation: real, correctly computed, but resampling 3 points 10,000 times
does not manufacture statistical power that 3 points do not have. Anyone
citing this comparison should cite the tie and the p-value together, not
the tie alone.


---

## 13. Interview-prep rigor pass, Step 2 of 4: does the judge score
    identical input the same way twice?

**Context.** Every finding in this file that cites a judge score or a
pairwise verdict (#8-#12) implicitly assumes the judge is a stable
measuring instrument — that if you asked it to grade the exact same
output twice, it would give roughly the same answer. That assumption had
never actually been tested. It was time to test it before defending any
of those numbers in an interview.

**What was added, in `eval.py`:**

- `--judge-reliability-check` (opt-in flag, off by default — this is a
  diagnostic, not a per-eval necessity) and `--reliability-n` (default 5).
- `_load_or_create_reliability_fixture()`: on first invocation, generates
  ONE real pipeline run and ONE real baseline run and saves both under
  `evals/fixtures/`. This one-time generation was unavoidable — baseline
  output has never been persisted anywhere else in this harness (see
  #10/#11, where recovering it after the fact needed a fresh call too) —
  but every subsequent invocation loads the saved files and makes ZERO
  system-under-test calls. This is deliberate, not just cheap: regenerating
  the pipeline/baseline text on each check would mix the system-under-test's
  own non-determinism into a test specifically designed to isolate the
  judge's, and the two sources of variance would be impossible to tell
  apart in the result.
- `run_judge_reliability_check()`: calls the judge N times on the identical
  fixed pair via both `judge_output()` and `judge_pairwise()`, reports the
  min/max/range of absolute scores per dimension per method, and the vote
  distribution of blinded winners per dimension.

**The real result (N=5, `scenario-b-high-tech`, Haiku judge), stated
plainly:** absolute scoring is fairly stable. Pipeline scored 5/5/5/5 on
4 of 5 calls and 4/4/4/4 uniformly lower on the fifth — one harsher call
across the board, not scattered per-dimension noise. Baseline scored
5/5/5/5 on all 5 calls, zero variance.

**Blinded pairwise verdicts are markedly less stable, and one dimension
has a real problem.** Completeness (4/5 pipeline, 1 flip) and
actionability (4/5 baseline, 1 flip) show a genuine, if imperfect,
majority. SAP grounding is weaker: baseline wins 3/5, with 2/5 flipping
away from it. **Accuracy has no stable majority at all** — the five
identical calls voted pipeline, pipeline, baseline, tie, baseline: a
literal 2-2-1 split. Asked to grade the exact same accuracy comparison
five times, the judge did not converge on an answer.

**A bug found in this new code itself, before it was trusted.** The
first version used `statistics.mode()` to compute a "majority verdict."
`mode()` does not raise or flag a tie among equally-frequent values — it
silently returns whichever one appears first in the input list. Against
accuracy's real 2-2-1 split, this returned `"pipeline"` (the first vote
in the list) as "the majority" and would have reported "3 of 5 flipped
from the majority" — technically arithmetically true, but a misleading
frame for a result that has no majority at all. Caught by reading the
raw vote list before trusting the summary line, the same discipline
every other bug in this file was caught with. Fixed: vote counts are now
computed via `Counter`, a strict-plurality check (`len(leaders) == 1`)
determines whether a stable majority exists at all, and the full vote
distribution (`vote_counts`) is always reported alongside — never a
single number standing in for a distribution that might not have a
single most-common value.

**What this means for every comparison already on file, stated
honestly.** #9 through #11 built their findings from *independent* judge
calls — different runs, never the identical input graded twice — so
nothing here invalidates them; averaging across independent samples is
exactly the right response to per-call noise, and that's what the
aggregate pairwise counts in #11 already do. What this DOES mean: a
*single* pairwise verdict, especially on accuracy, carries real,
now-measured judge noise on top of whatever true quality difference
exists between pipeline and baseline. If asked in an interview "how much
do you trust one individual pairwise call," the honest answer is now a
number, not a shrug: on this fixture and this judge, roughly 1-in-5
identical calls flip on three of four dimensions, and the fourth
dimension doesn't reliably converge at all.

**What this does NOT close, stated plainly.** This is one fixture pair,
one scenario, one judge model, N=5. It does not tell you whether Opus
(the judge used in #11's headline n=3 result) is more or less reliable
than Haiku, whether a different scenario would show the same
per-dimension pattern, or whether accuracy's instability here is a
property of this judge model generally or an artifact of this specific
pair being genuinely close in quality (both outputs scored near-perfect
on the absolute scale, which plausibly makes a close pairwise call
noisier than a lopsided one — a real hypothesis, not a proven one, since
there is only one fixture pair to check it against). A second fixture
pair, ideally one with a clearer quality gap between methods, would be
the natural next check — not built here, named here.


---

## 14. Interview-prep rigor pass, Step 3 of 4: a preventive guardrail,
    not another after-the-fact discovery

**Context.** Every single bug documented in this file — the Skill 01
`max_tokens` mismatch (#10), the two adversarial-eval false positives
(#10, #11), the judge budget/retry issues (#10, #11) — was caught the
same way: by re-reading output, or a raw file, or a log, after a run had
already happened. Nothing in the harness itself had ever caught a
problem before spending an API call on it. Asked "what would have caught
the original Skill 01 bug automatically," the honest answer before this
step was "nothing — it took someone reading six runs' worth of raw JSON
by hand."

**What was added, in `orchestrator.py`:**

`validate_skill_config(skills, field="max_tokens", outlier_ratio=0.5)`,
called once at the very top of `run_pipeline()`, before the API client is
even constructed. Flags any `SKILLS` entry whose `field` value is at or
below `outlier_ratio` of the group's maximum, and reports every outlier
found — skill ID, name, the value, the group max, the ratio — before a
single token is spent. Deliberately generic: `field` is a parameter, not
hardcoded to `max_tokens`, so a future per-skill numeric config value
(a timeout, a retry count, anything comparable across the four skills)
reuses this same function rather than needing a second copy.

**Design decision, made explicitly rather than defaulted into: fail, not
warn.** The task description offered both options. Chosen to fail
(`raise ValueError`) because a warning is precisely the failure mode
already demonstrated not to work — the real Skill 01 bug produced
silently wrong output on 6 consecutive runs with nothing in the pipeline
ever printing so much as a warning, because nothing was checking. This
guardrail runs before any API call, so failing costs nothing (no wasted
spend, no wasted wall-clock) and converts a scroll-past-able line into a
decision that has to be made. An escape hatch,
`ALLOW_CONFIG_OUTLIERS=1`, downgrades the failure to a printed warning
for a case where the difference is genuinely intentional — the guardrail
is a locked door with a key, not a wall with no way through.

**A bug in the guardrail itself, found before it was trusted.** The
first implementation compared with strict `<`
(`val < outlier_ratio * group_max`). The real bug this check exists to
catch is `max_tokens: 8192` against siblings at `16384` — and
`8192 / 16384` is exactly `0.5`, sitting precisely on the boundary a
strict `<` comparison excludes. Tested against the literal historical
values before trusting the function (not just reasoned about abstractly)
and the test caught it immediately: the exact bug this guardrail was
built to catch would have passed through uncaught by its own first
version. Fixed to `<=`, with the reasoning for that specific operator
choice written into a code comment so a future edit doesn't quietly flip
it back.

**Full test coverage run before commit** (all local, zero API cost — this
step needs no model calls): the current real `SKILLS` config (uniform
16384s) passes silently; the exact historical bug shape raises and names
the skill; the escape hatch downgrades to a warning; a single-skill list
has nothing to compare against and doesn't crash; a config with a
non-numeric field value doesn't crash; the exact boundary value (8192 vs
16384) raises; one step past the boundary (8193 vs 16384) does not raise.

**What this does NOT close, stated plainly.** This catches one shape of
config problem — a per-skill numeric value sitting far below its
siblings — and only for whatever field is passed to it (only
`max_tokens` is wired into `run_pipeline()` today). It does not validate
prompt content, tool wiring, model IDs, or any other class of
misconfiguration; it is a first guardrail, scoped exactly as small as the
task asked for, not a general config-linting framework. The
`outlier_ratio=0.5` default is a deliberate, literal match to the one
real bug on file, not a value derived from any broader analysis of what
ratio should generally be considered suspicious — a future, different
kind of outlier (say, a value 30% below its siblings rather than 50%)
would not be caught by the current default, and that's a real, named
limitation rather than an implied one.


---

## 15. Interview-prep rigor pass, Step 4 of 4: confidence/trace
    groundwork — and the silent empty-output bug it immediately exposed

**What Step 4 asked for** (explicitly scoped small, no UI): a
`confidence` field and a `trace` field on each skill's output in the
`state/` JSON, so "what does confidence actually trace to" has a
concrete answer rather than a promise.

**What was added, in `orchestrator.py`:**

- `_estimate_confidence(skill_id, metrics, max_tokens)` — returns
  `{"level": "high"|"medium"|"low", "basis": "<one line>"}`. The
  heuristic is written into the function's docstring rather than left
  implicit: `low` if the final response hit its token ceiling
  (truncation risk, regardless of content); otherwise for tool-using
  skills (02/03) the level is tied to what fraction of
  `lookup_scope_items` calls returned a real match — `high` ≥70%,
  `medium` ≥40%, `low` below that, on the reasoning that a module-fit
  claim grounded in a confirmed scope item is better supported than one
  the model reasoned out after an empty lookup. Skills 01/04 have no
  tool-grounding signal available at all, so they report `medium` with a
  basis that says exactly that — deliberately not `high`, because
  "nothing was detected wrong" is not evidence of correctness.
- `trace`: `{"tool_calls": [{tool, query, result_count, result_ids}, ...],
  "upstream_skills": [...]}`. Both already existed implicitly — the query
  and result were computed to build the next message, and upstream
  dependencies were visible in `build_user_message` — but were discarded
  once the loop moved on. Now captured in the output JSON instead of
  living only in a terminal's scrollback.

**Then verifying it against a real run immediately exposed a much larger
bug, which is the real story of this entry.**

**The bug: Skills 02 and 03 had been silently producing EMPTY output on
most runs across this entire session.** `call_claude_with_retry()` capped
the tool-use loop at 5 rounds:

```python
while response.stop_reason == "tool_use" and max_tool_rounds > 0:
```

On this task the model never self-terminates — it always wants another
scope-item lookup. So the loop routinely exited with `stop_reason` still
`"tool_use"`, leaving `response.content` holding only `tool_use` blocks
and **zero text blocks**. The extraction line then produced `""` — a
correct extraction from a response the model was never given the chance
to finish. Nothing errored. The empty string was stored and billed as
output. Confirmed across historical state files: Skills 02/03 output is
0 bytes on the large majority of every run in this session, back to the
first one.

**Why it went unnoticed for so long, which is the uncomfortable part.**
The eval harness judged the *concatenation* of all four skills' outputs.
Skills 01 and 04 produced 40k+ characters each, so the combined text
always looked substantial, and the judge always had plenty to grade.
Nothing anywhere compared per-skill output length to zero. Every
"pipeline vs baseline" number in #8-#14 was computed against what was
effectively a two-skill pipeline.

**The fix, and the important part about what actually fixed it.** The
instinct is "the cap was too low, raise it." That was tried first and
**measured to be wrong**: at 20 rounds the model made 123 tool calls,
cost $2.45 for a single skill, and *still* returned empty text — because
no cap value fixes a model that never stops asking for tools. The real
fix is a forced-synthesis fallback: when the loop exhausts with the model
still requesting tools, answer the pending tool calls, then make one
final call with `tools` removed.

**And removing `tools` alone was also verified insufficient** — a first
version of the fallback did exactly that, and the real API returned
`stop_reason='end_turn'` with **zero content blocks and 8 output
tokens**: a genuinely empty response. Diagnosed by adding a permanent
diagnostic (see below) and reproducing at a 2-round cap for roughly a
tenth the cost, rather than guessing. Cutting a mid-task model off from
its tools without telling it what to do instead leaves it with no
directive, and it produces nothing. The load-bearing part is an explicit
instruction, appended as a text block in the same user turn as the
tool_results: *stop calling tools, write your complete final response
now from what you have, and state plainly where lookups returned no
match rather than omitting or inventing.* With that, Skill 02 went from
0 characters to a complete 72,000-character analysis that explicitly
reports which lookups succeeded and which found nothing.

**Empty text is now always a reported defect**, never a silent return:
the harness prints `stop_reason`, the actual block types, and the output
token count. This is the check whose absence let the original bug live
across an entire session.

**`_MAX_TOOL_ROUNDS` is now a cost dial, not a correctness threshold.**
Set to 8 — real headroom over the original 5, well short of the 123-call
pathology at 20. Measured, all with the fallback working: 2 rounds → 16
calls/$0.69; 8 rounds → 45 calls/$1.35; 20 rounds → 123 calls/$2.45.
**Not empirically optimized** — no A/B eval across cap values was run, so
it is a reasonable default, not a tuned one.

**A precision bug in Step 4's own heuristic, caught on its first real
run.** `_estimate_confidence()` compared `metrics["output_tokens"]` —
which sums *every* call in the tool-use loop — against a *per-call*
`max_tokens` ceiling, and reported "17377/16384," two different
quantities. The verdict happened to be right, but the arithmetic was
wrong and would false-trigger on any tool-heavy run that was never
truncated. Fixed by recording `final_output_tokens` and
`final_stop_reason` (the single call that actually produces the text —
the only one truncation can affect) and comparing against those. The
corrected version now reports `16384/16384` with
`final_stop_reason: "max_tokens"` — truncation *proven*, not inferred.

**What this does NOT close, named rather than quietly carried:**

- **Skill 02's output is genuinely truncated.** `final_stop_reason:
  "max_tokens"` is proof its real output does not fit the current 16384
  ceiling. Deliberately not fixed here: raising one skill's `max_tokens`
  would trip Step 3's own config-outlier guardrail — correctly, since it
  would make the other three skills the outliers — so this is a
  deliberate config decision, not a one-line change. Step 4's
  `confidence` field now reports `low` with that exact basis on every
  affected run, which is exactly the job it was added to do.
- **Every pipeline number in #8-#14 needs a full rerun before it can be
  trusted.** This commit fixes the defect and flags the data; it does not
  regenerate it. The direction of the error is knowable, though, and
  worth stating: the "pipeline does not beat baseline" conclusion is
  **not overturned and is arguably reinforced** — a pipeline missing two
  of four steps' content would plausibly score worse, not better — while
  the **cost figures were understated**, since Skill 02 logged $0.67
  returning nothing and costs $1.35 returning real work. The headline
  "8.4× the baseline cost" is a floor, not the true multiple.
- **The confidence heuristic is simple and would need refinement before
  being trusted in production.** Tool-match rate is a reasonable proxy
  for grounding, but it says nothing about whether the *content* built on
  those lookups is correct, and Skills 01/04 have no grounding signal at
  all — they report `medium` by construction, which is an honest
  placeholder, not a measurement. Do not present this as a calibrated
  confidence score.
