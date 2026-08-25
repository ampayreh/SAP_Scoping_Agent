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
