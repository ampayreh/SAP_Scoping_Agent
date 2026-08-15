# Skill 04 Output: Executive Proposal for Highland Harvest Exports (HHE)

> **Fictional scenario.** This company, its founder, its facilities, its buyers, and every figure below are invented for benchmarking purposes. No resemblance to any real business is intended.

## Document Metadata

| Field | Value |
|---|---|
| **Prepared for** | Amina Cheyo, Founder, and the Lead Investor |
| **Company** | Highland Harvest Exports Ltd. (trading as "Mlima") |
| **Date** | February 2026 |
| **Document Classification** | Confidential: Client Use Only |
| **Version** | 1.0, For Discussion |
| **Source Brief** | DB-20260217-HHE (Skill 01 Discovery Brief, 74% completeness) |
| **Source Module Analysis** | MFA-20260217-HHE (Skill 02 Module Fit Analysis) |
| **Source Roadmap** | IR-20260217-HHE (Skill 03 Implementation Roadmap) |
| **Audience Calibration** | Founder + Lead Investor; growth-oriented, direct, practical tone |

---

## 1. Executive Summary

Highland Harvest Exports has accomplished something that most East African agribusiness startups never achieve. In under six years, Amina Cheyo has built the Mlima cashew brand into a premium raw-nut supplier shipping to specialty importers across Estonia, South Korea, Portugal, Canada, and India. From the Southern Highlands of Tanzania, working with over 3,200 smallholder farmers across four processing stages, HHE has earned recognition from the Tanzania Cashewnut Board as a model sourcing project.

The next chapter requires an operational foundation that does not exist today. Scaling from 3,200 to 7,000 farmers, expanding the Mlima brand with a Dar es Salaam retail line, and meeting rising European traceability expectations all demand integrated systems. Excel spreadsheets cannot track cashew lots across four processing stages. WhatsApp groups cannot reconcile six currencies. Paper-based records cannot satisfy EU food-safety documentation requests at scale.

We propose implementing **SAP S/4HANA Cloud** as the operational backbone for HHE's next growth phase:

- **End-to-end lot traceability** from farmer delivery at Njombe through drying, shelling, and grading to export container, linking every lot to its kernel outturn ratio, origin region, and moisture profile
- **Automated multi-currency financial management** across all six active currencies (TZS, USD, EUR, CAD, KRW, INR), eliminating manual FX reconciliation and delivering real-time profitability by lot, buyer, and market
- **Quality-driven sales execution** with kernel grade, moisture, and defect counts linked directly to batch records, enabling automated grade-based pricing for buyers like Baltic Nut Traders, Meridian Food Import, and Casa do Caju
- **Export documentation readiness** that positions HHE ahead of EU food-safety traceability expectations before competitors, protecting access to your European export markets
- **Investor-grade financial reporting** with real-time P&L, balance sheet, and cash flow available on demand, not after a week-long manual close

**Timeline:** 7.5 months from project kickoff to go-live, aligned with the cashew harvest season and operational before October 2026.

**Investment:** Total program investment in the range of **$98,000 to $190,000**, with annual recurring costs of approximately **$28,500/year**. A dual-path evaluation (SAP S/4HANA Cloud via GROW vs. SAP Business One) will confirm the optimal product fit during the first phase.

**Recommended next step:** A three-week Discover phase to validate scope, confirm product selection, and refine the investment estimate to within +/-15% accuracy.

---

## 2. Current State Assessment

### Business Context

Highland Harvest Exports operates at the intersection of subsistence agriculture and specialty global trade. Amina Cheyo entered the cashew industry in 2018 with a corporate background and a clear vision: to build a vertically integrated raw-cashew operation that pays farmers above-market premiums while delivering traceable, high-grade lots to the world's most demanding buyers.

That vision is working. HHE ships 20 to 35 containers of raw cashew annually to named buyers across five countries. The Mlima brand has earned a reputation for consistent kernel outturn and low defect rates, a mark that places HHE's product in the premium tier of regional production. The Tanzania Cashewnut Board has recognized HHE as a model sourcing project. Farmers who supply HHE receive premium pricing and agricultural extension support, creating a loyalty network that competitors struggle to replicate.

### Operational Challenges

The six pain points identified during discovery are not independent problems. They are symptoms of a single root cause: HHE has outgrown its operational infrastructure.

**Traceability breaks at scale.** HHE processes cashews through four distinct stages: raw intake, drying, shelling at Mafinga, and grading/export preparation. Each stage transforms the product and its value. Today, tracking a specific lot through all four stages requires cross-referencing multiple spreadsheets maintained by different people at two separate facilities. When Meridian Food Import in Seoul asks for the provenance of a specific lot, the answer takes hours to assemble. At 7,000 farmers with proportionally more lots in the pipeline, this becomes untenable.

**Multi-currency management consumes finance capacity.** Every farmer payment flows through the local mobile money provider in TZS. Every export invoice arrives in one of five foreign currencies. The reconciliation between these (manual, spreadsheet-based, after the fact) means that HHE's actual profitability per lot is not known until well after month-end. Contract pricing decisions for new harvest seasons are based on estimates rather than data.

**Quality records exist but are not actionable.** HHE's kernel outturn and grading performance are core competitive assets. But those records live on paper forms, disconnected from inventory lots and financial records. When a buyer requests a Certificate of Quality linked to a specific batch, generating that certificate is a manual assembly process. For a premium exporter where quality documentation is literally what justifies premium pricing, this is a structural vulnerability.

**Export documentation is a bottleneck and a risk.** Phytosanitary certificates, weight notes, bills of lading, EU food-safety traceability forms: each prepared manually for every container. A single error can hold a container at Dar es Salaam port for days, incurring demurrage charges and damaging buyer relationships. At current volume, this is manageable. At double the volume, it becomes a material financial risk.

### Technology Landscape

| Function | Current Tool | Critical Limitation |
|---|---|---|
| Financial tracking | Excel spreadsheets | No real-time visibility; no multi-currency automation; error-prone manual reconciliation |
| Farmer coordination | WhatsApp groups | No structured data; no audit trail; cannot scale beyond personal networks |
| Farmer payments | Regional mobile money provider | Not integrated with financial records; payments and accounting are disconnected |
| Quality records | Paper forms at Njombe and Mafinga | Not searchable, not linked to inventory lots, not auditable at scale |
| Export documentation | Manual preparation | Time-intensive, error-prone, no compliance automation |
| Brand/web presence | mlima-cashew.example (Wix) | Marketing only; no buyer portal or order management |

The fundamental issue is not that any single tool is inadequate for its original purpose. Rather, nothing connects to anything else. Every handoff between functions requires a human being to re-enter data, which introduces delay, error, and an inability to see the business as a whole in real time.

### Risk of Inaction

If HHE scales to 7,000 farmers on the current infrastructure:

1. **Inventory discrepancies will multiply.** 2.2x the farmers means 2.2x the purchase transactions, lots, and processing stages to track. At premium margins, even a 3 to 5% inventory shrinkage from tracking errors could cost $30,000 to $110,000 annually. This is money that is currently invisible because the tracking systems cannot detect it.

2. **EU food-safety compliance becomes a market access risk.** A meaningful share of HHE's confirmed export markets are in the EU. Enhanced import traceability documentation requirements mean paper-based traceability cannot produce sufficient records at scale. Losing access to EU buyers over documentation gaps would be damaging, as these relationships represent a significant share of HHE's revenue.

3. **Investor confidence erodes.** Institutional investors and impact funds increasingly require portfolio companies to demonstrate operational governance maturity. Spreadsheet-based operations at the revenue scale HHE is targeting signal a governance gap that will affect future fundraising and valuation.

4. **The team will burn out.** Manual processes do not scale linearly; they scale exponentially in terms of human effort. The people holding everything together on spreadsheets today cannot sustain that at 2.2x volume. The result is either quality failures, staff turnover, or both.

---

## 3. Proposed Solution

### Strategic Fit

SAP S/4HANA Cloud provides an integrated operational platform designed for companies managing complex supply chains across multiple currencies and regulatory environments. For agricultural commodity exporters specifically, the platform supports batch-managed inventory with full traceability, multi-currency trade finance, quality management with classification schemas, and export compliance documentation.

The critical point for HHE: you are not buying software features. You are buying the ability to scale from 20 containers to 50 containers per year without proportionally scaling your back-office headcount. Every process that is automated is a process that does not need another hire.

### Scope Overview

The proposed solution covers five core business areas with supporting technology:

**Core Scope (Phase 1):**

| Business Area | What It Enables for HHE |
|---|---|
| **Financial Management and Controlling** | Real-time multi-currency accounting across all 6 currencies (TZS, USD, EUR, CAD, KRW, INR). Automated FX conversion at transaction time. Profitability analysis by lot, buyer, region, and season. Month-end close reduced from days to hours. Investor-grade financial reporting available on demand: P&L, balance sheet, cash flow. |
| **Procurement and Inventory Management** | Farmer raw-cashew purchase recording with batch/lot assignment at point of receipt. Batch classification schema capturing: origin region, moisture at intake, kernel grade, outturn ratio, harvest date, defect rate, screen size. Full inventory visibility from Njombe collection station through Mafinga processing to export container. Mobile money payment integration for farmer settlements. |
| **Sales and Distribution** | Export sales order management with multi-currency pricing per buyer contract. Grade-differential pricing (lots with higher outturn ratios command premium pricing automatically). Automated invoice generation matching buyer contract terms. Shipment scheduling tied to inventory availability. Buyer-specific documentation packages for Baltic Nut Traders, Meridian Food Import, Casa do Caju, Northgate Commodities, and Sunrise Ingredients. |
| **Quality Management** | Digital quality records for every lot at every processing stage: incoming raw-cashew inspection, drying assessment, shelling yield, grading evaluation. Kernel grading protocol mapped to SAP inspection plans covering moisture, screen size, and defect counts. Lot-level traceability linking quality data to farmer source, processing batch, and export shipment. Automated Certificate of Quality generation for buyer documentation. |
| **Business Technology Platform (BTP)** | Integration layer connecting SAP to the mobile money provider for automated farmer payments. Offline-capable mobile application for field data capture at Njombe and farmer collection points. Traceability geo-location data capture for farmer plot coordinates (Phase 1 lightweight approach, ahead of full GTS implementation). |

**Phase 2 Candidates (6 to 12 months post go-live):**

| Capability | Rationale for Deferral |
|---|---|
| **Global Trade and Export Compliance (GTS)** | Full export compliance automation for phytosanitary and EU food-safety due diligence. Deferred from Phase 1 due to licensing cost; Phase 1 uses BTP-based traceability data capture as a bridge. |
| **Advanced Mobile Applications** | Farmer relationship management app, field quality inspection app with photo capture, farmer onboarding with GPS. Phase 1 delivers core mobile data capture; Phase 2 expands to full field operations. |
| **Warehouse Management (EWM upgrade)** | Advanced bin management, RF/barcode scanning at Njombe and Mafinga. Phase 1 uses embedded basic warehouse management; Phase 2 upgrades if complexity warrants. |

### Clean Core Approach

We recommend a Clean Core implementation, meaning the solution uses SAP standard processes wherever possible, with extensions built on the Business Technology Platform rather than through modifications to the core system. For HHE, this is an advantage:

- **No legacy to preserve.** HHE has no existing ERP, no existing customizations, no technical debt. This is a greenfield implementation and the cleanest possible starting point.
- **Standard processes represent best practice.** SAP's processes for financial management, procurement with batch management, sales, and quality management have been refined over thousands of implementations. Adopting them is not a compromise; it is an acceleration.
- **Where HHE's business is genuinely unique** (mobile money integration, farmer-specific mobile data capture, Tanzania export documentation templates), those extensions are built on BTP, keeping the core system clean and automatically upgradable.
- **Future-proofing.** A Clean Core means SAP's quarterly cloud updates apply automatically, and future AI capabilities (SAP Joule, embedded analytics, predictive inventory) will be available without a major upgrade project.

### Cloud Deployment

Cloud deployment is the right choice for HHE for four specific reasons:

1. **No on-premise infrastructure required.** HHE does not need to procure, house, or maintain servers at Njombe or Mafinga. SAP manages the infrastructure, security, backups, and disaster recovery.
2. **Predictable subscription cost.** Operating expense rather than capital expense, aligning with how investor-backed companies prefer to manage cash flow.
3. **Automatic updates.** HHE will always run on the latest version without scheduling downtime for upgrade projects.
4. **Access from anywhere.** The team at Njombe, the Mafinga processing facility, and buyers in Tallinn, Seoul, and Lisbon all access the same real-time data through a web browser.

---

## 4. Implementation Approach

### Methodology

The implementation follows **SAP Activate**, SAP's standard project methodology for cloud implementations. In practical terms: we start with focused workshops to confirm requirements (Discover/Explore), configure the system to match HHE's processes (Realize), test thoroughly with your team (Realize/Deploy), and go live with dedicated support (Deploy/Run).

### Phased Timeline

We recommend a **single go-live** for all core modules rather than a phased rollout. HHE's processes are tightly interconnected. A farmer purchase flows into inventory with batch assignment, through quality inspection at each processing stage, into a sales order with grade-based pricing, through export documentation, and into multi-currency financial accounting. Implementing these in sequence would require temporary bridge processes that add cost without lasting value.

| Milestone | Week | Month | Key Activities |
|---|---|---|---|
| **Project Kickoff** | 0 | May 2026 | Core team mobilization, governance setup, SAP GROW subscription |
| **Discover Complete** | 3 | May 2026 | Scope validated, infrastructure assessed, SAP GROW confirmed |
| **System Provisioned** | 5 | Jun 2026 | S/4HANA Cloud DEV/QAS/PRD landscapes operational |
| **Prepare Complete** | 8 | Jul 2026 | Org structure designed, master data strategy set, ERP fundamentals training done |
| **Fit-to-Standard Workshops** | 8 to 14 | Jul to Aug 2026 | Business process workshops for all five core areas |
| **Explore Complete** | 16 | Sep 2026 | All designs approved, gap resolution planned, integration architecture finalized |
| **Configuration Complete** | 22 | Oct 2026 | System configured, BTP extensions built, master data loaded |
| **UAT Complete** | 26 | Oct 2026 | Business users have validated all critical scenarios |
| **End-User Training** | 27 to 28 | Oct 2026 | Role-based training with laminated reference cards |
| **Go-Live** | 30 | Oct 2026 | Production system live, aligned with harvest season start |
| **First Month-End Close** | 34 | Nov 2026 | First full financial close on the new system |
| **Hypercare Complete** | 38 | Jan 2027 | Stabilized, knowledge transferred, Phase 2 planning initiated |

**Total duration: 7.5 months** (30 weeks to go-live, 38 weeks including hypercare). Go-live is targeted for October 2026 to be operational before the main harvest purchasing season begins.

### Team Structure

| Role | Responsibility | Source | Allocation |
|---|---|---|---|
| **Executive Sponsor** | Strategic direction, funding decisions, obstacle removal | Amina Cheyo (Founder) | 10% through project |
| **Project Champion** | Internal coordination, decision facilitation, staff engagement | HHE Operations Lead | 25 to 50% |
| **Business Process Leads** (3 to 4) | Requirements validation, testing, acceptance for their area | HHE (Finance, Operations, Export, Quality) | 25 to 50% during workshops, UAT |
| **Project Manager** | Day-to-day governance, timeline/budget management | Implementation Partner | 50 to 100% |
| **Solution Architect** | Technical design authority, integration oversight | Implementation Partner | 25 to 50% |
| **Functional Consultants** (2 to 3) | System configuration, Fit-to-Standard facilitation, testing | Implementation Partner | 50 to 100% during Explore/Realize |
| **Technical/Integration Lead** | BTP extensions, mobile money integration, data migration | Implementation Partner | 25 to 50% |
| **Change Management Lead** | Training design, communication, adoption monitoring | Implementation Partner | 25% (part-time) |

> **Critical success factor:** HHE must allocate 3 to 4 key staff members at approximately 50% of their time during the Explore and Realize phases (July to October 2026). An ERP implementation cannot be delegated entirely to external consultants. Your people must own the process decisions and validate that the system works for your actual business operations at Njombe and Mafinga.

### Change Management

The transition from Excel and WhatsApp to SAP is the single most important challenge in this implementation. HHE's team, particularly the 28 permanent staff at Njombe and 50 to 70 seasonal workers at Mafinga, may have limited experience with enterprise software. The change management approach is designed for this reality:

- **ERP fundamentals training in the Prepare phase.** Before anyone sees the system, the team understands what an ERP does and why it matters for HHE's growth.
- **Role-based training.** Collection station staff learn only the transactions they need (raw-cashew receipt, quality recording, batch creation); finance team learns multi-currency posting and reporting; export managers learn sales order and documentation workflows.
- **Laminated quick reference cards.** Printed, durable, designed for a working environment. English primary text with key terms in Swahili for field staff.
- **3 to 5 internal super users** identified early and trained intensively. They become the first line of support for their colleagues after go-live.
- **Communication through existing channels.** Project updates via WhatsApp groups (the channel staff already use) plus physical notice boards at Njombe and Mafinga.
- **On-site support during go-live.** At least one consultant physically present at each facility during the first full purchasing and processing cycle.

### Quality Assurance

Three safeguards prevent a failed go-live:

1. **Two data migration dry runs** before the final production load. Every error found in a dry run is an error that does not appear on Day 1.
2. **Full end-to-end process testing.** A complete cycle from farmer raw-cashew purchase through quality inspection, processing, export sale, and financial close, executed by HHE's own staff, not consultants.
3. **Formal Go/No-Go decision** one week before go-live, with explicit criteria: data migration accuracy above 98%, all critical test scenarios passed, all users trained, hypercare support confirmed on-site.

---

## 5. Investment Framework

### Cost Structure

The total program investment depends on a product decision that will be confirmed during the Discover phase: whether HHE implements **SAP S/4HANA Cloud Public Edition** (via SAP GROW) or **SAP Business One Cloud**.

The recommended path is S/4HANA Cloud via GROW. The depth of Quality Management and batch traceability that HHE's premium cashew business demands is significantly stronger in S/4HANA than in Business One. However, if the budget analysis shows S/4HANA exceeds investor appetite, Business One is a credible alternative that should be evaluated.

| Cost Category | Estimated Range | Notes |
|---|---|---|
| **SAP Licensing (Annual)** | $16,000 to $31,000/year | SAP GROW starter pack, 19 named users (8 Professional + 10 Limited Professional + 1 Developer) |
| **Implementation Partner** | $52,000 to $92,000 | Regional partner with East Africa experience; blended rate $100 to $150/hour; mix of onsite and remote delivery |
| **Client Internal Resources** | $10,000 to $20,000 | Loaded cost of staff time allocated to project (process owners, champion, training) |
| **Infrastructure & Connectivity** | $3,000 to $8,000 | Internet connectivity upgrade at Njombe if needed; 5 to 8 additional devices (laptops/tablets); backup power |
| **Data Migration** | $2,000 to $5,000 | Farmer master data cleansing from Excel (~3,200 records); opening balances; material/customer masters |
| **Training & Enablement** | $2,000 to $5,000 | Reference card production; SAP Learning Hub licenses; training facility setup |
| **Contingency (15 to 20%)** | $13,000 to $29,000 | Covers scope additions, extended timelines, additional training needs |
| **Total Program (Year 1)** | **$98,000 to $190,000** | Rough order of magnitude, refined to +/-15% during Discover/Explore |

**Annual Recurring Costs:**

| Category | Estimated Annual Cost |
|---|---|
| SAP Licensing | $19,000 |
| Managed Support Services | $6,500 |
| Cloud Infrastructure | $3,000 |
| **Total Annual Recurring** | **$28,500/year** |

> **Note:** These figures are rough order-of-magnitude estimates based on SAP partner benchmarks for mid-market implementations in East Africa. They will be refined to +/-15% accuracy during the Discover phase once the product selection is confirmed. They should not be used for final budget approval without that refinement.

### Return on Investment

The ROI case for HHE is built on four pillars:

**1. Inventory traceability recovers lost value.** Batch-managed inventory with full traceability closes the gaps where cashew volume is lost or misattributed between Njombe and the export container. Even a conservative 3 to 5% improvement in inventory accuracy on $900K to $3.1M of annual cashew purchases represents **$27,000 to $155,000 in recovered value annually**, value that is currently invisible.

**2. Multi-currency automation eliminates reconciliation cost and FX losses.** Manual currency conversion across six currencies creates reconciliation delays and FX exposure. Automating this eliminates an estimated 1 to 2% in transaction-level FX losses and frees the finance team from days of manual reconciliation each month. Estimated annual value: **$10,000 to $40,000**.

**3. Export documentation automation reduces risk and accelerates shipments.** Automated documentation with built-in compliance checks reduces preparation time by an estimated 60 to 70% and virtually eliminates the risk of containers held at port due to paperwork errors. A single delayed container costs $2,000 to $5,000 in demurrage; avoiding 2 to 3 such incidents per year saves **$4,000 to $15,000** plus the relationship value with buyers.

**4. Scalable operations avoid proportional headcount growth.** At 7,000 farmers, HHE would need 4 to 6 additional administrative staff ($30,000 to $60,000/year) to handle the increased volume on manual processes. SAP eliminates most of that need. The system scales without proportional staffing.

**Combined estimated annual benefit: $71,000 to $250,000**, implying a **payback period of approximately 12 to 24 months** from go-live on the lower investment path, or 18 to 30 months on the higher path. These estimates will be validated with HHE's actual financial data during the Explore phase.

### Cost of Inaction

Choosing not to invest in enterprise technology has its own cost:

- **Hiring cost:** 4 to 6 additional admin staff at 7,000-farmer scale = $30,000 to $60,000/year in recurring headcount that would not be needed with automation
- **EU food-safety compliance risk:** European buyers will increasingly require digital traceability documentation. Inability to provide it risks disqualification from markets that represent a meaningful share of HHE's revenue.
- **Investor confidence:** Spreadsheet-based operations at $2M+ revenue signal a governance gap that affects valuation and future fundraising
- **Quality premium erosion:** Without digital quality traceability, HHE cannot systematically prove the lot-level provenance and grading data that justify premium pricing. Buyers may default HHE to commodity pricing tiers.

---

## 6. Risk Management

| # | Risk | Business Impact | Our Mitigation |
|---|---|---|---|
| 1 | **Staff resistance to new ways of working.** Field teams at Njombe and seasonal workers at Mafinga are accustomed to Excel and WhatsApp. | Low adoption means running two parallel systems, doubling effort instead of reducing it. The investment fails to deliver ROI. | Early engagement of key staff in system design. Role-specific training with laminated reference cards. Identify 3 to 5 internal champions. On-site support during first full harvest cycle. |
| 2 | **Internet connectivity at rural operations.** Njombe collection station operates in a rural area with potentially unreliable connectivity. | Staff cannot access the system during critical raw-cashew purchasing and quality inspection, creating data gaps. | Design for offline-first mobile data capture at Njombe. Evaluate mobile network coverage during Discover. Budget for connectivity upgrade or backup solutions. |
| 3 | **No internal IT support.** HHE does not currently have dedicated IT staff. | After the implementation partner disengages, there is no one to manage user issues, system administration, or minor configuration changes. | Designate or hire a part-time IT coordinator before go-live. Include admin training in project scope. Establish a Year 1 managed services agreement with the partner. |
| 4 | **Budget pressure from scope expansion.** During workshops, the team may identify additional requirements that expand scope. | Project cost exceeds approved budget; timeline extends; investor confidence erodes. | Strict scope governance with formal change request process. "Phase 2 parking lot" for valid but non-critical requirements. Budget contingency agreed upfront. |
| 5 | **Mobile money integration complexity.** Payment integration is custom development dependent on a third-party platform. | Farmer payment processing disrupted during transition; provider API changes outside HHE's control. | Engage the provider's technical team early. Build robust error handling. Implement manual payment fallback for system outages. Proof-of-concept in Explore phase. |

### Governance

A governance structure calibrated for a project of this scale:

- **Weekly check-in** (30 minutes): Amina Cheyo + Project Manager + Business Process Leads. Covers progress review, decisions needed, and blockers.
- **Bi-weekly investor update** (15 minutes): Amina briefs the lead investor on status, budget consumption, and any escalations.
- **Phase gate reviews** at the end of Discover, Explore, Realize, and pre-Go-Live, with documented Go/No-Go decisions requiring Amina's signature.

### Success Factors

For this project to succeed, the following must be true:

1. **Amina Cheyo commits to active sponsorship.** Not just approval, but visible engagement with the project team and clear communication to staff that this is a priority.
2. **Three to four key staff members are available at 50% capacity** during the Explore and Realize phases (July to October 2026).
3. **Internet connectivity at Njombe** is sufficient for cloud access, or offline capability is built into the design.
4. **The organization accepts process change.** Some current habits will evolve to align with SAP standard best practices. This is a feature, not a limitation.
5. **Budget contingency (15 to 20%)** is approved upfront and managed through a formal change process.

---

## 7. Why Now

Highland Harvest Exports is at an inflection point. The plan to scale from 3,200 to 7,000 farmers is not just a volume target. It is a transformation from an entrepreneurial operation held together by Amina Cheyo's personal drive and a dedicated team's manual effort into an institutional operation powered by systems, processes, and data. That transformation requires an operational foundation that does not exist today.

**Three reasons the timing is right:**

### 1. Export-traceability expectations create a competitive advantage window

European buyers increasingly expect digital traceability documentation, including geo-located production data, for the products they import. A meaningful share of HHE's confirmed export buyers are in the EU. Implementing SAP with traceability-capable data capture now positions HHE as a preferred supplier for European buyers who are working to strengthen their own supply-chain documentation. Being ahead of documentation expectations is not just risk mitigation; it is a sales advantage.

### 2. Greenfield advantage is perishable

Today, HHE has no legacy ERP, no entrenched customizations, no technical debt. A greenfield SAP implementation is the simplest and most cost-effective type. If HHE waits and grows further on spreadsheets, the eventual ERP implementation will be harder: more data to migrate, more established habits to change, more manual workarounds that people will resist giving up. The cost of implementing at 7,000 farmers will be materially higher than implementing at 3,200.

### 3. Investor expectations demand operational maturity

Institutional investors in East African agribusiness, whether impact funds, DFIs, or commercial PE, increasingly require portfolio companies to demonstrate operational governance maturity through enterprise systems. An SAP implementation signals to the current lead investor and to future investors that HHE is building infrastructure for long-term institutional value, not just short-term revenue growth. It also provides the financial reporting transparency that investor oversight requires.

### Quick Wins Available in Phase 1

- **Automated multi-currency invoicing** that eliminates manual FX calculations from Day 1 of go-live
- **Real-time financial reporting** for the investor within the first month-end close on the new system (November 2026)
- **Lot-level traceability** with buyer-facing quality documentation generated directly from SAP immediately upon go-live
- **Farmer payment reconciliation** with mobile money payments automatically matched to vendor records in SAP, ending manual reconciliation

### Recommended Next Steps

| Step | Timeline | Outcome |
|---|---|---|
| **Decision to proceed** | March 2026 | Executive commitment and budget allocation for the Discover phase |
| **Discover phase** | April 2026 (3 weeks) | Validated scope, confirmed product selection (S/4HANA GROW vs. Business One), refined budget to +/-15% |
| **Partner and SAP contracting** | April to May 2026 | SAP GROW subscription agreement, implementation partner SOW signed |
| **Project kickoff** | May 2026 | Team mobilized, governance established, system provisioning initiated |
| **Go-live** | October 2026 | Core system operational before the main harvest purchasing season |
| **Hypercare complete** | January 2027 | Stabilized, knowledge transferred, Phase 2 planning initiated |

> We look forward to discussing this proposal with Amina and the investment team. The next step is a three-week Discover phase that will validate the requirements, confirm the right SAP product for HHE, and produce a refined implementation plan with a firm budget. We are prepared to begin that phase within 30 days of the decision to proceed.

---

## Appendices (Available Upon Request)

- **A:** Detailed Module Scope Matrix: fit/gap analysis per business area with SAP scope item references (from Skill 02)
- **B:** Full Implementation Timeline: week-by-week view with resource assignments and critical path (from Skill 03)
- **C:** Team Structure: organization chart with named roles and allocation percentages
- **D:** Detailed Cost Breakdown: by phase, by resource category, with assumptions stated
- **E:** SAP Reference Information: scope items for agricultural commodity export, traceability compliance architecture, kernel-grading-to-QM mapping (from Skill 05)
- **F:** Risk Register: complete 12-risk register with probability, impact, mitigation, and contingency for each (from Skill 03)
- **G:** HHE Discovery Brief: structured JSON discovery document at 74% completeness (from Skill 01)

---

## Cross-Skill Consistency Verification

| Dimension | Skill 01 (Discovery) | Skill 02 (Module Fit) | Skill 03 (Roadmap) | This Proposal |
|---|---|---|---|---|
| **Module scope** | FI, CO, MM, SD, QM (high); WM, GTS, BTP (medium) | FI, CO, MM, SD, QM (Phase 1); BTP (Phase 1); WM, GTS (Phase 2) | FI/CO, MM, SD, QM + BTP (Wave 1) | FI/CO, MM, SD, QM + BTP (Phase 1); GTS, WM (Phase 2) |
| **User count** | 65 employees, ~19 system users estimated | 19 users (8 Prof + 10 Ltd + 1 Dev) | 19 users | 19 named users |
| **Timeline** | Recommended before October harvest | 7.5 months (30 wk go-live) | 30 weeks go-live, 38 weeks total | 7.5 months, go-live October 2026 |
| **Budget** | Tight, investor-funded | SAP GROW recommended (lowest TCO) | $98K to $190K total; $28.5K/yr recurring | $98K to $190K total; $28.5K/yr recurring |
| **Deployment** | Cloud preferred (greenfield, budget-conscious) | S/4HANA Cloud Public Edition via GROW | GROW confirmed | S/4HANA Cloud via GROW (recommended) |
| **Top risk** | Change management (Excel to ERP) | Change management + farmer procurement | Change management rated CRITICAL | Staff resistance to new ways of working |
| **Currencies** | 6 (TZS, USD, EUR, CAD, KRW, INR) | 6 currencies confirmed | Multi-currency 1.1x multiplier applied | 6 currencies referenced |

---

*End of Skill 04 Output*

*Generated by SAP S/4HANA Implementation Scoping Agent, Skill 04: Executive Proposal Drafter*
*Source data completeness: 74% (Skill 01) | Confidence level: MEDIUM-HIGH*
