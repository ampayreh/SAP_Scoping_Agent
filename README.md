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
│  │     05 SAP Best Practices Fetcher (MCP Tool)          │   │
│  │     Grounds all skills in SAP official guidance       │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
│  ─ ─ ─ ─ ─ ─ ─ ─ Future Integration ─ ─ ─ ─ ─ ─ ─ ─ ─   │
│  SAP Cloud ALM │ SAP Signavio │ SAP LeanIX │ A2A / MCP     │
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

## Project Structure

```
sap-s4hana-scoping-agent/
├── README.md
├── skills/
│   ├── 01-client-discovery-intake.md
│   ├── 02-module-fit-analyzer.md
│   ├── 03-implementation-roadmap.md
│   ├── 04-executive-proposal-drafter.md
│   └── 05-sap-best-practices-fetcher.md
├── tools/
│   ├── proposal-to-pdf.py          # Convert proposals to McKinsey-grade PDF
│   ├── proposal-style.css          # Professional consulting stylesheet
│   └── README.md
├── benchmarks/
│   ├── scenario-a-agribusiness/
│   └── scenario-b-high-tech/
├── docs/
│   └── tutorial.md
└── examples/
```

## Benchmark Scenarios

- **Scenario A (Mid-market Agribusiness):** Fictional Tanzanian raw cashew export company, ~65 employees, fragmented tooling, multi-currency, export compliance
- **Scenario B (High-tech Manufacturing):** Satellite manufacturing, ~500+ users, complex BOM, multi-site, existing SAP landscape migration

## How to Use

1. Start with **Skill 01** — provide your client context (industry, size, pain points, current systems)
2. Feed the structured discovery brief into **Skill 02** for module fit analysis
3. Pass the module analysis to **Skill 03** for roadmap generation
4. Synthesize everything with **Skill 04** for an executive-ready proposal
5. Convert the proposal to PDF: `python3 tools/proposal-to-pdf.py <skill-04-output.md>`
6. Use **Skill 05** at any point to ground recommendations in SAP best practices

Each skill can also be used independently for targeted analysis.

## Author

**Graeme Tobias Ampeire** — MSIS Candidate, UW Foster School of Business (2026)
SAP-certified Enterprise Architect | 12+ years digital transformation across Africa, Europe, and the US

## Course

MSIS 549 — AI and Generative AI for Business Applications
University of Washington, Foster School of Business
Professor Léonard Boussioux | Winter Quarter 2026
