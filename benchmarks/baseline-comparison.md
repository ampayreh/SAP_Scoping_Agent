# Baseline Comparison: Single-Prompt LLM Outputs

## Methodology

To evaluate whether the multi-skill agentic approach produces meaningfully better scoping deliverables than a straightforward LLM interaction, we ran each scenario through a single-prompt baseline. The baseline uses the prompt template defined in `benchmark-methodology.md`:

```
You are an experienced SAP S/4HANA implementation consultant and enterprise architect.
A potential client has provided the following information about their company and needs.
Please provide a comprehensive implementation scoping analysis including:
1. A structured assessment of the client's current state and requirements
2. A module fit analysis mapping their needs to SAP S/4HANA modules
3. A phased implementation roadmap with timeline and resource estimates
4. An executive-level proposal summary suitable for C-level stakeholders

Client information:
[SCENARIO BRIEF]
```

The baseline was run using Claude (same model as the skills pack) with the scenario brief inserted verbatim. No additional system prompts, skill specifications, or structured output schemas were provided. The response below represents a typical single-prompt output.

---

## Scenario A Baseline: Highland Harvest Exports (HHE)

> **Fictional scenario.** This company and every figure below are invented for benchmarking purposes.

### Prompt Used

The baseline prompt above with the HHE client brief from `scenario-a-agribusiness/input.md`.

### LLM Response

#### 1. Current State Assessment

Highland Harvest Exports (HHE) is a raw cashew export company based in the Southern Highlands of Tanzania with approximately 65 employees. The company purchases raw cashew nuts from over 3,200 smallholder farmers across the region, processes them at its facilities, and exports to buyers in Europe, North America, and Asia.

**Current Systems:**
- Excel spreadsheets for all operations
- WhatsApp groups for communication
- Regional mobile money provider for farmer collections
- Wix website

**Key Pain Points:**
- Cannot track inventory from farm gate to export container
- Multi-currency management is difficult (TZS, USD, EUR, and other buyer currencies)
- Export documentation is time-consuming
- No real financial reporting
- Kernel-grade traceability done on paper
- Systems cannot handle planned scale to 7,000 farmers

#### 2. Module Fit Analysis

Based on HHE's requirements, the following SAP S/4HANA modules are recommended:

- **FI (Financial Accounting):** Essential for multi-currency management, financial reporting, and month-end close automation. HHE handles multiple currencies including TZS, USD, EUR, CAD, KRW, and INR.
- **CO (Controlling):** Needed for profitability analysis and cost tracking across operations.
- **MM (Materials Management):** Required for procurement from farmers and inventory management. Batch management can help with traceability requirements.
- **SD (Sales & Distribution):** Necessary for managing export sales orders and customer contracts with international buyers.
- **QM (Quality Management):** Useful for tracking cashew kernel grades throughout the processing chain.
- **WM (Warehouse Management):** Can help manage inventory at the collection station and processing facility.

**Additional considerations:**
- GTS (Global Trade Services) could help with export documentation but may be complex for a company this size
- BTP integration may be needed for mobile money connection

#### 3. Implementation Roadmap

**Phase 1 (Months 1 to 3): Core Finance and Procurement**
- Implement FI/CO for financial management
- Set up MM for farmer procurement
- Configure multi-currency handling
- Basic master data setup

**Phase 2 (Months 4 to 6): Sales and Quality**
- Implement SD for export sales management
- Configure QM for quality tracking
- Set up batch management for traceability
- Export documentation setup

**Phase 3 (Months 7 to 9): Optimization**
- Warehouse management configuration
- Reporting and analytics
- Mobile money integration
- User training and go-live

**Resource Estimate:**
- 1 Project Manager
- 2 to 3 SAP functional consultants
- 1 Technical/integration consultant
- Total budget estimate: $210,000 to $520,000

#### 4. Executive Summary

HHE is experiencing growth pains that are common among mid-market agribusinesses scaling beyond their initial systems. The transition from Excel and WhatsApp to an integrated ERP system will address the core challenges of traceability, financial management, and scalability.

SAP S/4HANA Cloud offers a comprehensive solution that can grow with HHE. The key benefits include:
- End-to-end inventory traceability
- Automated multi-currency financial management
- Streamlined export documentation
- Quality management integrated with inventory
- Scalable platform for growth to 7,000 farmers

The estimated investment of $210,000 to $520,000 should be evaluated against the operational efficiencies gained and the risk reduction in export compliance and inventory management. The ROI should be achievable within 2 to 3 years given the planned growth trajectory.

We recommend beginning with a discovery workshop to confirm scope and refine the implementation timeline and budget estimate.

---

## Scenario B Baseline: Constellation Satellite Systems (CSS)

### Prompt Used

The baseline prompt above with the CSS client brief from `scenario-b-high-tech/input.md`.

### LLM Response

#### 1. Current State Assessment

Constellation Satellite Systems (CSS) is a satellite manufacturing and launch services company with approximately 2,500 employees and $1.2B annual revenue. The company operates across three sites: Redmond, WA (headquarters and manufacturing), Huntsville, AL (manufacturing), and Cape Canaveral, FL (launch operations).

**Current SAP Landscape:**
- SAP ECC 6.0 EHP8 on-premise, installed 2015, heavily customized
- 800 active SAP users
- Modules: FI/CO, MM, SD, PP, QM, PM, PS
- 2,400 custom ABAP objects and 47 custom transactions
- Multiple integrations: Teamcenter PLM, Apriso MES, Salesforce CRM, Workday HCM, Anaplan, plus 12 custom middleware interfaces
- SAP Basis team of 4 FTEs
- ECC mainstream maintenance ends 2027 (extended to 2030)

**Key Pain Points:**
- Heavily customized system is difficult to maintain
- BOM management issues between engineering and manufacturing
- ITAR compliance managed through partial GTS and manual processes
- No real-time manufacturing visibility (4-hour MES lag)
- Financial close takes 12 business days
- Poor supply chain visibility for long-lead components
- IFRS 15/ASC 606 revenue recognition not properly configured

#### 2. Module Fit Analysis

CSS already uses most core SAP modules. The migration to S/4HANA should focus on enhancing existing capabilities:

- **FI/CO:** Upgrade to S/4HANA Universal Journal for faster close. Implement IFRS 15 revenue recognition. Program-level profitability analysis.
- **MM:** Enhanced procurement for long-lead electronics. Better supplier collaboration capabilities.
- **SD:** Milestone billing for satellite programs. Integration with Salesforce CRM.
- **PP:** S/4HANA's enhanced BOM management. Better PLM integration with Teamcenter. Production planning for scale-up to 15 satellites/month.
- **QM:** Enhanced quality management for space-grade components. Non-conformance management improvements.
- **PM:** Calibration and clean room equipment maintenance.
- **PS:** Enhanced project system with better earned value management capabilities in S/4HANA.
- **GTS:** Full ITAR/EAR compliance implementation. License management and deemed export controls.

#### 3. Implementation Roadmap

**Phase 1 (Months 1 to 8): Core Finance and Compliance**
- System conversion preparation and custom code analysis
- FI/CO migration with IFRS 15 configuration
- GTS full implementation for ITAR compliance
- Basic MM/SD migration

**Phase 2 (Months 9 to 16): Manufacturing and Operations**
- PP migration with enhanced BOM management
- QM and PM migration
- PLM integration redesign (Teamcenter)
- MES integration redesign (Apriso)

**Phase 3 (Months 17 to 22): Optimization and Integration**
- PS enhancement with earned value management
- Analytics and reporting
- Remaining integration cleanup
- Custom code retirement

**Resource Estimate:**
- 15 to 20 implementation partner FTEs
- CSS internal team of 10 to 15 dedicated resources
- Total budget: $15,000,000 to $20,000,000

#### 4. Executive Summary

CSS faces a mandatory migration from SAP ECC to S/4HANA before maintenance ends. This is both a risk mitigation exercise and an opportunity to modernize operations for the planned production scale-up.

Key benefits of the migration:
- Reduced financial close from 12 to 5 business days
- Real-time manufacturing visibility
- Improved BOM management across the product lifecycle
- Full ITAR/EAR compliance through GTS
- Proper revenue recognition for satellite program contracts
- Reduced custom code footprint (targeting 60% reduction)

The transformation will require 18 to 22 months and an investment of $15M to $20M, which aligns with the allocated budget of $15M to $25M. Given the two recent failed IT projects, strong program governance and change management will be essential for success.

We recommend beginning with a 6-week Prepare phase to conduct custom code analysis, define the conversion approach, and establish program governance.

---

## Comparison Analysis

### What the Baseline Gets Right

Both baseline outputs demonstrate reasonable SAP knowledge and provide a serviceable high-level scoping summary. The baseline correctly identifies:
- Core modules needed for each scenario
- Approximate budget ranges
- Major pain points and their SAP solutions
- General implementation timeline structure

### What the Baseline Misses

| Dimension | Skills Pack | Baseline | Gap |
|---|---|---|---|
| **Output structure** | Defined JSON schemas with typed fields, enabling downstream consumption | Prose with bullet lists, no machine-readable format | Skills pack output can be programmatically consumed by subsequent skills |
| **Completeness scoring** | Quantitative (74% for HHE, 90% for CSS) with severity-tagged gaps | No gap detection or completeness assessment | Skills pack explicitly identifies what information is missing and how critical each gap is |
| **Inference tagging** | Every inference explicitly tagged with [INFERRED] and reasoning | Inferences made silently without transparency | Skills pack creates an auditable trail of assumptions |
| **SAP terminology** | Uses exact scope item IDs (1A2, 1NM, 2QN), SAP process names, SAP Activate phases | Generic module descriptions without SAP reference specificity | Skills pack outputs are directly usable in SAP implementation methodology |
| **Clean Core assessment** | Explicit maturity level (A through D), remediation plan, target state | Not mentioned | Critical for S/4HANA migrations; skills pack addresses SAP's current strategic direction |
| **SAP toolchain references** | Specific recommendations for Signavio, LeanIX, Cloud ALM, J4C | Not mentioned | Skills pack positions outputs within the SAP ecosystem |
| **Fit scoring** | Per-module 1 to 5 fit scoring with gap-level detail | Descriptive only, no quantitative assessment | Skills pack enables prioritization and objective comparison |
| **Integration map** | Explicit mandatory vs. optional integration dependencies | Brief mentions of integrations | Skills pack identifies the integration architecture implications |
| **HHE product sizing** | Business One vs. S/4HANA Cloud GROW analysis with decision criteria | Assumes S/4HANA without evaluating alternatives | Skills pack prevents overselling by considering the right-sized product |
| **Export traceability** | Identified as important for EU market access, BTP architecture proposed | Not mentioned | Skills pack catches documentation expectations the baseline overlooks entirely |
| **Currency depth** | All 6 active currencies identified with parallel currency strategy | Only 3 currencies noted | Skills pack captures the full operational complexity |
| **CSS custom code** | Detailed remediation framework with phase-by-phase approach, ATC integration, object categorization | Brief mention of custom code cleanup | Skills pack provides actionable remediation strategy |
| **Organizational risk** | Change fatigue from failed projects identified as top risk with specific mitigation | Brief mention of governance needs | Skills pack provides scenario-specific risk assessment |
| **Cross-skill consistency** | Figures verified across all 4 skill outputs | N/A (single output) | Skills pack self-validates across deliverables |

### Quantitative Comparison

**Scenario A (HHE):**
- Baseline output: ~150 lines of prose
- Skills pack output: 2,400+ lines across 5 coordinated skill outputs, plus PDF
- Information density ratio: approximately 10 to 15x more specific, actionable content

**Scenario B (CSS):**
- Baseline output: ~120 lines of prose
- Skills pack output: 1,800+ lines across 5 coordinated skill outputs
- Information density ratio: approximately 12 to 15x more specific, actionable content

### Key Insight

The baseline produces a competent first draft that a senior consultant might use as a starting point for 2 to 3 more days of detailed work. The skills pack produces a near-complete scoping deliverable set that a consultant could present (with review and refinement) within hours. The difference is not that the baseline is wrong; it is that the baseline is shallow. The structured, multi-skill approach forces depth at each stage that a single-prompt response naturally skips.
