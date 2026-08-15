# Building an Agentic AI Skills Pack for SAP S/4HANA Implementation Scoping

**Author:** Graeme Tobias Ampeire
**Course:** MSIS 549, AI and Generative AI for Business Applications
**Institution:** University of Washington, Foster School of Business
**Professor:** Leonard Boussioux | Winter Quarter 2026

**GitHub Repository:** [github.com/ampayreh/ScopingAgent](https://github.com/ampayreh/ScopingAgent)

---

## Table of Contents

1. [Problem Statement and Motivation](#1-problem-statement-and-motivation)
2. [SAP AI Ecosystem Positioning](#2-sap-ai-ecosystem-positioning)
3. [System Design and Architecture](#3-system-design-and-architecture)
4. [Skill Documentation and Prompt Engineering](#4-skill-documentation-and-prompt-engineering)
5. [Prompt Iterations: Before and After](#5-prompt-iterations-before-and-after)
6. [Building Process and Bottlenecks](#6-building-process-and-bottlenecks)
7. [Benchmark Methodology and Findings](#7-benchmark-methodology-and-findings)
8. [Reflection: The AI-Augmented Enterprise Architect](#8-reflection-the-ai-augmented-enterprise-architect)

---

## 1. Problem Statement and Motivation

### The Discovery Phase Problem

The discovery and scoping phase of an SAP S/4HANA implementation is the most time-consuming, unstructured part of every engagement. Enterprise Architects spend **2 to 4 weeks** gathering client context, mapping requirements to SAP modules, identifying integration dependencies, building roadmaps, and drafting proposals, often with inconsistent quality depending on the consultant's experience level.

This problem is universal. Accenture, Deloitte, EY, Amazon Web Services, and mid-market firms like West Monroe all deploy senior architects to run discovery workshops. The quality of scoping output depends on the individual consultant's SAP product knowledge, industry experience, and ability to synthesize unstructured information. Senior consultants outperform juniors not because the framework is different, but because they have internalized more patterns from past projects.

### The Agentic AI Opportunity

What if we could encode those patterns into a reusable skills pack that any consultant, regardless of seniority, could use to produce expert-level scoping outputs? This is the promise of agentic AI in enterprise consulting: not replacing the architect, but augmenting them with an AI system that can:

1. **Structure** unstructured client input into standardized discovery briefs
2. **Map** requirements to SAP modules using SAP's own best practice framework
3. **Generate** phased roadmaps calibrated to client size and complexity
4. **Draft** executive proposals that translate technical analysis into business value
5. **Ground** all recommendations in SAP's official guidance and methodology

### Why This Project, Why Now

Three convergent trends make this project timely. First, SAP's AI ecosystem has matured (2,400+ Joule skills, J4C adopted by KPMG/Deloitte, Signavio AI modeler), but no tool chains discovery-to-roadmap autonomously. Second, agentic AI has become practical through Claude's tool use, MCP protocol, and multi-step reasoning. Third, SAP's own "Rise of the Super Architect" sessions at the February 2026 EA Learning Forum signal that AI augmentation is the next frontier for enterprise architecture.

### Personal Motivation

As an SAP-certified Enterprise Architect with 12+ years of implementation experience across Africa, Europe, and the US, I have lived this problem at Matum Consulting, SAP UCC Magdeburg, and BDO East Africa. At every stage, I have seen how much time is consumed by the unstructured front end of every engagement and how much quality varies between consultants. This project answers: "What would the AI-augmented version of my own consulting practice look like?"

---

## 2. SAP AI Ecosystem Positioning

### What SAP Has Built (February 2026)

Any project building AI tools for SAP consulting must position itself relative to what SAP already offers.

**SAP Joule** is the AI copilot network: 2,400+ skills across S/4HANA Cloud, SuccessFactors, Signavio, LeanIX, and more. Joule for Consultants (J4C), built on Anthropic Claude via Amazon Bedrock, draws on 9+ TB of SAP content and has been adopted by KPMG, Deloitte, and Wipro. It scores 95%+ on SAP certification exams and saves consultants roughly 1.5 hours per day. Its key limitation: J4C is a knowledge retrieval tool, not a workflow orchestrator.

**SAP Signavio** handles process intelligence (Gartner MQ Leader for Process Mining) with AI features including text-to-BPMN modeling and an AI-Assisted Process Recommender covering 5,000+ SAP best practices. **SAP LeanIX** manages enterprise architecture (Gartner MQ Leader, 5 consecutive years) with AI-Assisted Inventory Builder achieving 80% time reduction. **SAP Cloud ALM** manages implementation lifecycle with AI-assisted requirement generation from workshop transcripts.

### Where the Gap Is

| SAP Tool | What It Does Well | What It Cannot Do |
|---|---|---|
| J4C | Answers SAP questions from 9+ TB of content | Chain multi-step scoping decisions autonomously |
| Signavio | Mines processes, recommends best practices | Generate implementation roadmaps from analysis |
| LeanIX | Maps application portfolios, assesses risk | Produce client-ready transformation proposals |
| Cloud ALM | Manages governance, generates requirements | Orchestrate the pre-project discovery phase |

**The gap:** No SAP-native capability today chains discovery, landscape analysis, fit/gap assessment, Clean Core compliance, roadmap generation, and executive proposal into a single agentic workflow. Each step exists in a different tool; the orchestration layer does not exist as a product.

### How This Skills Pack Fills the Gap

This project builds the missing orchestration layer: outputs feed into Cloud ALM, Signavio, and LeanIX rather than replacing them. Skills map to SAP Activate's Discover and Prepare phases. Every module assessment includes Clean Core compliance scoring. All outputs use SAP standard terminology. The MCP tool design (Skill 05) demonstrates the integration pattern for SAP's A2A/MCP protocols.

---

## 3. System Design and Architecture

### Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                    Skills Pack Workflow                         │
│                                                                │
│  Unstructured      ┌──────────────┐    Structured              │
│  Client Info  ───> │ 01 Discovery  │ ──> Brief (JSON) ──>      │
│  (any format)      │    Intake     │                            │
│                    └──────────────┘   ┌──────────────┐         │
│                                       │ 02 Module Fit │         │
│                                       │   Analyzer    │         │
│                                       └──────┬───────┘         │
│                    Module Fit (JSON)          │                 │
│                           │                  │                 │
│                           v                  │                 │
│                    ┌──────────────┐           │                 │
│                    │ 03 Roadmap    │           │                 │
│                    │  Generator    │           │                 │
│                    └──────┬───────┘           │                 │
│                           │                  │                 │
│                           v                  │                 │
│                    ┌─────────────────────────────────────┐      │
│                    │ 04 Executive Proposal Drafter        │      │
│                    │ (Consumes outputs from 01, 02, 03)  │      │
│                    └─────────────────────────────────────┘      │
│                                                                │
│  ┌────────────────────────────────────────────────────────┐    │
│  │ 05 SAP Best Practices Fetcher (MCP Tool)               │    │
│  │ Knowledge backbone: scope items, process flows,         │    │
│  │ industry maps, Clean Core guidance                      │    │
│  └────────────────────────────────────────────────────────┘    │
│                                                                │
│  - - - - - - - - Future Integration - - - - - - - - - - -     │
│  SAP Cloud ALM | SAP Signavio | SAP LeanIX | A2A / MCP        │
└─────────────────────────────────────────────────────────────────┘
```

### Design Decisions

| Decision | Rationale |
|---|---|
| **Markdown skill files (Path A)** | Portable, version-controllable, Claude-native |
| **JSON intermediate formats** | Enables programmatic consumption between skills |
| **Markdown final output (Skill 04)** | Executive proposals are human-facing documents |
| **MCP tool design (Skill 05)** | Demonstrates future SAP integration pattern |
| **SAP Activate phase mapping** | Methodological credibility with SAP practitioners |
| **Inference tagging** | `[INFERRED]` tags enable trust and audit trails |
| **Completeness scoring** | Prevents garbage-in-garbage-out across the chain |

### Why Agentic (Not Just "Better Prompts")

A single prompt can produce decent SAP scoping output. The agentic approach adds: (1) structured intermediate representations that prevent information loss between steps; (2) specialized reasoning per skill; (3) quality gates via completeness scoring; (4) composability, since skills can run independently; (5) selective iteration, where you can re-run Skill 03 without re-running Skills 01 and 02; and (6) auditability through inspectable intermediate outputs.

---

## 4. Skill Documentation and Prompt Engineering

### Skill Summary

| Skill | Lines | Key Innovation | Output |
|---|---|---|---|
| 01: Client Discovery Intake | 594 | Inference engine with explicit tagging, completeness scoring | JSON |
| 02: Module Fit Analyzer | 1,426 | Per-module fit scoring with Clean Core compliance per gap | JSON |
| 03: Implementation Roadmap | 1,528 | SAP Activate phase calibration by client size/complexity | JSON |
| 04: Executive Proposal Drafter | 621 | C-level language translation, risk-of-inaction framing | Markdown |
| 05: SAP Best Practices Fetcher | 667 | MCP tool spec with curated knowledge base | JSON |

### Cross-Skill Design Patterns

Five patterns run through every skill. **Schema-first design:** each skill defines its output schema before its behavior, so downstream consumers know what to expect. **SAP terminology normalization:** client language ("shipping") becomes SAP standard ("Outbound Delivery") at Skill 01. **Inference transparency:** every inference carries `[INFERRED]` and reasoning. **SAP toolchain awareness:** every skill explains how its output relates to Cloud ALM, Signavio, LeanIX, and J4C. **Failure mode documentation:** each skill describes how it handles degraded input and contradictions.

Detailed prompt documentation for each skill is in the `/skills` directory of the repository.

---

## 5. Prompt Iterations: Before and After

### Skill 01: Client Discovery Intake

**v1:** "Extract the client's company name, industry, employee count, current systems, and pain points from the input text and organize them into categories."

**Problem:** A flat list of facts with no inference, no gap detection, no SAP terminology mapping. Unusable without significant manual enrichment.

**v2:** Full intake agent with completeness scoring (0 to 100%), severity-tagged gaps, inference engine with `[INFERRED]` tagging, SAP industry classification, module signal generation, and toolchain recommendations.

**Impact:** Output went from roughly 200 words of flat facts to a 3,000-word structured brief that Skill 02 can consume without additional client interaction.

### Skill 02: Module Fit Analyzer

**v1:** "Given the client's requirements, recommend which SAP S/4HANA modules they should implement." This produced a bulleted list with generic descriptions and no fit/gap scoring.

**v2:** Comprehensive analyzer with per-module scoring (1 to 5 scale), integration dependency mapping, Clean Core compliance assessment per gap, cross-module design considerations, and sizing recommendation.

### Skill 03: Implementation Roadmap

**v1:** "Create a phased implementation plan for SAP S/4HANA." A 50-employee greenfield and a 2,500-employee brownfield got identical 18-month timelines.

**v2:** Adaptive generator that calibrates phase durations, resource models, and wave structures based on client size, scope complexity, change readiness, and transformation type. Phase durations scale from 6 to 9 months (mid-market greenfield) to 18 to 24 months (enterprise brownfield).

### Skill 04: Executive Proposal Drafter

**v1:** "Write an executive summary of the SAP implementation analysis." Output read like a technical report, used module codes (FI, CO, MM) instead of business language, and lacked ROI framing.

**v2:** Full proposal with audience calibration, business language translation ("Financial Management" not "FI/CO"), ROI quantification, risk-of-inaction framing, and scenario-specific narrative.

---

## 6. Building Process and Bottlenecks

### Development Timeline

| Phase | Duration | Activities |
|---|---|---|
| Research and Design | Days 1 to 3 | SAP AI ecosystem analysis; gap identification; architecture design; skill decomposition |
| Skill 01: Discovery | Days 3 to 5 | Inference engine, completeness scoring, terminology normalization |
| Skill 02: Module Fit | Days 5 to 8 | Per-module scoring, integration mapping, Clean Core assessment (3 major revisions) |
| Skill 03: Roadmap | Days 8 to 10 | Adaptive phase calibration, SAP Activate alignment, budget framework |
| Skill 04: Proposal | Days 10 to 12 | Audience calibration, business language translation, consistency verification |
| Skill 05: Best Practices | Days 12 to 13 | MCP tool spec, knowledge base design, query taxonomy |
| Benchmarks and Tooling | Days 13 to 15 | Scenario testing, baseline comparison, PDF export, scoring, tutorial |

**Platform:** Claude Code (Anthropic) with Claude Opus. **Skill format:** Markdown (Path A). **Testing:** Manual execution against two benchmark scenarios. **PDF tooling:** Python + WeasyPrint.

### Bottlenecks Encountered

**1. Prompt length vs. quality.** Skills 02 and 03 (1,426 and 1,528 lines respectively) push context window limits. The solution: make each prompt self-contained with explicit output schemas rather than relying on examples, which consume more tokens without proportional quality gain.

**2. Consistency across runs.** LLM outputs are non-deterministic. Mitigations: (a) explicit JSON schemas so structure is consistent even when content varies; (b) numerical scoring rubrics (fit scores 1 to 5) that anchor outputs to specific criteria; (c) a cross-skill consistency check in Skill 04. Despite these measures, some narrative variation persists.

**3. SAP knowledge accuracy.** Verifying that scope item IDs, module capabilities, and methodology references are correct requires domain expertise. The approach: use SAP's Best Practice Explorer and Help Portal as ground truth, and include disclaimers where scope item references are directional rather than catalog-exact.

**4. JSON output reliability.** Large JSON blocks (400+ lines) occasionally had structural issues: missing brackets, mismatched quotes. Fixed by adding explicit formatting instructions and providing complete schema skeletons as templates.

**5. Skill chaining and information loss.** Early Skill 01 output was missing SAP module signals, forcing Skill 02 to infer module relevance from scratch. Adding an `initial_module_signals` section to Skill 01 solved this. Similarly, Skill 04 needed a cross-skill consistency section to avoid contradictory figures across upstream outputs.

**6. Calibration of estimates.** Timeline and budget estimates in Skills 03 and 04 needed to be realistic, not just plausible. This required embedding calibration heuristics from professional experience: mid-market greenfield at 6 to 9 months, enterprise brownfield at 18 to 24 months, partner day rates at $1,500 to $2,500.

**7. AI text markers.** Proposal output initially exhibited overuse of em-dashes, a common AI-generated text pattern. Addressed by adding explicit punctuation style rules to the prompt and rewriting outputs to use colons, semicolons, and parentheses. Broader lesson: client-facing AI outputs need explicit style guidelines to avoid undermining credibility.

### Lessons Learned

1. **Schema-first design is essential.** Defining output schemas before writing prompt behavior was the most impactful design decision. It prevents information loss, enables consistency verification, and makes outputs programmatically consumable.

2. **The inference engine is the most valuable innovation.** The `[INFERRED]` tagging system creates a transparency layer absent from traditional consulting deliverables. When a consultant writes "the client needs QM," it is unclear whether the client stated that or the consultant inferred it.

3. **SAP ecosystem positioning matters.** Adding references to Signavio, LeanIX, Cloud ALM, and J4C transformed outputs from "generic AI analysis" to "SAP-ecosystem-aware analysis."

4. **Greenfield and brownfield diverge significantly.** Running both scenarios revealed different analytical pathways: greenfield needs product sizing and workforce readiness; brownfield needs custom code remediation and system conversion planning.

5. **Presentation affects perceived quality.** Adding McKinsey-grade PDF formatting significantly increased perceived output quality, even though the content was identical to the markdown version.

---

## 7. Benchmark Methodology and Findings

### Methodology

Two primary scenarios were evaluated: a mid-market agribusiness (greenfield) and a high-tech manufacturing enterprise (brownfield). Three edge cases tested ambiguous input, Clean Core resistance, and ecosystem-aware clients. The baseline was a single-prompt LLM response. Metrics: Completeness, Accuracy, Actionability, and Consistency, each scored 0 to 5. Full details are in `benchmarks/benchmark-methodology.md`.

### Findings

The skills pack outperformed the single-prompt baseline by **+1.44 points** on a 5-point scale across both scenarios. Full scoring justifications are in `benchmarks/scoring-results.md`.

| Metric | Skills Pack (A) | Baseline (A) | Skills Pack (B) | Baseline (B) |
|---|---|---|---|---|
| Completeness | 4.5 | 2.5 | 4.5 | 3.0 |
| Accuracy | 4.5 | 3.0 | 4.0 | 3.0 |
| Actionability | 4.0 | 2.0 | 4.0 | 2.5 |
| Consistency | 4.0 | 3.0 | 4.5 | 3.5 |
| **Average** | **4.25** | **2.63** | **4.25** | **3.00** |

**Time saved:** 8 to 12 days (Scenario A) and 12 to 18 days (Scenario B) versus manual consultant process.

### Standout Findings

**Scenario A (HHE, agribusiness greenfield):** The skills pack flagged EU food-safety import traceability documentation requirements by analyzing buyer geography (multiple confirmed export markets are in the EU). The baseline missed this entirely. Notably, the skills pack also correctly avoided citing the EU Deforestation Regulation (EUDR) — a common error, since EUDR covers coffee, cocoa, palm oil, soy, cattle, and wood, but not cashew. For a fictional raw cashew exporter, EU market-access compliance is a general food-safety documentation requirement, not an EUDR one, and getting that distinction right is itself a signal of scoping quality.

**Scenario B (CSS, high-tech brownfield):** The skills pack produced a custom code remediation framework referencing SAP's ATC, CCM Worklist, and Simplification Item Catalog. The baseline mentioned "custom code cleanup" without actionable methodology. For a system with 2,400 custom ABAP objects, the remediation strategy is the single most important technical decision.

### Key Insights

1. **The delta is widest on Completeness and Actionability** (+1.75 average each), the dimensions most critical for real consulting use. Structure forces depth.

2. **The baseline performs better on detailed input.** Scenario B's baseline (3.00/5) outscored Scenario A's (2.63/5) because the CSS input was richer. The skills pack's advantage is greatest when input is ambiguous, because the inference engine surfaces gaps rather than ignoring them.

3. **Consistency is the smallest delta** (+1.0 average). A single document is inherently consistent with itself. Maintaining coherence across 5 outputs totaling 1,800 to 2,400+ lines makes the skills pack's 4.0 to 4.5 score more impressive in context.

4. **Time compression is the headline benefit.** The skills pack reduces a 2 to 4 week manual process to 2 to 4 hours, representing a 10 to 20x productivity improvement.

5. **The baseline is not wrong; it is shallow.** A single-prompt response produces a competent first draft. The skills pack produces a near-finished deliverable set. The difference is "ideas to explore" versus "analysis to present."

---

## 8. Reflection: The AI-Augmented Enterprise Architect

### What This Means for the Role

The enterprise architect's value has always been synthesis: connecting business strategy to technology decisions across organizational boundaries. This project demonstrates that agentic AI can encode the structural patterns of expert-level scoping while preserving the human architect's role in three areas:

1. **Relationship judgment.** AI can analyze requirements, but the architect reads the room. Who is the real decision-maker? Is the stated budget real? Is the organization actually ready for change?
2. **Strategic counsel.** AI can generate options, but the architect advises on which path serves long-term interests, even when that means "SAP might not be the right choice for you."
3. **Accountability.** AI can draft a proposal, but the architect puts their name on it. The skills pack is a tool; the architect is the professional.

### Agentic Orchestration: The Next Frontier

SAP's integrated toolchain (Signavio + LeanIX + Cloud ALM) contains powerful individual capabilities. Today, a human architect must decide what to analyze, how to interpret gaps, and how to synthesize everything into a roadmap. The next frontier is agentic orchestration across the toolchain: an AI system that queries LeanIX for application portfolios, directs Signavio to mine processes, consumes Cloud ALM requirements, and synthesizes a coherent roadmap.

SAP's direction points here. The A2A protocol, MCP support for HANA Cloud, Joule Studio Agent Builder, and the Sapphire 2025 transformation agent demo all signal full agentic orchestration as the strategic vision. This skills pack is a working prototype of that vision, built with today's technology.

### For the SAP EA Community

Building this skills pack taught me that the most valuable part of the architect's work is not the analysis itself. It is the judgment about what to analyze, for whom, and why. Agentic AI can compress the mechanical work of scoping from weeks to hours. That does not make the architect less valuable. It makes judgment, relationship skills, and strategic insight more valuable, because those become the differentiators in a world where the analytical baseline is automated.

---

## Appendix A: Project Repository Structure

**Repository:** [github.com/ampayreh/ScopingAgent](https://github.com/ampayreh/ScopingAgent)

```
sap-s4hana-scoping-agent/
├── README.md
├── skills/                                    # Skill specifications
│   ├── 01-client-discovery-intake.md          (594 lines)
│   ├── 02-module-fit-analyzer.md              (1,426 lines)
│   ├── 03-implementation-roadmap.md           (1,528 lines)
│   ├── 04-executive-proposal-drafter.md       (621 lines)
│   └── 05-sap-best-practices-fetcher.md       (667 lines)
├── tools/                                     # PDF export tooling
│   ├── proposal-to-pdf.py
│   ├── proposal-style.css
│   └── README.md
├── benchmarks/                                # Evaluation framework
│   ├── benchmark-methodology.md
│   ├── baseline-comparison.md
│   ├── scoring-results.md
│   ├── scenario-a-agribusiness/               # Greenfield (HHE)
│   │   ├── input.md
│   │   ├── skill-01 through skill-05-output.md
│   │   └── skill-04-output.pdf
│   └── scenario-b-high-tech/                  # Brownfield (CSS)
│       ├── input.md
│       └── skill-01 through skill-05-output.md
└── docs/
    ├── tutorial.md                            # This document
    └── tutorial.pdf
```

## Appendix B: SAP Certifications Referenced

SAP Activate Project Manager; SAP Enterprise Architecture Framework; SAP Signavio Process Management; S/4HANA Implementation Scenarios for Architects; S/4HANA Business Process Integration; SAP ERP Foundation and Integration; Business Process Automation with SAP Intelligent RPA; additional SAP UCC Magdeburg curriculum certifications.

## Appendix C: Key SAP References

- SAP Activate Methodology: https://support.sap.com/en/offerings-programs/methodology.html
- SAP Best Practice Explorer: https://rapid.sap.com/bp/
- SAP Clean Core: https://www.sap.com/products/erp/s4hana/clean-core.html
- SAP Joule: https://www.sap.com/products/artificial-intelligence/ai-assistant.html
- SAP LeanIX: https://www.leanix.net/
- SAP Signavio: https://www.signavio.com/
- SAP Cloud ALM: https://support.sap.com/en/alm/sap-cloud-alm.html

## Appendix D: Benchmark Summary

| | Scenario A (Agribusiness) | Scenario B (High-Tech) | Overall |
|---|---|---|---|
| **Skills Pack** | 4.25/5 | 4.25/5 | **4.25/5** |
| **Baseline** | 2.63/5 | 3.00/5 | **2.81/5** |
| **Delta** | +1.63 | +1.25 | **+1.44** |

| Scenario | Manual Process | With Skills Pack | Savings |
|---|---|---|---|
| A (greenfield) | 10 to 15 days | 1 to 2 days | 8 to 12 days |
| B (brownfield) | 15 to 25 days | 2 to 4 days | 12 to 18 days |

Full scoring justifications and baseline outputs are in `benchmarks/scoring-results.md` and `benchmarks/baseline-comparison.md`.
