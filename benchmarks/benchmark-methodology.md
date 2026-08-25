# Benchmark Methodology

## Overview

This benchmark evaluates the SAP S/4HANA Implementation Scoping Agent skills pack against two real-world-modeled scenarios, comparing agentic workflow outputs to single-prompt LLM baselines. The evaluation measures whether structured, multi-skill orchestration produces meaningfully better scoping deliverables than giving an LLM the same information in a single prompt.

## Evaluation Framework

### Metrics (0-5 Scale)

| Metric | Description | Scoring Criteria |
|---|---|---|
| **Completeness** | Does the output cover all critical scoping dimensions? | 0: Missing major areas. 1: Covers <40% of dimensions. 2: Covers ~50%. 3: Covers ~70%. 4: Covers ~90%. 5: Comprehensive coverage with no significant gaps |
| **Accuracy** | Are module recommendations and timeline estimates reasonable? | 0: Fundamentally wrong. 1: Major errors. 2: Some correct, some misleading. 3: Mostly reasonable with minor issues. 4: Accurate with appropriate caveats. 5: Expert-level accuracy |
| **Actionability** | Could a real consultant use this as a starting point? | 0: Unusable. 1: Generic/vague. 2: Some actionable elements. 3: Usable with significant rework. 4: Usable with minor refinement. 5: Ready to present with formatting only |
| **Consistency** | Do repeated runs produce similar quality? *(as of `eval.py`'s 2026-08-25 fix, computed programmatically from the standard deviation of cross-run scores — not judge-estimated. See DECISIONS.md #8 for why.)* | 0: Wildly different each run. 1: Major variations. 2: Moderate variations. 3: Generally consistent with some variation. 4: Highly consistent. 5: Near-identical quality across runs |
| **Time Saved** | Estimated reduction vs. manual process | Qualitative estimate: hours/days saved compared to a consultant performing the same analysis manually |

### Scoring Protocol

1. **Run each scenario 3 times** through the full skills pack pipeline (Skills 01→02→03→04, with Skill 05 supporting)
2. **Run each scenario 3 times** as a single-prompt baseline (provide all client info in one prompt, ask for complete scoping output)
3. **Score each dimension** for each run using the 0-5 rubric
4. **Average scores** across runs for consistency measurement
5. **Document specific examples** of where the skills pack outperformed or underperformed the baseline

### Evaluation Dimensions per Skill

**Skill 01 (Discovery Intake) Evaluation:**
- Did it capture all stated facts correctly?
- Were inferences reasonable and clearly tagged?
- Were clarifying questions relevant and prioritized?
- Was SAP terminology normalization accurate?
- Was the completeness score realistic?

**Skill 02 (Module Fit Analyzer) Evaluation:**
- Were module relevance ratings appropriate for the scenario?
- Were fit scores realistic (not uniformly high)?
- Did it identify genuine gaps and customization needs?
- Was the integration dependency map logical?
- Did Clean Core assessment make sense for the client context?

**Skill 03 (Implementation Roadmap) Evaluation:**
- Were phase durations realistic for the scope and company size?
- Was the resource model appropriate (not over-staffed or under-staffed)?
- Were risks specific to the scenario (not generic)?
- Was the budget framework in a reasonable range?
- Did it align with SAP Activate methodology correctly?

**Skill 04 (Executive Proposal) Evaluation:**
- Was the tone appropriate for C-level audience?
- Were technical details translated into business terms?
- Was the investment framework presented as ranges (not false precision)?
- Did the "Why Now" section connect to the client's specific situation?
- Would a real CEO/investor find this credible?

---

## Test Scenarios

### Scenario A: Mid-Market Agribusiness (Greenfield)

**Profile:** Highland Harvest Exports — Tanzanian raw cashew export company (fictional; see `scenario-a-agribusiness/`)
**Complexity Level:** Medium (small company, clear requirements, greenfield)
**Key Testing Dimensions:** Multi-currency, batch traceability, export compliance, mobile money integration, change management for non-digital workforce

**Client Brief (Input to Skill 01):**

```
We're a raw cashew nut export company based in the Southern Highlands of Tanzania called
Highland Harvest Exports. About 65 employees. We buy raw cashew nuts from 3,200+ smallholder
farmers across the region, dry and grade them at our processing facility, and export to
buyers in Europe, North America, and Asia.

Currently everything runs on Excel spreadsheets and WhatsApp groups. We use a local mobile
money provider for farmer payments and have a basic Wix website. No ERP at all.

Our biggest pain points:
- We can't track inventory from farm gate to export container accurately
- Currency management is a nightmare (TZS for farmer payments, USD for exports, EUR and
  other currencies for some buyers)
- Export documentation takes forever — phytosanitary certificates, weight notes, bills of
  lading, EU food-safety traceability paperwork
- We have no real financial reporting — everything is reconciled manually at month end
- Kernel-grade traceability is critical for premium buyers but we're doing it on paper
- We want to scale to 7,000 farmers in the next 2 years but our systems can't handle
  the current volume

We've heard about SAP but honestly don't know if it's the right fit for a company our
size. Budget is tight but our lead investor is willing to fund technology if the ROI is clear.
```

**What Good Output Looks Like (Scoring Guide):**
- Should flag SAP Business One or SAP GROW as potentially better fit than full S/4HANA
- FI/CO, MM, SD, QM should be scored as critical modules
- GTS should be flagged as relevant but potentially out of budget for Phase 1
- Should identify BTP need for mobile money integration
- Timeline should be 6-9 months (not 18-24 months — this is small scope)
- Budget framework should be $160K-$440K range depending on product choice
- Should flag change management as #1 risk (Excel → ERP for non-technical workforce)
- Should mention EU food-safety import traceability as a documentation driver (note: EUDR itself does not cover cashews — a correct analysis should not invoke it here)
- Proposal should speak to investor ROI, not just technical capabilities

---

### Scenario B: High-Tech Manufacturing Enterprise (Brownfield)

**Profile:** Constellation Satellite Systems — satellite manufacturing company (modeled on Amazon Kuiper/LEO program context)
**Complexity Level:** High (large org, complex BOM, existing SAP, export controls, multi-site)
**Key Testing Dimensions:** Complex BOM management, project systems, ITAR/EAR compliance, multi-site manufacturing, SAP system conversion, Clean Core for brownfield

**Client Brief (Input to Skill 01):**

```
Constellation Satellite Systems (CSS) is a satellite manufacturing and launch services
company headquartered in Redmond, WA with manufacturing facilities in Redmond, WA and
Huntsville, AL, plus a launch operations center in Cape Canaveral, FL.

We have approximately 2,500 employees across all sites. Annual revenue is ~$1.2B.
We manufacture Low Earth Orbit (LEO) communication satellites — currently producing
at a rate of 5 satellites per month with plans to scale to 15/month within 18 months
to support our constellation deployment timeline.

Current SAP landscape:
- SAP ECC 6.0 EHP8 on-premise (installed 2015, heavily customized)
- ~800 active SAP users (Professional + Limited Professional licenses)
- Modules in use: FI/CO, MM, SD, PP, QM, PM, PS
- ~2,400 custom ABAP objects (reports, enhancements, interfaces)
- 47 custom transactions
- Integration with: Teamcenter PLM (Siemens), MES system (Apriso/Dassault),
  Salesforce CRM, Workday HCM, Anaplan (planning), and 12 custom middleware interfaces
- SAP Basis team of 4 FTEs
- Maintenance ending: SAP ECC mainstream maintenance ends 2027, extended to 2030

Key pain points:
- ECC system is heavily customized and increasingly difficult to maintain
- Custom code creates upgrade barriers — we've skipped 3 enhancement packs
- BOM management is a nightmare — engineering BOMs in Teamcenter don't sync
  cleanly with manufacturing BOMs in SAP PP. As-built BOMs are tracked manually
- Project System (PS) is used for satellite program tracking but earned value
  management is done in Excel outside SAP
- ITAR compliance is managed through a combination of GTS (partial implementation),
  manual processes, and a separate access control database
- No real-time manufacturing visibility — MES-to-SAP integration has 4-hour lag
- Financial close takes 12 business days — target is 5 days
- Supply chain visibility is poor — long-lead components (18+ month lead times
  for space-grade electronics) have no predictive tracking
- We need to support IFRS 15/ASC 606 revenue recognition for long-term contracts
  but current FI configuration doesn't handle milestone-based recognition properly

Strategic drivers:
- Board has mandated S/4HANA migration by end of 2028 (before ECC maintenance ends)
- CEO wants "digital factory" capabilities — real-time production visibility, predictive
  quality, AI-assisted supply chain planning
- CFO wants to reduce close from 12 days to 5 days and implement proper program-level
  profitability analysis
- VP Manufacturing wants integrated BOM management (single source of truth from
  engineering through as-built)
- CISO is concerned about ITAR compliance gaps and wants GTS fully implemented
- CIO wants to reduce total custom code by 60% and move to Clean Core

Additional context:
- We're a subsidiary of a larger aerospace conglomerate that uses SAP S/4HANA Cloud
  (Private Edition) — there's pressure to align
- The parent company uses SAP Signavio for process management and LeanIX for
  enterprise architecture — we're expected to adopt these tools
- Budget: $15-25M has been allocated for the transformation program
- Timeline: Board deadline is December 2028 go-live for core finance + operations
- We've had two failed IT projects in the past 3 years (MES upgrade, PLM migration)
  which has created organizational skepticism about large IT programs
```

**What Good Output Looks Like (Scoring Guide):**
- Should recommend System Conversion (Brownfield) approach given existing ECC + parent alignment
- All major modules (FI/CO, MM, SD, PP, QM, PM, PS, GTS) should be Critical
- Custom code analysis should be prominently featured — 2,400 objects is significant
- Clean Core assessment should flag Level C or D with aggressive remediation plan
- BOM management (PP + PLM integration) should be identified as highest complexity item
- ITAR/GTS should be flagged as non-negotiable and a Phase 1 must-have
- Timeline should be 18-24 months with 2-3 waves
- Resource model should include 15-25 FTE implementation partner team
- Budget should align with $15-25M range (validate, don't just echo)
- Should recommend SAP S/4HANA Cloud Private Edition (parent alignment)
- Should reference Signavio for process mining of current state
- Should reference LeanIX for application landscape rationalization
- Should flag organizational change fatigue from failed IT projects as top risk
- Proposal should address both board mandate and organizational skepticism

---

### Edge Case Scenarios

#### Edge Case 1: Ambiguous Input with Contradictions

```
We need SAP. We're a mid-size company. Maybe 200 employees, maybe more.
We do manufacturing and also services. Our current ERP is "fine but we
need to upgrade." Budget is unlimited but we need to keep costs down.
We want everything SAP offers but only need basic functionality. Go-live
should be in 3 months. We're not in a rush. Our CEO doesn't really
support this project but the board mandated it.
```

**Expected behavior:** Should flag contradictions explicitly, set confidence to LOW, generate extensive clarifying questions, and warn that proceeding without resolution will produce unreliable outputs.

#### Edge Case 2: Non-Standard Scenario (Heavy Custom Code, Clean Core Resistance)

```
We're a pharmaceutical manufacturer running SAP ECC with 6,000+ custom ABAP
objects. Our business processes are highly specialized due to FDA regulations
and we believe 80% of our customizations are legally required. We've been told
we need to move to S/4HANA but our IT team is firmly against Clean Core —
they believe standard SAP cannot support our regulatory requirements. We want
to migrate everything as-is. Timeline: 3 years. Budget: $40M.
```

**Expected behavior:** Should respectfully challenge the "migrate as-is" approach, explain Clean Core benefits while acknowledging regulatory constraints, recommend custom code analysis to verify which customizations are truly required vs. habit, suggest a phased approach starting with custom code remediation, and reference FDA/GxP-specific SAP best practices.

#### Edge Case 3: Ecosystem-Aware Scenario

```
We're already using SAP Signavio for process mining across our 12 plants
and SAP LeanIX for application portfolio management. We have a Joule for
Consultants license through our Deloitte engagement. We want to evaluate
S/4HANA migration but we already have significant tooling investment.
How does your scoping analysis work alongside our existing SAP tools?
```

**Expected behavior:** Should recognize the existing toolchain and explicitly reference how skills pack outputs feed into Signavio (process models), LeanIX (application inventory), and Cloud ALM (project governance). Should NOT duplicate capabilities these tools already provide. Should recommend using J4C for detailed configuration questions during Explore phase.

---

## Baseline Comparison Protocol

### Single-Prompt Baseline

For each scenario, use the following single prompt to establish a baseline:

```
You are an experienced SAP S/4HANA implementation consultant and enterprise architect.
A potential client has provided the following information about their company and needs.
Please provide a comprehensive implementation scoping analysis including:
1. A structured assessment of the client's current state and requirements
2. A module fit analysis mapping their needs to SAP S/4HANA modules
3. A phased implementation roadmap with timeline and resource estimates
4. An executive-level proposal summary suitable for C-level stakeholders

Client information:
[INSERT SCENARIO BRIEF HERE]
```

### Comparison Criteria

| Dimension | What to Compare |
|---|---|
| **Structure** | Is the skills pack output more consistently structured than the baseline? |
| **Depth** | Does the skills pack produce deeper analysis per dimension? |
| **SAP Specificity** | Does the skills pack use correct SAP terminology, scope items, and methodology? |
| **Gap Detection** | Does the skills pack identify information gaps and contradictions? |
| **Inference Quality** | Does the skills pack make and tag reasonable inferences? |
| **Actionability** | Which output could a consultant more readily use? |
| **Clean Core** | Does the skills pack assess Clean Core compliance? (Baseline likely won't) |
| **SAP Toolchain** | Does the skills pack reference Signavio, LeanIX, Cloud ALM? (Baseline likely won't) |
| **Consistency** | Which produces more consistent quality across multiple runs? |

---

## Results Template

### Scenario [A/B] — Run [1/2/3]

| Metric | Skills Pack Score | Baseline Score | Delta | Notes |
|---|---|---|---|---|
| Completeness | /5 | /5 | | |
| Accuracy | /5 | /5 | | |
| Actionability | /5 | /5 | | |
| Consistency | /5 | /5 | | |
| **Average** | **/5** | **/5** | | |

**Time Saved Estimate:** ___ hours/days vs. manual process

**Specific Strengths (Skills Pack):**
-

**Specific Weaknesses (Skills Pack):**
-

**Specific Strengths (Baseline):**
-

**Specific Weaknesses (Baseline):**
-

---

## Summary Scorecard Template

| | Scenario A (Agribusiness) | Scenario B (High-Tech) | Edge Cases | Overall |
|---|---|---|---|---|
| **Skills Pack Avg** | /5 | /5 | Pass/Fail | /5 |
| **Baseline Avg** | /5 | /5 | N/A | /5 |
| **Delta** | | | | |
| **Key Insight** | | | | |
