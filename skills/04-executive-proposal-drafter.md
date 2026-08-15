# Skill 04: Executive Proposal Drafter

## Purpose

Synthesize outputs from Skills 01 (Client Discovery Intake), 02 (Module Fit Analyzer), and 03 (Implementation Roadmap Generator) into a polished, client-ready executive proposal document. The output is a scope summary, strategic approach, timeline overview, investment estimate, risk mitigation strategy, and expected business outcomes — all calibrated for a C-level audience rather than technical documentation. This is the deliverable that lands on the CFO's or CEO's desk.

**SAP Ecosystem Positioning:** This skill produces the kind of pre-sales proposal or Statement of Work (SOW) preamble that consulting firms (Accenture, Deloitte, EY, KPMG, West Monroe) create at the end of the Discover/Prepare phase. SAP's own tools do not generate executive-facing proposal narratives. Cloud ALM manages project governance, Signavio visualizes processes, LeanIX maps portfolios, and Joule for Consultants retrieves implementation guidance — but none of them weave those artifacts into a compelling business narrative aimed at a decision-maker who will never open a Fiori launchpad. The human consultant has always been responsible for that synthesis. This skill automates the document production, letting the consultant focus on relationship management, strategic counsel, and the judgment calls that machines cannot make: reading the room, adjusting the pitch, knowing when to push and when to pause.

---

## Inputs

| Input Source | Content Consumed | Key Fields Used |
|---|---|---|
| **Skill 01 — Client Discovery Intake** | Structured discovery brief | `client_profile`, `business_requirements.primary_drivers`, `current_landscape`, `compliance_and_regulatory`, `transformation_context`, `stakeholder_map`, `clarifying_questions` |
| **Skill 02 — Module Fit Analyzer** | Module fit analysis | Module recommendations with fit/gap scoring, Clean Core compliance assessment, integration dependency map, capability coverage matrix, risk flags per module |
| **Skill 03 — Implementation Roadmap Generator** | Implementation roadmap | Phased timeline, resource plan, budget framework, risk register, go-live strategy, change management plan, quality gates |
| **Skill 05 — SAP Best Practices Fetcher** (optional) | Industry-specific SAP best practices | Reference process flows, industry solution maps, benchmark data, SAP GROW/RISE positioning guidance |

**Minimum viable input:** The drafter requires complete outputs from Skills 01 and 02 at minimum. Skill 03 output significantly strengthens Sections 4-5. If Skill 03 is unavailable, the drafter will produce a lighter implementation approach section with appropriate caveats.

---

## Output: Executive Proposal Document

The output is a structured narrative document in Markdown format with clear section headers, designed to be converted to PDF or inserted into a branded proposal template. **PDF conversion is supported via the companion tool `tools/proposal-to-pdf.py`, which applies McKinsey-grade consulting styling including a cover page, table of contents, page numbers, and professional typography. Run `python3 tools/proposal-to-pdf.py <output.md>` to generate the PDF.** Every sentence must earn its place — executives do not read padding.

### Section 1: Executive Summary (1 page)

- Opening hook connecting to the client's stated strategic vision (not SAP's vision)
- Problem statement in business terms — what is broken and what it costs them
- Proposed solution summary: what SAP S/4HANA enables for this specific client
- Three to five key outcomes with expected ROI indicators
- Investment range and timeline headline (one line each)
- Clear call to action with proposed next step

### Section 2: Current State Assessment (1-2 pages)

- Business context and market position
- Current operational challenges drawn directly from Skill 01 discovery brief pain points
- Technology landscape gaps — what they have, what is missing, where the fragmentation hurts
- Risk of inaction: what happens to this business in 12-24 months if they do not transform
- Competitive context: how peers in their industry or region are leveraging enterprise technology (not necessarily SAP-specific — credibility matters more than brand promotion)

### Section 3: Proposed Solution (2-3 pages)

- SAP S/4HANA value proposition specific to their industry vertical
- Module scope summary using business-oriented descriptions, never raw module codes:
  - FI/CO becomes "Financial Management and Controlling"
  - MM becomes "Procurement and Inventory Management"
  - SD becomes "Sales and Distribution"
  - QM becomes "Quality Management"
  - PP becomes "Production Planning and Execution"
  - WM/EWM becomes "Warehouse and Logistics Management"
  - GTS becomes "Global Trade and Export Compliance"
  - PM becomes "Asset and Maintenance Management"
  - PS becomes "Project Management"
  - HCM/SF becomes "Human Capital Management"
- Key capabilities enabled per business area — written as outcomes, not features
- Integration architecture overview simplified for executives (a conceptual diagram description, not a technical architecture)
- Clean Core approach explanation: why adopting standard processes is a strategic advantage, not a limitation
- Cloud deployment benefits framed around the client's priorities (speed, cost, scalability, security — whichever resonates)

### Section 4: Implementation Approach (1-2 pages)

- SAP Activate methodology overview in plain language (no acronyms without definition)
- Phased timeline with key milestones presented in a visual-friendly format (milestone table)
- Go-live strategy: big bang vs. phased, and why the recommended approach fits this client
- Team structure: client and partner roles, with clear accountability descriptions
- Change management approach: how people will be prepared for the transition
- Quality assurance strategy: what safeguards prevent a failed go-live

### Section 5: Investment Framework (1 page)

- Total cost of ownership summary presented as ranges, never as single-point estimates
- Cost categories: licensing/subscription, implementation services, internal resources and backfill, training and enablement, infrastructure and integration, contingency
- ROI narrative: expected operational savings, efficiency gains, risk reduction, and revenue enablement — quantified where data permits, qualified where it does not
- Payback period estimate with stated assumptions
- Comparison to cost of inaction: what the client will spend on workarounds, manual processes, compliance risk, and missed opportunities if they do nothing

### Section 6: Risk Management (0.5-1 page)

- Top five risks translated entirely to business terms (no technical jargon)
- Mitigation strategy for each risk — concrete, not generic
- Governance approach: how risks will be monitored and escalated
- Success factors and prerequisites: what must be true for this project to succeed

### Section 7: Why [Partner Name] / Why Now (0.5-1 page)

- Compelling, specific reasons to move forward — not generic urgency language
- Market, regulatory, or competitive urgency if applicable
- Quick wins available within the first phase
- Clear next steps and decision points with a proposed timeline for the decision

### Appendix References (not generated, but cited for completeness)

- Detailed module scope matrix (from Skill 02)
- Full implementation timeline with Gantt-level detail (from Skill 03)
- Team structure organization chart
- Detailed cost breakdown by phase
- Relevant SAP case studies and reference customers
- SAP best practice process flows (from Skill 05)

---

## Step-by-Step Behavior

### Step 1: Input Synthesis

Consume and cross-reference outputs from Skills 01, 02, and 03. Build an internal context model that captures:

- The client's strategic narrative (why they are doing this, what success looks like)
- The factual foundation (company size, industry, geography, current systems, pain points)
- The technical recommendation (modules, integrations, deployment model, timeline, budget)
- Unresolved gaps and caveats flagged by upstream skills

Validate internal consistency. If Skill 03's budget framework contradicts Skill 01's budget signals (e.g., the roadmap suggests a $1M program but the client indicated a $200K budget), flag this tension and adjust the proposal narrative to address it directly rather than ignoring it.

### Step 2: Audience Calibration

Determine tone, depth, emphasis, and framing based on the stakeholder map from Skill 01:

- **CEO / Managing Director audience:** Lead with vision, growth enablement, competitive positioning. Minimize operational detail. Maximize strategic impact language.
- **CFO / Finance audience:** Lead with ROI, payback period, cost of inaction. Be precise on investment ranges. Show the math behind the business case.
- **CIO / IT leadership audience:** Balance business outcomes with architecture credibility. Include enough technical substance to build trust without overwhelming non-technical co-readers.
- **Investor / Board audience:** Lead with scalability, risk reduction, governance improvement. Frame as infrastructure for the next growth stage.
- **Mixed audience (default):** Balance all perspectives. Lead with business impact, support with financials, ground with implementation credibility.

If the stakeholder map is incomplete, default to a CFO/CEO combined audience — the most common decision-maker pair for ERP investments.

### Step 3: Narrative Framing

Construct the strategic story arc that runs through the entire proposal:

1. **Problem:** The client's current state is unsustainable at their target scale
2. **Vision:** The client has articulated an ambitious future state
3. **Gap:** Specific operational and technological gaps stand between current and future state
4. **Solution:** SAP S/4HANA, configured appropriately, closes those gaps
5. **Proof:** The approach is grounded in methodology, best practices, and realistic planning
6. **Action:** Clear, low-friction next steps reduce the perceived risk of saying "yes"

This arc must feel specific to the client. If a reader could swap in a different company name and the proposal still reads correctly, the narrative framing has failed.

### Step 4: Section Drafting

Generate each section of the proposal using the appropriate business language register:

- **Active voice**, not passive. "This implementation will reduce your month-end close from 12 days to 3 days" — not "A reduction in month-end close cycle time is anticipated."
- **Client-centric framing.** Every capability described in terms of what it does for them, not what SAP does. "You will have real-time visibility into inventory across all locations" — not "SAP S/4HANA provides real-time inventory management capabilities."
- **Confident but honest.** State what will be delivered. Acknowledge what is uncertain. Never overstate certainty to win the deal.
- **Specific quantification where data supports it.** "Based on industry benchmarks for companies your size, clients typically reduce manual reconciliation effort by 60-80%" — not "significant efficiency improvements."
- **No orphaned jargon.** Every technical term that must appear is defined in context on first use.
- **No em-dashes.** Do not use em-dashes (—) anywhere in the output. They are overused in AI-generated text and signal machine authorship to experienced readers. Instead, use colons to introduce explanations, semicolons to join related independent clauses, periods to break long sentences, commas for lighter pauses, or parentheses for asides. For example: "HHE's processes are tightly interconnected. A farmer purchase flows into inventory..." rather than "HHE's processes are tightly interconnected — a farmer purchase flows into inventory..." Similarly, use "to" for ranges ("$98,000 to $190,000") rather than en-dashes or hyphens between numbers.

### Step 5: Quantification

Translate technical findings from Skills 02 and 03 into business metrics:

- Module fit scores become "coverage of your critical business requirements"
- Process automation percentages become "hours saved per month" or "FTEs freed for strategic work"
- System integration counts become "elimination of manual data re-entry between X and Y"
- Data quality improvements become "reduction in month-end adjustments" or "audit findings eliminated"
- Timeline phases become "you will see first results by [date]"

Where hard data is unavailable, use qualified ranges with stated assumptions: "Based on SAP benchmarks for mid-market agricultural exporters, companies typically achieve a 40-60% reduction in export documentation processing time. We will validate this estimate during the Explore phase with your actual process data."

### Step 6: Risk Translation

Convert every technical risk from the Skill 03 risk register into business impact language:

| Technical Risk | Business Translation |
|---|---|
| Data migration quality issues | "Inaccurate opening balances could delay first audited financial close on the new system" |
| Integration complexity with the mobile money provider | "Mobile money payment processing could be disrupted during cutover without careful planning" |
| Scope creep from undefined requirements | "Uncontrolled additions could push the timeline past your investor reporting deadline and exceed the approved budget" |
| Change management resistance | "If field staff do not adopt the new system, you will be running two processes in parallel — doubling cost instead of reducing it" |
| Insufficient testing cycles | "Going live with untested scenarios means discovering problems with real customer orders instead of test data" |

### Step 7: Visual Formatting

Structure the document for executive readability:

- Clear section headers with consistent hierarchy (H1 for title, H2 for sections, H3 for subsections)
- Bullet points for lists of three or more items
- Tables for comparative information (timeline milestones, cost categories, risk/mitigation pairs)
- Bold text for key figures, dates, and decision points
- Callout blocks (blockquotes) for critical insights or warnings
- Timeline milestones in a scannable table format
- No wall-of-text paragraphs exceeding five sentences

### Step 7b: PDF Export Compatibility

When generating the markdown output, ensure it is compatible with the PDF export tool (`tools/proposal-to-pdf.py`):

- **Metadata block:** Include a "Document Metadata" table at the top of the output with fields for "Prepared for", "Company", "Date", "Document Classification", and "Version". The PDF tool extracts these for the cover page.
- **Consistent H2 numbering:** Use `## 1. Executive Summary`, `## 2. Current State Assessment`, etc. The PDF tool generates the table of contents from H2 elements.
- **Table formatting:** Use standard markdown pipe tables. The PDF tool renders these with professional styling (dark blue header rows, alternating row shading) automatically.
- **Blockquote callouts:** Use `>` blockquotes for critical warnings and important notes. The PDF tool renders these as styled callout boxes with blue accent borders.
- **Section dividers:** Use `---` horizontal rules between major sections. The PDF tool renders these as subtle separator lines.
- **No HTML in markdown:** Keep the output as pure markdown. The PDF tool handles all HTML conversion and styling.
- **Internal sections:** The "Cross-Skill Consistency Verification" table and end-of-document boilerplate are automatically stripped from the PDF output — they are for internal quality assurance, not client presentation.

### Step 8: Quality Review

Before finalizing, validate:

- **Internal consistency:** Do the timeline, budget, and scope align? Does the executive summary accurately reflect the detail sections?
- **Tone alignment:** Is the language appropriate for the identified audience? Is it free of jargon that was not defined?
- **Completeness:** Are all seven sections populated? Are there obvious gaps that undermine credibility?
- **Specificity test:** Would this proposal read differently if the client name were changed? (If not, it is too generic.)
- **Promise audit:** Has anything been stated as a certainty that is actually an assumption? Are all ranges presented as ranges?
- **Call to action:** Does the proposal end with a clear, actionable next step?

---

## Constraints and Failure Modes

| Constraint | Handling | Severity |
|---|---|---|
| **Insufficient upstream data** (Skills 01-03 not complete) | Generate what is possible; insert clearly marked placeholder sections with "[REQUIRES INPUT FROM SKILL XX]" flags. Never fabricate data to fill gaps. If Skill 01 is missing, the proposal cannot be generated. | Critical |
| **Over-promising on ROI** | All ROI figures must use conservative estimates presented as ranges. Include "based on SAP industry benchmarks" or "subject to validation during Explore phase" qualifiers. Never state a precise ROI percentage without a source. | High |
| **Technical jargon leaking into executive document** | Every technical term is translated on first use. Module codes never appear without business descriptions. Architecture terminology is replaced with outcome language. Run a final pass specifically for jargon removal. | High |
| **Budget sensitivity** | Some clients do not want investment figures in early-stage documents (especially if the document may circulate beyond the intended audience). If the discovery brief flags budget sensitivity, present the Investment Framework section as a separate appendix or omit specific ranges in favor of "investment framework to be detailed in the next phase." | Medium |
| **Competitive sensitivity** | Never name competitor solutions (Oracle, Dynamics, Odoo, etc.) unless the client explicitly introduced them in the discovery brief. If the client is evaluating alternatives, position SAP on its own merits without negative comparison. | Medium |
| **Cultural and regional considerations** | Proposal tone and formality level vary by market. A proposal for a Tanzanian company with international investors differs from one for a German Mittelstand firm or a US Fortune 500. Adjust formality, directness, and the balance between relationship language and data language. | Medium |
| **Generic proposals** | The most common failure mode. Every section must contain specific references to the client's name, industry, stated pain points, and strategic objectives. Use the specificity test from Step 8. If a section could apply to any client, rewrite it. | High |
| **Scope mismatch between narrative and technical detail** | If the executive summary promises capabilities that the module fit analysis does not support, the proposal loses credibility with technical reviewers who read the appendix. Cross-reference every claim against Skill 02 output. | High |
| **Outdated SAP pricing or licensing references** | SAP licensing models change frequently (GROW with SAP, RISE with SAP, BTP credits). Avoid stating specific licensing costs; frame as "SAP licensing under the [GROW/RISE] model, to be quoted by SAP directly based on confirmed scope." | Medium |

---

## Example Usage

### Context

> **Fictional scenario.** This company and every figure below are invented for benchmarking purposes.

The following example synthesizes the Highland Harvest Exports scenario from Skills 01-03. Highland Harvest Exports (HHE) is an investor-backed raw cashew exporter based in the Njombe area, Southern Highlands of Tanzania, with approximately 65 employees, sourcing from 3,200+ smallholder farmers and exporting to buyers in Europe, North America, and Asia. Their current operations run on Excel spreadsheets, WhatsApp coordination, and a regional mobile money provider — with no ERP system. They plan to scale to 7,000 farmers within two years, and their lead investor is willing to fund enterprise technology if the ROI is clear.

The audience for this proposal is the Founder/Managing Director and the lead investor.

---

### Sample Output: Full Executive Proposal

---

# SAP S/4HANA Implementation Proposal

## Highland Harvest Exports Ltd.

**Prepared for:** The Managing Director and Board of Directors, Highland Harvest Exports Ltd.

**Date:** February 2026

**Document Classification:** Confidential — Client Use Only

**Version:** 1.0 — For Discussion

---

## 1. Executive Summary

Highland Harvest Exports has built something remarkable: a premium raw cashew export operation that connects 3,200 smallholder farmers in the Southern Highlands of Tanzania to discerning buyers across Europe, North America, and Asia. The quality of your cashew kernels, the depth of your farmer relationships, and the reputation you have established in premium markets — including recognition as a model sourcing project by the Tanzania Cashewnut Board — are genuine competitive advantages that most agribusiness companies spend years trying to develop.

Your ambition to scale to 7,000 farmers within two years is both commercially sound and operationally urgent. The premium cashew market rewards consistent quality at volume, and your buyer relationships can absorb significantly more supply — provided you can guarantee the traceability, consistency, and compliance that those buyers demand.

The challenge is straightforward: your current operational infrastructure — Excel spreadsheets, WhatsApp coordination, and manual export documentation — served you well at startup scale, but it will not survive the transition to 7,000 farmers. The cracks are already visible: inventory discrepancies between the farm gate and the export container, manual currency conversions across six currencies creating reconciliation delays, paper-based quality records that cannot satisfy buyer traceability audits, and a month-end close process that consumes your finance team for days. These are not inconveniences — they are scaling risks that will compound as you grow.

We propose implementing SAP S/4HANA Cloud as the operational backbone for Highland Harvest Exports's next growth phase. The solution will deliver:

- **End-to-end traceability** from farmer purchase through drying, shelling, grading, and export — enabling you to tell every buyer the story of every lot
- **Automated multi-currency financial management** across TZS, USD, EUR, CAD, KRW, and INR — eliminating manual FX reconciliation and giving you real-time visibility into profitability by lot, buyer, and market
- **Export compliance automation** — reducing documentation processing time by an estimated 50-70% and virtually eliminating the risk of shipment delays due to paperwork errors
- **Real-time financial reporting** — compressing month-end close from days to hours and providing investor-grade financial visibility at any point in the month
- **Scalable operations** — a platform that supports 7,000 farmers, then more, without requiring a system replacement

**Timeline:** 7-9 months from project kickoff to go-live, with core financial management operational within 4 months.

**Investment:** Total program investment in the range of **$65,000-$190,000** (rough order of magnitude), depending on final scope decisions around SAP S/4HANA Cloud Public Edition versus SAP Business One — both of which are viable for a company of your size and trajectory.

**Recommended next step:** A two-week Explore workshop to validate requirements, confirm the product selection, and refine the investment estimate to within +/- 15% accuracy.

---

## 2. Current State Assessment

### Business Context

Highland Harvest Exports operates in one of the most demanding segments of global agriculture: premium raw cashew export. Your business requires simultaneous excellence in farmer sourcing, drying and shelling operations, quality grading, multi-currency trade finance, and international logistics — all while maintaining the traceability documentation that premium buyers treat as non-negotiable.

You have achieved this with approximately 65 employees and a technology stack that consists primarily of personal productivity tools. That is a testament to the capability of your team. It is also an indication of how much latent capacity is being consumed by manual processes that technology should handle.

### Operational Challenges

The six pain points identified during the discovery phase are interconnected, not isolated:

**Inventory traceability gaps** directly undermine **quality traceability**, which in turn threatens your **buyer relationships**. When a premium buyer in Seoul asks for the lot provenance of the kernels in a sample shipment, the answer should take seconds, not hours. Currently, reconstructing that chain from your spreadsheets requires cross-referencing multiple files, and accuracy depends on whether the collection station staff recorded the data consistently that day.

**Manual multi-currency management** creates **financial reporting delays**. Every farmer payment is in TZS, every export invoice is in USD, EUR, CAD, KRW, or INR, and the FX reconciliation between them is performed manually. This means your actual profitability by lot or by buyer is not known until well after month-end — which means pricing decisions for new contracts are based on estimates rather than data.

**Paper-based export documentation** is both a time cost and a risk. A single error on a phytosanitary certificate or EU food-safety traceability form can hold a container at the port for days. At current volume, this is a nuisance. At 7,000-farmer volume with multiple containers shipping simultaneously, a documentation error becomes a material financial event.

### Technology Landscape

Your current landscape has no integration layer connecting operational data:

| Function | Current Tool | Limitation |
|---|---|---|
| Financial tracking | Excel spreadsheets | No real-time visibility, no multi-currency automation, error-prone manual reconciliation |
| Farmer coordination | WhatsApp groups | No structured data capture, no audit trail, no scalability beyond personal networks |
| Farmer payments | Regional mobile money provider | Not integrated with financial records — payments and accounting are disconnected |
| Quality records | Paper forms | Not searchable, not auditable at scale, no link to inventory lots |
| Export documentation | Manual preparation | Time-intensive, error-prone, no compliance automation |
| Website | Wix | No e-commerce or buyer portal capability |

The fundamental issue is not that any single tool is inadequate — it is that nothing connects to anything else. Every handoff between functions requires a human being to re-enter data, which introduces delay, error, and an inability to see the business as a whole in real time.

### Risk of Inaction

If Highland Harvest Exports scales to 7,000 farmers on the current infrastructure, the following outcomes are predictable:

1. **Inventory discrepancies will multiply.** More than double the farmers means more than double the purchase transactions, more than double the lots to track, more than double the opportunities for data to fall through the cracks. At premium cashew margins, a 3-5% inventory shrinkage due to tracking errors could cost $25,000-$60,000 annually.

2. **Financial close will become untenable.** A month-end process that takes days at 3,200-farmer volume will take weeks at 7,000. Your investor will receive financial reports that are perpetually stale.

3. **Buyer audit failures become likely.** Premium buyers — particularly in the EU — are increasing traceability requirements. General EU food-safety import traceability documentation will require supply chain records that paper-based systems simply cannot produce at scale. (Note: the EU Deforestation Regulation does not currently cover cashew, so compliance here is a food-safety/import-documentation matter, not an EUDR one.)

4. **Your team will burn out.** Manual processes do not scale linearly; they scale exponentially in terms of human effort. The people who are holding everything together on spreadsheets today will not be able to sustain that at more than double the volume.

The cost of inaction is not zero. It is the sum of these risks, plus the opportunity cost of growth you cannot pursue because your operations cannot support it.

---

## 3. Proposed Solution

### Strategic Fit

SAP S/4HANA Cloud provides an integrated operational platform purpose-built for companies managing complex supply chains across multiple currencies and regulatory environments. For agricultural commodity exporters specifically, the platform offers pre-configured processes for batch-managed inventory, multi-currency trade finance, quality management with full traceability, and export compliance documentation.

The critical point for Highland Harvest Exports is this: you are not buying software features. You are buying the ability to scale without proportionally scaling your back-office headcount. Every process that is automated is a process that does not need another hire at 7,000 farmers.

### Module Scope

The proposed solution covers five core business areas, with two supporting capabilities:

**Core Scope:**

| Business Area | What It Enables for Highland Harvest Exports |
|---|---|
| **Financial Management and Controlling** | Real-time multi-currency accounting (TZS, USD, EUR, CAD, KRW, INR). Automated FX conversion at transaction time. Profitability analysis by lot, buyer, region, and season. Month-end close reduced from days to hours. Investor-grade financial reporting available on demand. |
| **Procurement and Inventory Management** | Farmer purchase recording with batch/lot assignment at the point of buying. Full inventory visibility from farm gate through the Njombe collection station, the Mafinga processing facility, grading, and warehouse to export container. Mobile money payment integration for farmer settlements. |
| **Sales and Distribution** | Export sales order management with multi-currency pricing. Automated invoice generation matching buyer contract terms. Shipment scheduling tied to inventory availability. Buyer-specific documentation packages. |
| **Quality Management** | Digital quality records for every lot: moisture content, whole/broken kernel count, defect rate, kernel outturn ratio. Lot-level traceability linking quality data to farmer source, processing batch, and export shipment. Automated quality-based grading and pricing. |
| **Global Trade and Export Compliance** | Export documentation automation: phytosanitary certificates, EU food-safety traceability certificates, weight notes, bills of lading. Compliance checks before shipment release. Document templates aligned with destination country requirements (EU, North America, Asia). |

**Supporting Capabilities:**

| Capability | Role |
|---|---|
| **SAP Business Technology Platform (BTP)** | Integration layer connecting SAP to the regional mobile money provider and potentially to the Tanzania Cashewnut Board reporting system. Mobile application extensions for field data capture at the collection station. |
| **SAP Analytics Cloud** | Management dashboards for the founder and investor: real-time financial position, inventory pipeline, export forecast, and farmer sourcing metrics. |

### Clean Core Approach

We recommend a Clean Core implementation — meaning the solution will use SAP standard processes wherever possible, with extensions built on the Business Technology Platform rather than through modifications to the core system. For Highland Harvest Exports, this is an advantage rather than a constraint:

- You have no legacy system to migrate from and no existing customizations to preserve. This is a greenfield implementation — the cleanest possible starting point.
- Standard SAP processes for financial management, procurement, and sales have been refined over thousands of implementations. They represent proven best practice, not a compromise.
- Where your business requires something SAP does not offer out of the box — such as the mobile money integration or farmer-specific mobile data capture — those extensions will be built on BTP, keeping the core system clean and upgradable.

A Clean Core today means that SAP's quarterly cloud updates apply to your system automatically, and future AI capabilities (SAP Joule, embedded analytics, predictive inventory) will be available to you without a major upgrade project.

### Cloud Deployment

A cloud deployment is the right choice for Highland Harvest Exports for four specific reasons:

1. **No on-premise infrastructure required.** You do not need to procure, house, or maintain servers. SAP manages the infrastructure, security, and backups.
2. **Predictable subscription cost.** Operating expense rather than capital expense — aligning with how investor-backed companies prefer to manage cash flow.
3. **Automatic updates.** You will always run on the latest version without scheduling downtime for upgrade projects.
4. **Access from anywhere.** Your team at the Njombe collection station, your processing facility in Mafinga, and your buyers across three continents access the same real-time data.

---

## 4. Implementation Approach

### Methodology

The implementation will follow SAP Activate — SAP's standard project methodology — organized into four phases. In practical terms, this means we start with focused workshops to confirm your requirements, configure the system to match your processes, test thoroughly with your team, and go live with full support.

### Phased Timeline

We recommend a single go-live for all core modules rather than a phased rollout. Highland Harvest Exports's processes are tightly interconnected — a farmer purchase flows into inventory, through quality grading, into a sales order, through export documentation, and into financial accounting. Implementing these in sequence would require temporary bridge processes that add complexity without lasting value.

| Milestone | Timeline | Key Activities |
|---|---|---|
| **Project Kickoff** | Month 1 | Core team mobilization, project governance setup, infrastructure provisioning |
| **Explore (Requirements Validation)** | Months 1-2 | Business process workshops covering all five core areas. Confirm standard process fit. Document gap requirements. Finalize integration design for mobile money. |
| **Realize (Build and Configure)** | Months 3-5 | System configuration, BTP extension development (mobile money integration, mobile capture), data migration preparation, unit testing |
| **Data Migration Dry Run 1** | Month 4 | First test load of master data (farmer records, material masters, chart of accounts, customer masters) |
| **Integration Testing** | Month 5 | End-to-end process testing: farmer purchase through export shipment through financial close |
| **User Acceptance Testing** | Month 6 | Business users execute real scenarios. Defect resolution. Training delivery. |
| **Data Migration Final** | Month 7 | Production data load. Opening balances. Cutover planning finalized. |
| **Go-Live and Hypercare** | Month 7-8 | System go-live. On-site support for first full business cycle (farmer purchasing period through export shipment). Daily issue resolution. |
| **Stabilization** | Months 8-9 | First month-end close on the new system. Performance optimization. Knowledge transfer to internal team. |

**Total duration: 7-9 months**, depending on client team availability and the complexity of the mobile money integration.

### Team Structure

| Role | Responsibility | Source |
|---|---|---|
| **Project Sponsor** | Strategic direction, funding decisions, obstacle removal | Highland Harvest Exports (Founder/MD) |
| **Project Manager** | Day-to-day project governance, timeline and budget management | Implementation partner |
| **Business Process Leads** (3-4 people) | Requirements validation, testing, user acceptance for their functional area | Highland Harvest Exports (Operations, Finance, Export/Sales, Quality) |
| **SAP Functional Consultants** (2-3 people) | System configuration, process design, testing support | Implementation partner |
| **Technical/Integration Lead** | BTP extensions, mobile money integration, data migration | Implementation partner |
| **Change Management Lead** | Training design, communication, adoption monitoring | Implementation partner (part-time) |
| **IT Coordinator** | Infrastructure liaison, security, user administration | Highland Harvest Exports (may need to hire or designate) |

> **Important:** Highland Harvest Exports will need to allocate 3-4 key staff members at approximately 50% of their time for the duration of the project. This is the single most important success factor. An ERP implementation cannot be delegated entirely to external consultants — your people must own the process decisions and validate that the system works for your actual business.

### Change Management

The transition from Excel and WhatsApp to SAP is significant for a team of 65 people, many of whom may have limited experience with enterprise software. The change management approach will include:

- **Early engagement:** Key users involved from Month 1, not introduced to the system at go-live
- **Role-based training:** Collection station staff, field agents, finance team, and export managers each receive training specific to their daily tasks — not a generic system overview
- **Parallel running:** For the first purchasing cycle after go-live, critical processes will be tracked in both the old method and SAP to build confidence and catch gaps
- **On-site support:** At least one consultant physically present at the Njombe collection station and the Mafinga processing facility during the first full operating cycle post-go-live
- **Connectivity planning:** If internet reliability at the collection station is a concern (common in rural Southern Highlands operations), the solution will include offline-capable mobile data capture that synchronizes when connectivity is available

### Quality Assurance

Three safeguards prevent a failed go-live:

1. **Two data migration dry runs** before the final migration — every error found in a dry run is an error that does not appear in production
2. **Full end-to-end process testing** covering at least 90% of expected transaction scenarios, executed by business users (not consultants)
3. **Go/No-Go decision gate** one week before go-live, with explicit criteria: data migration accuracy above 98%, all critical test scenarios passed, all users trained, and hypercare support confirmed on-site

---

## 5. Investment Framework

### Cost Structure

The total program investment depends on a key product decision that will be confirmed during the Explore phase: whether Highland Harvest Exports implements **SAP S/4HANA Cloud Public Edition** (via SAP GROW with SAP) or **SAP Business One Cloud**. Both are legitimate options for a company of your size and complexity.

| Cost Category | SAP Business One Path | S/4HANA Cloud (GROW) Path | Notes |
|---|---|---|---|
| **SAP Licensing (Annual)** | $10,000-$18,000/year | $28,500-$40,000/year | Based on estimated 15-19 named users. SAP GROW includes starter credits for BTP. |
| **Implementation Services** | $32,000-$62,000 | $42,000-$88,000 | Functional consulting, technical development, project management, change management |
| **Data Migration** | $4,000-$8,000 | $6,000-$12,000 | Master data cleansing, opening balances, historical data conversion |
| **Integration (Mobile Money + BTP)** | $6,000-$12,000 | $6,000-$12,000 | Mobile money integration, potential Tanzania Cashewnut Board reporting interface |
| **Training and Enablement** | $4,000-$8,000 | $6,000-$12,000 | Role-based training materials, train-the-trainer, post-go-live coaching |
| **Contingency (15%)** | $9,000-$16,000 | $9,500-$26,000 | Industry standard contingency for scope or timeline adjustments |
| **Total Program (Year 1)** | **$65,000-$124,000** | **$98,000-$190,000** | Rough order of magnitude; refined to +/-15% during Explore phase |

> **Note:** These figures are rough order of magnitude estimates based on SAP partner benchmarks for mid-market implementations in the agricultural sector. They will be refined to +/-15% accuracy during the Explore workshop once the product selection is confirmed and the detailed scope is finalized. They should not be used for budget approval without that refinement.

### Return on Investment

The ROI case for Highland Harvest Exports is built on four pillars:

**1. Labor efficiency from process automation.** At current volume, your team spends an estimated 60-90 person-hours per month on manual data entry, reconciliation, and document preparation that SAP will automate. At 7,000-farmer volume, that figure would grow to 150-220 hours without automation. Conservatively, SAP eliminates 60-80% of this manual effort, freeing 1-3 FTE equivalents for value-adding work (or avoiding 1-3 hires as you scale).

**2. Inventory shrinkage reduction.** Batch-managed inventory with full traceability closes the gaps where cashew volume is lost or misattributed between farm gate and export. Even a conservative 2-3% improvement in inventory accuracy on $0.9-3.1M of annual cashew purchases represents $18,000-$93,000 in recovered value annually.

**3. Export compliance risk elimination.** A single container held at the port due to documentation errors can cost $2,000-$5,000 in demurrage charges and strained buyer relationships. Automated documentation with built-in compliance checks makes this risk negligible.

**4. Faster financial close enables faster decisions.** Moving from a 10-day month-end close to a 2-day close means management decisions are based on data that is 8 days fresher. For a company making purchasing decisions in a commodity market with daily price movements, this is material.

**Estimated payback period:** 18-30 months from go-live (SAP Business One path) or 24-36 months (S/4HANA Cloud path), assuming revenue growth to the $2-4M range associated with the 7,000-farmer target. These estimates will be validated with actual financial data during the Explore phase.

### Cost of Inaction

Choosing not to invest in enterprise technology is itself a decision with a cost:

- **Hiring cost:** Scaling to 7,000 farmers on manual processes will require 3-5 additional administrative staff ($22,000-$45,000/year in fully loaded cost) to handle the increased volume — staff who would not be needed with automation
- **Opportunity cost:** Buyers with EU food-safety traceability requirements may disqualify suppliers who cannot produce digital chain-of-custody documentation. Losing a single premium buyer contract over traceability gaps costs more than the technology investment.
- **Investor confidence:** Institutional investors and impact funds increasingly require portfolio companies to demonstrate operational governance maturity. Spreadsheet-based operations at $2M+ revenue signal a governance gap.

---

## 6. Risk Management

| # | Risk | Business Impact | Mitigation |
|---|---|---|---|
| 1 | **Change management resistance** — Staff accustomed to Excel and WhatsApp may resist adopting a new system, particularly field-based teams with limited technology exposure | Low adoption means the company runs two parallel systems, doubling effort instead of reducing it. The investment fails to deliver ROI. | Early engagement of key users in system design. Role-specific training (not generic). Identify and empower internal champions at each site. Parallel running period with hands-on support. |
| 2 | **Internet connectivity at rural operations** — The collection station and farmer buying points in the Southern Highlands may have unreliable internet access | Users cannot access the system during critical purchasing and processing activities, reverting to paper processes and creating data gaps | Design for offline-first mobile data capture. Evaluate mobile network coverage at all operating locations during the Explore phase. Identify backup connectivity options (satellite, mobile hotspot). |
| 3 | **Internal IT capacity** — Highland Harvest Exports does not currently have dedicated IT staff to support an enterprise system post-go-live | After the implementation partner disengages, there is no one to manage user issues, system administration, or minor configuration changes | Designate or hire a part-time IT coordinator before go-live. Include admin training in the project scope. Establish a managed services agreement with the implementation partner for Year 1 post-go-live support. |
| 4 | **Budget overrun from scope expansion** — During requirements workshops, the team may identify additional needs that expand the original scope | Project cost exceeds approved budget; timeline extends past target dates; investor confidence erodes | Strict scope governance with a formal change request process. Maintain a "Phase 2 parking lot" for valid requirements that are not critical for initial go-live. Agree on the budget contingency allocation before the project starts. |
| 5 | **Data quality in migration** — Existing spreadsheet data may be inconsistent, incomplete, or formatted in ways that require significant cleansing before migration | Inaccurate opening balances, missing farmer records, or incorrect inventory quantities on Day 1 undermine trust in the new system | Begin data cleansing three months before go-live. Two dry-run migrations to identify and fix issues. Accept that some historical data may not migrate and plan for manual verification of critical records. |

### Governance

A lightweight governance structure appropriate for a project of this scale:

- **Weekly steering committee** (30 minutes): Project Sponsor + Project Manager + Business Process Leads. Review progress, decisions needed, risks.
- **Bi-weekly investor update** (15 minutes): Project Sponsor briefs the lead investor on status, budget consumption, and any escalations.
- **Formal phase gate reviews** at the end of Explore, Realize, and Testing phases — with documented Go/No-Go decisions.

### Success Factors

For this project to succeed, the following must be true:

1. The Founder/Managing Director commits to active sponsorship — not just approval, but visible engagement with the project team
2. Three to four key staff members are available at 50% capacity for the project duration
3. Internet connectivity at the collection station is sufficient (or offline capability is built into the design)
4. The organization accepts that some current processes will change to align with SAP standard best practices — not every current habit will be replicated in the new system
5. Budget contingency (15%) is approved upfront rather than negotiated during the project when it is most needed

---

## 7. Why Now

Highland Harvest Exports is at an inflection point. The decision to scale from 3,200 to 7,000 farmers is not just a volume target — it is a transformation of the business from an entrepreneurial operation held together by individual effort into an institutional operation powered by systems and processes. That transformation requires an operational foundation that does not exist today.

**Three reasons the timing is right:**

**1. You are ahead of the compliance curve.** EU import rules increasingly require exporters to provide digital food-safety traceability documentation for every shipment. Implementing SAP now means you will be compliant before your competitors, positioning Highland Harvest Exports as a preferred supplier for European buyers who are scrambling to meet the same requirements.

**2. Greenfield advantage is perishable.** Today, you have no legacy system, no entrenched customizations, no technical debt. A greenfield SAP implementation is the simplest and most cost-effective type. If you wait and grow further on spreadsheets, you will eventually implement an ERP — but the data migration will be harder, the change management will be more disruptive, and the cost will be higher.

**3. Investor expectations are rising.** Institutional investors in East African agribusiness — whether impact funds, DFIs, or commercial PE — increasingly expect portfolio companies to demonstrate operational maturity through enterprise systems. An SAP implementation signals to current and future investors that Highland Harvest Exports is building infrastructure for long-term institutional value, not just short-term revenue growth.

**Quick wins available in Phase 1:**

- Automated financial reporting for the investor within the first month-end close on the new system (Month 8-9)
- Multi-currency invoicing eliminating manual FX calculations from Day 1 of go-live
- Lot-level traceability providing buyer-facing documentation immediately upon go-live

### Recommended Next Steps

| Step | Timeline | Outcome |
|---|---|---|
| **Decision to proceed** | By end of February 2026 | Executive commitment and budget allocation for the Explore phase |
| **Explore workshop** | March 2026 (2 weeks) | Validated requirements, confirmed product selection (S/4HANA Cloud vs. Business One), refined budget estimate to +/-15% |
| **Partner and SAP contracting** | April 2026 | SAP licensing agreement, implementation partner SOW signed |
| **Project kickoff** | May 2026 | Team mobilized, governance established, system provisioned |
| **Targeted go-live** | September - October 2026 | Core system operational before the start of the next major harvest season |

> We look forward to discussing this proposal with you and your investor. The next step is a two-week Explore workshop that will validate the requirements, confirm the right SAP product for Highland Harvest Exports, and produce a detailed implementation plan with a firm budget. We are prepared to begin that workshop within 30 days of your decision to proceed.

---

**Appendices (available upon request):**

- A: Detailed Module Scope Matrix — fit/gap analysis per business area
- B: Full Implementation Timeline — Gantt-level view with resource assignments
- C: Team Structure — organization chart with named roles
- D: Detailed Cost Breakdown — by phase, by resource, by cost category
- E: SAP Reference Customers — agricultural exporters on SAP S/4HANA Cloud and SAP Business One
- F: SAP Best Practice Process Flows — standard processes for agricultural commodity export

---

*End of Example Output*

---

## Integration Points

| Upstream Skill | Proposal Section(s) Fed | Specific Data Consumed |
|---|---|---|
| **Skill 01 — Client Discovery Intake** | Section 2 (Current State Assessment), Section 1 (Executive Summary), Audience Calibration (Step 2) | `client_profile` for company context; `business_requirements.primary_drivers` for problem framing; `current_landscape` for technology gap analysis; `stakeholder_map` for audience targeting; `transformation_context.budget_signals` for investment sensitivity; `compliance_and_regulatory` for EUDR and trade compliance framing |
| **Skill 02 — Module Fit Analyzer** | Section 3 (Proposed Solution), Section 6 (Risk Management) | Module recommendations and fit/gap scores translated into business capability descriptions; Clean Core assessment informing the "why standard processes" narrative; integration dependency map informing the BTP/mobile-money discussion; risk flags per module feeding the risk register |
| **Skill 03 — Implementation Roadmap Generator** | Section 4 (Implementation Approach), Section 5 (Investment Framework), Section 6 (Risk Management) | Phased timeline converted to milestone table; resource plan converted to team structure table; budget framework converted to investment ranges; risk register converted to business-impact language; go-live strategy and change management approach |
| **Skill 05 — SAP Best Practices Fetcher** | Section 3 (Proposed Solution — industry-specific positioning), Section 7 (Why Now — SAP ecosystem value) | Industry-specific reference architectures; SAP best practice process counts for the client's industry; GROW vs. RISE positioning guidance; SAP reference customer examples |

### Cross-Skill Consistency Checks

The drafter must validate that the following are consistent across all upstream inputs:

- **Module scope in Section 3** matches the modules recommended by Skill 02 (no modules appear in the proposal that were not analyzed)
- **Timeline in Section 4** matches the roadmap from Skill 03 (no milestones are invented or resequenced)
- **Budget in Section 5** aligns with the financial framework from Skill 03 (no figures are changed without flagging the adjustment and rationale)
- **Risks in Section 6** include all Critical and High risks from Skill 03's risk register (none are silently dropped)
- **Client profile details** (employee count, farmer count, currencies, geographies) are consistent with Skill 01's discovery brief (no accidental mutations)

---

## Prompt Engineering Notes

### Key Design Decisions

**1. Why Markdown narrative output rather than JSON.**

Skills 01-03 produce structured data (JSON schemas, scoring matrices, timeline tables) because their consumers are other skills or technical consultants who need programmatic access to the data. Skill 04's consumer is a human executive who will read a document, probably as a PDF. Narrative Markdown is the correct output format because it mirrors what the end reader will actually see. Forcing an executive proposal into JSON and then templating it into a document adds an unnecessary transformation step and strips the narrative quality that makes a proposal persuasive.

**2. Why C-level language translation matters.**

No one sells SAP to a CEO by saying "FI/CO." No CFO has ever approved a budget because a proposal mentioned "batch determination with automatic lot assignment." The language translation from SAP terminology to business outcome language is not cosmetic — it is the difference between a proposal that gets read and one that gets forwarded to IT with a note saying "please evaluate." Module codes are a communication shorthand for SAP consultants. They are a barrier for everyone else. The explicit translation table in Section 3 (FI/CO becomes "Financial Management and Controlling") is not just formatting guidance — it is a design constraint that forces the model to think in terms of business outcomes rather than product features.

**3. The "risk of inaction" section.**

This is arguably the most important section in the proposal for driving a decision. Executives do not buy ERP systems because the features are impressive — they buy them because the alternative is worse. Framing the cost of not acting (inventory shrinkage, compliance risk, hiring costs, investor confidence erosion) makes the investment decision a comparison between two costs rather than a comparison between spending money and spending nothing. This is standard practice in management consulting proposals, and it is absent from every vendor-generated proposal template because vendors are uncomfortable saying "here is what happens if you do nothing" (it implies the customer has a choice). A good consultant says it directly.

**4. Why investment is presented as ranges.**

At the Discover/Prepare phase, estimation accuracy is inherently +/- 30-50%. Presenting a single-point estimate (e.g., "$287,500") communicates false precision that undermines credibility with financially sophisticated audiences. Ranges communicate honesty about the stage of estimation while still providing the decision-maker with enough information to evaluate whether the investment is in the right order of magnitude. The ranges narrow as the project progresses: Explore phase produces +/-15% estimates, and the final SOW produces a firm fixed price or time-and-materials ceiling.

**5. How the proposal adapts tone for different audiences.**

The Step 2 audience calibration is critical. Consider three different clients reading a proposal:

- **Investor-backed East African agribusiness (Highland Harvest Exports):** Tone is direct, practical, growth-oriented. Emphasize scalability, investor reporting, and operational maturity. Acknowledge budget sensitivity. Avoid condescension about the client's current tools — they got this far on spreadsheets, which deserves respect.
- **German Mittelstand manufacturer:** Tone is formal, technically precise, process-oriented. Emphasize engineering excellence, compliance rigor, and Industrie 4.0 alignment. Longer sentences, more detailed technical justification, reference to DIN/ISO standards.
- **US Fortune 500 subsidiary:** Tone is polished, strategy-forward, benchmark-oriented. Emphasize competitive positioning, board-level governance, and integration with existing SAP landscape. Assume the audience has seen SAP proposals before — do not explain SAP from scratch.
- **Government entity:** Tone is formal, compliance-heavy, risk-averse. Emphasize regulatory compliance, data sovereignty, security certifications, and public sector reference customers. Avoid aggressive ROI claims; focus on risk mitigation and mandate compliance.

The model must detect these audience signals from the Skill 01 discovery brief and adjust accordingly.

**6. Why the proposal references SAP's ecosystem (GROW, RISE, BTP) as strategic value rather than just product features.**

SAP's commercial programs (GROW with SAP for mid-market, RISE with SAP for enterprise) and platform capabilities (BTP, AI, Analytics Cloud) are not just products — they are strategic commitments from SAP about where they are investing. For a CEO, "GROW with SAP includes innovation credits that give you access to AI and analytics capabilities as SAP releases them" is more compelling than "BTP provides a cloud-native extension framework." The proposal should position SAP's ecosystem as a long-term partnership, not a one-time software purchase. This is how the best consulting firms sell SAP, and it is how this skill should frame it.

### Iteration History

**v1 (Initial):** The first version of this skill produced a structurally correct proposal that read like a product brochure. It listed SAP features, organized them by module, and attached a generic timeline and budget table. The output was technically accurate but strategically useless — it did not tell the client's story, it told SAP's story. A CFO reading it would learn about SAP S/4HANA but would not understand why their company specifically needed it or what would happen if they said no. The executive summary was a paragraph of marketing language. The risk section was a list of generic project risks. The "Why Now" section was a list of SAP product release dates.

**v2 (Current):** Three fundamental changes made the output usable as an actual client deliverable:

1. **Client-first narrative architecture.** The story arc (Problem, Vision, Gap, Solution, Proof, Action) forces every section to be grounded in the client's reality. The executive summary now opens with the client's strategic vision, not SAP's value proposition. The solution section describes what the client will be able to do, not what SAP's modules contain. This is the difference between "SAP S/4HANA provides real-time multi-currency processing" and "You will see the profitability of every lot in real time, in any currency, without waiting for month-end reconciliation."

2. **Quantification discipline.** v1 used qualitative language ("significant improvement," "enhanced visibility," "streamlined processes"). v2 requires quantified ranges with stated assumptions wherever data supports them. "60-80% reduction in manual reconciliation effort based on SAP benchmarks for mid-market implementations" is credible. "Significant improvement in reconciliation efficiency" is not. When data does not support quantification, v2 says so explicitly rather than hiding behind vague adjectives.

3. **Risk of inaction section.** This was entirely absent in v1. Adding it transformed the proposal from a feature catalog into a decision framework. The realization that drove this change: an executive does not need to be persuaded that SAP is good. They need to be persuaded that doing nothing is worse than the disruption and cost of an implementation. The risk of inaction section provides that framing.

**Planned v3 improvements:**

- Automated competitive positioning when the discovery brief indicates the client is evaluating alternatives (Oracle Cloud, Dynamics 365, Odoo, NetSuite)
- Dynamic appendix generation — actually produce the detailed module scope matrix and timeline rather than referencing them
- Multi-language output support (English, French, German, Spanish) for global consulting firms
- **PDF export tool (implemented)** — `tools/proposal-to-pdf.py` converts Skill 04 markdown output to a McKinsey-grade styled PDF with cover page, table of contents, professional typography, and page numbers. See `tools/README.md` for usage.
- Integration with branded proposal templates (PowerPoint, Word) via document generation APIs
- Feedback loop from Skill 01's clarifying questions — if critical gaps were never filled, the proposal should explicitly caveat the affected sections rather than silently using inferred data
