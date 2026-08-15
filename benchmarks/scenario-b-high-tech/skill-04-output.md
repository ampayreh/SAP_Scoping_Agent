# Skill 04 Output: Executive Proposal for Constellation Satellite Systems (CSS)

## Document Metadata

| Field | Value |
|---|---|
| **Prepared for** | Board of Directors, CEO, CFO, CIO, CISO, and VP Manufacturing |
| **Company** | Constellation Satellite Systems (CSS), a subsidiary of [Parent Conglomerate] |
| **Date** | February 2026 |
| **Document Classification** | Confidential: Board Use Only |
| **Version** | 1.0, For Discussion |
| **Source Brief** | DB-20260222-CSS (Skill 01 Discovery Brief, 90% completeness) |
| **Source Module Analysis** | MFA-20260222-CSS (Skill 02 Module Fit Analysis) |
| **Source Roadmap** | IR-20260222-CSS (Skill 03 Implementation Roadmap) |
| **Audience Calibration** | Board of Directors, C-Suite, VP Manufacturing; authoritative, data-driven tone addressing both the mandate and organizational skepticism from prior project failures |

---

## 1. Executive Summary

Constellation Satellite Systems has established itself as a premier LEO satellite manufacturer, generating $1.2B in annual revenue and preparing to scale production from 5 to 15 satellites per month. The board's mandate to migrate from SAP ECC 6.0 to S/4HANA by December 2028 is both a platform necessity and a strategic opportunity. ECC mainstream maintenance ends in 2027, with extended maintenance expiring in 2030. The 2,400 custom ABAP objects and 47 custom transactions that currently sustain CSS operations sit on an expiring foundation. Continuing on ECC is not a viable long-term option; the question is whether CSS executes this transition on its own terms or is forced into it under pressure.

This proposal recommends a system conversion (brownfield) to S/4HANA Cloud Private Edition via SAP RISE, executed over 22 months in a pre-project phase followed by three implementation waves. The brownfield approach preserves 10 years of financial history, master data, and configuration that CSS cannot afford to rebuild. It retains user familiarity with existing processes while modernizing the platform, and it aligns CSS with the parent company's S/4HANA Cloud Private Edition standard. The alternative, a greenfield reimplementation, would cost more, take longer, and force wholesale process redesign on an organization that has already endured two failed IT projects in three years.

The transformation delivers five measurable outcomes: financial close compression from 12 business days to 5, eliminating approximately $1.5M annually in reconciliation overhead; full ITAR/EAR compliance via integrated Global Trade Services, closing gaps that currently expose CSS to fines of up to $1.2M per violation; real-time manufacturing visibility through MES integration, replacing the current 4-hour data lag that costs an estimated $2M to $3M annually in rework and scheduling disruption; integrated BOM lifecycle management from engineering through manufacturing through as-built configuration, establishing the digital foundation for 15 satellites per month; and a 60% reduction in custom code, lowering annual support costs by an estimated $2M while enabling continuous platform innovation.

**Investment:** $18M to $23M over 22 months, within the board-approved $15M to $25M allocation. Annual run rate post go-live decreases by an estimated $3M to $5M through reduced support costs, finance efficiency, and compliance risk elimination. **Timeline:** Pre-project phase beginning Q3 2026, Wave 1 (finance and compliance) go-live Q2 2028, Wave 2 (manufacturing and operations) go-live Q4 2028, Wave 3 (advanced analytics) delivered H1 2029. **Recommended next step:** Authorize the 12-week pre-project phase to execute custom code analysis, ITAR data scoping, and integration architecture design.

---

## 2. Current State Assessment

### Business Context

CSS employs approximately 2,500 people across three facilities: Redmond, WA (satellite manufacturing headquarters), Huntsville, AL (subassembly manufacturing), and Cape Canaveral, FL (final integration, test, and launch operations). The company manufactures LEO constellation satellites for commercial and government customers, with production currently at 5 satellites per month and a contracted ramp to 15 per month within 18 months. At full production rate, that manufacturing volume represents approximately $2.4B in annual revenue.

CSS operates SAP ECC 6.0 EHP8, installed in 2015, with approximately 800 active SAP users across all three sites. The ECC system supports Financial Accounting, Controlling, Materials Management, Sales and Distribution, Production Planning, Quality Management, Plant Maintenance, Project System, and a partial Global Trade Services implementation. Workday handles human capital management, Salesforce manages customer relationships, Siemens Teamcenter serves as the PLM system for engineering BOMs, Dassault Apriso provides shop floor MES execution, and Anaplan supports financial and operational planning.

### Operational Challenges

The discovery phase identified eight interconnected operational pain points, each of which compounds the others.

**Custom code burden blocks platform evolution.** 2,400 custom ABAP objects and 47 custom transactions have accumulated over a decade of ECC operation. Three enhancement packs have been skipped because custom code conflicts made upgrades prohibitively expensive. The 4-person Basis team spends the majority of its capacity maintaining customizations rather than enabling new capabilities. Annual support cost for this custom footprint is estimated at $3M to $4M. Every month CSS remains on ECC, the technical debt grows.

**BOM management fragmentation creates manufacturing risk.** Engineering BOMs reside in Teamcenter. Manufacturing BOMs are maintained separately in SAP PP with lossy synchronization. As-built configurations are tracked manually outside both systems. Three disconnected BOM representations mean that when an engineering change order is issued, it takes days to propagate through the manufacturing process, and there is no automated verification that the satellite on the production line matches the approved design. At 15 satellites per month, this fragmentation becomes a quality and schedule risk of the first order.

**ITAR compliance operates on manual controls and hope.** Satellites are ITAR-controlled defense articles under USML Category XV. CSS currently manages export compliance through a partial GTS implementation, manual processes, and a separate access control database. Denied party screening covers some transaction types but not all. License management (DSP-5, DSP-73, TAA, MLA) is tracked in spreadsheets. Deemed export controls for foreign person access to technical data rely on a system that is not integrated with SAP. A single ITAR violation can result in fines up to $1.2M per occurrence, debarment from government contracts, and criminal liability.

**MES integration lag blinds manufacturing leadership.** The current interface between Apriso MES and SAP operates on a 4-hour batch cycle. Production planners and program managers cannot see real-time manufacturing status. Quality escapes are discovered after the fact rather than prevented in process. The estimated annual impact from rework, scrap, and scheduling disruption attributable to this visibility gap is $2M to $3M.

**Financial close consumes 12 business days.** Manual reconciliations between FI and CO, Excel-based earned value management, and multi-step intercompany processing extend the monthly close to 12 business days. The CFO's target is 5 days. Revenue recognition for long-term satellite contracts (IFRS 15/ASC 606) is handled manually outside SAP, adding compliance risk and audit exposure. Program-level profitability is not visible until weeks after period end.

### Technology Landscape

| Function | Current System | Key Limitation |
|---|---|---|
| ERP (Core) | SAP ECC 6.0 EHP8 (2015) | 2,400 custom objects; 3 skipped enhancement packs; maintenance ending 2027/2030 |
| PLM | Siemens Teamcenter | Engineering BOM authority; lossy sync with SAP PP manufacturing BOM |
| MES | Dassault Apriso | 4-hour batch integration lag with SAP; no real-time visibility |
| CRM | Salesforce | No integration with SAP SD for order/billing flow |
| HCM | Workday | Cost center and employee master sync required |
| Planning | Anaplan | No integration with SAP CO/PS for actuals vs. forecast |
| Middleware | 12 custom interfaces | Unspecified technology; fragile, undocumented integration backbone |
| Export Compliance | Partial GTS + manual + separate database | Fragmented ITAR controls; audit-risky |

### Risk of Inaction

Remaining on ECC beyond 2027 exposes CSS to four compounding risks.

1. **Platform obsolescence.** SAP ECC mainstream maintenance ends in 2027. Extended maintenance to 2030 is available at premium cost, but SAP will not deliver functional enhancements, and the partner ecosystem's ECC expertise is migrating to S/4HANA. Every year of delay narrows the available implementation talent pool.

2. **ITAR compliance exposure intensifies.** The current fragmented compliance model is a known vulnerability. Defense prime contractors are increasing flow-down requirements for supply chain compliance transparency. The Department of State is increasing enforcement activity. The risk is not theoretical; it is active and growing.

3. **Production scaling is blocked.** Ramping from 5 to 15 satellites per month on a manufacturing platform with 4-hour data lag, fragmented BOMs, and manual quality tracking is operationally dangerous. Real-time manufacturing visibility is not a nice-to-have at 15 units per month; it is a prerequisite.

4. **Parent company alignment timeline closes.** The parent conglomerate has standardized on S/4HANA Cloud Private Edition with Signavio and LeanIX. CSS's delayed migration creates an integration gap with the parent's consolidation and governance framework that will become more difficult to close over time.

---

## 3. Transformation Vision

### What CSS Gains

The S/4HANA transformation delivers capabilities organized around CSS's five stated strategic priorities.

**Real-time manufacturing visibility and digital factory readiness.** MES integration moves from a 4-hour batch cycle to near-real-time data exchange. Production planners see live manufacturing status across Redmond, Huntsville, and Cape Canaveral. Quality inspection results flow directly into SAP from the shop floor, enabling in-process intervention rather than after-the-fact discovery. This is the operational foundation required to sustain 15 satellites per month.

**Integrated BOM lifecycle from engineering through as-built.** Bidirectional PLM integration with Teamcenter establishes a single source of truth for engineering BOMs that flows cleanly into SAP manufacturing BOMs. As-built configurations are captured in SAP through serialized production order confirmations, closing the current manual tracking gap. Engineering change orders propagate from Teamcenter to the shop floor with effectivity date control.

**Full ITAR/EAR compliance through integrated Global Trade Services.** A complete GTS implementation replaces the current patchwork of partial automation, manual processes, and separate databases. Denied party screening covers all transaction types. License management is automated with utilization tracking and expiration alerts. Product classification at the material master level enforces ITAR/EAR jurisdiction determination. Deemed export access controls are enforced within the SAP authorization model. The result is an audit-ready compliance posture that eliminates the current regulatory exposure.

**Five-day financial close with program-level profitability.** The S/4HANA Universal Journal eliminates the separate FI and CO reconciliation that drives the current 12-day cycle. Revenue Accounting and Reporting (RAR) automates IFRS 15/ASC 606 revenue recognition for milestone-based satellite contracts. Earned value management moves from Excel into Project System with integrated cost actuals. Program-level profitability analysis provides the CFO with real-time visibility into satellite program margins. The close target of 5 days is achievable within 2 to 3 close cycles after go-live, based on industry benchmarks for companies of comparable complexity.

**Clean Core and continuous innovation.** A 60% reduction in custom code, from 2,400 objects to approximately 960 retained, lowers annual support costs by an estimated $2M and enables CSS to adopt SAP's quarterly cloud updates automatically. Retained extensions migrate to the Business Technology Platform, keeping the S/4HANA core clean and upgradable. Future capabilities, including AI-driven quality prediction, predictive maintenance, and advanced supply chain analytics, become accessible without a major upgrade project.

### Module Scope

| Business Area | Modules | Wave | What It Delivers |
|---|---|---|---|
| Financial Management and Controlling | FI, CO, RAR | Wave 1 | 5-day close, automated revenue recognition, program-level profitability, parent company consolidation |
| Export Compliance | GTS | Wave 1 | Full ITAR/EAR compliance: screening, license management, classification, deemed export controls |
| Manufacturing and Quality | PP, QM | Wave 2 | BOM lifecycle integration, real-time MES connectivity, AS9100D quality management, serialized traceability |
| Supply Chain and Procurement | MM | Wave 2 | Long-lead component planning, supplier quality integration, 3x procurement volume scaling |
| Sales and Program Management | SD, PS | Wave 2 | Milestone billing, Salesforce integration, earned value management, WBS-based program tracking |
| Asset and Maintenance Management | PM | Wave 2 | Preventive and corrective maintenance, calibration management, predictive maintenance readiness |
| Integration and Extension Platform | BTP | All Waves | Middleware consolidation (12 interfaces), PLM/MES integration, retained custom code hosting, ITAR access governance |
| Advanced Analytics | SAC, AI Core | Wave 3 | Predictive quality, predictive maintenance, operational dashboards, demand sensing |

### Integration Architecture

The current integration landscape consists of 12 custom middleware interfaces connecting SAP ECC to Teamcenter, Apriso, Salesforce, Workday, Anaplan, and other systems. The technology underpinning these interfaces is undocumented and fragile. The transformation replaces this with a unified integration architecture on SAP Business Technology Platform (BTP) Integration Suite.

Five major external system integrations define the architecture.

| External System | Integration Pattern | Direction | Wave | Complexity |
|---|---|---|---|---|
| Siemens Teamcenter (PLM) | Real-time API via BTP or SAP Engineering Control Center | Bidirectional | Wave 2 | High: BOM lifecycle, engineering changes, as-built feedback |
| Dassault Apriso (MES) | Real-time API via BTP Integration Suite | Bidirectional | Wave 2 | High: production confirmations, material consumption, quality results |
| Salesforce (CRM) | Real-time API via BTP (pre-built content) | Bidirectional | Wave 2 | Medium: opportunity to sales order, billing status sync |
| Workday (HCM) | Batch API via BTP (pre-built content) | Bidirectional | Wave 1 | Medium: cost center sync, employee master, time entry |
| Anaplan (Planning) | Batch API via BTP Integration Suite | Bidirectional | Wave 1 | Medium: CO/PS actuals outbound, approved budgets inbound |

The remaining custom middleware interfaces are inventoried, classified, and migrated to BTP Integration Suite across all three waves, with prioritization aligned to module go-live dependencies.

### Clean Core Approach

CSS currently operates at Clean Core Level D: 2,400 custom ABAP objects, 47 custom transactions, and 3 skipped enhancement packs. The target is Level B (Clean Core with Extensions) within 18 months of final go-live.

Achieving this requires a disciplined four-category classification of every custom object.

| Category | Target % | Description | Action |
|---|---|---|---|
| **Retire** | 60% (~1,440 objects) | Standard S/4HANA functionality replaces the custom code | Decommission; adopt standard process |
| **Adapt** | 15 to 20% (~360 to 480 objects) | S/4HANA simplification adjustments needed for compatibility | Modify for S/4HANA syntax/data model; retain on-stack |
| **Retain on-stack** | 10 to 15% (~240 to 360 objects) | Business-critical; no standard equivalent; S/4HANA compatible | Keep in S/4HANA core; document and manage |
| **Move to BTP** | 10 to 15% (~240 to 360 objects) | Custom extensions requiring side-by-side deployment | Migrate to BTP ABAP Environment |

The CIO's 60% retirement target is aggressive but achievable based on SAP Custom Code Migration Worklist benchmarks for companies of comparable customization density. The pre-project phase will validate this target against CSS's actual custom code portfolio before any implementation budget is committed.

Clean Core is not an abstract aspiration. It has a concrete financial impact: every custom object retired is an object that does not need to be tested during upgrades, supported by the Basis team, or documented for knowledge transfer. At CSS's scale, the difference between Level D and Level B represents approximately $2M annually in reduced total cost of ownership.

---

## 4. Implementation Approach

### System Conversion (Brownfield) Rationale

The recommended approach is a system conversion, commonly called a brownfield migration. CSS's ECC 6.0 EHP8 system is technically converted to S/4HANA, preserving the existing database, configuration, master data, and transactional history. This approach is recommended for four specific reasons.

1. **Preservation of institutional knowledge.** Ten years of financial accounting configuration, cost center structures, material masters, project system templates, and quality inspection plans represent significant intellectual property. Rebuilding this in a greenfield implementation would add 6 to 12 months and $4M to $8M to the program.

2. **User familiarity reduces change risk.** CSS's 800 SAP users know the existing processes and data structures. A brownfield conversion retains that familiarity while upgrading the platform and user experience to S/4HANA Fiori. Given the organizational skepticism from two failed IT projects, minimizing disruption is a strategic imperative.

3. **ITAR audit trail continuity.** ITAR compliance requires retention and accessibility of historical transactional data related to controlled articles. A system conversion preserves this audit trail within the production system. A greenfield approach would require a separate archival strategy with compliance counsel validation.

4. **Parent company alignment.** The parent conglomerate operates on S/4HANA Cloud Private Edition. CSS's brownfield conversion to the same platform enables standardized consolidation, shared governance tools (Signavio, LeanIX), and a common managed service model.

### Program Structure

The implementation follows SAP Activate methodology, organized into a pre-project phase and three implementation waves, each concluding with an independent go-live decision.

| Phase | Timeline | Duration | Scope | Key Outcomes |
|---|---|---|---|---|
| **Pre-Project** | Q3 to Q4 2026 | 12 weeks | Custom code analysis (2,400 objects), ITAR data scoping, integration architecture design, change readiness assessment, PLM/MES integration prototyping | Classification of all custom objects; ITAR scope confirmed; integration architecture approved; change readiness baseline established |
| **Wave 1: Finance and Compliance** | Q1 to Q2 2028 | 6 months | FI, CO, RAR, GTS, BTP (foundation) | 5-day close capability; RAR activated for IFRS 15/ASC 606; full GTS for ITAR/EAR; BTP Integration Suite deployed; 12 middleware interfaces modernized (priority set) |
| **Wave 2: Manufacturing and Operations** | Q3 to Q4 2028 | 6 months | PP, QM, MM, SD, PS, PM, BTP (PLM/MES integration) | Real-time MES integration; integrated BOM lifecycle; production planning for 15 units/month; milestone billing; earned value management; AS9100D quality compliance |
| **Wave 3: Advanced Analytics** | H1 2029 | 6 months | SAC, AI Core, predictive quality, predictive maintenance, enhanced dashboards | Predictive quality analytics; predictive maintenance for manufacturing equipment; real-time operational dashboards; demand sensing evaluation |

> **Board deadline compliance:** Wave 2 go-live in Q4 2028 satisfies the board-mandated December 2028 deadline for core finance and operations. Wave 3 delivers optimization capabilities in H1 2029 on a stabilized foundation.

### SAP Activate Alignment

Each wave follows the four-phase SAP Activate structure: Discover, Prepare, Explore, Realize, and Deploy. Within each wave, the approach includes Fit-to-Standard workshops (comparing CSS requirements against standard S/4HANA processes), iterative configuration sprints, two data migration dry runs, full end-to-end integration testing, user acceptance testing with CSS business users executing real scenarios, and a formal Go/No-Go decision requiring executive sponsor approval before each go-live.

### Team Structure

| Role | Responsibility | Source |
|---|---|---|
| **Executive Sponsor** | Board-level accountability; funding; obstacle removal | CEO or CIO (to be confirmed) |
| **Program Director** | Day-to-day program governance; budget and timeline management | Implementation Partner (senior) |
| **Business Process Leads** (8 to 10) | Requirements validation, testing, acceptance for their functional domain | CSS (Finance, Manufacturing, Quality, Supply Chain, Programs, Compliance, IT) |
| **Solution Architect** | Technical design authority; integration architecture; Clean Core governance | Implementation Partner |
| **Functional Consultants** (10 to 14) | System configuration, Fit-to-Standard facilitation, testing | Implementation Partner |
| **Technical/Integration Team** (6 to 8) | BTP development, custom code remediation, PLM/MES integration, middleware modernization | Implementation Partner + CSS Basis team |
| **Change Management Lead** | OCM strategy, communications, training, adoption tracking | Implementation Partner (dedicated) |
| **Site Change Champions** (3) | On-site engagement, resistance management, feedback collection | CSS (one per site: Redmond, Huntsville, Cape Canaveral) |
| **ITAR Compliance Lead** | GTS design validation, deemed export architecture, compliance audit readiness | CSS CISO office + external compliance counsel |

### Change Management Approach

Given the organizational context of two failed IT projects, change management is not a supporting workstream; it is a core program deliverable. The approach addresses the specific challenge CSS faces: rebuilding organizational trust in technology-driven transformation.

**Change readiness assessment (pre-project).** A formal, site-by-site assessment conducted by an independent OCM specialist. This assessment includes structured interviews with middle management and shop floor representatives, analysis of the failed MES and PLM project post-mortems, and identification of specific resistance patterns, trust gaps, and communication failures from prior projects. The results directly inform the Wave 1 communication strategy.

**Site-level change champions.** One designated change champion at each site (Redmond, Huntsville, Cape Canaveral) serves as the local voice of the program. These are respected operational leaders, not IT staff, who translate program objectives into language their colleagues understand and trust. They are allocated at 25% capacity throughout the program.

**Early wins strategy.** Wave 1 is designed to deliver visible improvements before Wave 2 introduces manufacturing process changes. New Fiori self-service applications for time entry, purchase requisition approval, and expense reporting reach every SAP user. Automated compliance screening replaces manual spreadsheet lookups for the GTS team. The 5-day financial close is measurable and verifiable. These tangible results build credibility incrementally.

**Role-based training at scale.** All 800 SAP users receive training designed for their specific role and site context. Shop floor operators at Redmond and Huntsville learn the transactions they need for production confirmation and quality recording. Finance users learn the new close process and Fiori analytical apps. Program managers learn Project System EVM and milestone tracking. Training is delivered on-site at each facility, not through generic e-learning modules.

---

## 5. Investment Framework

### Budget Overview

| Cost Category | Estimated Range | Notes |
|---|---|---|
| **SAP Licensing (RISE)** | $3.0M to $4.0M/year | S/4HANA Cloud Private Edition via RISE; 800 users (350 Professional, 400 Limited Professional, 50 Developer); BTP Enterprise Agreement; SAC |
| **Implementation Services** | $8.0M to $11.0M | Systems integrator for all three waves; blended rate inclusive of functional, technical, and change management resources |
| **Custom Code Remediation** | $1.5M to $2.5M | Analysis, classification, retirement, adaptation, and BTP migration of 2,400 ABAP objects |
| **Integration Development** | $2.0M to $3.0M | PLM (Teamcenter), MES (Apriso), CRM (Salesforce), HCM (Workday), Planning (Anaplan) integrations via BTP; middleware modernization for 12 custom interfaces |
| **Internal Resources and Backfill** | $1.5M to $2.0M | CSS staff allocated to project (business process leads, IT team, change champions); backfill for operational roles during peak project phases |
| **Training and Enablement** | $0.5M to $0.8M | Role-based training for 800 users; SAP Learning Hub; super user development; site-specific training delivery at three locations |
| **Contingency (10 to 15%)** | $1.5M to $2.7M | Scope additions, integration complexity overruns, extended timelines |
| **Total Program Investment** | **$18.0M to $23.0M** | Within board-approved $15M to $25M allocation |

### Annual Run Rate Post Go-Live

| Category | Estimated Annual Cost |
|---|---|
| SAP RISE Subscription (S/4HANA Cloud PE + BTP) | $3.2M |
| Application Managed Services | $0.8M |
| Internal IT Support (redeployed Basis team) | $0.6M |
| **Total Annual Recurring** | **$4.6M** |

> **Context:** CSS currently spends an estimated $6M to $8M annually on ECC on-premise hosting, Basis team support, custom code maintenance, and manual workaround labor. The post-transformation run rate of $4.6M represents a net annual saving of $1.4M to $3.4M in direct IT costs, before accounting for operational efficiency gains.

### Return on Investment

The ROI case is built on five quantifiable value drivers.

**1. Financial close efficiency.** Reducing the close cycle from 12 days to 5 days recovers approximately $1.5M annually in finance team capacity that is currently consumed by manual reconciliation, intercompany processing, and Excel-based revenue recognition. This capacity can be redirected to financial analysis, forecasting, and strategic decision support.

**2. ITAR compliance risk elimination.** A single ITAR violation can result in fines up to $1.2M per occurrence and debarment from government contracts. The current fragmented compliance posture is a known risk that the board carries every quarter. Full GTS implementation eliminates this exposure. The value is measured not in savings but in risk that ceases to exist.

**3. Manufacturing visibility and production efficiency.** Eliminating the 4-hour MES data lag and integrating the BOM lifecycle reduces rework, scrap, and scheduling disruption estimated at $2M to $3M annually. As production scales to 15 satellites per month, the impact of these inefficiencies would grow proportionally without intervention.

**4. Custom code retirement savings.** Reducing 2,400 custom objects by 60% lowers annual support and maintenance costs by an estimated $2M. Equally important, it eliminates the upgrade barrier that has prevented CSS from adopting three enhancement packs and will prevent adoption of future S/4HANA innovations.

**5. Production scaling enablement.** The ramp from 5 to 15 satellites per month represents a growth from $1.2B to approximately $2.4B in annual revenue. The current ERP infrastructure cannot support this scale. The S/4HANA platform provides the operational backbone for that growth. This is not a cost savings; it is a revenue enablement investment.

**Combined estimated annual benefit: $7M to $10M**, implying a **payback period of approximately 2 to 3 years** from Wave 1 go-live. These estimates will be validated with CSS's actual financial data during the pre-project phase.

### Cost of Inaction

Choosing to defer the S/4HANA migration has its own cost, and that cost compounds annually.

| Cost of Inaction Category | Estimated Annual Impact |
|---|---|
| ECC extended maintenance premium (post-2027) | $0.5M to $1.0M incremental |
| Custom code maintenance and Basis team support (status quo) | $3M to $4M continuing |
| ITAR compliance risk exposure (potential per-violation fines) | Up to $1.2M per occurrence |
| MES data lag: rework, scrap, and schedule disruption | $2M to $3M continuing |
| Finance team capacity consumed by 12-day close process | $1.5M continuing |
| Inability to scale production to 15 satellites/month | Revenue growth constraint ($1.2B+ at risk) |
| **Total quantifiable annual cost of inaction** | **$8M to $11M+** |

The $18M to $23M program investment, viewed against an $8M to $11M annual cost of inaction, yields a breakeven within 2 to 3 years even before accounting for the revenue enablement of the production ramp. Deferral does not save money. It shifts cost from a controlled, planned investment into uncontrolled operational drag and regulatory exposure.

---

## 6. Why Now

Four converging factors make this the right time to execute.

### 1. The ECC maintenance clock is running

SAP ECC mainstream maintenance ends in 2027. Extended maintenance is available to 2030 at premium cost, but with no functional enhancements, a shrinking support ecosystem, and increasing difficulty hiring ECC-skilled consultants. The board-mandated December 2028 go-live provides a 2-year buffer before extended maintenance expiration. Delay compresses that buffer and increases execution risk. Starting the pre-project phase in Q3 2026 provides a realistic 22-month runway to meet the board deadline.

### 2. Production ramp demands a digital foundation

CSS has committed to tripling satellite production within 18 months. That commitment was made to constellation customers who have contracted delivery schedules. Running a 3x production ramp on a manufacturing platform with 4-hour data lag, fragmented BOMs, and manual quality tracking is operationally reckless. The S/4HANA platform with real-time MES integration and integrated BOM lifecycle management is the digital factory foundation that the production ramp requires.

### 3. ITAR compliance gaps are an active risk

The current compliance posture is not merely imperfect; it is fragmented in ways that a determined auditor or disgruntled employee could exploit. Every month that CSS operates with partial GTS, manual license tracking, and a separate access control database is a month of active regulatory exposure. Full GTS implementation closes these gaps permanently.

### 4. Parent company alignment has a window

The parent conglomerate has standardized on S/4HANA Cloud Private Edition and is actively deploying Signavio and LeanIX across subsidiaries. CSS's timely migration positions the company as a model subsidiary transformation, strengthening its standing within the conglomerate. Delaying creates a widening governance and technology gap that will be more expensive to close later.

---

## 7. Why This Program Will Succeed

This section addresses the question that everyone in this room is thinking: why will this program succeed when the MES upgrade and PLM migration did not?

The Board, leadership team, and workforce at CSS have legitimate reasons for skepticism. Two significant IT projects have failed in the past three years, eroding confidence in technology-driven transformation programs. This proposal does not dismiss that history. It learns from it.

### What is different this time

**Proven methodology, not custom invention.** SAP Activate is a structured project methodology refined across tens of thousands of S/4HANA implementations globally. It defines clear phase gates, deliverables, and quality checkpoints. The MES and PLM projects, based on the post-mortem assessments, lacked a comparable governance framework. This program follows an established playbook with measurable milestones at every stage.

**Phased delivery, not big-bang risk.** The three-wave structure means CSS never bets the entire program on a single go-live. Wave 1 delivers finance and compliance. If Wave 1 encounters issues, they are resolved before Wave 2 begins. Each wave has an independent Go/No-Go decision requiring executive approval. This is fundamentally different from a single-event deployment where everything must work simultaneously.

**Pre-project custom code analysis reduces the largest uncertainty.** The 2,400 custom ABAP objects are the single biggest risk factor in this program. Rather than discovering their impact during implementation, the 12-week pre-project phase classifies every object before a single dollar of implementation budget is spent. If the analysis reveals that the 60% retirement target is not achievable, the program scope, timeline, and budget are adjusted before the first wave begins. This is risk management, not risk avoidance.

**Dedicated change management as a funded workstream.** The failed projects reportedly underinvested in organizational change. This program allocates 12% to 15% of total budget to change management: a dedicated OCM lead, a change champion at each of the three sites, formal change readiness assessment, communication campaigns, role-based training for all 800 users, and on-site support during every go-live. Change management is not an afterthought; it is a line item with a budget, a plan, and accountability.

**Board-level governance with monthly steering committee.** The program steering committee will include the CEO, CFO, CIO, and CISO, meeting monthly. This is not a quarterly status update buried in an IT portfolio review. It is active governance with decision authority and escalation accountability. The steering committee approves every Go/No-Go decision before each wave go-live. If the program is off track, the Board will know within 30 days, not 6 months.

**An experienced implementation partner with aerospace and defense credentials.** The selected systems integrator must demonstrate prior S/4HANA brownfield conversion experience at scale, aerospace and defense industry specialization, ITAR compliance project experience, and a named team with verifiable references. This is not a project for a generalist firm learning on CSS's budget.

**Early wins to rebuild organizational confidence.** Wave 1 is deliberately designed to deliver visible, tangible improvements before the more disruptive manufacturing transformation in Wave 2. A 5-day financial close, automated compliance screening, and modern Fiori self-service applications demonstrate that the program delivers results. By the time Wave 2 begins, the organization has seen evidence that this program is different.

### Governance Structure

| Governance Body | Frequency | Participants | Authority |
|---|---|---|---|
| **Board Steering Committee** | Monthly | CEO, CFO, CIO, CISO, Program Director | Go/No-Go decisions, budget approval, strategic direction, escalation resolution |
| **Program Review** | Bi-weekly | CIO, VP Manufacturing, Business Process Leads, Program Director, Solution Architect | Scope decisions, risk mitigation, cross-wave coordination |
| **Wave Execution Stand-up** | Weekly | Program Director, Functional Leads, Technical Lead, OCM Lead | Progress tracking, issue resolution, dependency management |
| **Site Coordination** | Weekly | Site Change Champions, Program Director | Site-specific readiness, local issue resolution, training scheduling |

---

## 8. Risk Management

| # | Risk | Business Impact | Mitigation |
|---|---|---|---|
| 1 | **Organizational change fatigue from two failed IT projects.** Middle management and shop floor personnel are skeptical of large technology programs. | Low adoption; parallel manual processes persist; investment fails to deliver ROI. | Dedicated OCM workstream funded at 12 to 15% of budget. Change readiness assessment conducted in pre-project. Formal post-mortem of failed MES and PLM projects to identify and address root causes. Early wins in Wave 1 to rebuild confidence. |
| 2 | **Production ramp conflict with system conversion.** The 3x production ramp (5 to 15 satellites/month) overlaps with the implementation timeline. Manufacturing disruption during cutover could have multi-million-dollar revenue impact. | Delayed constellation deployment, contract penalties, customer relationship damage. | Wave structure separates financial cutover (Wave 1) from manufacturing cutover (Wave 2). Wave 2 cutover planned during a reduced production window. Parallel run of MES integration (old and new) during transition. Manufacturing continuity plan required before Wave 2 Go/No-Go. |
| 3 | **ITAR compliance gaps during GTS transition.** Moving from partial GTS plus manual controls to full GTS creates a transition period where compliance may be inconsistent. | Regulatory fines (up to $1.2M per violation), government contract debarment, criminal liability. | All existing manual ITAR controls remain active in parallel until full GTS is validated. DDTC-registered compliance counsel engaged during design. Pre-go-live ITAR compliance audit required. GTS placed in Wave 1 to minimize transition duration. |
| 4 | **PLM/MES integration complexity.** Teamcenter BOM integration and Apriso real-time connectivity are the two most technically complex integrations in the program. | Delayed Wave 2 go-live; manufacturing continues on fragmented BOM and 4-hour data lag. | Integration architecture design begins in pre-project phase (not Wave 2). Proof-of-concept prototypes for both integrations completed before Wave 2 Explore phase. Fallback BOM management process defined. |
| 5 | **Custom code remediation falls below 60% retirement target.** If fewer custom objects can be retired than expected, testing scope, timeline, and budget increase. | Budget overrun, timeline extension, potential breach of December 2028 deadline. | Pre-project custom code analysis (12 weeks) classifies all 2,400 objects before implementation begins. If retirement rate falls below 50%, escalation to steering committee for scope and budget adjustment before Wave 1 starts. |

---

## 9. Recommended Next Steps

| Step | Timeline | Outcome |
|---|---|---|
| **Board approval to proceed** | March 2026 | Budget allocation for pre-project phase; executive sponsor confirmed |
| **Implementation partner selection** | April to May 2026 | RFP, evaluation, and SOW execution with aerospace-qualified SI |
| **Pre-project phase launch** | Q3 2026 (12 weeks) | Custom code analysis complete; ITAR data scope confirmed; integration architecture approved; change readiness baseline established |
| **SAP RISE contracting** | Q3 2026 | S/4HANA Cloud Private Edition subscription, BTP Enterprise Agreement, infrastructure sizing confirmed with parent company MSP |
| **Wave 1 kickoff** | Q1 2027 | Discover/Prepare phase begins for FI, CO, RAR, GTS |
| **Wave 1 go-live** | Q2 2028 | Financial Management, Controlling, Revenue Recognition, Global Trade Services operational |
| **Wave 2 go-live** | Q4 2028 | Manufacturing, Quality, Supply Chain, Sales, Project System, Maintenance operational; board deadline met |
| **Wave 3 delivery** | H1 2029 | Advanced analytics, predictive quality, predictive maintenance deployed on stabilized foundation |

> This proposal provides the board with the information needed to authorize the pre-project phase. That 12-week phase is designed to resolve the largest uncertainties (custom code scope, ITAR data boundaries, integration architecture) before committing the full $18M to $23M implementation budget. The pre-project phase investment is approximately $1.5M to $2.0M, fully creditable to the overall program. It is the lowest-risk way to begin.

---

## Appendices (Available Upon Request)

- **A:** Detailed Module Scope Matrix: fit/gap analysis per module with SAP scope item references, fit scores, and Clean Core assessments (from Skill 02)
- **B:** Full Implementation Timeline: wave-by-wave view with resource assignments, critical path, and milestone dependencies (from Skill 03)
- **C:** Team Structure: organization chart with named roles, allocation percentages, and partner staffing model
- **D:** Detailed Cost Breakdown: by wave, by cost category, with stated assumptions and sensitivity analysis
- **E:** Custom Code Analysis Framework: classification methodology, retirement criteria, BTP migration approach
- **F:** Risk Register: complete risk register with probability, impact, mitigation, and contingency for each identified risk (from Skill 03)
- **G:** SAP Reference Architecture: Aerospace and Defense industry solution map, scope item catalog, and integration patterns (from Skill 05)
- **H:** CSS Discovery Brief: structured discovery document at 90% completeness (from Skill 01)

---

## Cross-Skill Consistency Verification

| Dimension | Skill 01 (Discovery) | Skill 02 (Module Fit) | Skill 03 (Roadmap) | This Proposal |
|---|---|---|---|---|
| **Employee count** | ~2,500 | 2,500 | 2,500 | 2,500 |
| **Revenue** | ~$1.2B | $1.2B | $1.2B | $1.2B |
| **SAP users** | ~800 | 800 (350 Prof + 400 Ltd + 50 Dev) | 800 | ~800 |
| **Custom objects** | 2,400 ABAP + 47 custom transactions | 2,400 + 47 confirmed | 2,400 + 47 | 2,400 + 47 |
| **Budget** | $15M to $25M allocated | Reasonable but tight | $18M to $23M | $18M to $23M (within $15M to $25M) |
| **Timeline** | 18 to 24 months; December 2028 deadline | 3 waves; 18 to 24 months | Pre-project + 3 waves (22 months) | 22 months; Dec 2028 Wave 2 go-live |
| **Deployment model** | S/4HANA Cloud Private Edition (parent mandate) | S/4HANA Cloud PE via RISE confirmed | RISE confirmed | S/4HANA Cloud PE via SAP RISE |
| **Module count** | 9 current + GTS full + RAR new | 10 modules assessed + BTP | 10 modules + BTP across 3 waves | 10 modules + BTP across 3 waves |
| **Clean Core** | Level D current; Level B target | Level D current; Level B target (18 months post go-live) | 60% custom code retirement target | Level D current; Level B target |
| **Top risk** | Change fatigue (2 failed projects) | Change fatigue + PLM/MES integration | Change fatigue rated CRITICAL | Change fatigue; addressed in dedicated section |
| **Sites** | Redmond WA, Huntsville AL, Cape Canaveral FL | 3 plants confirmed | 3-site deployment | 3 sites |

---

*End of Skill 04 Output*

*Generated by SAP S/4HANA Implementation Scoping Agent, Skill 04: Executive Proposal Drafter*
*Source data completeness: 90% (Skill 01) | Confidence level: HIGH*
