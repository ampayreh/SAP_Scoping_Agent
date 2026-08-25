# SAP S/4HANA Implementation Scoping Agent

An agentic AI skills pack that orchestrates the discovery-to-roadmap arc of SAP S/4HANA implementation scoping — compressing 2-4 weeks of manual consulting effort into a structured, repeatable workflow.

## Problem

The discovery and scoping phase of an SAP S/4HANA implementation is the most time-consuming, unstructured part of every engagement. Enterprise Architects and implementation consultants spend 2-4 weeks gathering client context, mapping requirements to modules, identifying integration dependencies, building roadmaps, and drafting proposals — often with inconsistent quality depending on individual consultant experience.

## SAP AI Ecosystem Positioning

SAP has built an extensive AI ecosystem (2,400+ Joule skills, Joule for Consultants, Signavio, LeanIX, Cloud ALM). However, **no native capability today chains the discovery-to-roadmap arc into a single agentic workflow**. Each step exists as a capability in a different tool; the orchestration layer connecting them does not exist as a product. This skills pack fills that gap.

| SAP Capability | What It Does | What It Doesn't Do |
|---|---|---|
| Joule for Consultants (J4C) | Knowledge retrieval from 9+ TB SAP content | Workflow orchestration, multi-step scoping |
| SAP LeanIX | Application portfolio visibility, capability mapping | Autonomous landscape-to-roadmap generation |
| SAP Signavio | Process mining, BPMN modeling, best practices | Cross-tool scoping synthesis |
| SAP Cloud ALM | Project governance, requirement generation | Discovery-phase orchestration |
| Digital Discovery Assessment | Scope item recommendation | Full fit/gap + roadmap + proposal generation |

This skills pack is **complementary** to SAP's toolchain — its outputs feed into Cloud ALM, Signavio, and LeanIX rather than replacing them.

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Skills Pack Workflow                       │
│                                                              │
│  ┌──────────────┐    ┌──────────────┐    ┌───────────────┐  │
│  │ 01 Client     │───▶│ 02 Module     │───▶│ 03 Roadmap    │  │
│  │ Discovery     │    │ Fit Analyzer  │    │ Generator     │  │
│  │ Intake        │    │               │    │               │  │
│  └──────────────┘    └──────────────┘    └───────┬───────┘  │
│         │                    │                    │          │
│         │                    │                    │          │
│         ▼                    ▼                    ▼          │
│  ┌──────────────────────────────────────────────────────┐   │
│  │            04 Executive Proposal Drafter              │   │
│  └──────────────────────────────────────────────────────┘   │
│                              │                               │
│  ┌──────────────────────────────────────────────────────┐   │
│  │     05 SAP Best Practices Fetcher (MCP Server)        │   │
│  │     mcp_server.py — stdio transport, 20 scope items  │   │
│  │     Grounds all skills in SAP official guidance       │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
│  ─ ─ ─ ─ ─ ─ ─ ─ Future Integration ─ ─ ─ ─ ─ ─ ─ ─ ─   │
│  SAP Cloud ALM │ SAP Signavio │ SAP LeanIX │ A2A           │
└─────────────────────────────────────────────────────────────┘
```

## Skills

| # | Skill | Input | Output | SAP Activate Phase |
|---|---|---|---|---|
| 01 | Client Discovery Intake | Unstructured client info | Structured discovery brief | Discover |
| 02 | Module Fit Analyzer | Discovery brief | Fit/gap scoring, module map | Discover → Prepare |
| 03 | Implementation Roadmap | Module fit analysis | Phased plan with timelines | Prepare |
| 04 | Executive Proposal Drafter | Skills 1-3 outputs | Client-ready proposal | Prepare |
| 05 | SAP Best Practices Fetcher | Module/industry query | Best practices, patterns | Cross-cutting |

## Quickstart

```bash
# Clone and install
git clone https://github.com/ampayreh/SAP_Scoping_Agent.git
cd SAP_Scoping_Agent
pip install -r requirements.txt

# Set your API key
export ANTHROPIC_API_KEY=sk-ant-...

# Run the full pipeline on a benchmark scenario
python orchestrator.py --input benchmarks/scenario-a-agribusiness/input.md --no-gate

# Run with human-approval gate before proposal generation
python orchestrator.py --input benchmarks/scenario-a-agribusiness/input.md

# Resume a failed run from where it stopped
python orchestrator.py --resume state/run-20260816T120000.json

# Run the evaluation harness (3 runs per scenario for variance)
python eval.py --runs 3

# Test the MCP server locally (no MCP client needed)
python mcp_server.py --test "finance"
python mcp_server.py --test "MM"

# Run the MCP server over stdio (for Claude Desktop or MCP clients)
python mcp_server.py
```

### Claude Desktop Configuration

To use the scope-item lookup from Claude Desktop, add to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "sap-scope-items": {
      "command": "python",
      "args": ["/path/to/SAP_Scoping_Agent/mcp_server.py"]
    }
  }
}
```

## Project Structure

```
SAP_Scoping_Agent/
├── orchestrator.py                # Pipeline orchestrator (Claude API + tool use)
├── eval.py                        # Evaluation harness (pipeline vs baseline, LLM judge)
├── mcp_server.py                  # MCP server for scope-item lookup (stdio transport)
├── requirements.txt               # Python dependencies (anthropic, httpx, mcp)
├── DECISIONS.md                   # Documented architectural decisions
├── skills/
│   ├── 01-client-discovery-intake.md
│   ├── 02-module-fit-analyzer.md
│   ├── 03-implementation-roadmap.md
│   ├── 04-executive-proposal-drafter.md
│   └── 05-sap-best-practices-fetcher.md   # MCP tool specification
├── tools/
│   ├── proposal-to-pdf.py         # Convert proposals to PDF
│   ├── proposal-style.css         # Consulting-grade stylesheet
│   └── README.md
├── benchmarks/
│   ├── scenario-a-agribusiness/   # Fictional mid-market (HHE, Tanzania)
│   ├── scenario-b-high-tech/      # Fictional large enterprise
│   ├── benchmark-methodology.md   # Scoring rubric and protocol
│   └── scoring-results.md
├── evals/                         # Eval results (generated by eval.py)
├── state/                         # Pipeline state (generated by orchestrator.py)
└── docs/
    └── tutorial.md
```

## Benchmark Scenarios

- **Scenario A (Mid-market Agribusiness):** Fictional Tanzanian raw cashew export company (Highland Harvest Exports), ~65 employees, fragmented tooling, multi-currency, export compliance
- **Scenario B (High-tech Manufacturing):** Fictional satellite manufacturer, ~500+ users, complex BOM, multi-site, existing SAP landscape migration

## How to Use

**Automated pipeline (recommended):**

```bash
python orchestrator.py --input your-client-brief.md
```

The orchestrator chains Skills 01→04 sequentially, persisting state after each step. A human-approval gate pauses before proposal generation so you can review the module fit and roadmap. Skills 02 and 03 have access to a scope-item lookup tool via Claude's tool-use capability.

**Manual skill-by-skill:**

1. Start with **Skill 01** — provide your client context (industry, size, pain points, current systems)
2. Feed the structured discovery brief into **Skill 02** for module fit analysis
3. Pass the module analysis to **Skill 03** for roadmap generation
4. Synthesize everything with **Skill 04** for an executive-ready proposal
5. Convert the proposal to PDF: `python3 tools/proposal-to-pdf.py <skill-04-output.md>`
6. Use **Skill 05** at any point to ground recommendations in SAP best practices

Each skill can also be used independently for targeted analysis.

## Evaluation Methodology

`eval.py` grades the pipeline against a single-prompt baseline two ways, both
blinded to which method produced the output:

- **Absolute scoring (0-5 per dimension)** — completeness, accuracy,
  actionability, SAP grounding. The judge sees only the output and the
  scenario; it is never told which method produced it.
- **Blinded pairwise comparison** — the same run's pipeline and baseline
  outputs are shown to the judge anonymized as "Response A" / "Response B"
  (randomized per call, never revealed), and the judge picks a winner or a
  tie per dimension with a mandatory quoted excerpt as evidence. This is
  what actually discriminates between the two methods — an absolute 0-5
  scale on its own tends to cluster near the top and can't tell you which
  is better, only that both are "good."
- **Consistency** is computed from the standard deviation of scores across
  repeated runs (`--runs N`), not estimated by the judge.
- **Judge independence is enforced by default**, not just possible: the
  judge model defaults to a different model line than the system under
  test, and the harness warns loudly if a run's configuration collapses
  them to the same model.

See `DECISIONS.md` #8 for the full account of why the eval harness needed
this fix, and `evals/RESULTS.md` for the header on any committed run
stating the exact system/judge models used and whether they were
independent for that run.

## What This Does Not Do

- **Not a production deployment.** The orchestrator runs locally against the Claude API. It is not a hosted service, does not handle concurrent users, and has no authentication layer.
- **Not connected to live SAP APIs.** `mcp_server.py` implements a real MCP server (stdio transport, MCP SDK v2.0) exposing a curated 20-item scope-item catalogue. In production, the same MCP interface would front SAP's Best Practice Explorer, Signavio, or LeanIX — the pipeline consumer sees the same `lookup_scope_items` / `list_all_scope_items` tools regardless of the backing data source.
- **Not a substitute for a consultant.** The outputs are starting points that compress 2-4 weeks of discovery into hours. A qualified SAP consultant must review all recommendations before presenting to a client.

## Author

**Graeme Tobias Ampeire** — Applied AI Architect
SAP-certified Enterprise Architect | 12+ years digital transformation across Africa, Europe, and the US

## Course

MSIS 549 — AI and Generative AI for Business Applications
University of Washington, Foster School of Business
Professor Léonard Boussioux | Winter Quarter 2026
