# Skill 05 Output: SAP Best Practices Fetcher -- CSS Queries

## Query 1: Custom Code Remediation for ECC-to-S/4HANA System Conversion

### Input
```json
{
  "query_type": "clean_core_guidance",
  "module": "ABAP/Clean Core",
  "industry": "High Tech",
  "deployment_model": "private_cloud",
  "source_system": "SAP ECC 6.0 EHP8",
  "specific_topic": "analyzing and remediating 2,400+ custom ABAP objects, 47 custom transactions during brownfield system conversion to S/4HANA Cloud Private Edition"
}
```

### Output
```json
{
  "results": [
    {
      "title": "Custom Code Remediation Strategy for Large-Scale Brownfield Conversion",
      "category": "Clean Core Guidance",
      "sap_reference_id": "SAP Custom Code Migration (CCM) Worklist + Simplification Item Catalog + ATC Cloud Readiness Checks",
      "content": "For CSS's 2,400 custom ABAP objects, apply the SAP Custom Code Migration analysis framework in three phases. Phase 1, Automated Analysis: Run SAP Custom Code Migration app (transaction /UI2/CL_CCM or Fiori app F5670) against the full custom code inventory. The tool cross-references each object against the S/4HANA Simplification Item Catalog, identifying: (a) objects referencing deprecated database tables (e.g., BSEG, BSID, BSIK, KONV replaced by ACDOCA, PRCD_ELEMENTS); (b) objects using obsolete function modules or BAPIs; (c) objects impacted by business function changes or data model simplifications. Typical finding distribution for a heavily customized ECC system: 20 to 30% require mandatory remediation (direct incompatibilities), 30 to 40% require adaptation (deprecated APIs with available replacements), 20 to 30% can be retired (redundant with S/4HANA standard), 10 to 15% are functionally clean and migrate as-is. Phase 2, Disposition Decision: For each object apply the Clean Core decision framework: (1) Can standard S/4HANA replace it? Retire the custom code. (2) Can key user extensibility (custom fields, custom logic via BAdIs) replace it? Convert to embedded extension. (3) Does it require complex logic or external integration? Move to BTP side-by-side extension. (4) Is classic ABAP modification unavoidable? Retain under Tier 2 ABAP for Cloud with architectural review board approval. Phase 3, Remediation Execution: Prioritize by module dependency (FI/CO first, then MM/SD, then PP/QM/PS). Use ABAP Test Cockpit (ATC) with cloud-readiness check variant to validate each remediated object. Target: reduce 2,400 objects to fewer than 1,000, with zero Tier 3 classic ABAP objects remaining.",
      "relevance_score": 0.97,
      "source": "SAP Clean Core Framework + SAP Custom Code Migration Tool + S/4HANA Simplification Item Catalog",
      "applicability_notes": "CSS's 2,400 custom objects and 47 custom transactions represent a Level D (Legacy Extensions) Clean Core maturity rating. The CIO's target of 60% custom code reduction is achievable based on industry benchmarks for similarly customized ECC systems. Key risk: the 47 custom transactions likely have deep user adoption and process dependencies. Each must be individually assessed for functional equivalence in S/4HANA Fiori apps. Recommend allocating 3 to 4 months for Phase 1 and Phase 2 analysis before the main conversion project begins, running as a pre-project initiative."
    },
    {
      "title": "ABAP Cloud Development Model for Private Cloud Deployment",
      "category": "Clean Core Guidance",
      "sap_reference_id": "ABAP Cloud Development Model - Tier 2 (ABAP for Cloud)",
      "content": "S/4HANA Cloud Private Edition supports Tier 2 ABAP development, which grants access to released SAP APIs plus a defined set of non-released objects via compatibility contracts. This is the correct target model for CSS. Key principles: (1) All new custom development must use released APIs exclusively (Tier 1 compliant) to ensure future portability. (2) Existing custom code that cannot be fully refactored may operate under Tier 2 with documented compatibility contracts, but this creates future technical debt. (3) BTP side-by-side extensions are preferred for net-new capabilities (e.g., real-time MES dashboard, predictive quality analytics) to maintain Clean Core Level B compliance. (4) Custom transactions should be replaced with Fiori apps where SAP standard equivalents exist; remaining unique transactions should be rebuilt as custom Fiori apps on BTP. Target Clean Core maturity: Level B (Mostly Clean) at go-live, with a roadmap to Level A within 24 months post-conversion.",
      "relevance_score": 0.93,
      "source": "SAP ABAP Cloud Development Model + Clean Core Maturity Framework",
      "applicability_notes": "Parent company alignment is a factor here. If the parent operates at Clean Core Level A or B, CSS should target the same level to enable future consolidation scenarios. The 4-person SAP Basis team should be upskilled on ABAP Cloud development during the project, converting from classic ABAP expertise to cloud-native development skills."
    }
  ],
  "metadata": {
    "query_type": "clean_core_guidance",
    "total_results": 2,
    "knowledge_currency": "Based on SAP S/4HANA 2024/2025 Simplification Item Catalog and Clean Core framework as of TechEd 2025. Custom Code Migration tooling is stable across releases.",
    "disclaimer": "Custom code analysis results are highly environment-specific. The disposition percentages cited are industry benchmarks and actual results for CSS will depend on the specific objects, their business criticality, and user adoption patterns. Run the actual CCM analysis tool against CSS's ECC system for precise findings."
  }
}
```

---

## Query 2: BOM Management Architecture: Engineering-to-Manufacturing-to-As-Built

### Input
```json
{
  "query_type": "process_flow",
  "module": "PP",
  "industry": "High Tech",
  "deployment_model": "private_cloud",
  "specific_topic": "integrated BOM management for satellite manufacturing: engineering BOM from Teamcenter PLM, manufacturing BOM in SAP PP, as-built BOM per serial number, with engineering change management"
}
```

### Output
```json
{
  "results": [
    {
      "title": "Three-Tier BOM Architecture for Satellite Manufacturing with PLM Integration",
      "category": "Process Flow",
      "sap_reference_id": "PP-BOM (Bill of Material) + PLM Integration + Engineering Change Management (ECM) + Serial Number Management",
      "content": "Configure a three-tier BOM architecture for CSS's satellite manufacturing. Tier 1, Engineering BOM (eBOM): Maintained in Teamcenter PLM as the as-designed structure. Contains all engineering parts, specifications, and design intent. Synchronized to SAP via PLM-ERP integration (Teamcenter Gateway for SAP or SAP Integration Suite iFlow). Key fields transferred: material number, BOM header, item components, quantities, engineering change number, effectivity dates. Tier 2, Manufacturing BOM (mBOM): Maintained in SAP PP as the as-planned structure optimized for production execution. Differences from eBOM include: phantom assemblies resolved into flat structure for shop floor, manufacturing-specific items added (consumables, fixtures, test equipment references), operation-level component assignments for backflushing, alternative components for approved substitutions. BOM transfer logic: automated eBOM-to-mBOM transfer with manual review for structural differences, tracked via Engineering Change Management (ECM) with change master records (CC01/CC02). Tier 3, As-Built BOM: Actual components installed per satellite serial number, captured through production order confirmations and serial number assignments. Process: (a) at each operation confirmation, record actual component serial numbers consumed; (b) deviations from mBOM (substitutions, rework, non-conformance dispositions) logged with reason codes; (c) as-built record becomes the permanent configuration baseline for the satellite. Integration with QM: inspection results linked to serial number at each manufacturing milestone. Integration with PM: as-built BOM transfers to equipment master for in-orbit support and anomaly investigation.",
      "relevance_score": 0.96,
      "source": "SAP PP Best Practices for Discrete Manufacturing + SAP PLM Integration Patterns for Aerospace",
      "applicability_notes": "This is the highest-complexity BOM scenario in SAP. CSS's current pain point (Teamcenter BOMs not syncing cleanly with SAP PP) is a well-known challenge in aerospace. The integration architecture must be designed jointly with the Teamcenter PLM team. Key decision: whether to use SAP's native ECM or rely on Teamcenter's change management with one-way push to SAP. For satellite manufacturing at 5 to 15 units per month, the as-built BOM volume is manageable; the complexity lies in the depth of each BOM (typically 3,000 to 10,000 components per satellite) and the serial-number-level traceability requirement. Recommend a dedicated BOM integration workstream in Wave 2 (PP/QM/PS wave)."
    }
  ],
  "metadata": {
    "query_type": "process_flow",
    "total_results": 1,
    "knowledge_currency": "SAP PP BOM management and PLM integration patterns are well-established for aerospace. Teamcenter Gateway for SAP is a Siemens product; confirm current version compatibility with S/4HANA Cloud PE.",
    "disclaimer": "BOM integration architecture between Teamcenter and S/4HANA is highly specific to the PLM version, data model, and engineering processes in place. Engage both the SAP implementation partner and the Teamcenter support team for detailed integration design."
  }
}
```

---

## Query 3: ITAR/EAR Export Control Compliance with SAP GTS

### Input
```json
{
  "query_type": "scope_items",
  "module": "GTS",
  "industry": "Aerospace and Defense",
  "deployment_model": "private_cloud",
  "specific_topic": "ITAR compliance for satellite manufacturing: defense article classification, deemed export tracking, license management, sanctioned party screening, technology control plans"
}
```

### Output
```json
{
  "results": [
    {
      "title": "SAP GTS for ITAR/EAR Export Compliance in Satellite Manufacturing",
      "category": "Scope Item",
      "sap_reference_id": "SAP GTS - Compliance Management + License Management + Sanctioned Party List Screening",
      "content": "Implement SAP GTS as the central export compliance platform for CSS. Configuration scope: (1) COMPLIANCE MANAGEMENT: Sanctioned party list (SPL) screening integrated into SD order creation and delivery processing. Automated download and update of OFAC SDN List, Entity List (BIS), Denied Persons List, Unverified List, Debarred List (DDTC). Screen all business partners (customers, vendors, freight forwarders, end users) against all applicable lists. Configure screening at sales order, delivery, shipment, and purchase order (for re-export scenarios). (2) LICENSE MANAGEMENT: ITAR Technical Assistance Agreements (TAAs), Manufacturing License Agreements (MLAs), and DSP-5 export licenses tracked in GTS license master. License determination at sales order: system checks material ECCN/USML classification against destination country and end user, determines if license required, and assigns available license with quantity/value drawdown tracking. License expiration monitoring with automated alerts. (3) PRODUCT CLASSIFICATION: Maintain dual classification for all materials: USML category (United States Munitions List, Categories IV and XV for satellite-related items) and ECCN (Commerce Control List for EAR-controlled items). Classification drives license determination, screening stringency, and documentation requirements. (4) DEEMED EXPORT CONTROL: Track foreign national employee access to ITAR-controlled technical data. GTS integration with HR master data to flag personnel nationality; access authorization workflow for controlled technical data based on Technology Control Plan (TCP) requirements.",
      "relevance_score": 0.98,
      "source": "SAP GTS Best Practices for Aerospace and Defense + ITAR/EAR Compliance Patterns",
      "applicability_notes": "ITAR compliance is non-negotiable for CSS and must be Phase 1 scope. CSS's current partial GTS implementation with manual workarounds creates significant compliance risk. Full GTS implementation eliminates the separate access control database the CISO is concerned about. Key design decision: GTS can run as an embedded component within S/4HANA or as a standalone system with RFC integration. For Private Cloud deployment, embedded GTS is recommended to reduce integration complexity. Critical: ITAR violations carry penalties up to $1M per violation and debarment from government contracts. This makes GTS the highest-priority compliance workstream in the entire program."
    },
    {
      "title": "Deemed Export Tracking and Technology Control Plan Integration",
      "category": "Scope Item",
      "sap_reference_id": "SAP GTS - Deemed Export Management + Document Access Control",
      "content": "Configure deemed export controls to address CSS's ITAR obligation for controlling access to defense articles and technical data by foreign nationals within the organization. Architecture: (1) HR Integration: Workday HCM provides employee nationality data to SAP via integration; nationality mapped to country control status (denied countries, restricted countries, allied countries). (2) Access Authorization: GTS maintains authorization matrix linking employee clearance level, material/document USML classification, and applicable license or exemption. (3) Technology Control Plan (TCP): Each satellite program has a TCP defining which technical data is controlled and which personnel are authorized. GTS enforces TCP at the document and transaction level. (4) Audit Trail: All access authorization decisions, license checks, and screening results are logged for DDTC (Directorate of Defense Trade Controls) audit readiness. Retention period: 5 years minimum per ITAR requirements.",
      "relevance_score": 0.94,
      "source": "SAP GTS Deemed Export Management + ITAR 22 CFR Part 120-130",
      "applicability_notes": "Deemed export control is the most operationally complex aspect of ITAR compliance for a multi-site manufacturer. CSS's 2,500 employees across three sites must all be screened. The Workday HCM integration is critical for maintaining current nationality data. Recommend engaging ITAR legal counsel during the GTS design phase to validate the authorization matrix and TCP enforcement logic. The separate access control database currently in use should be migrated into GTS to create a single system of record."
    }
  ],
  "metadata": {
    "query_type": "scope_items",
    "total_results": 2,
    "knowledge_currency": "ITAR/EAR regulations as of 2025. SAP GTS compliance management capabilities are mature and well-established for aerospace and defense. DDTC registration and compliance program requirements should be validated with ITAR counsel.",
    "disclaimer": "Export control compliance is a legal obligation with severe penalties for non-compliance. All GTS configuration decisions must be reviewed and approved by CSS's trade compliance officer and external ITAR legal counsel. SAP GTS is a tool that supports compliance; it does not constitute a compliance program on its own."
  }
}
```

---

## Query 4: IFRS 15/ASC 606 Revenue Recognition for Long-Term Satellite Contracts

### Input
```json
{
  "query_type": "scope_items",
  "module": "FI",
  "industry": "High Tech",
  "deployment_model": "private_cloud",
  "specific_topic": "IFRS 15 and ASC 606 revenue recognition for long-term satellite manufacturing and launch services contracts with milestone-based billing, percentage-of-completion recognition, and program-level profitability analysis"
}
```

### Output
```json
{
  "results": [
    {
      "title": "Revenue Accounting and Reporting (RAR) for Long-Term Satellite Contracts",
      "category": "Scope Item",
      "sap_reference_id": "1I1 (Revenue Accounting and Reporting) + PS (Project System) Integration + Event-Based Revenue Recognition",
      "content": "Implement SAP Revenue Accounting and Reporting (RAR, scope item 1I1) for CSS's satellite program contracts. Configuration: (1) CONTRACT IDENTIFICATION: Each satellite program contract registered in RAR with performance obligation decomposition per IFRS 15 five-step model. Typical satellite contract performance obligations: satellite design and engineering, satellite manufacturing and integration, launch services (if bundled), on-orbit commissioning, extended warranty or mission support. (2) TRANSACTION PRICE ALLOCATION: Standalone selling price (SSP) determination for each performance obligation using adjusted market assessment or expected cost plus margin approach. Variable consideration (incentive fees, penalty clauses) estimated and constrained per IFRS 15.56-58. (3) REVENUE RECOGNITION METHOD: Over-time recognition using cost-to-cost input method (percentage of completion). Cost basis: actual project costs posted to WBS elements in Project System (PS) compared to estimated total cost at completion. Progress calculation: cost incurred to date / estimated total cost = percentage complete. Revenue recognized = percentage complete x total transaction price allocated to the performance obligation. (4) MILESTONE BILLING INTEGRATION: Billing plans in SD/PS trigger customer invoices at contractual milestones (e.g., Preliminary Design Review, Critical Design Review, Integration Complete, Pre-Ship Review, Launch, On-Orbit Acceptance). RAR manages the timing difference between billing (milestone-based) and revenue recognition (cost-to-cost). Contract assets (unbilled revenue) and contract liabilities (deferred revenue) posted automatically. (5) PROGRAM PROFITABILITY: CO-PA integration with project-based margin analysis. Profitability by satellite program, by contract, and by performance obligation. Earned Value Management (EVM) indicators (CPI, SPI) calculated from PS actuals vs. plan.",
      "relevance_score": 0.96,
      "source": "SAP RAR (Revenue Accounting and Reporting) + IFRS 15/ASC 606 Implementation Guide + PS Integration Patterns",
      "applicability_notes": "This directly addresses the CFO's requirement for proper program-level profitability analysis and the pain point around milestone-based revenue recognition. RAR replaces the legacy SD revenue recognition approach (VFKKR) which is deprecated in S/4HANA. Key benefit: RAR automates the contract asset/liability calculations that are likely being done manually in CSS's current ECC environment. The PS integration is critical because satellite program costs flow through WBS elements; RAR must consume these costs as input to the percentage-of-completion calculation. Recommend configuring RAR in parallel with PS during Wave 1 (Finance wave) to ensure the cost-to-cost method works correctly with CSS's WBS structure."
    },
    {
      "title": "Project System Integration for Earned Value Management",
      "category": "Scope Item",
      "sap_reference_id": "PS (Project System) + Earned Value Analysis + Milestone Billing",
      "content": "Configure PS Earned Value Management to replace CSS's current Excel-based EVM process. Configuration: (1) WBS STRUCTURE: Hierarchical WBS per satellite program aligned to contract performance obligations and Work Breakdown Structure Dictionary (MIL-STD-881 for defense contracts). Levels: Program, Satellite Unit, Phase (Design, Build, Test, Launch), Work Package. (2) EARNED VALUE CALCULATION: Planned Value (PV) from WBS budget, Actual Cost (AC) from posted actuals (material, labor, overhead via CO allocations), Earned Value (EV) from milestone completion or weighted milestones method. CPI = EV/AC, SPI = EV/PV. Estimate at Completion (EAC) calculated using CPI-based formula. (3) MILESTONE BILLING: Billing plan elements linked to WBS milestones. Billing request auto-created when milestone confirmed in PS network. Integration with RAR for revenue timing. (4) MULTI-YEAR BUDGET MANAGEMENT: Annual budget distribution across WBS with commitment tracking. Purchase requisitions and purchase orders create commitments against WBS budget. Funds management integration for budget availability check at procurement.",
      "relevance_score": 0.92,
      "source": "SAP PS Best Practices for Aerospace Program Management + MIL-STD-881 WBS Standards",
      "applicability_notes": "Moving EVM from Excel into SAP PS is a high-value quick win for the CFO. Current Excel-based EVM is likely error-prone, lacks audit trail, and cannot provide real-time program health indicators. PS-based EVM integrates directly with actual cost postings, eliminating manual data reconciliation. For defense/government contracts, PS-based EVM can be configured to produce IPMR (Integrated Program Management Report) format 1-5 outputs if required by contract terms."
    }
  ],
  "metadata": {
    "query_type": "scope_items",
    "total_results": 2,
    "knowledge_currency": "SAP RAR is the strategic solution for IFRS 15/ASC 606 in S/4HANA, fully replacing legacy revenue recognition. PS Earned Value Analysis has been available since ECC but is significantly enhanced in S/4HANA with Fiori-based reporting.",
    "disclaimer": "Revenue recognition under IFRS 15/ASC 606 involves significant accounting judgment (performance obligation identification, SSP allocation, variable consideration estimation). All RAR configuration must be reviewed and approved by CSS's external auditors and corporate accounting team. SOX compliance requirements for revenue recognition controls must also be addressed in the system design."
  }
}
```

---

## Query 5: System Conversion (Brownfield) Migration Approach for ECC to S/4HANA

### Input
```json
{
  "query_type": "reference_architecture",
  "deployment_model": "private_cloud",
  "source_system": "SAP ECC 6.0 EHP8",
  "company_size": "large_enterprise",
  "specific_topic": "brownfield system conversion approach for satellite manufacturer with 2,400 custom ABAP objects, multi-site deployment across 3 US locations, parent company alignment to S/4HANA Cloud Private Edition"
}
```

### Output
```json
{
  "results": [
    {
      "title": "System Conversion (Brownfield) Reference Architecture for ECC-to-S/4HANA Cloud Private Edition",
      "category": "Reference Architecture",
      "sap_reference_id": "SAP RISE - System Conversion Path + SUM (Software Update Manager) + DMO (Database Migration Option)",
      "content": "Recommended migration approach for CSS: System Conversion (Brownfield) via SAP RISE with S/4HANA Cloud Private Edition. Rationale: (1) CSS has 10 years of master data and transactional history in ECC that has business value (serial number traceability, as-built records, program cost history). Greenfield would require data migration with risk of losing traceability. (2) Parent company alignment to S/4HANA Cloud PE makes RISE the correct commercial vehicle. (3) Brownfield preserves existing configuration baseline, reducing re-implementation effort for stable processes. Technical approach: (a) PRE-CONVERSION (3 to 6 months): Custom code remediation (see Query 1), data quality assessment and cleansing, sandbox conversion trial run, Signavio process discovery to baseline current-state processes. (b) CONVERSION EXECUTION (2 to 3 months): SUM (Software Update Manager) with DMO (Database Migration Option) to convert ECC 6.0 EHP8 to S/4HANA and migrate database to HANA in a single step. Technical conversion of a system this size typically requires 2 to 3 sandbox conversions, 1 dress rehearsal, and 1 production conversion. Downtime window for production conversion: target 48 to 72 hours with SUM optimizations (NZDT procedures where applicable). (c) POST-CONVERSION FUNCTIONAL ADAPTATION (6 to 12 months): Activate new S/4HANA capabilities in waves. Wave 1: Finance (Universal Journal, RAR, new asset accounting). Wave 2: Production and Quality (BOM integration, MES real-time, as-built). Wave 3: Trade Compliance (full GTS, ITAR). Wave 4: Advanced capabilities (embedded analytics, predictive quality, planning optimization). Infrastructure: SAP-managed HANA Enterprise Cloud (HEC) or hyperscaler-hosted (AWS/Azure) Private Cloud infrastructure. Target architecture: single S/4HANA production instance serving all three sites (Redmond, Huntsville, Cape Canaveral) with site-specific plant configuration.",
      "relevance_score": 0.97,
      "source": "SAP RISE System Conversion Methodology + SUM/DMO Technical Guidance + Multi-Site Deployment Patterns",
      "applicability_notes": "Brownfield is the correct approach for CSS given the depth of existing configuration, serial number history, and the board's December 2028 deadline. A greenfield re-implementation of this complexity would take 24 to 30 months, exceeding the deadline. System conversion enables go-live within 18 to 22 months while preserving data continuity. Key risk: the 2,400 custom objects MUST be remediated before conversion; SUM will fail if incompatible custom code is present in the system. This is why the pre-conversion custom code remediation phase (Query 1) is a critical-path prerequisite. The two previously failed IT projects (MES upgrade, PLM migration) create organizational skepticism that must be addressed through strong executive sponsorship, phased delivery with visible early wins, and an independent quality assurance function."
    },
    {
      "title": "Integration Architecture for S/4HANA Cloud PE with Satellite Manufacturing Ecosystem",
      "category": "Reference Architecture",
      "sap_reference_id": "SAP Integration Suite + BTP Middleware + Multi-System Landscape Architecture",
      "content": "Target integration architecture for CSS's system landscape post-conversion: (1) SAP Integration Suite (CPI) as the central integration platform replacing the 12 custom middleware interfaces. Standard integration patterns: Teamcenter PLM to S/4HANA (BOM sync, ECM, material master): SAP Integration Suite with Teamcenter adapter or Siemens Teamcenter Gateway for SAP. Target: near-real-time eBOM-to-mBOM synchronization replacing current batch sync with 4-hour lag. Apriso MES to S/4HANA (production orders, confirmations, quality results): SAP Integration Suite with MES adapter or SAP Digital Manufacturing Cloud (DMC) as intermediary. Target: real-time production visibility (CEO's digital factory requirement). Salesforce CRM to S/4HANA (opportunities, orders, customer master): Standard CPI iFlow content package for Salesforce integration. Bi-directional: opportunity-to-quote in Salesforce, quote-to-order in SAP, order status back to Salesforce. Workday HCM to S/4HANA (organizational data, cost center assignments, employee master for GTS deemed export): Standard CPI iFlow content package for Workday integration. One-way: Workday as system of record for HR, SAP consumes organizational and employee data. Anaplan to S/4HANA (planning data, forecast, budget): API-based integration via CPI. Anaplan for demand and supply planning, SAP for execution and actuals. (2) BTP as Extension Platform: Side-by-side extensions for digital factory dashboard (real-time MES data visualization), predictive quality analytics (ML models on HANA Cloud), supply chain risk monitoring for long-lead components. (3) Integration Governance: API Management layer for all inbound/outbound APIs. Event Mesh for event-driven patterns (e.g., production milestone completion triggers Salesforce update and RAR revenue event).",
      "relevance_score": 0.91,
      "source": "SAP Integration Suite Reference Architecture + BTP Extension Patterns + Aerospace Manufacturing Integration Patterns",
      "applicability_notes": "Consolidating 12 custom middleware interfaces into SAP Integration Suite is a major architectural improvement that directly supports Clean Core objectives. Each existing interface must be analyzed for: data volume, frequency, error handling, and business criticality. Prioritize the MES and PLM integrations (highest business impact) in Wave 2. Salesforce and Workday integrations (lower complexity) can be addressed in Wave 1. The Anaplan integration should be reviewed for potential replacement by SAP IBP (Integrated Business Planning) if parent company uses IBP, but this is a separate decision from the core S/4HANA conversion."
    }
  ],
  "metadata": {
    "query_type": "reference_architecture",
    "total_results": 2,
    "knowledge_currency": "SAP RISE system conversion methodology as of 2025. SUM/DMO tooling is continuously updated; confirm minimum SUM version for ECC 6.0 EHP8 to S/4HANA 2025 conversion path.",
    "disclaimer": "System conversion planning requires detailed technical assessment of the source ECC system, including database size, custom code inventory, add-on compatibility, and integration landscape. The reference architecture presented here is directional. Engage SAP or a certified implementation partner for a formal System Conversion Assessment (SCA) before committing to the conversion approach and timeline."
  }
}
```

---

## Summary: Key Best Practices Applied to CSS

| Topic | Key Recommendation | SAP Reference |
|---|---|---|
| Custom Code Remediation | Run CCM analysis on 2,400 objects; target 60% retirement/consolidation; achieve Clean Core Level B at go-live | CCM Worklist + ATC Cloud Readiness |
| BOM Management | Three-tier architecture (eBOM/mBOM/as-built) with Teamcenter PLM integration via SAP Integration Suite | PP-BOM + ECM + Serial Number Mgmt |
| ITAR/EAR Compliance | Full GTS implementation in Phase 1; embedded deployment; SPL screening, license management, deemed export controls | SAP GTS Compliance + License Mgmt |
| Revenue Recognition | SAP RAR for IFRS 15/ASC 606 with cost-to-cost method; PS integration for EVM replacing Excel-based tracking | 1I1 (RAR) + PS Earned Value |
| System Conversion | Brownfield via RISE; SUM/DMO conversion with 3 to 6 month pre-conversion remediation phase; 4-wave post-conversion activation | RISE System Conversion + SUM/DMO |
| Integration Architecture | SAP Integration Suite replacing 12 custom middleware interfaces; BTP for digital factory extensions | CPI + BTP + Event Mesh |
