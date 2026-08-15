# Skill 02 Output: Module Fit Analyzer -- Constellation Satellite Systems (CSS)

## Analysis Metadata

| Field | Value |
|---|---|
| **Analysis ID** | MFA-20260222-CSS |
| **Source Brief** | DB-20260222-CSS (Skill 01 Discovery Brief) |
| **Created Date** | 2026-02-22 |
| **Confidence Level** | HIGH |
| **Data Completeness** | 90% (from Skill 01) |

---

## Module Assessment Matrix

```json
{
  "module_fit_analysis": {
    "metadata": {
      "analysis_id": "MFA-20260222-CSS",
      "source_brief_id": "DB-20260222-CSS",
      "created_date": "2026-02-22T00:00:00Z",
      "confidence_level": "HIGH",
      "assumptions": [
        "Revenue of approximately $1.2B based on client brief; subsidiary of a larger aerospace conglomerate",
        "S/4HANA Cloud Private Edition is the target deployment model per parent company alignment mandate",
        "System conversion (brownfield) path is confirmed; preserves 10+ years of ECC transactional and master data history",
        "800 active SAP users across Professional and Limited Professional license types (exact breakdown not confirmed)",
        "ECC database size not yet provided; sizing estimates assume a mid-range A&D manufacturer (2 to 5 TB)",
        "ITAR-controlled data resides within the SAP perimeter; exact scope of ITAR-classified master data objects requires CISO validation",
        "Parent company managed service provider will host the S/4HANA Cloud Private Edition tenant (to be confirmed)",
        "Custom code analysis (2,400 ABAP objects, 47 custom transactions) has not yet been performed via SAP Custom Code Migration Worklist; classifications in this analysis are directional"
      ]
    },

    "sizing_recommendation": {
      "recommended_deployment_model": "S/4HANA Cloud Private Edition",
      "sap_program": "SAP RISE",
      "rationale": "CSS's deployment model is driven by three converging requirements: (1) Parent company alignment mandate on S/4HANA Cloud Private Edition, which provides a shared platform standard across the conglomerate. (2) ITAR data residency requirements necessitate a dedicated tenant with US-jurisdiction hosting, US-person access controls, and FedRAMP-aligned infrastructure; Public Edition's multi-tenant architecture cannot satisfy these constraints. (3) The brownfield system conversion path from ECC 6.0 EHP8 is supported only in Private Edition and On-Premise deployments, and the parent company mandate eliminates On-Premise. Private Edition also provides the custom code migration path needed for the retained ABAP objects that survive the 60% reduction target. The SAP RISE commercial model bundles infrastructure, application management, and BTP credits, simplifying the commercial relationship and aligning with parent company procurement patterns.",
      "alternative_considered": "S/4HANA On-Premise",
      "alternative_rationale": "On-Premise was considered given the heavy customization footprint and ITAR requirements. However, the parent company mandate for Cloud Private Edition, combined with the desire to reduce Basis team burden (currently 4 FTEs) and align with a managed service model, makes On-Premise a non-preferred option. On-Premise remains the fallback if Cloud Private Edition cannot satisfy specific ITAR infrastructure requirements identified during detailed CISO review.",
      "estimated_total_users": {
        "professional": 350,
        "limited_professional": 400,
        "developer": 50,
        "user_breakdown": [
          { "role": "Finance and Controlling (FI/CO)", "type": "Professional", "count": 40 },
          { "role": "Procurement and Materials Management (MM)", "type": "Professional", "count": 50 },
          { "role": "Sales and Distribution (SD)", "type": "Professional", "count": 25 },
          { "role": "Production Planning and Manufacturing (PP)", "type": "Professional", "count": 60 },
          { "role": "Quality Management (QM)", "type": "Professional", "count": 35 },
          { "role": "Plant Maintenance (PM)", "type": "Professional", "count": 20 },
          { "role": "Project System and Program Management (PS)", "type": "Professional", "count": 30 },
          { "role": "GTS and Export Compliance (GTS)", "type": "Professional", "count": 15 },
          { "role": "IT and Basis Administration", "type": "Professional", "count": 15 },
          { "role": "Management and Executive Reporting", "type": "Professional", "count": 60 },
          { "role": "Shop Floor Operators (MES-integrated)", "type": "Limited Professional", "count": 150 },
          { "role": "Warehouse and Inventory Staff", "type": "Limited Professional", "count": 60 },
          { "role": "Quality Inspectors (shop floor)", "type": "Limited Professional", "count": 40 },
          { "role": "Maintenance Technicians", "type": "Limited Professional", "count": 30 },
          { "role": "Project Team Members (read/time entry)", "type": "Limited Professional", "count": 80 },
          { "role": "General Self-Service (approvals, time, expenses)", "type": "Limited Professional", "count": 40 },
          { "role": "ABAP Developers and BTP Developers", "type": "Developer", "count": 30 },
          { "role": "Basis and Integration Administrators", "type": "Developer", "count": 20 }
        ]
      },
      "estimated_system_sizing": "L",
      "high_availability_needs": "Yes",
      "disaster_recovery_needs": "Yes",
      "notes": "Total estimated users: 800 (350 Professional + 400 Limited Professional + 50 Developer). System sizing is Large based on: $1.2B revenue, complex BOM structures with serialized satellite units, multi-site manufacturing, high transaction volume during production ramp (15 satellites/month target), and ITAR audit trail retention requirements. High availability is mandatory given manufacturing continuity requirements during 3x production ramp. Disaster recovery is required for ITAR compliance and DCAA audit readiness. Infrastructure must be FedRAMP-aligned or equivalent to satisfy ITAR data residency."
    },

    "module_assessments": [
      {
        "module_code": "FI",
        "module_name": "Financial Accounting",
        "relevance": "CRITICAL",
        "fit_score": 3.5,
        "fit_rating": "Good Fit with Configuration Gaps",
        "business_driver": "5-day financial close target (down from 12 days), IFRS 15/ASC 606 milestone-based revenue recognition via RAR, SOX compliance for financial controls, parent company consolidation reporting, multi-currency support for European supplier payments",
        "key_scope_items": [
          { "scope_item_id": "J58", "name": "General Ledger Accounting", "fit": 4, "notes": "S/4HANA Universal Journal (ACDOCA) consolidates FI and CO postings, eliminating reconciliation overhead that contributes to the 12-day close. Parallel ledger configuration needed for: (a) US GAAP primary ledger, (b) IFRS ledger for parent consolidation, (c) potential tax ledger. Standard configuration." },
          { "scope_item_id": "J77", "name": "Accounts Payable", "fit": 4, "notes": "Standard AP for supplier invoice processing. Space-grade component suppliers (European, domestic) use standard three-way match. Payment program with USD primary and EUR for European suppliers. Standard functionality." },
          { "scope_item_id": "BDJ", "name": "Accounts Receivable", "fit": 3, "notes": "Satellite program receivables are milestone-based, not standard invoice-on-delivery. AR must integrate with PS milestone billing and RAR for revenue recognition. Requires configuration alignment with milestone billing plan in SD/PS." },
          { "scope_item_id": "BKP", "name": "Asset Accounting", "fit": 4, "notes": "Significant fixed asset base: manufacturing equipment, clean room infrastructure, test equipment, launch support equipment. Standard asset accounting with parallel valuation for US GAAP and IFRS depreciation methods." },
          { "scope_item_id": "J82", "name": "Currency and Exchange Rates", "fit": 4, "notes": "USD primary with EUR for European supplier payments. Parallel currency for parent company consolidation (confirm parent reporting currency). Standard multi-currency configuration." },
          { "scope_item_id": "RAR", "name": "Revenue Accounting and Reporting", "fit": 2, "notes": "CRITICAL GAP: Currently handled manually outside SAP. RAR activation required for IFRS 15/ASC 606 compliance with milestone-based, percentage-of-completion, and deliverable-based recognition methods for long-term satellite and launch service contracts. New scope item requiring full configuration and historical data migration for open contracts." },
          { "scope_item_id": "FI-LC", "name": "Intercompany and Consolidation", "fit": 3, "notes": "Intercompany processing with parent conglomerate. S/4HANA intercompany reconciliation with real-time matching. Consolidation data feed to parent company system (format and frequency to be confirmed)." }
        ],
        "gaps_identified": [
          {
            "gap_description": "IFRS 15/ASC 606 revenue recognition is not configured in current ECC; milestone-based recognition for satellite program contracts is handled entirely in manual Excel workbooks outside SAP",
            "gap_severity": "Critical",
            "resolution_approach": "Activate S/4HANA Revenue Accounting and Reporting (RAR). Configure revenue recognition rules for three contract types: (a) satellite manufacturing (milestone-based), (b) launch services (deliverable-based), (c) ground station services (time-based). Migrate open contract obligations from Excel to RAR. Integrate with SD billing milestones and PS WBS milestones.",
            "estimated_effort": "8 to 12 weeks design, configuration, and testing",
            "clean_core_impact": "None; RAR is standard S/4HANA functionality"
          },
          {
            "gap_description": "12-day financial close cycle driven by manual reconciliations, Excel-based EVM consolidation, and multi-step intercompany processing; target is 5 days",
            "gap_severity": "High",
            "resolution_approach": "Leverage S/4HANA Universal Journal to eliminate FI-CO reconciliation steps. Implement automated intercompany matching. Deploy SAP Fiori Financial Close Cockpit (scope item 4HK) for close task management and status tracking. Automate period-end accruals and allocations. Target: 5-day close achievable within 2 to 3 close cycles post go-live.",
            "estimated_effort": "4 to 6 weeks close process redesign and configuration",
            "clean_core_impact": "None; standard S/4HANA close management"
          },
          {
            "gap_description": "Parallel currency configuration for parent company consolidation reporting not established; parent reporting currency and intercompany accounting rules not yet confirmed",
            "gap_severity": "Medium",
            "resolution_approach": "Configure group currency in S/4HANA ledger. Establish intercompany billing and transfer pricing rules. Align chart of accounts mapping with parent company consolidation system. Requires parent company finance team engagement.",
            "estimated_effort": "3 to 4 weeks configuration (dependent on parent company requirements gathering)",
            "clean_core_impact": "None; standard configuration"
          }
        ],
        "clean_core_assessment": {
          "level": "B",
          "standard_process_adoption_rate": "85%",
          "extensions_needed": [
            {
              "extension_description": "DCAA-compliant cost accounting reports for government contract compliance",
              "extension_type": "Key User App",
              "clean_core_impact": "Low",
              "justification": "Standard SAP reporting does not produce DCAA-formatted cost accounting reports. Key User extensibility to create compliant report layouts without modifying core FI logic."
            }
          ],
          "modifications_flagged": []
        }
      },

      {
        "module_code": "CO",
        "module_name": "Controlling",
        "relevance": "CRITICAL",
        "fit_score": 3.0,
        "fit_rating": "Moderate Fit with Significant Configuration Required",
        "business_driver": "Program-level profitability analysis for satellite programs, earned value management (EVM) integration with PS, product costing for complex satellite BOMs, cost center accounting across three sites, overhead allocation for government contract compliance",
        "key_scope_items": [
          { "scope_item_id": "J59", "name": "Cost Center Accounting", "fit": 4, "notes": "Cost centers for Redmond manufacturing, Huntsville manufacturing, Cape Canaveral launch operations, corporate functions. Standard configuration with allocation cycles." },
          { "scope_item_id": "1YR", "name": "Profitability Analysis", "fit": 3, "notes": "CO-PA must support program-level profitability for satellite constellations (not just product-level). Characteristics: satellite program, contract type, customer, launch campaign, cost element group. Requires careful operating concern design." },
          { "scope_item_id": "J60", "name": "Product Cost Planning", "fit": 2, "notes": "SIGNIFICANT GAP: Satellite manufacturing involves complex multi-level BOMs with 5,000+ components, long production cycles (months per unit), and engineering change orders during production. Standard product cost planning needs extensive configuration for: (a) BOM-based cost rollup with engineering change effectivity, (b) activity-based costing for clean room operations, (c) serialized unit costing." },
          { "scope_item_id": "J61", "name": "Internal Orders", "fit": 4, "notes": "Internal orders for non-recurring engineering (NRE), R&D programs, and capital projects. Standard configuration." }
        ],
        "gaps_identified": [
          {
            "gap_description": "Program-level profitability analysis for satellite constellation programs is not supported by standard product-level CO-PA; requires operating concern design that spans multiple sales orders, projects, and production orders under a single program umbrella",
            "gap_severity": "High",
            "resolution_approach": "Design CO-PA operating concern with program-level characteristics. Use derivation rules to assign transactions (sales orders, production orders, WBS elements) to satellite programs. Consider margin analysis using both costing-based and account-based CO-PA in S/4HANA. Integrate with PS for program cost collection.",
            "estimated_effort": "6 to 8 weeks operating concern design and configuration",
            "clean_core_impact": "Low; standard CO-PA configuration with custom derivation rules"
          },
          {
            "gap_description": "Earned value management (EVM) currently performed in Excel outside SAP; no integration between PS cost actuals and EVM calculations",
            "gap_severity": "High",
            "resolution_approach": "Implement S/4HANA Project System earned value analysis (PS-EVM). Configure EVM methods (cost-based, effort-based) per WBS element. Integrate with CO for actual cost collection and budget data. Eliminate Excel-based EVM workbooks. If S/4HANA PS-EVM does not meet DCAA requirements for EVMS (ANSI/EIA-748), evaluate BTP-based integration with a dedicated EVM tool.",
            "estimated_effort": "6 to 8 weeks (dependent on PS implementation scope)",
            "clean_core_impact": "None if standard PS-EVM is sufficient; Medium if BTP integration with external EVM tool is required"
          },
          {
            "gap_description": "Product costing for satellite assemblies with complex multi-level BOMs (5,000+ components), engineering change effectivity, and serialized unit costing requires extensive configuration beyond standard product cost planning",
            "gap_severity": "High",
            "resolution_approach": "Configure product cost planning with: (a) multi-level BOM cost rollup from Teamcenter-sourced manufacturing BOM, (b) activity types for clean room hours, test hours, and integration labor, (c) make/buy analysis for subassemblies, (d) serialized cost collection per satellite unit via production order settlement to PS WBS elements.",
            "estimated_effort": "8 to 10 weeks design and configuration",
            "clean_core_impact": "Low; standard product costing with detailed master data configuration"
          }
        ],
        "clean_core_assessment": {
          "level": "B",
          "standard_process_adoption_rate": "75%",
          "extensions_needed": [
            {
              "extension_description": "DCAA-compliant incurred cost submission report generation",
              "extension_type": "Key User App",
              "clean_core_impact": "Low",
              "justification": "Government contract cost accounting requires specific report formats not available in standard SAP CO reporting. Key User extensibility for report layouts."
            },
            {
              "extension_description": "Anaplan integration for planning actuals vs. forecast comparison",
              "extension_type": "BTP Side-by-Side",
              "clean_core_impact": "None",
              "justification": "Anaplan is the existing planning tool. BTP Integration Suite iFlow to synchronize CO actuals with Anaplan planning models."
            }
          ],
          "modifications_flagged": []
        }
      },

      {
        "module_code": "MM",
        "module_name": "Materials Management",
        "relevance": "CRITICAL",
        "fit_score": 3.5,
        "fit_rating": "Good Fit with Supply Chain Extension Gaps",
        "business_driver": "Space-grade electronics procurement with 18+ month lead times, multi-site inventory management (Redmond, Huntsville, Cape Canaveral), supplier quality integration, serialized component traceability, and scaling procurement volume for 3x production ramp",
        "key_scope_items": [
          { "scope_item_id": "1A2", "name": "Purchasing", "fit": 4, "notes": "Standard procurement for space-grade components, COTS electronics, mechanical assemblies, and services. Long-term purchase agreements with strategic suppliers. Standard PO processing with three-way match." },
          { "scope_item_id": "1NM", "name": "Inventory Management", "fit": 4, "notes": "Batch and serial number management for satellite components. Multi-site inventory across Redmond and Huntsville manufacturing facilities. Standard inventory management with serialization." },
          { "scope_item_id": "1B4", "name": "Goods Receipt", "fit": 4, "notes": "Standard goods receipt with quality inspection trigger for incoming space-grade components. Serialized receipt for tracked components. Standard MIGO functionality." },
          { "scope_item_id": "2OM", "name": "Source Determination and Supplier Evaluation", "fit": 3, "notes": "Supplier evaluation criteria must include space-grade qualification status, AS9100 certification, ITAR compliance, delivery performance against long lead times. Requires configuration of evaluation criteria beyond standard commercial metrics." }
        ],
        "gaps_identified": [
          {
            "gap_description": "No predictive tracking for space-grade electronic components with 18+ month lead times; supply chain disruptions discovered reactively; demand planning disconnected from production schedule",
            "gap_severity": "Critical",
            "resolution_approach": "Configure long-term purchase scheduling agreements with delivery schedule lines spanning 18+ months. Implement MRP planning with long-range planning horizons. Evaluate SAP IBP for demand/supply planning if Anaplan does not cover long-lead component visibility. Alternatively, extend Anaplan integration via BTP to feed demand signals into MM purchasing.",
            "estimated_effort": "6 to 8 weeks for MRP configuration; 8 to 12 weeks if IBP is added to scope",
            "clean_core_impact": "None for MRP configuration; BTP extension for Anaplan or IBP integration"
          },
          {
            "gap_description": "Supplier quality integration is limited; space-grade component qualification and lot acceptance processes require tighter MM-QM integration with supplier performance tracking",
            "gap_severity": "High",
            "resolution_approach": "Configure QM source inspection for critical suppliers. Implement supplier quality score integration with purchasing info records. Establish quality certificates (CoC, CoA) as mandatory at goods receipt for space-grade materials. Standard MM-QM integration with enhanced master data configuration.",
            "estimated_effort": "4 to 6 weeks configuration",
            "clean_core_impact": "None; standard MM-QM integration"
          },
          {
            "gap_description": "Procurement volume scaling from 5 to 15 satellites per month (3x increase) requires procurement process optimization, automated requisition generation, and supplier capacity management not currently in place",
            "gap_severity": "Medium",
            "resolution_approach": "Implement MRP-driven procurement with automatic creation of purchase requisitions. Configure release strategies for high-value procurements. Establish blanket purchase orders for recurring components. Optimize procurement workflows using SAP Fiori Manage Purchase Requisitions app.",
            "estimated_effort": "3 to 4 weeks configuration and process optimization",
            "clean_core_impact": "None; standard S/4HANA procurement functionality"
          }
        ],
        "clean_core_assessment": {
          "level": "B",
          "standard_process_adoption_rate": "80%",
          "extensions_needed": [
            {
              "extension_description": "Supplier collaboration portal for space-grade component suppliers (forecast sharing, delivery confirmation, quality certificate upload)",
              "extension_type": "BTP Side-by-Side",
              "clean_core_impact": "None",
              "justification": "Standard SAP supplier portal (Ariba Network) may not meet the specialized requirements for ITAR-controlled supply chain collaboration. BTP-based portal provides controlled external access without exposing ITAR data."
            }
          ],
          "modifications_flagged": []
        }
      },

      {
        "module_code": "SD",
        "module_name": "Sales and Distribution",
        "relevance": "HIGH",
        "fit_score": 3.5,
        "fit_rating": "Good Fit with Contract Management Gaps",
        "business_driver": "Satellite program sales order management, milestone billing for long-term contracts, launch services contract management, Salesforce CRM integration, and government contract terms and conditions",
        "key_scope_items": [
          { "scope_item_id": "BD1", "name": "Sales Order Management", "fit": 3, "notes": "Satellite program sales involve complex contract structures with multiple deliverables (satellite units, launch services, ground station services, warranty/support). Standard sales orders may need project-linked sales document types for milestone-based billing. Configuration required." },
          { "scope_item_id": "BD9", "name": "Billing", "fit": 3, "notes": "Milestone billing for satellite programs requires billing plan configuration tied to PS milestones (design review, manufacturing complete, integration and test, launch, in-orbit acceptance). Non-standard billing cadence; requires billing plan master data per contract." },
          { "scope_item_id": "1CX", "name": "Service Contract Management", "fit": 3, "notes": "Launch services and in-orbit support contracts require service contract management with deliverable tracking. Evaluate S/4HANA Service capabilities vs. Salesforce service management. Integration point with CRM." },
          { "scope_item_id": "BKC", "name": "Pricing", "fit": 4, "notes": "Contract-based pricing with escalation clauses, change order pricing, and government contract pricing structures (cost-plus, fixed-price, time-and-materials). Standard condition technique with condition tables." }
        ],
        "gaps_identified": [
          {
            "gap_description": "Milestone billing for satellite program contracts is not configured; billing must be triggered by project milestone completion in PS rather than goods delivery",
            "gap_severity": "High",
            "resolution_approach": "Configure milestone billing plans in SD linked to PS WBS milestones. Each contract receives a billing plan with milestone-based payment terms (e.g., 20% at CDR, 30% at manufacturing complete, 30% at launch, 20% at in-orbit acceptance). Standard SD-PS integration for milestone billing.",
            "estimated_effort": "4 to 6 weeks design and configuration",
            "clean_core_impact": "None; standard SD-PS milestone billing"
          },
          {
            "gap_description": "Salesforce is the CRM system of record; no integration currently exists between Salesforce opportunity/contract data and SAP SD sales orders",
            "gap_severity": "Medium",
            "resolution_approach": "Implement Salesforce-to-SAP SD integration via BTP Integration Suite. Bidirectional sync for: (a) Salesforce opportunity to SAP sales order creation, (b) SAP billing milestone status back to Salesforce for customer visibility, (c) master data sync (customer, contact). Standard integration pattern available from SAP.",
            "estimated_effort": "6 to 8 weeks BTP integration development",
            "clean_core_impact": "None; BTP side-by-side integration"
          }
        ],
        "clean_core_assessment": {
          "level": "A",
          "standard_process_adoption_rate": "85%",
          "extensions_needed": [
            {
              "extension_description": "Salesforce CRM integration via BTP Integration Suite",
              "extension_type": "BTP Side-by-Side",
              "clean_core_impact": "None",
              "justification": "Salesforce is the retained CRM system of record. Integration is standard BTP pattern; no modification to SD core."
            }
          ],
          "modifications_flagged": []
        }
      },

      {
        "module_code": "PP",
        "module_name": "Production Planning",
        "relevance": "CRITICAL",
        "fit_score": 2.5,
        "fit_rating": "Weak Fit with Critical Integration and BOM Management Gaps",
        "business_driver": "Satellite manufacturing BOM management (engineering, manufacturing, as-built), production scheduling for 15 satellites/month target, MES integration with Apriso (real-time), PLM integration with Teamcenter, and serialized production order tracking per satellite unit",
        "key_scope_items": [
          { "scope_item_id": "1MP", "name": "Production Order Processing", "fit": 3, "notes": "Standard discrete manufacturing production orders for satellite assembly. Serialized production orders per satellite unit. Order confirmation from MES (Apriso). Standard with integration dependency on MES." },
          { "scope_item_id": "1MO", "name": "BOM Management", "fit": 2, "notes": "CRITICAL GAP: Three disconnected BOM representations currently exist (engineering in Teamcenter, manufacturing in SAP PP, as-built tracked manually). S/4HANA BOM management is the manufacturing BOM authority, but bi-directional sync with Teamcenter for engineering changes and as-built configuration capture require integration that does not exist in standard SAP." },
          { "scope_item_id": "1MN", "name": "MRP (Material Requirements Planning)", "fit": 3, "notes": "MRP for satellite component planning. Must accommodate 18+ month lead times for space-grade electronics and manage the 3x production ramp from 5 to 15 units/month. Standard MRP with long planning horizons and planning strategy configuration." },
          { "scope_item_id": "1MR", "name": "Capacity Planning", "fit": 3, "notes": "Clean room capacity, test chamber capacity, and integration bay capacity are critical bottlenecks during production ramp. Standard capacity planning with work center configuration." }
        ],
        "gaps_identified": [
          {
            "gap_description": "Engineering BOM in Teamcenter PLM does not synchronize cleanly with manufacturing BOM in SAP PP; as-built BOM is tracked manually outside both systems; three disconnected BOM representations create traceability gaps and rework",
            "gap_severity": "Critical",
            "resolution_approach": "Implement bidirectional PLM integration between Teamcenter and S/4HANA PP via SAP Engineering Control Center (ECTR) or BTP-based integration. Define BOM lifecycle: (a) engineering BOM authored in Teamcenter, (b) released to SAP PP as manufacturing BOM via integration, (c) as-built configuration captured in SAP PP through serialized production order confirmations. Engineering change management (ECM) must flow from Teamcenter to SAP with effectivity dates. This is the single most complex integration in the program.",
            "estimated_effort": "12 to 16 weeks for PLM integration design, development, and testing",
            "clean_core_impact": "Medium; BTP-based integration is Clean Core compliant, but the complexity of BOM lifecycle management may require custom logic for change effectivity handling"
          },
          {
            "gap_description": "MES (Apriso) to SAP integration has a 4-hour data lag; no real-time manufacturing visibility during satellite assembly and integration",
            "gap_severity": "Critical",
            "resolution_approach": "Replace batch-based MES integration with real-time or near-real-time integration via BTP Integration Suite. Implement production order confirmation from Apriso to SAP PP in real-time. Backflush material consumption at confirmation. Capture serialized component installation (as-built) at each manufacturing step. Target latency: under 5 minutes.",
            "estimated_effort": "8 to 12 weeks for MES integration redesign and implementation",
            "clean_core_impact": "None; BTP Integration Suite handles the integration layer"
          },
          {
            "gap_description": "Production scaling from 5 to 15 satellites per month requires production scheduling, capacity planning, and workforce planning capabilities that are not currently configured in SAP PP",
            "gap_severity": "High",
            "resolution_approach": "Configure detailed production scheduling with finite capacity planning. Establish work centers for clean rooms, integration bays, and test chambers with capacity constraints. Implement scheduling board (Fiori app) for production planners. Integrate with MRP for component availability checks.",
            "estimated_effort": "6 to 8 weeks configuration",
            "clean_core_impact": "None; standard PP configuration"
          }
        ],
        "clean_core_assessment": {
          "level": "C",
          "standard_process_adoption_rate": "60%",
          "extensions_needed": [
            {
              "extension_description": "Teamcenter PLM bidirectional BOM integration via BTP or SAP ECTR",
              "extension_type": "BTP Side-by-Side",
              "clean_core_impact": "Medium",
              "justification": "No standard SAP connector delivers the full BOM lifecycle management (engineering to manufacturing to as-built) required for satellite manufacturing. Integration must handle engineering change effectivity, BOM comparison, and release workflows."
            },
            {
              "extension_description": "Apriso MES real-time production order confirmation and as-built capture",
              "extension_type": "BTP Side-by-Side",
              "clean_core_impact": "None",
              "justification": "Standard BTP Integration Suite pattern for MES connectivity. Replaces the current 4-hour batch interface with event-driven integration."
            }
          ],
          "modifications_flagged": [
            {
              "modification_description": "Custom BOM comparison logic for engineering vs. manufacturing vs. as-built configuration tracking",
              "reason": "Standard SAP BOM comparison does not support three-way comparison across PLM-sourced engineering BOM, SAP manufacturing BOM, and serialized as-built configuration",
              "clean_core_violation": true,
              "recommended_alternative": "Implement BOM comparison logic as a BTP side-by-side extension rather than in-app modification. Use SAP ECTR or custom BTP application to provide the comparison dashboard, keeping the S/4HANA PP core clean."
            }
          ]
        }
      },

      {
        "module_code": "QM",
        "module_name": "Quality Management",
        "relevance": "CRITICAL",
        "fit_score": 3.0,
        "fit_rating": "Moderate Fit with Aerospace Quality Compliance Gaps",
        "business_driver": "AS9100D aerospace quality management system compliance, serialized inspection per satellite unit, supplier quality management for space-grade components, non-conformance management with root cause analysis, and predictive quality analytics (target state)",
        "key_scope_items": [
          { "scope_item_id": "2QN", "name": "Quality Inspection", "fit": 3, "notes": "Inspection plans for incoming material inspection (space-grade components), in-process inspection (satellite assembly steps), and final acceptance testing. Standard QM inspection with detailed characteristic configuration for aerospace specifications." },
          { "scope_item_id": "2QR", "name": "Quality Notifications", "fit": 3, "notes": "Non-conformance reports (NCRs), corrective action requests (CARs), and material review board (MRB) disposition tracking. Standard quality notification processing with custom notification types for aerospace NCR workflow." },
          { "scope_item_id": "2QP", "name": "Quality Certificates", "fit": 4, "notes": "Certificate of Conformance (CoC) generation per satellite unit. Supplier certificate management (CoC, CoA) at goods receipt. Standard certificate management." },
          { "scope_item_id": "QM-PP", "name": "QM-PP Integration (In-Process Inspection)", "fit": 3, "notes": "In-process inspection triggered at manufacturing milestones during satellite assembly. Inspection results recorded in QM, linked to serialized production order in PP. Standard integration with configuration required for inspection point triggers." }
        ],
        "gaps_identified": [
          {
            "gap_description": "AS9100D compliance requires specific quality processes (first article inspection, process FMEA, control plans, PPAP equivalents) that are not pre-configured in standard SAP QM",
            "gap_severity": "High",
            "resolution_approach": "Configure QM to support AS9100D workflows: (a) first article inspection as a specific inspection type with full dimensional and functional verification, (b) control plan linkage to inspection plans, (c) nonconformance classification aligned with AS9100D clause requirements, (d) audit management for internal and external quality audits. Standard QM configuration; no custom code required.",
            "estimated_effort": "6 to 8 weeks aerospace QM configuration",
            "clean_core_impact": "None; standard QM configuration with aerospace-specific master data"
          },
          {
            "gap_description": "Non-conformance management for satellite components requires material review board (MRB) workflow with use-as-is, rework, scrap, and return-to-vendor dispositions; current process is partially manual",
            "gap_severity": "Medium",
            "resolution_approach": "Configure quality notification types for NCR with multi-step approval workflow. Implement MRB disposition actions as standard QM tasks. Link NCR disposition to inventory management actions (scrap, rework order, return delivery). Standard QM notification workflow.",
            "estimated_effort": "3 to 4 weeks configuration",
            "clean_core_impact": "None; standard QM notification workflow"
          },
          {
            "gap_description": "No predictive quality analytics capability; quality trends and defect prediction during production ramp require analytics beyond standard QM reporting",
            "gap_severity": "Low",
            "resolution_approach": "Phase 2/3 initiative: deploy SAP Analytics Cloud (SAC) with embedded analytics on QM inspection data. Evaluate AI/ML models for defect prediction based on in-process inspection results, supplier quality scores, and environmental parameters (clean room conditions). BTP-based analytics extension.",
            "estimated_effort": "8 to 12 weeks (Phase 2/3 scope)",
            "clean_core_impact": "None; BTP/SAC extension"
          }
        ],
        "clean_core_assessment": {
          "level": "A",
          "standard_process_adoption_rate": "80%",
          "extensions_needed": [
            {
              "extension_description": "Predictive quality analytics dashboard using SAC and BTP",
              "extension_type": "BTP Side-by-Side",
              "clean_core_impact": "None",
              "justification": "Standard QM provides retrospective quality reporting. Predictive analytics for defect prevention during production ramp requires SAC/BTP extension. Phase 2/3 scope."
            }
          ],
          "modifications_flagged": []
        }
      },

      {
        "module_code": "PM",
        "module_name": "Plant Maintenance",
        "relevance": "HIGH",
        "fit_score": 3.5,
        "fit_rating": "Good Fit with Calibration Management Gap",
        "business_driver": "Manufacturing equipment maintenance across Redmond and Huntsville sites, clean room infrastructure maintenance (HVAC, particulate filtration, environmental controls), test equipment calibration management, and predictive maintenance potential during production ramp",
        "key_scope_items": [
          { "scope_item_id": "2NX", "name": "Preventive Maintenance", "fit": 4, "notes": "Time-based and counter-based preventive maintenance plans for manufacturing equipment, clean room systems, and launch support equipment. Standard PM functionality." },
          { "scope_item_id": "2NY", "name": "Corrective Maintenance", "fit": 4, "notes": "Work order management for equipment breakdowns and unplanned repairs. Integration with MM for spare parts procurement. Standard maintenance order processing." },
          { "scope_item_id": "2NZ", "name": "Equipment and Functional Location Management", "fit": 4, "notes": "Equipment master records for manufacturing equipment, test chambers, clean rooms. Functional location hierarchy for Redmond, Huntsville, and Cape Canaveral facilities. Standard master data configuration." }
        ],
        "gaps_identified": [
          {
            "gap_description": "Clean room equipment maintenance requires integration with environmental monitoring systems to track particulate counts, temperature, and humidity; maintenance triggers based on environmental excursions are not standard PM functionality",
            "gap_severity": "Medium",
            "resolution_approach": "Phase 2/3: integrate clean room environmental monitoring with PM via BTP IoT services. Environmental excursions trigger maintenance notifications automatically. Phase 1: use standard time-based preventive maintenance for clean room systems.",
            "estimated_effort": "Phase 1: 2 to 3 weeks standard PM configuration; Phase 2/3: 6 to 8 weeks BTP IoT integration",
            "clean_core_impact": "None; BTP integration for predictive maintenance is side-by-side"
          },
          {
            "gap_description": "Calibration management for test equipment (vibration tables, thermal vacuum chambers, antenna test ranges) requires tracking of calibration due dates, calibration certificates, and out-of-calibration impact assessment on product quality; standard PM does not include dedicated calibration management",
            "gap_severity": "High",
            "resolution_approach": "Implement calibration management using PM measurement points and measuring documents. Configure calibration scheduling as time-based maintenance plans linked to test equipment. Track calibration certificates as PM documents. Evaluate SAP Environment, Health, and Safety (EHS) calibration management as an alternative. Standard PM with enhanced master data.",
            "estimated_effort": "4 to 6 weeks configuration",
            "clean_core_impact": "Low; standard PM configuration with additional master data for calibration tracking"
          }
        ],
        "clean_core_assessment": {
          "level": "A",
          "standard_process_adoption_rate": "85%",
          "extensions_needed": [
            {
              "extension_description": "IoT-based predictive maintenance for manufacturing equipment via BTP",
              "extension_type": "BTP Side-by-Side",
              "clean_core_impact": "None",
              "justification": "Predictive maintenance using sensor data from manufacturing equipment is a Phase 2/3 initiative. BTP IoT services provide the data collection and ML inference layer; PM provides the maintenance execution layer."
            }
          ],
          "modifications_flagged": []
        }
      },

      {
        "module_code": "PS",
        "module_name": "Project System",
        "relevance": "CRITICAL",
        "fit_score": 2.5,
        "fit_rating": "Weak Fit with Earned Value and Program Management Gaps",
        "business_driver": "Satellite program management via WBS structures, earned value management (replacing Excel-based EVM), milestone tracking for customer billing, program-level cost collection and reporting, and integration with Anaplan for program financial planning",
        "key_scope_items": [
          { "scope_item_id": "J56", "name": "Project Planning and WBS", "fit": 3, "notes": "WBS structures for satellite programs: program level, satellite unit level, and work package level (design, manufacturing, integration and test, launch, in-orbit checkout). Standard WBS with multi-level hierarchy. Requires template WBS for each contract type." },
          { "scope_item_id": "J57", "name": "Project Budgeting and Cost Control", "fit": 3, "notes": "Budget allocation to WBS elements with availability control. Actual cost collection from CO (production orders, purchase orders, internal activity allocation). Standard PS budgeting with CO integration." },
          { "scope_item_id": "PS-MILE", "name": "Milestone Tracking", "fit": 3, "notes": "Project milestones linked to customer billing (SD milestone billing plan) and internal program reviews (PDR, CDR, TRR, FRR). Standard milestone functionality with SD integration." },
          { "scope_item_id": "PS-EVM", "name": "Earned Value Analysis", "fit": 2, "notes": "CRITICAL GAP: EVM is currently performed entirely in Excel. S/4HANA PS provides basic earned value analysis but may not satisfy DCAA EVMS (ANSI/EIA-748) requirements for government contracts. Requires detailed evaluation of PS-EVM capabilities vs. EVMS standard compliance." }
        ],
        "gaps_identified": [
          {
            "gap_description": "Earned value management is performed in Excel outside SAP; no integration between PS cost actuals, schedule data, and EVM calculations; DCAA EVMS compliance (ANSI/EIA-748) is a potential requirement for government contracts",
            "gap_severity": "Critical",
            "resolution_approach": "Phase 1: Implement S/4HANA PS earned value analysis using standard measurement techniques (cost-based, effort-based, milestone-based). Integrate with CO for actual cost and with PS scheduling for schedule performance. Phase 2: If DCAA EVMS compliance requires features beyond PS-EVM (e.g., integrated baseline reviews, variance analysis thresholds, corrective action tracking), evaluate BTP integration with a dedicated EVMS tool (e.g., Deltek Cobra, Empower) and use SAP PS as the cost collection engine.",
            "estimated_effort": "Phase 1: 6 to 8 weeks; Phase 2: 8 to 12 weeks if external EVMS integration is needed",
            "clean_core_impact": "None for Phase 1 (standard PS-EVM); Medium for Phase 2 if BTP integration with external EVMS tool is required"
          },
          {
            "gap_description": "Anaplan is the current planning tool for program financial forecasting; no integration exists between Anaplan planning data and SAP PS budget/actual data",
            "gap_severity": "High",
            "resolution_approach": "Implement BTP Integration Suite iFlow for Anaplan-to-SAP PS bidirectional data exchange. Outbound: PS budget and actual cost data to Anaplan for forecast modeling. Inbound: Anaplan approved budgets to PS WBS budget allocation. Evaluate whether Anaplan can be replaced by SAP Analytics Cloud (SAC) planning in a future phase to consolidate the planning landscape.",
            "estimated_effort": "4 to 6 weeks BTP integration development",
            "clean_core_impact": "None; BTP side-by-side integration"
          },
          {
            "gap_description": "WBS structures for satellite programs need template-based creation for repeatable program types (constellation satellite, custom satellite, launch services); no WBS templates currently exist in SAP PS",
            "gap_severity": "Medium",
            "resolution_approach": "Create standard WBS templates for each program type. Include standard milestones, cost element groups, and settlement rules. Configure project builder for template-based project creation. Standard PS functionality.",
            "estimated_effort": "3 to 4 weeks template design and configuration",
            "clean_core_impact": "None; standard PS template functionality"
          }
        ],
        "clean_core_assessment": {
          "level": "B",
          "standard_process_adoption_rate": "65%",
          "extensions_needed": [
            {
              "extension_description": "Anaplan bidirectional integration for program financial planning",
              "extension_type": "BTP Side-by-Side",
              "clean_core_impact": "None",
              "justification": "Anaplan is the retained planning tool. BTP integration keeps PS core clean while enabling data exchange."
            },
            {
              "extension_description": "EVMS-compliant earned value dashboard (if DCAA EVMS compliance is required)",
              "extension_type": "BTP Side-by-Side",
              "clean_core_impact": "Medium",
              "justification": "If standard PS-EVM does not satisfy ANSI/EIA-748, a BTP-hosted dashboard aggregating PS actuals, schedule data, and EVM calculations provides compliance without modifying PS core."
            }
          ],
          "modifications_flagged": []
        }
      },

      {
        "module_code": "GTS",
        "module_name": "Global Trade Services",
        "relevance": "CRITICAL",
        "fit_score": 2.0,
        "fit_rating": "Weak Fit with Major Compliance Gaps -- Full Implementation Required",
        "business_driver": "ITAR/EAR export control compliance is NON-NEGOTIABLE. Satellites are ITAR-controlled defense articles under USML Category XV. Full GTS implementation replaces the current fragmented combination of partial GTS, manual processes, and a separate access control database. This is the single highest-compliance-risk module in the program.",
        "key_scope_items": [
          { "scope_item_id": "GTS-SPL", "name": "Sanctioned Party List Screening", "fit": 3, "notes": "Denied party screening against US government lists (SDN, Entity List, Unverified List, Denied Persons List, Debarred List). Standard GTS screening engine with list update subscription. Current partial implementation covers some screening; must be extended to all transaction types." },
          { "scope_item_id": "GTS-LIC", "name": "License Management", "fit": 2, "notes": "CRITICAL GAP: ITAR license management (DSP-5, DSP-73, TAA, MLA) requires tracking of license conditions, quantities consumed, expiration dates, and provisos. Current license tracking is partially manual with spreadsheet supplements. Full GTS license management activation required." },
          { "scope_item_id": "GTS-CLASS", "name": "Product Classification", "fit": 2, "notes": "CRITICAL GAP: ITAR/EAR classification at the material master level (USML Category, ECCN, jurisdiction determination) must be maintained for all controlled items, technical data, and software. Current classification is fragmented across multiple systems." },
          { "scope_item_id": "GTS-COMP", "name": "Compliance Management", "fit": 2, "notes": "Automated compliance determination before any export, re-export, or deemed export transaction. Integration with SD (delivery), MM (procurement of controlled items), and PS (technology access). Currently manual or partially automated." }
        ],
        "gaps_identified": [
          {
            "gap_description": "ITAR/EAR classification management is fragmented across partial GTS implementation, manual processes, and a separate access control database; no single system of record for export control classification of materials, technical data, and software",
            "gap_severity": "Critical",
            "resolution_approach": "Full GTS activation with: (a) USML/CCL classification maintained in GTS product classification at material master level, (b) jurisdiction determination rules (ITAR vs. EAR) configured in GTS, (c) classification inheritance for BOMs (controlled components make the assembly controlled), (d) document-level ITAR classification for technical data packages. Migrate all existing classifications from the separate access control database into GTS.",
            "estimated_effort": "10 to 14 weeks design, data migration, configuration, and testing",
            "clean_core_impact": "None; GTS is standard SAP functionality"
          },
          {
            "gap_description": "License management for ITAR licenses (DSP-5, DSP-73, TAA, MLA) is partially manual with spreadsheet tracking; license utilization, expiration tracking, and proviso compliance are not automated",
            "gap_severity": "Critical",
            "resolution_approach": "Configure GTS license management for all ITAR license types. Implement license determination rules that automatically identify required licenses based on: destination country, end-use, end-user, and product classification. Track license utilization (quantity and value consumed) against license limits. Automated expiration alerts and renewal workflows.",
            "estimated_effort": "6 to 8 weeks configuration and data migration",
            "clean_core_impact": "None; standard GTS license management"
          },
          {
            "gap_description": "Deemed export controls (access by foreign persons to ITAR-controlled technical data within the US) are not enforced within SAP; current enforcement relies on a separate access control database",
            "gap_severity": "Critical",
            "resolution_approach": "Implement deemed export controls via: (a) SAP authorization concept integration with GTS (restrict access to ITAR-classified materials, BOMs, documents, and transactions based on citizenship/residency attributes in user master), (b) technology control plan (TCP) enforcement within SAP for classified programs, (c) audit trail for all access to ITAR-controlled data within SAP. This requires coordination between GTS, security/authorization, and the CISO office.",
            "estimated_effort": "8 to 12 weeks (cross-functional: GTS, Security, Basis, BTP)",
            "clean_core_impact": "Medium; deemed export access controls may require authorization enhancements beyond standard SAP roles. Implement via BTP-based access governance where possible to keep core authorization model standard."
          },
          {
            "gap_description": "Technology transfer controls for satellite technical data shared with launch service providers, component suppliers, or international partners are not enforced systematically within SAP",
            "gap_severity": "High",
            "resolution_approach": "Configure GTS compliance checks triggered by: (a) SD delivery to foreign consignees, (b) MM purchase orders with foreign suppliers that include technical data, (c) PS project access for international team members. Implement technology control plans as GTS compliance documents linked to satellite programs.",
            "estimated_effort": "4 to 6 weeks configuration",
            "clean_core_impact": "None; standard GTS compliance integration"
          }
        ],
        "clean_core_assessment": {
          "level": "B",
          "standard_process_adoption_rate": "55%",
          "extensions_needed": [
            {
              "extension_description": "ITAR access governance integration linking GTS classification to SAP authorization model",
              "extension_type": "BTP Side-by-Side",
              "clean_core_impact": "Medium",
              "justification": "Standard SAP authorization does not natively enforce ITAR-based access restrictions tied to material classification. BTP-based access governance service provides the bridge between GTS classification and authorization without modifying core security."
            },
            {
              "extension_description": "ITAR compliance audit trail and reporting dashboard",
              "extension_type": "BTP Side-by-Side",
              "clean_core_impact": "None",
              "justification": "DDTC audit reporting and ITAR compliance dashboards require aggregation of GTS screening results, license utilization, deemed export access logs, and technology transfer records. BTP/SAC-based reporting provides the consolidated view."
            }
          ],
          "modifications_flagged": [
            {
              "modification_description": "Deemed export access control enforcement within SAP authorization model",
              "reason": "Standard SAP authorization roles do not include citizenship or residency-based access restrictions required for ITAR deemed export compliance",
              "clean_core_violation": true,
              "recommended_alternative": "Implement via SAP Cloud Identity Access Governance (IAG) on BTP or via a custom BTP microservice that evaluates ITAR access eligibility before granting transaction access. Keep the core SAP authorization model standard and enforce ITAR restrictions at the governance layer."
            }
          ]
        }
      },

      {
        "module_code": "BTP",
        "module_name": "Business Technology Platform",
        "relevance": "CRITICAL",
        "fit_score": "N/A",
        "fit_rating": "Infrastructure Platform -- Required for Clean Core Strategy and Integration Modernization",
        "business_driver": "BTP is the foundational infrastructure platform for: (1) PLM integration with Teamcenter, (2) MES integration with Apriso, (3) CRM integration with Salesforce, (4) HCM integration with Workday, (5) planning integration with Anaplan, (6) middleware consolidation replacing 12 custom interfaces, (7) hosting retained custom extensions per Clean Core strategy, and (8) ITAR access governance services",
        "key_scope_items": [
          { "scope_item_id": "BTP-IS", "name": "Integration Suite", "fit": 4, "notes": "Primary integration middleware replacing 12 custom interfaces. Pre-built integration content available for Salesforce, Workday, and Teamcenter. Custom iFlows needed for Apriso MES and Anaplan." },
          { "scope_item_id": "BTP-BUILD", "name": "SAP Build (Apps, Process Automation, Work Zone)", "fit": 3, "notes": "Key User extensibility for custom reports, dashboards, and lightweight apps. SAP Build Process Automation for workflow automation (approval processes, compliance workflows). SAP Build Work Zone for unified launchpad." },
          { "scope_item_id": "BTP-ABAP", "name": "ABAP Environment (Steampunk)", "fit": 3, "notes": "Target runtime for retained custom ABAP extensions that cannot be replaced by standard S/4HANA functionality and cannot be implemented as Key User extensions. Estimated 10 to 15% of the 2,400 custom objects may require migration to BTP ABAP Environment." },
          { "scope_item_id": "BTP-AI", "name": "SAP AI Core / AI Foundation", "fit": 2, "notes": "Phase 2/3: AI/ML capabilities for predictive quality, predictive maintenance, and demand sensing. Requires data foundation and model training. Not Phase 1 scope." }
        ],
        "gaps_identified": [
          {
            "gap_description": "12 custom middleware interfaces must be modernized; current integration technology stack is unspecified and likely heterogeneous",
            "gap_severity": "High",
            "resolution_approach": "Inventory all 12 interfaces during the Explore phase. Classify each interface by: source/target system, data objects, frequency, volume, and current technology. Design target integration architecture on BTP Integration Suite. Prioritize: (a) Teamcenter PLM (critical path for PP), (b) Apriso MES (critical path for manufacturing visibility), (c) Salesforce CRM (high value for SD), (d) Workday HCM (medium, cost center/employee sync), (e) Anaplan (medium, CO/PS actuals). Sequence middleware modernization across waves aligned with module go-live.",
            "estimated_effort": "4 to 6 weeks architecture and inventory; 6 to 8 weeks per integration (staggered across waves)",
            "clean_core_impact": "None; BTP Integration Suite is the Clean Core-compliant integration platform"
          },
          {
            "gap_description": "Custom code migration: approximately 240 to 360 ABAP objects (10 to 15% of 2,400) are expected to require migration to BTP ABAP Environment after the retire/adapt/retain classification",
            "gap_severity": "Medium",
            "resolution_approach": "Run SAP Custom Code Migration Worklist and ABAP Test Cockpit (ATC) against all 2,400 objects. Classify into: (a) retire (standard S/4HANA replaces), (b) adapt (simplification adjustments for S/4HANA compatibility), (c) retain on-stack (business-critical, no standard equivalent, compatible with S/4HANA), (d) move to BTP (side-by-side extension on BTP ABAP Environment). Target: 60% retire, 15 to 20% adapt, 10 to 15% retain on-stack, 10 to 15% move to BTP.",
            "estimated_effort": "6 to 8 weeks analysis; 12 to 16 weeks remediation and migration (phased across waves)",
            "clean_core_impact": "High positive impact; this is the primary Clean Core remediation workstream"
          }
        ],
        "clean_core_assessment": {
          "level": "B",
          "standard_process_adoption_rate": "N/A (platform)",
          "extensions_needed": [
            {
              "extension_description": "BTP Integration Suite iFlows for Teamcenter, Apriso, Salesforce, Workday, and Anaplan",
              "extension_type": "BTP Side-by-Side",
              "clean_core_impact": "None",
              "justification": "Integration middleware is the standard BTP use case. Each integration follows SAP-recommended patterns for third-party connectivity."
            },
            {
              "extension_description": "BTP ABAP Environment for retained custom extensions",
              "extension_type": "BTP Side-by-Side",
              "clean_core_impact": "None",
              "justification": "Custom ABAP extensions that cannot be retired or adapted are migrated to BTP ABAP Environment, keeping the S/4HANA core clean."
            }
          ],
          "modifications_flagged": []
        }
      }
    ],

    "integration_map": {
      "cross_module_dependencies": [
        {
          "from_module": "PP",
          "to_module": "MM",
          "integration_type": "Automatic MRP and Component Procurement",
          "description": "MRP in PP generates purchase requisitions in MM for satellite components based on BOM explosion and production schedule. Component availability check in production order triggers procurement.",
          "criticality": "Mandatory",
          "configuration_notes": "MRP planning file, procurement type in material master, source determination for space-grade components."
        },
        {
          "from_module": "PP",
          "to_module": "CO",
          "integration_type": "Production Order Cost Collection",
          "description": "Production order confirmations post actual costs to CO. Activity confirmations allocate clean room hours, test hours, and labor costs. Settlement to PS WBS elements for program-level cost aggregation.",
          "criticality": "Mandatory",
          "configuration_notes": "Activity types for manufacturing work centers. Settlement rules for production order to WBS. Cost element mapping."
        },
        {
          "from_module": "PP",
          "to_module": "QM",
          "integration_type": "In-Process Inspection Trigger",
          "description": "Production order operations trigger inspection lots at defined manufacturing milestones. Inspection results determine production step approval or NCR generation.",
          "criticality": "Mandatory",
          "configuration_notes": "Inspection type 03 (in-process). Inspection plan linked to routing operations. Results recording integration."
        },
        {
          "from_module": "PS",
          "to_module": "CO",
          "integration_type": "Program Cost Collection and EVM",
          "description": "PS WBS elements collect costs from production orders (PP-CO settlement), purchase orders (MM), internal activity allocation, and overhead. EVM calculations use PS budget and actual data.",
          "criticality": "Mandatory",
          "configuration_notes": "WBS element as cost object. Budget profile and availability control. EVM measurement techniques."
        },
        {
          "from_module": "PS",
          "to_module": "SD",
          "integration_type": "Milestone Billing",
          "description": "PS milestones trigger SD billing. Milestone completion in PS releases billing request in SD. Billing plan in SD is linked to PS WBS milestones.",
          "criticality": "Mandatory",
          "configuration_notes": "Milestone billing plan in SD linked to PS milestone. Billing type for milestone invoicing."
        },
        {
          "from_module": "SD",
          "to_module": "FI",
          "integration_type": "Automatic Posting",
          "description": "Milestone billing documents create FI-AR postings (customer receivables, revenue). Revenue flows to RAR for IFRS 15/ASC 606 recognition treatment.",
          "criticality": "Mandatory",
          "configuration_notes": "Revenue account determination. RAR contract assignment. Currency conversion for foreign-currency contracts."
        },
        {
          "from_module": "MM",
          "to_module": "FI",
          "integration_type": "Automatic Posting",
          "description": "Goods receipt and invoice verification trigger FI postings (GR/IR clearing, vendor liability, inventory valuation). Three-way match for all procurement.",
          "criticality": "Mandatory",
          "configuration_notes": "Automatic account determination. Material ledger activated for actual costing."
        },
        {
          "from_module": "MM",
          "to_module": "QM",
          "integration_type": "Incoming Inspection",
          "description": "Goods receipt of space-grade components triggers automatic incoming inspection lot. Inspection results determine stock posting (unrestricted, blocked, quality).",
          "criticality": "Mandatory",
          "configuration_notes": "QM inspection type 01 (goods receipt). Source inspection for critical suppliers. Certificate check at goods receipt."
        },
        {
          "from_module": "GTS",
          "to_module": "SD",
          "integration_type": "Compliance Check at Delivery",
          "description": "GTS compliance check triggered before delivery release. Sanctioned party screening, license determination, and classification verification. Delivery blocked if compliance check fails.",
          "criticality": "Mandatory",
          "configuration_notes": "GTS integration with SD delivery. Compliance check trigger at delivery creation. Block/release workflow."
        },
        {
          "from_module": "GTS",
          "to_module": "MM",
          "integration_type": "Procurement Compliance",
          "description": "GTS compliance check for procurement of controlled items. Supplier screening against denied party lists. End-use/end-user verification for dual-use items.",
          "criticality": "Mandatory",
          "configuration_notes": "GTS integration with MM purchase order. Supplier screening at PO creation."
        },
        {
          "from_module": "PM",
          "to_module": "MM",
          "integration_type": "Spare Parts Procurement",
          "description": "Maintenance orders generate material reservations for spare parts. If parts not in stock, purchase requisitions created in MM.",
          "criticality": "High",
          "configuration_notes": "Component planning in maintenance orders. MM integration for reservation and procurement."
        }
      ],
      "non_sap_interfaces": [
        {
          "external_system": "Siemens Teamcenter (PLM)",
          "interface_type": "Real-time API (via BTP Integration Suite or SAP ECTR)",
          "direction": "Bidirectional",
          "data_objects": ["Engineering BOM release to SAP manufacturing BOM", "Engineering change orders", "Document management (drawings, specifications)", "As-built configuration feedback"],
          "integration_technology": "BTP Integration Suite or SAP Engineering Control Center (ECTR)",
          "complexity": "High",
          "clean_core_compliant": true
        },
        {
          "external_system": "Apriso MES (Dassault Systemes)",
          "interface_type": "Real-time API (via BTP Integration Suite)",
          "direction": "Bidirectional",
          "data_objects": ["Production order dispatch to MES", "Production confirmation from MES", "Material consumption/backflush", "Serialized component installation (as-built)", "Quality inspection results"],
          "integration_technology": "BTP Integration Suite",
          "complexity": "High",
          "clean_core_compliant": true
        },
        {
          "external_system": "Salesforce (CRM)",
          "interface_type": "Real-time API (via BTP Integration Suite)",
          "direction": "Bidirectional",
          "data_objects": ["Opportunity to sales order", "Customer master data sync", "Billing milestone status", "Contract amendments"],
          "integration_technology": "BTP Integration Suite (pre-built content available)",
          "complexity": "Medium",
          "clean_core_compliant": true
        },
        {
          "external_system": "Workday (HCM)",
          "interface_type": "Batch API (via BTP Integration Suite)",
          "direction": "Bidirectional",
          "data_objects": ["Cost center/employee master sync (Workday to SAP)", "Time entry data for PS project costing", "Organizational structure sync"],
          "integration_technology": "BTP Integration Suite (pre-built content available)",
          "complexity": "Medium",
          "clean_core_compliant": true
        },
        {
          "external_system": "Anaplan (Planning)",
          "interface_type": "Batch API (via BTP Integration Suite)",
          "direction": "Bidirectional",
          "data_objects": ["CO/PS actual cost data to Anaplan", "Approved budgets from Anaplan to PS", "Forecast data exchange"],
          "integration_technology": "BTP Integration Suite",
          "complexity": "Medium",
          "clean_core_compliant": true
        }
      ],
      "data_flow_diagram_description": "The primary data flow for CSS follows the satellite program lifecycle. Opportunities originate in Salesforce and flow to SD as sales orders with milestone billing plans. PS WBS structures govern program cost collection and EVM. PP receives manufacturing BOMs from Teamcenter PLM and dispatches production orders to Apriso MES. MES confirmations flow back through BTP to PP (production status), QM (inspection results), and CO (actual costs). MM procures components via MRP-driven requisitions with GTS compliance screening on all export-controlled items. PS milestones trigger SD billing, which posts to FI-AR and RAR for revenue recognition. CO aggregates program costs from PP (production), MM (materials), and internal allocations for program profitability analysis. FI consolidation data feeds to the parent company. GTS enforces compliance checks across SD (deliveries), MM (procurement), and PS (technology access) for all ITAR-controlled transactions."
    },

    "clean_core_assessment": {
      "overall_assessment": "D",
      "overall_assessment_label": "Legacy Extensions (Current State)",
      "rationale": "CSS currently operates at Clean Core Level D with 2,400 custom ABAP objects, 47 custom transactions, 3 skipped enhancement packs, and fragmented manual workarounds across multiple modules. The transformation target is Level B (Clean Core with Extensions) within 18 months post go-live. Achieving this requires: (a) retiring approximately 60% of custom objects through standard S/4HANA functionality adoption, (b) adapting 15 to 20% for S/4HANA compatibility, (c) retaining 10 to 15% on-stack where no standard equivalent exists, and (d) migrating 10 to 15% to BTP ABAP Environment as side-by-side extensions. The primary risk to achieving Level B is the PP module, where complex BOM lifecycle management and PLM integration may require custom logic that pushes PP toward Level C. GTS deemed export access governance is the other area where Clean Core compliance requires careful architectural decisions.",
      "target_assessment": "B",
      "target_assessment_label": "Clean Core with Extensions (Target: 18 Months Post Go-Live)",
      "per_module_assessment": [
        { "module_code": "FI", "clean_core_level": "B", "rationale": "Standard S/4HANA financial accounting with RAR activation. DCAA reporting requires Key User extensions." },
        { "module_code": "CO", "clean_core_level": "B", "rationale": "Standard CO-PA and product costing with Anaplan integration via BTP." },
        { "module_code": "MM", "clean_core_level": "B", "rationale": "Standard procurement and inventory with supplier collaboration extension on BTP." },
        { "module_code": "SD", "clean_core_level": "A", "rationale": "Standard sales and billing with Salesforce integration via BTP." },
        { "module_code": "PP", "clean_core_level": "C", "rationale": "Complex BOM lifecycle and PLM/MES integrations push PP toward Level C. BTP-based integration is compliant, but BOM comparison logic may require custom development." },
        { "module_code": "QM", "clean_core_level": "A", "rationale": "Standard QM configuration for AS9100D. Predictive analytics via BTP/SAC is fully side-by-side." },
        { "module_code": "PM", "clean_core_level": "A", "rationale": "Standard preventive and corrective maintenance. IoT predictive maintenance via BTP is Phase 2/3." },
        { "module_code": "PS", "clean_core_level": "B", "rationale": "Standard PS with EVM. Anaplan and potential external EVMS integration via BTP." },
        { "module_code": "GTS", "clean_core_level": "B", "rationale": "Standard GTS compliance with BTP-based ITAR access governance extension." },
        { "module_code": "BTP", "clean_core_level": "B", "rationale": "Platform hosting integrations and retained extensions. Clean Core by design." }
      ],
      "btp_extension_summary": {
        "total_extensions_recommended": 12,
        "extension_categories": [
          "Integration (Teamcenter PLM, Apriso MES, Salesforce CRM, Workday HCM, Anaplan Planning)",
          "Custom Code Migration (BTP ABAP Environment for retained ABAP objects)",
          "Access Governance (ITAR deemed export access control)",
          "Analytics (Predictive quality, predictive maintenance, ITAR compliance dashboard)",
          "Reporting (DCAA-compliant cost accounting reports)"
        ],
        "estimated_btp_services": [
          "BTP Integration Suite (primary integration middleware)",
          "BTP ABAP Environment (retained custom extensions)",
          "SAP Build Apps (Key User extensibility)",
          "SAP Build Process Automation (approval and compliance workflows)",
          "SAP Build Work Zone (unified Fiori launchpad)",
          "SAP Analytics Cloud (program dashboards, predictive analytics)",
          "SAP Cloud Identity Access Governance (ITAR access control)"
        ],
        "btp_licensing_impact": "BTP consumption is a significant cost component given the integration-heavy architecture (5 major external system integrations plus middleware consolidation for 12 custom interfaces). Estimate BTP licensing at 20 to 30% of the S/4HANA Cloud Private Edition subscription. Recommend BTP Enterprise Agreement for predictable annual cost. The parent company's existing BTP entitlements (if any) should be evaluated for shared licensing opportunities."
      }
    },

    "cross_module_design_considerations": {
      "organizational_structure": {
        "company_codes": { "count": 1, "rationale": "Single CSS legal entity (confirm intercompany structure with parent conglomerate; if CSS has multiple legal entities, additional company codes are required)" },
        "controlling_areas": { "count": 1, "rationale": "Single controlling area for CSS covering all three sites. Operating concern designed for program-level profitability analysis." },
        "plants": { "count": 3, "rationale": "Redmond WA (satellite manufacturing primary), Huntsville AL (manufacturing), Cape Canaveral FL (launch operations). Three plants enable site-specific production planning, inventory management, and cost collection." },
        "storage_locations": { "count": "8 to 12", "rationale": "Multiple storage locations per plant for component stores, clean room staging, integration areas, shipping/receiving, and quality hold areas." },
        "sales_organizations": { "count": 1, "rationale": "Single sales organization for all satellite, launch, and service sales." },
        "distribution_channels": { "count": 2, "rationale": "Government/defense contracts (channel 10) and commercial contracts (channel 20) to support different pricing, billing, and compliance requirements." },
        "purchasing_organizations": { "count": 1, "rationale": "Centralized purchasing organization with site-level purchasing groups for local procurement." },
        "design_notes": "The three-plant structure is critical for accurate production planning and cost collection across geographically dispersed manufacturing. Redmond is the primary satellite assembly site; Huntsville performs subassembly manufacturing; Cape Canaveral handles final integration, test, and launch preparation. Inter-plant stock transfers are expected for subassemblies moving from Huntsville to Redmond or Cape Canaveral."
      },
      "master_data_harmonization": [
        {
          "master_data_object": "Material Master",
          "current_state": "Material masters exist in ECC but are not aligned with Teamcenter part numbering; dual numbering systems create reconciliation overhead",
          "harmonization_effort": "High",
          "key_decisions": [
            "Adopt Teamcenter part number as SAP material number (recommended) or maintain cross-reference table",
            "Define material type strategy for satellite assemblies, subassemblies, raw materials, and services",
            "Establish serialization profile for all satellite-level and critical-component-level items"
          ],
          "cross_module_impact": ["PP", "MM", "QM", "CO", "GTS"]
        },
        {
          "master_data_object": "Business Partner (Customer and Vendor)",
          "current_state": "Customer and vendor masters in ECC; migration to S/4HANA Business Partner model required",
          "harmonization_effort": "Medium",
          "key_decisions": [
            "Business partner migration strategy (conversion from KNA1/LFA1 to BUT000)",
            "GTS partner screening profile for all customers and vendors",
            "Salesforce customer record alignment with SAP Business Partner"
          ],
          "cross_module_impact": ["SD", "MM", "FI", "GTS"]
        },
        {
          "master_data_object": "BOM (Bill of Materials)",
          "current_state": "Engineering BOMs in Teamcenter; manufacturing BOMs in SAP PP; as-built tracked manually; no single source of truth",
          "harmonization_effort": "High",
          "key_decisions": [
            "Define BOM lifecycle governance: Teamcenter as engineering BOM authority, SAP PP as manufacturing BOM authority",
            "Establish BOM release and change management workflow between Teamcenter and SAP",
            "Define as-built BOM capture process in SAP PP via serialized production order confirmations"
          ],
          "cross_module_impact": ["PP", "CO", "QM", "GTS"]
        },
        {
          "master_data_object": "WBS and Project Templates",
          "current_state": "WBS structures in ECC PS; EVM data in Excel; no standardized project templates",
          "harmonization_effort": "Medium",
          "key_decisions": [
            "Define standard WBS templates by program type (constellation, custom, launch services)",
            "Establish cost element group structure for DCAA-compliant cost reporting",
            "Define EVM measurement technique per WBS level"
          ],
          "cross_module_impact": ["PS", "CO", "SD", "FI"]
        }
      ],
      "number_range_management": {
        "strategy": "Mixed (internal for most objects; external for material numbers if adopting Teamcenter part numbers)",
        "key_objects": ["Material number", "Sales order", "Production order", "WBS element", "Purchase order", "Maintenance order", "GTS compliance document"],
        "notes": "If Teamcenter part numbers are adopted as SAP material numbers, external number ranges are required. All other objects use SAP internal numbering. Number range harmonization is a prerequisite for system conversion."
      },
      "authorization_concept": {
        "complexity": "Complex",
        "key_considerations": [
          "ITAR-based access restrictions require citizenship/residency-aware authorization (deemed export compliance)",
          "Multi-site authorization: users may have access to their site only or cross-site access depending on role",
          "GTS compliance roles: restricted access to export-controlled data, license information, and classification data",
          "Program-level access controls: satellite program data may be restricted by customer contract (e.g., government classified programs)",
          "Segregation of duties for SOX compliance (financial controls)",
          "Parent company audit access requirements"
        ],
        "role_count_estimate": 60
      }
    },

    "sap_toolchain_integration": {
      "signavio_recommendations": [
        {
          "use_case": "Current-state process mining on ECC production system to baseline existing processes before conversion. Priority domains: financial close, BOM change management, procurement for long-lead components, ITAR compliance workflows.",
          "timing": "Pre-implementation (Discover/Prepare phase)",
          "modules_affected": ["FI", "CO", "PP", "MM", "GTS"],
          "value_proposition": "Signavio Process Intelligence provides data-driven process baselines from ECC transaction logs. Quantifies actual close cycle steps, BOM change lead times, and procurement cycle times. Benchmarks against SAP Best Practices for Aerospace and Defense."
        },
        {
          "use_case": "Target-state process design using SAP Best Practices for A&D as reference models. Fit-to-Standard workshops use Signavio process diagrams to identify gaps between standard processes and CSS requirements.",
          "timing": "During Explore phase",
          "modules_affected": ["ALL"],
          "value_proposition": "Reduces Fit-to-Standard workshop effort by 30 to 40% through pre-built process reference models. Accelerates gap identification and design decision documentation."
        },
        {
          "use_case": "Post-go-live process compliance monitoring. Verify that actual S/4HANA process execution matches designed target-state processes.",
          "timing": "Post Go-Live",
          "modules_affected": ["ALL"],
          "value_proposition": "Continuous process monitoring identifies process deviations, workarounds, and automation opportunities after go-live."
        }
      ],
      "leanix_recommendations": [
        {
          "use_case": "Application portfolio rationalization and integration architecture target-state design. Map all current applications (SAP ECC, Teamcenter, Apriso, Salesforce, Workday, Anaplan, 12 custom middleware interfaces) and define the S/4HANA plus BTP target architecture.",
          "timing": "Pre-implementation (Discover/Prepare phase)",
          "value_proposition": "LeanIX provides the architectural blueprint for integration modernization. Identifies redundant applications, consolidation opportunities (e.g., Anaplan vs. IBP evaluation), and the middleware migration roadmap."
        },
        {
          "use_case": "Ongoing enterprise architecture governance post-transformation. Maintain visibility into the CSS application landscape as it evolves.",
          "timing": "Post Go-Live",
          "value_proposition": "Parent company mandate requires LeanIX adoption. Ensures architectural decisions are documented and governed at the enterprise level."
        }
      ],
      "cloud_alm_setup": {
        "requirements_to_track": 85,
        "solution_processes_to_configure": [
          "Record-to-Report (FI/CO) including 5-day close and RAR",
          "Source-to-Pay (MM/FI/GTS) including long-lead procurement and compliance screening",
          "Plan-to-Fulfill (PP/MM/QM) including BOM lifecycle and MES integration",
          "Order-to-Cash (SD/FI/PS) including milestone billing and revenue recognition",
          "Project-to-Profit (PS/CO) including EVM and program profitability",
          "Maintain-to-Operate (PM) including calibration management",
          "Export Compliance (GTS) including ITAR/EAR full lifecycle"
        ],
        "test_scope_implications": "End-to-end integration testing is critical given the cross-module and cross-system dependencies. Test scenarios must trace the full satellite program lifecycle: sales order creation (SD/Salesforce), project initiation (PS), BOM release (Teamcenter/PP), production execution (PP/MES/QM), milestone billing (PS/SD/FI), revenue recognition (RAR), and export compliance (GTS). Estimate 200+ end-to-end test cases across 3 waves. Cloud ALM Test Management provides traceability from requirements to test cases to defects.",
        "deployment_tracking_needs": "Multi-wave deployment across 18 to 24 months. Cloud ALM Deployment Management for transport tracking, wave-specific go-live readiness assessments, and cutover planning. Each wave requires a separate cutover runbook: Wave 1 (finance, GTS), Wave 2 (manufacturing, supply chain, project systems), Wave 3 (advanced analytics, predictive capabilities)."
      }
    },

    "risk_assessment": {
      "overall_risk_level": "High",
      "per_module_risks": [
        {
          "module_code": "PP",
          "risk_level": "High",
          "risks": [
            {
              "risk_description": "Teamcenter PLM integration for bidirectional BOM lifecycle management is the most technically complex integration in the program. Failure or delay in this integration directly impacts manufacturing operations during the 3x production ramp.",
              "risk_category": "Integration",
              "likelihood": "High",
              "impact": "High",
              "mitigation": "Begin PLM integration design in the Prepare phase (before Explore). Engage Siemens Teamcenter integration specialists and SAP ECTR expertise. Prototype the BOM release and engineering change flow early. Define a fallback BOM management process if integration is delayed."
            },
            {
              "risk_description": "MES (Apriso) real-time integration replacement of the current 4-hour batch interface involves significant technical risk and must not disrupt manufacturing operations during the production ramp.",
              "risk_category": "Integration",
              "likelihood": "Medium",
              "impact": "High",
              "mitigation": "Implement MES integration in parallel with the existing batch interface. Run both interfaces simultaneously during a transition period. Validate data consistency between real-time and batch feeds before decommissioning the batch interface."
            }
          ]
        },
        {
          "module_code": "GTS",
          "risk_level": "High",
          "risks": [
            {
              "risk_description": "ITAR compliance gaps during the transition from partial GTS plus manual processes to full GTS implementation. Any compliance failure during the transition period could result in regulatory action, contract default, or criminal liability.",
              "risk_category": "Compliance",
              "likelihood": "Medium",
              "impact": "Critical",
              "mitigation": "Maintain all existing manual ITAR controls in parallel with GTS implementation until full GTS validation is complete. Engage DDTC-registered compliance counsel during GTS design. Conduct a pre-go-live ITAR compliance audit. GTS must be in Wave 1 to minimize the duration of the transition period."
            },
            {
              "risk_description": "Deemed export access control implementation within SAP is architecturally complex and touches security, authorization, GTS, and BTP layers.",
              "risk_category": "Technical",
              "likelihood": "High",
              "impact": "High",
              "mitigation": "Engage SAP security and GTS specialists with ITAR experience. Design the deemed export access model during the Explore phase with CISO involvement. Validate with a proof of concept before committing to the architectural approach (SAP IAG vs. custom BTP microservice)."
            }
          ]
        },
        {
          "module_code": "PS",
          "risk_level": "Medium",
          "risks": [
            {
              "risk_description": "S/4HANA PS earned value analysis may not fully satisfy DCAA EVMS (ANSI/EIA-748) requirements, potentially requiring an additional external EVMS tool integration.",
              "risk_category": "Functional",
              "likelihood": "Medium",
              "impact": "Medium",
              "mitigation": "Conduct an EVMS requirements gap analysis during the Explore phase comparing S/4HANA PS-EVM capabilities to ANSI/EIA-748 requirements. If gaps are identified, evaluate external EVMS tool integration options before Wave 2 design freeze."
            }
          ]
        },
        {
          "module_code": "FI",
          "risk_level": "Medium",
          "risks": [
            {
              "risk_description": "RAR (Revenue Accounting and Reporting) activation requires migration of open contract revenue recognition obligations from Excel to SAP; historical data quality and completeness are uncertain.",
              "risk_category": "Data",
              "likelihood": "Medium",
              "impact": "High",
              "mitigation": "Begin open contract inventory and revenue recognition data cleansing in the Prepare phase. Engage external audit firm to validate opening balances for RAR migration. Define a parallel-run period where both Excel-based and SAP-based revenue recognition run simultaneously."
            }
          ]
        }
      ],
      "cross_cutting_risks": [
        {
          "risk_description": "Organizational change fatigue from two failed IT projects (MES upgrade, PLM migration) in the past three years. Middle management and shop floor personnel are skeptical of large technology programs. Change management failure is the top overall program risk.",
          "risk_category": "Organizational",
          "affected_modules": ["ALL"],
          "mitigation": "Establish a dedicated OCM workstream with change champions at each site (Redmond, Huntsville, Cape Canaveral). Conduct a formal change readiness assessment and post-mortem analysis of the failed MES and PLM projects. Design an early wins strategy: deliver visible, tangible improvements (e.g., Fiori self-service apps, automated reports) in Wave 1 to build credibility before larger process changes in Wave 2. Budget 12 to 15% of program cost for OCM."
        },
        {
          "risk_description": "Production ramp from 5 to 15 satellites per month overlaps with the S/4HANA system conversion timeline. Manufacturing disruption during cutover could have multi-million-dollar revenue impact and delay constellation deployment.",
          "risk_category": "Operational",
          "affected_modules": ["PP", "QM", "MM", "PM"],
          "mitigation": "Design cutover plans that minimize manufacturing downtime. Consider wave sequencing that implements finance and GTS (Wave 1) before manufacturing modules (Wave 2) to separate financial system changes from production system changes. Plan Wave 2 cutover during a planned production pause or reduced production period if the constellation deployment schedule allows."
        },
        {
          "risk_description": "Custom code remediation (2,400 ABAP objects, 47 custom transactions) is the critical path for the program timeline and budget. Delays in custom code analysis or higher-than-expected retain/migrate ratios directly impact both schedule and cost.",
          "risk_category": "Technical",
          "affected_modules": ["ALL"],
          "mitigation": "Run SAP Custom Code Migration Worklist and ABAP Test Cockpit immediately as a pre-program activity. Classify all 2,400 objects before the Explore phase begins. Establish a dedicated custom code remediation team. Monitor retire/adapt/retain/move ratios against the 60% retirement target. If retirement rate falls below 50%, escalate to program steering committee for scope and budget adjustment."
        },
        {
          "risk_description": "Budget risk: $15 to $25M is achievable but tight for a brownfield conversion of this complexity (heavy customization, 5 major integrations, ITAR compliance, multi-wave deployment). Scope creep or integration complexity overruns could exceed the upper budget bound.",
          "risk_category": "Financial",
          "affected_modules": ["ALL"],
          "mitigation": "Establish firm scope boundaries per wave with change control governance. Maintain a 10 to 15% contingency reserve. Identify scope deferral candidates: IBP (keep Anaplan), predictive maintenance (defer to Phase 3), digital twin (defer to Phase 3). Monitor actual vs. budget at wave-level granularity."
        }
      ]
    },

    "downstream_handoff": {
      "ready_for_roadmap_generation": true,
      "ready_for_proposal_drafting": true,
      "module_priority_sequence": ["FI", "CO", "GTS", "MM", "SD", "PS", "PP", "QM", "PM", "BTP"],
      "key_decisions_needed_before_roadmap": [
        "ECC database size (TB) for system conversion duration planning and infrastructure sizing",
        "Custom code preliminary classification results from SAP Custom Code Migration Worklist (critical path)",
        "Legal entity structure confirmation: single CSS entity or multiple entities requiring intercompany configuration",
        "ITAR data scope within SAP: which master data objects and transactions carry ITAR classification (CISO input required)",
        "Parent company S/4HANA Cloud Private Edition managed service provider and hosting requirements",
        "DCAA EVMS requirement confirmation: is ANSI/EIA-748 compliance required for CSS government contracts?",
        "Anaplan retention decision: keep Anaplan with BTP integration or evaluate replacement with SAP IBP/SAC Planning?"
      ],
      "recommended_next_steps": [
        "1. Execute SAP Custom Code Migration Worklist and ABAP Test Cockpit analysis immediately; this is the program critical path activity.",
        "2. Engage CISO for ITAR data scope mapping within SAP; GTS implementation design depends on this input.",
        "3. Validate parent company integration requirements: consolidation reporting format, intercompany rules, shared BTP entitlements, managed service provider alignment.",
        "4. Deploy Signavio for ECC process mining (parent mandate); priority processes: financial close, BOM change management, procurement, ITAR compliance.",
        "5. Deploy LeanIX for application portfolio mapping (parent mandate); map all 12 middleware interfaces and 5 major external systems.",
        "6. Conduct formal change readiness assessment across all three sites; incorporate lessons learned from failed MES and PLM projects.",
        "7. Engage SAP for system conversion assessment and S/4HANA Cloud Private Edition sizing based on ECC database profile.",
        "8. Schedule executive alignment workshop: confirm single accountable sponsor, validate wave structure, and secure OCM investment commitment."
      ],
      "signals_for_skill_03": {
        "phase_1_candidates": ["FI", "CO", "GTS", "BTP (Integration Suite foundation)"],
        "phase_2_candidates": ["PP", "QM", "MM", "SD", "PS", "PM", "BTP (PLM/MES integrations)"],
        "future_phase_candidates": ["Predictive quality analytics (SAC/BTP AI)", "Predictive maintenance (BTP IoT)", "Digital twin", "IBP (if Anaplan replaced)"],
        "critical_path_modules": ["FI", "GTS", "PP"],
        "wave_rationale": "Wave 1 prioritizes financial close improvement and ITAR compliance (the two highest-risk domains) while establishing the BTP integration foundation. Wave 2 delivers the manufacturing transformation (BOM lifecycle, MES integration, production scaling) alongside supply chain and project system improvements. Wave 3 layers advanced analytics and predictive capabilities on the stabilized foundation."
      },
      "signals_for_skill_04": {
        "headline_value_drivers": [
          "ITAR compliance transformation: from fragmented manual controls to fully integrated GTS, eliminating the single largest regulatory risk facing the company",
          "5-day financial close (from 12 days) with automated reconciliation and real-time program profitability",
          "Digital factory: real-time manufacturing visibility, integrated BOM lifecycle, and production scaling to 15 satellites per month",
          "60% custom code reduction and Clean Core alignment, reducing total cost of ownership and enabling continuous S/4HANA innovation adoption",
          "Parent company alignment on S/4HANA Cloud Private Edition, Signavio, and LeanIX, establishing CSS as a model subsidiary transformation"
        ],
        "key_risk_messages": [
          "Organizational change fatigue from two failed IT projects is the top program risk; dedicated OCM investment is essential",
          "PLM (Teamcenter) and MES (Apriso) integrations are technically complex and sit on the critical path for Wave 2",
          "ITAR compliance transition period must be carefully managed to avoid regulatory exposure during GTS implementation",
          "Budget ($15 to $25M) is achievable but tight; scope discipline and contingency reserves are mandatory"
        ],
        "investment_justification_data": [
          "Current 12-day close costs approximately $1.5M annually in finance team overtime and delayed reporting; 5-day close recovers capacity",
          "ITAR compliance risk: a single violation can result in fines up to $1.2M per occurrence and debarment from government contracts",
          "4-hour MES data lag causes estimated $2 to $3M annual impact in rework, scrap, and production schedule disruption",
          "47 custom transactions and 2,400 custom objects cost an estimated $3 to $4M annually in support, maintenance, and upgrade avoidance",
          "Production ramp from 5 to 15 satellites/month represents approximately $2.4B in annual revenue at full rate; ERP must scale to support this growth"
        ]
      }
    }
  }
}
```

---

## Module Fit Summary Table

| Module | Relevance | Fit Score | Clean Core | Wave | Key Decision |
|---|---|---|---|---|---|
| **FI** | CRITICAL | 3.5/5 | Level B | Wave 1 | RAR activation and open contract migration for IFRS 15/ASC 606 |
| **CO** | CRITICAL | 3.0/5 | Level B | Wave 1 | Program-level CO-PA operating concern design; EVM measurement approach |
| **MM** | CRITICAL | 3.5/5 | Level B | Wave 2 | Long-lead component planning approach (MRP vs. IBP vs. Anaplan extension) |
| **SD** | HIGH | 3.5/5 | Level A | Wave 2 | Milestone billing plan design; Salesforce CRM integration scope |
| **PP** | CRITICAL | 2.5/5 | Level C | Wave 2 | Teamcenter PLM integration architecture (ECTR vs. BTP custom); as-built BOM approach |
| **QM** | CRITICAL | 3.0/5 | Level A | Wave 2 | AS9100D inspection plan configuration; NCR/MRB workflow design |
| **PM** | HIGH | 3.5/5 | Level A | Wave 2 | Calibration management approach; predictive maintenance deferral to Wave 3 |
| **PS** | CRITICAL | 2.5/5 | Level B | Wave 2 | DCAA EVMS compliance validation; Anaplan integration scope |
| **GTS** | CRITICAL | 2.0/5 | Level B | Wave 1 | ITAR classification data migration; deemed export access architecture |
| **BTP** | CRITICAL | N/A | Level B | All Waves | Middleware consolidation sequence; BTP Enterprise Agreement sizing |

---

## Key Recommendations

1. **Deploy S/4HANA Cloud Private Edition via SAP RISE** as mandated by the parent company. Private Edition satisfies ITAR data residency, supports the brownfield system conversion path, and enables custom code migration for retained ABAP objects.

2. **Wave 1 (Q2 2028): Finance, Controlling, and GTS.** Prioritize the two highest-risk domains (ITAR compliance and financial close) while establishing the BTP integration foundation. GTS must be in Wave 1 to minimize the duration of the fragmented compliance transition period.

3. **Wave 2 (Q4 2028): Manufacturing, Supply Chain, and Project Systems.** Deliver the digital factory transformation (BOM lifecycle, MES integration, production scaling) alongside MM, SD, PS, and PM. This wave depends on PLM and MES integrations that must begin design in the Prepare phase.

4. **Wave 3 (H1 2029): Advanced Analytics and Predictive Capabilities.** Layer predictive quality, predictive maintenance, and enhanced analytics on the stabilized S/4HANA foundation. Evaluate IBP vs. Anaplan retention decision at this stage.

5. **Execute custom code analysis immediately.** The SAP Custom Code Migration Worklist and ABAP Test Cockpit analysis of all 2,400 objects is the single most critical path activity. Results determine the feasibility of the 60% retirement target, the budget impact of remediation, and the scope of BTP ABAP Environment migration.

6. **Invest in organizational change management at 12 to 15% of program budget.** The legacy of two failed IT projects makes OCM the top program risk. A dedicated OCM workstream with site-level change champions, an early wins strategy, and a formal change readiness assessment are prerequisites for program success.

7. **Begin PLM (Teamcenter) and MES (Apriso) integration design early.** These are the two most technically complex integrations and sit on the critical path for Wave 2. Starting architectural design during the Prepare phase (before Explore) provides the lead time needed for these high-risk integrations.

8. **Maintain existing ITAR manual controls in parallel with GTS implementation.** No compliance gaps are acceptable during the transition. The existing separate access control database and manual processes remain active until full GTS validation and compliance audit confirm readiness.

---

*Generated by SAP S/4HANA Implementation Scoping Agent -- Skill 02: Module Fit Analyzer*
*Source data completeness: 90% (Skill 01) | Analysis confidence: HIGH*
*Clean Core Current State: Level D (2,400 custom objects) | Target: Level B (18 months post go-live)*
