# Skill 02: Module Fit Analyzer

## Purpose

Takes the structured discovery brief from Skill 01 (Client Discovery Intake Agent) and performs detailed fit/gap analysis against SAP S/4HANA modules. This skill replicates the analytical work a senior SAP Solution Architect performs when mapping client requirements to specific SAP modules — scoring fit versus gap, identifying integration dependencies and cross-module considerations, and flagging areas needing customization versus standard process adoption.

**SAP Ecosystem Positioning:** This skill performs the analytical work that happens between SAP's Digital Discovery Assessment (DDA) scope item selection and the Fit-to-Standard workshops in the Explore phase of SAP Activate. While DDA recommends scope items at a catalog level and Signavio's Process Recommender benchmarks against 5,000+ best practices, neither produces the consultant-grade fit/gap scoring with integration dependency mapping that this skill generates. The output is designed to feed into SAP Cloud ALM as requirements (linking to Solution Process flows) and into Signavio for target-state process modeling. It also provides the module-level detail needed by Skill 03 (Implementation Roadmap Generator) to sequence phases and by Skill 04 (Executive Proposal Drafter) to justify investment.

---

## Inputs

| Input | Source | Required? |
|---|---|---|
| **Complete structured discovery brief JSON** | Skill 01 output | Yes |
| **Industry-specific scope items** | Skill 05 (SAP Best Practices Fetcher) output | Optional — enriches fit scoring with SAP-published reference content |
| **Client-provided process documentation** | Direct upload | Optional — improves gap analysis accuracy |
| **SAP product availability matrix** | SAP reference data | Optional — used for deployment model recommendation |

**Minimum viable input:** The complete Skill 01 discovery brief JSON with `data_completeness_score` >= 40% and `confidence_level` of MEDIUM or higher. If completeness is below 40%, the skill returns a partial analysis with prominent warnings and a request to re-run Skill 01 with additional client data.

---

## Output: Module Fit Analysis Report

The agent produces a structured JSON report with the following schema:

```json
{
  "module_fit_analysis": {
    "metadata": {
      "analysis_id": "MFA-{YYYYMMDD}-{CLIENT_SHORT}",
      "source_brief_id": "DB-{matching Skill 01 brief_id}",
      "created_date": "ISO 8601",
      "analysis_confidence": "HIGH | MEDIUM | LOW",
      "brief_completeness_at_analysis": "percentage from source brief",
      "assumptions_made": ["list of key assumptions driving the analysis"],
      "limitations": ["list of factors that reduce analysis confidence"]
    },

    "module_assessment_matrix": [
      {
        "module_code": "SAP abbreviation (FI, CO, MM, SD, etc.)",
        "module_name": "Full SAP module name",
        "relevance": "Critical | High | Medium | Low | Not Applicable",
        "fit_score": {
          "score": "1-5 integer",
          "label": "Major Gap | Significant Customization | Moderate Configuration | Minor Configuration | Standard Fit",
          "rationale": "Detailed explanation of fit score"
        },
        "gap_analysis": [
          {
            "requirement": "What the client needs",
            "sap_standard_capability": "What SAP provides out of the box",
            "gap_type": "No Gap | Configuration Gap | Extension Gap | Modification Gap | Functional Gap",
            "resolution_approach": "Standard config | BTP extension | Key User Extensibility | Classic modification | Partner solution | Out of scope",
            "clean_core_compliant": true,
            "effort_estimate": "Low | Medium | High",
            "notes": ""
          }
        ],
        "key_scope_items": [
          {
            "scope_item_id": "SAP best practice scope item ID (e.g., 1YR, J58, BKP)",
            "scope_item_name": "Scope item description",
            "activation_type": "Mandatory | Recommended | Optional",
            "notes": ""
          }
        ],
        "estimated_users": {
          "professional": 0,
          "limited_professional": 0,
          "developer": 0,
          "rationale": "Explanation of user count estimate"
        },
        "license_implications": "SAP licensing considerations for this module",
        "implementation_notes": "Module-specific implementation guidance",
        "data_migration_complexity": "Low | Medium | High",
        "data_migration_notes": ""
      }
    ],

    "integration_dependency_map": {
      "mandatory_bundles": [
        {
          "bundle_name": "Descriptive name",
          "modules": ["list of module codes"],
          "rationale": "Why these must be implemented together",
          "data_dependencies": ["specific data flows requiring co-implementation"]
        }
      ],
      "optional_integrations": [
        {
          "source_module": "",
          "target_module": "",
          "integration_value": "Description of value gained",
          "can_defer": true,
          "deferral_impact": "What is lost if deferred"
        }
      ],
      "non_sap_interfaces": [
        {
          "external_system": "",
          "interface_type": "Real-time API | Batch file | Middleware | Manual",
          "direction": "Inbound | Outbound | Bidirectional",
          "data_objects": ["list of data types exchanged"],
          "integration_technology": "BTP Integration Suite | SAP PI/PO | Direct API | File transfer",
          "complexity": "Low | Medium | High",
          "clean_core_compliant": true
        }
      ],
      "data_flow_diagram_description": "Narrative description of key data flows across modules and external systems"
    },

    "cross_module_considerations": {
      "organizational_structure": {
        "company_codes": { "count": 0, "rationale": "" },
        "controlling_areas": { "count": 0, "rationale": "" },
        "plants": { "count": 0, "rationale": "" },
        "storage_locations": { "count": 0, "rationale": "" },
        "sales_organizations": { "count": 0, "rationale": "" },
        "distribution_channels": { "count": 0, "rationale": "" },
        "purchasing_organizations": { "count": 0, "rationale": "" },
        "design_notes": "Key organizational structure decisions and their implications"
      },
      "master_data_harmonization": [
        {
          "master_data_object": "Business Partner | Material | G/L Account | Cost Center | Profit Center | etc.",
          "current_state": "Description of current data state",
          "harmonization_effort": "Low | Medium | High",
          "key_decisions": ["list of decisions needed"],
          "cross_module_impact": ["which modules are affected"]
        }
      ],
      "number_range_management": {
        "strategy": "Internal | External | Mixed",
        "key_objects": ["list of objects requiring number range decisions"],
        "notes": ""
      },
      "authorization_concept": {
        "complexity": "Simple | Moderate | Complex",
        "key_considerations": ["list of authorization design considerations"],
        "role_count_estimate": 0
      }
    },

    "clean_core_compliance": {
      "overall_assessment": "A | B | C | D",
      "overall_assessment_label": "Clean Core Native | Clean Core with Extensions | Clean Core Partial | Non-Compliant",
      "rationale": "Overall Clean Core posture explanation",
      "per_module_assessment": [
        {
          "module_code": "",
          "clean_core_level": "A | B | C | D",
          "standard_process_adoption_rate": "percentage",
          "extensions_needed": [
            {
              "extension_description": "",
              "extension_type": "Key User App | BTP Side-by-Side | Classic In-App | Partner Add-On",
              "clean_core_impact": "None | Low | Medium | High",
              "justification": ""
            }
          ],
          "modifications_flagged": [
            {
              "modification_description": "",
              "reason": "",
              "clean_core_violation": true,
              "recommended_alternative": ""
            }
          ]
        }
      ],
      "btp_extension_summary": {
        "total_extensions_recommended": 0,
        "extension_categories": ["list of extension types needed"],
        "estimated_btp_services": ["list of BTP services required"],
        "btp_licensing_impact": ""
      }
    },

    "risk_assessment": {
      "overall_risk_level": "Low | Medium | High | Critical",
      "per_module_risks": [
        {
          "module_code": "",
          "risk_level": "Low | Medium | High",
          "risks": [
            {
              "risk_description": "",
              "risk_category": "Technical | Functional | Organizational | Data | Integration | Compliance",
              "likelihood": "Low | Medium | High",
              "impact": "Low | Medium | High",
              "mitigation": ""
            }
          ]
        }
      ],
      "cross_cutting_risks": [
        {
          "risk_description": "",
          "risk_category": "",
          "affected_modules": [],
          "mitigation": ""
        }
      ]
    },

    "sap_toolchain_integration": {
      "signavio_recommendations": [
        {
          "use_case": "",
          "timing": "Pre-implementation | During Explore | During Realize | Post Go-Live",
          "modules_affected": [],
          "value_proposition": ""
        }
      ],
      "leanix_recommendations": [
        {
          "use_case": "",
          "timing": "",
          "value_proposition": ""
        }
      ],
      "cloud_alm_setup": {
        "requirements_to_track": 0,
        "solution_processes_to_configure": [],
        "test_scope_implications": "",
        "deployment_tracking_needs": ""
      }
    },

    "sizing_recommendation": {
      "recommended_deployment_model": "S/4HANA Cloud Public Edition | S/4HANA Cloud Private Edition | S/4HANA On-Premise",
      "sap_program": "SAP GROW | SAP RISE | Direct License",
      "rationale": "Detailed justification for deployment model recommendation",
      "alternative_considered": "Alternative product if applicable (e.g., SAP Business One)",
      "alternative_rationale": "Why the alternative was considered and whether it should be pursued",
      "estimated_total_users": {
        "professional": 0,
        "limited_professional": 0,
        "developer": 0
      },
      "estimated_system_sizing": "T-shirt size (XS | S | M | L | XL)",
      "high_availability_needs": "Yes | No",
      "disaster_recovery_needs": "Yes | No",
      "notes": ""
    },

    "downstream_handoff": {
      "ready_for_roadmap_generation": true,
      "ready_for_proposal_drafting": true,
      "module_priority_sequence": ["ordered list of modules for implementation phasing"],
      "key_decisions_needed_before_roadmap": [],
      "recommended_next_steps": [],
      "signals_for_skill_03": {
        "phase_1_candidates": [],
        "phase_2_candidates": [],
        "future_phase_candidates": [],
        "critical_path_modules": []
      },
      "signals_for_skill_04": {
        "headline_value_drivers": [],
        "key_risk_messages": [],
        "investment_justification_data": []
      }
    }
  }
}
```

---

## Step-by-Step Behavior

### Step 1: Discovery Brief Validation

- Parse the incoming Skill 01 JSON and validate structural completeness
- Check that all required sections are present: `client_profile`, `current_landscape`, `business_requirements`, `compliance_and_regulatory`, `transformation_context`, `initial_module_signals`
- Verify `data_completeness_score` >= 40% — if below, return an early termination response with:
  - List of missing Critical fields that block analysis
  - Recommended questions to ask the client
  - Partial analysis of only those modules with sufficient data
- Verify `confidence_level` is MEDIUM or higher — if LOW, proceed but add prominent warnings to every module assessment
- Flag any `[INFERRED]` tags from Skill 01 that could materially affect fit scoring, and note assumptions carried forward
- **SAP Activate alignment:** This validation mirrors the "Discover Phase Quality Gate" where project teams confirm sufficient scope clarity before entering the Explore phase

### Step 2: Module Relevance Scoring

- Start from the `initial_module_signals` in the Skill 01 brief and refine using full requirement analysis
- Map each stated business requirement to SAP's process hierarchy:
  - Level 1: Line of Business (Finance, Procurement, Supply Chain, Sales, etc.)
  - Level 2: Process area (Record-to-Report, Source-to-Pay, Plan-to-Fulfill, Order-to-Cash, etc.)
  - Level 3: Specific process (General Ledger Accounting, Accounts Payable, Purchase Order Processing, etc.)
  - Level 4: Process step (Post Journal Entry, Three-Way Match, Create Sales Order, etc.)
- Score each module as Critical / High / Medium / Low / Not Applicable based on:
  - Direct requirement alignment (client explicitly stated the need)
  - Indirect requirement alignment (module is needed to support a stated requirement)
  - Industry-standard expectations (modules typically deployed in this industry/company profile)
  - Organizational complexity drivers (legal entities, plants, currencies, etc.)
- Cross-reference against SAP's Scope Item catalog for the relevant deployment model (Cloud Public Edition scope items, Private Edition scope items, or on-premise)
- **SAP reference:** Align with SAP's process taxonomy as documented in SAP Signavio Process Navigator and the SAP Best Practices Explorer

### Step 3: Fit/Gap Analysis Per Module

For each module scored as Critical, High, or Medium in Step 2, perform a detailed fit/gap analysis:

- **Fit assessment:** Compare each client requirement against SAP S/4HANA standard functionality for that module. Use the 1-5 scoring scale:
  - **5 — Standard Fit:** SAP standard process covers the requirement with no configuration beyond initial setup. Example: standard general ledger accounting, basic purchase order processing
  - **4 — Minor Configuration:** SAP covers the requirement with standard configuration options (IMG settings, business rules, output determination). Example: multi-currency with standard FX processing, standard batch management
  - **3 — Moderate Configuration:** SAP covers the core requirement but needs meaningful configuration work, custom forms/reports, or Key User Extensibility apps. Example: industry-specific pricing procedures, country-specific tax determination
  - **2 — Significant Customization:** SAP provides a foundation but requires BTP-based extensions, ABAP enhancements, or partner add-ons to meet the requirement. Example: mobile money integration, non-standard quality grading systems
  - **1 — Major Gap:** SAP does not natively support the requirement; requires classic modification, third-party product, or the requirement must be descoped. Example: fully custom manufacturing execution processes, niche regulatory compliance outside SAP-supported geographies

- **Gap categorization:** For every gap identified, classify it as:
  - **Configuration Gap:** Addressable through standard SAP configuration (IMG, Fiori configuration apps)
  - **Extension Gap:** Requires BTP extension or Key User Extensibility (Clean Core compliant)
  - **Modification Gap:** Requires classic ABAP modification or enhancement (potentially violates Clean Core)
  - **Functional Gap:** SAP does not provide the functionality; requires third-party or workaround
  - **No Gap:** SAP standard covers the requirement fully

- Reference specific SAP Best Practice scope items where applicable (e.g., "1YR — Accounts Receivable", "J58 — Material Quality Management", "BKP — Basic Controlling/Profitability Analysis")
- Estimate user counts per module by mapping job roles to license types:
  - **Professional User:** Full transactional access (finance managers, procurement leads, sales admins)
  - **Limited Professional User:** Limited transactional access with restricted process scope
  - **Developer User:** Technical users building extensions on BTP

### Step 4: Integration Dependency Mapping

- Identify **mandatory module bundles** — modules that share master data objects, transactional documents, or real-time posting flows and therefore must be implemented concurrently:
  - FI and CO are always bundled (controlling postings derive from financial postings)
  - MM and FI-AP are bundled (goods receipt drives accounts payable)
  - SD and FI-AR are bundled (billing drives accounts receivable)
  - QM and MM are bundled when inspection lots trigger on goods receipt
  - WM/EWM and MM are bundled (warehouse movements reference material documents)
  - GTS and SD are bundled for export scenarios (customs documents derive from delivery/billing)

- Identify **optional integration paths** — modules that add value when connected but can be deferred:
  - CO-PA (Profitability Analysis) can run after FI/CO base go-live
  - Advanced QM (stability studies, certificate management) can follow basic QM
  - BTP extensions can be added incrementally after core go-live

- Map **non-SAP interfaces** with technology recommendations:
  - Payment gateways (mobile money, bank integrations) via BTP Integration Suite
  - E-commerce platforms via SAP Commerce Cloud or standard APIs
  - Government/regulatory portals via file-based or API interfaces
  - Legacy data sources via SAP Data Services or BTP Data Intelligence

- Generate a narrative data flow description that traces a key business transaction end-to-end across modules (e.g., farm-gate commodity purchase through processing, quality grading, export sale, and financial settlement)

### Step 5: Clean Core Compliance Check

- Assess each module against SAP's Clean Core 4-level maturity model:
  - **Level A — Clean Core Native:** 100% standard processes, no custom code, extensions only via approved BTP patterns
  - **Level B — Clean Core with Extensions:** Standard core processes with side-by-side BTP extensions for differentiation
  - **Level C — Clean Core Partial:** Mostly standard but some in-app extensions or Key User Extensibility used; no classic modifications
  - **Level D — Non-Compliant:** Classic ABAP modifications, custom reports overriding standard, or modifications to core data models

- For each module, calculate an estimated "standard process adoption rate" (percentage of requirements met by SAP standard vs. requiring extension/modification)
- Flag every requirement that would potentially violate Clean Core principles and provide a recommended alternative approach
- Assess BTP extension requirements holistically:
  - Which BTP services are needed (Integration Suite, Build Apps, Build Work Zone, etc.)?
  - What is the cumulative BTP licensing impact?
  - Can any BTP extensions be replaced with Key User Extensibility (lower cost, lower maintenance)?

- **Greenfield advantage assessment:** For clients with no existing SAP footprint, explicitly note the opportunity to adopt standard processes from day one and avoid technical debt

### Step 6: Cross-Module Design Considerations

- **Organizational structure design:** Recommend the enterprise structure based on client profile:
  - Company codes (driven by legal entities and statutory reporting requirements)
  - Controlling areas (typically 1:1 with company codes unless cross-company cost allocation is needed)
  - Plants (driven by physical locations — factories, warehouses, processing facilities)
  - Storage locations (sub-divisions of plants for inventory management)
  - Sales organizations and distribution channels (driven by go-to-market structure)
  - Purchasing organizations (driven by procurement authority structure)
  - Note: Enterprise structure decisions are foundational and extremely costly to change post go-live; flag decisions requiring client confirmation

- **Master data harmonization:**
  - Business Partner (BP) master: consolidation strategy for customers, vendors, and farmer/grower records
  - Material master: classification, unit of measure standardization, batch management settings
  - Chart of Accounts: SAP standard vs. industry-specific, operating vs. group chart of accounts for multi-entity reporting
  - Cost center and profit center hierarchy design
  - Note dependencies between master data objects and the modules that consume them

- **Number range management:** Recommend internal vs. external number assignment strategy for key document types (purchase orders, sales orders, accounting documents, material numbers, batch numbers)

- **Authorization concept:** Estimate complexity based on organizational structure, user roles, and segregation-of-duties requirements. Reference SAP standard role templates where applicable.

### Step 7: Risk Assessment

For each module scored as Critical or High, and for key cross-cutting concerns, assess:

- **Technical risks:** Integration complexity, data migration volume and quality, customization scope, BTP extension development effort
- **Functional risks:** Process gaps requiring workarounds, missing SAP functionality for industry-specific needs, dependency on future SAP roadmap features
- **Organizational risks:** Change management burden, user adoption challenges, training complexity, key-user availability during implementation
- **Data risks:** Master data quality issues, data cleansing scope, historical data migration decisions (how many years of history?)
- **Integration risks:** External system interface complexity, real-time vs. batch timing considerations, error handling and monitoring
- **Compliance risks:** Regulatory requirements not fully covered by SAP standard, localization gaps for specific countries

Provide a specific mitigation recommendation for each identified risk.

### Step 8: Output Assembly and Downstream Handoff

- Compile all assessments into the structured JSON output schema
- Generate the `sizing_recommendation` based on:
  - Total module scope and complexity
  - User count and license type distribution
  - Deployment model alignment (Cloud Public Edition constraints vs. Private Edition flexibility vs. On-Premise control)
  - SAP GROW (mid-market, standard adoption, lower TCO) vs. RISE (enterprise, more customization, managed services) fit
  - Consider alternative SAP products (SAP Business One for sub-$50M revenue companies)

- Generate `downstream_handoff` signals:
  - **For Skill 03 (Implementation Roadmap):** Module priority sequence, mandatory bundles, phase candidates, critical path identification
  - **For Skill 04 (Executive Proposal):** Headline value drivers, key risk messages, investment justification data points
  - **For Skill 05 (SAP Best Practices Fetcher):** List of scope items to pull detailed reference content for

- Perform a final consistency check:
  - Do fit scores align with gap counts? (A module with many gaps should not have a high fit score)
  - Are integration dependencies internally consistent? (If MM-FI integration is mandatory, both modules must be in Phase 1)
  - Does the sizing recommendation align with the module scope? (S/4HANA Cloud Public Edition has scope item restrictions)

---

## Constraints and Failure Modes

| Constraint | Handling |
|---|---|
| **Insufficient discovery brief** | If `data_completeness_score` < 40%, return partial analysis with prominent warning. If specific module-relevant data is missing, score that module as "Insufficient Data" rather than guessing the fit score. List the exact data needed to complete the assessment. |
| **Modules outside SAP S/4HANA scope** | If client requirements map to systems outside S/4HANA (MES, PLM, LIMS, standalone CRM), flag these explicitly as "Out of SAP S/4HANA scope — evaluate SAP partner solutions or SAP Industry Cloud" and do not include them in the fit/gap matrix. Provide SAP ecosystem alternatives where they exist (e.g., SAP Digital Manufacturing for MES, SAP Enterprise Product Development for PLM). |
| **Conflicting requirements** | If the discovery brief contains requirements that conflict with each other (e.g., "fully standard processes" + "must replicate exact current workflow"), flag the contradiction, score the module assuming standard adoption, and note the risk of scope creep if the conflict is not resolved. |
| **Over-scoping risk** | If the total module scope exceeds what is reasonable for the client's size, budget, and timeline, add an explicit "Scope Warning" section. Recommend a phased approach and identify which modules can be deferred without breaking core functionality. Apply a heuristic: companies under 200 employees rarely need more than 6-8 modules in Phase 1. |
| **Underestimating integration complexity** | If more than 3 non-SAP system interfaces are identified, flag the integration workstream as a distinct risk factor and recommend a dedicated integration architect. Note that BTP Integration Suite licensing is incremental to S/4HANA licensing. |
| **Clean Core uncertainty** | If a requirement falls in a gray area between BTP extension and classic modification, default to recommending the BTP approach and flag it for detailed technical assessment during the Explore phase. Never recommend a classic modification without noting the Clean Core implication. |
| **Geographic/localization gaps** | If the client operates in countries where SAP localization coverage is limited (some African, Central Asian, or Pacific Island nations), flag this as a risk and recommend checking SAP's country version availability matrix before committing to scope. |

---

## Example Usage

### Input: Highland Harvest Exports Ltd. Discovery Brief

The complete Skill 01 output for Highland Harvest Exports Ltd. (brief ID: DB-20260217-HHE) is used as input. Key parameters driving this analysis:

- **Industry:** Consumer Products — Agricultural Commodities (Premium Cashew)
- **Size:** ~65 employees, revenue unknown (assumed sub-$10M based on size and market)
- **Current ERP:** None (Excel-based)
- **Transformation type:** Greenfield
- **Key requirements:** Inventory traceability, multi-currency FI, export documentation, quality management, scalability to 7,000 farmers
- **Budget:** Tight, investor-funded contingent on ROI

### Sample Output

```json
{
  "module_fit_analysis": {
    "metadata": {
      "analysis_id": "MFA-20260217-HHE",
      "source_brief_id": "DB-20260217-HHE",
      "created_date": "2026-02-17T00:00:00Z",
      "analysis_confidence": "MEDIUM",
      "brief_completeness_at_analysis": "62%",
      "assumptions_made": [
        "Revenue assumed sub-$10M USD based on 65-employee cashew export operation in Tanzania",
        "Single legal entity assumed (one company code)",
        "Farmer procurement is through direct smallholder purchase at farm gate or collection points",
        "Cashew processing includes raw intake and drying (collection station), drying, processing facilitying, grading, and export packaging",
        "No manufacturing complexity beyond agricultural processing",
        "Internet connectivity assumed available at Njombe headquarters; intermittent at field locations",
        "the regional mobile money provider integration is critical for farmer payment disbursement, not just collection"
      ],
      "limitations": [
        "Revenue not confirmed — deployment model recommendation may change significantly",
        "No user count by role provided — license estimates are directional",
        "No regulatory details confirmed beyond export documentation — compliance scope may expand",
        "No infrastructure assessment — connectivity constraints could impact deployment model"
      ]
    },

    "module_assessment_matrix": [
      {
        "module_code": "FI",
        "module_name": "Financial Accounting",
        "relevance": "Critical",
        "fit_score": {
          "score": 5,
          "label": "Standard Fit",
          "rationale": "SAP FI is a mature, well-proven module for multi-currency financial accounting. General ledger, accounts payable, accounts receivable, asset accounting, and bank accounting are all standard scope items. Multi-currency processing with automatic FX gain/loss posting is native functionality. Tanzania-specific localizations for tax and statutory reporting should be verified against SAP's country version matrix, but core FI functionality is a strong fit. Greenfield deployment means no legacy chart of accounts to migrate — client can adopt SAP's standard reference chart of accounts."
        },
        "gap_analysis": [
          {
            "requirement": "Multi-currency processing (TZS, USD, EUR, INR)",
            "sap_standard_capability": "FI supports unlimited parallel currencies with automatic FX translation using daily/monthly exchange rate tables. SAP provides standard FX revaluation programs for open items and balance sheet accounts.",
            "gap_type": "No Gap",
            "resolution_approach": "Standard config",
            "clean_core_compliant": true,
            "effort_estimate": "Low",
            "notes": "Exchange rate source needs to be defined — likely Bank of Tanzania or ECB. Daily rate update can be automated via BTP or manual entry."
          },
          {
            "requirement": "Financial reporting (P&L, balance sheet, cash flow)",
            "sap_standard_capability": "SAP S/4HANA provides real-time financial statements via the Universal Journal (ACDOCA). Fiori apps for P&L, balance sheet, and cash flow reporting are standard. Embedded analytics via SAP Analytics Cloud (SAC) integration available.",
            "gap_type": "No Gap",
            "resolution_approach": "Standard config",
            "clean_core_compliant": true,
            "effort_estimate": "Low",
            "notes": "Investor reporting requirements may need custom SAC stories — assess in Explore phase."
          },
          {
            "requirement": "Monthly close process automation",
            "sap_standard_capability": "SAP S/4HANA Financial Close Cockpit provides guided close task management. Automated recurring entries, accruals, and FX revaluation are standard.",
            "gap_type": "No Gap",
            "resolution_approach": "Standard config",
            "clean_core_compliant": true,
            "effort_estimate": "Low",
            "notes": "Moving from manual Excel reconciliation to SAP financial close will be a significant process improvement and change management effort despite minimal technical gap."
          },
          {
            "requirement": "Tanzania tax compliance and statutory reporting",
            "sap_standard_capability": "SAP provides Tanzania country version localization — verify current scope in SAP Note 2793345 or equivalent. VAT, withholding tax, and corporate income tax determination are generally supported for East African markets.",
            "gap_type": "Configuration Gap",
            "resolution_approach": "Standard config",
            "clean_core_compliant": true,
            "effort_estimate": "Medium",
            "notes": "Tanzania Revenue Authority (URA) e-invoicing and EFRIS compliance may require verification. If SAP standard does not cover Tanzania EFRIS, a BTP extension or partner solution may be needed — flag for Explore phase."
          }
        ],
        "key_scope_items": [
          { "scope_item_id": "J77", "scope_item_name": "General Ledger Accounting", "activation_type": "Mandatory", "notes": "" },
          { "scope_item_id": "1YR", "scope_item_name": "Accounts Receivable", "activation_type": "Mandatory", "notes": "Export buyer invoicing" },
          { "scope_item_id": "J78", "scope_item_name": "Accounts Payable", "activation_type": "Mandatory", "notes": "Farmer and vendor payments" },
          { "scope_item_id": "BKI", "scope_item_name": "Bank Account Management", "activation_type": "Mandatory", "notes": "Multi-currency bank accounts" },
          { "scope_item_id": "J80", "scope_item_name": "Asset Accounting", "activation_type": "Recommended", "notes": "Processing equipment, vehicles" },
          { "scope_item_id": "BF7", "scope_item_name": "Financial Close", "activation_type": "Recommended", "notes": "Automated period-end close" }
        ],
        "estimated_users": {
          "professional": 3,
          "limited_professional": 2,
          "developer": 0,
          "rationale": "Finance manager + 1-2 accountants as Professional; management dashboard users as Limited Professional"
        },
        "license_implications": "FI is included in all S/4HANA editions. No additional module licensing required.",
        "implementation_notes": "Greenfield advantage — adopt SAP standard chart of accounts (e.g., YCOA reference) from day one. Multi-currency setup is straightforward. Key decision: local currency (TZS) as company code currency with USD as parallel currency for group/investor reporting.",
        "data_migration_complexity": "Low",
        "data_migration_notes": "No legacy ERP data to migrate. Opening balances as of go-live cutover date. Bank master data and business partner (vendor/customer) master data migration from Excel."
      },

      {
        "module_code": "CO",
        "module_name": "Controlling",
        "relevance": "Critical",
        "fit_score": {
          "score": 4,
          "label": "Minor Configuration",
          "rationale": "SAP CO provides cost center accounting, internal orders, and profitability analysis that map well to HHE's needs. Profitability analysis by cashew lot, buyer, region, and certification type requires CO-PA configuration but is well within standard functionality. The minor gap is in agricultural commodity-specific cost allocation patterns (e.g., attributing processing costs across multiple cashew lots based on weight/grade), which requires thoughtful configuration of cost allocation cycles but no custom code."
        },
        "gap_analysis": [
          {
            "requirement": "Cost tracking per cashew lot from farm gate through export",
            "sap_standard_capability": "CO supports cost object tracking via internal orders or product cost collectors. Combined with batch management in MM, per-lot cost accumulation is achievable through standard cost allocation.",
            "gap_type": "Configuration Gap",
            "resolution_approach": "Standard config",
            "clean_core_compliant": true,
            "effort_estimate": "Medium",
            "notes": "Design decision needed: use internal orders per lot vs. product cost collectors. For agricultural commodities with blending/grading, internal orders per processing batch may be more flexible."
          },
          {
            "requirement": "Profitability analysis by buyer, region, and certification",
            "sap_standard_capability": "CO-PA (Profitability Analysis) supports multi-dimensional margin analysis with configurable characteristics. Buyer, region, and certification can be defined as CO-PA characteristics.",
            "gap_type": "Configuration Gap",
            "resolution_approach": "Standard config",
            "clean_core_compliant": true,
            "effort_estimate": "Medium",
            "notes": "Recommend account-based CO-PA in S/4HANA (costing-based CO-PA is deprecated). Define derivation rules for automatic characteristic assignment."
          }
        ],
        "key_scope_items": [
          { "scope_item_id": "J79", "scope_item_name": "Overhead Cost Management", "activation_type": "Mandatory", "notes": "Cost center accounting for collection station, office, logistics" },
          { "scope_item_id": "BKP", "scope_item_name": "Basic Controlling and Profitability Analysis", "activation_type": "Mandatory", "notes": "Per-lot and per-buyer profitability" },
          { "scope_item_id": "J82", "scope_item_name": "Internal Orders", "activation_type": "Recommended", "notes": "Per-lot cost tracking if internal order approach is selected" }
        ],
        "estimated_users": {
          "professional": 2,
          "limited_professional": 2,
          "developer": 0,
          "rationale": "Finance manager + operations manager as Professional; management reporting users as Limited Professional"
        },
        "license_implications": "CO is included in all S/4HANA editions alongside FI. CO-PA does not require separate licensing.",
        "implementation_notes": "CO design should be finalized alongside FI — the organizational structure (cost centers, profit centers) is shared. Key design workshops needed for cost allocation methodology and CO-PA characteristic definition.",
        "data_migration_complexity": "Low",
        "data_migration_notes": "No legacy cost center or profit center data. Define structure fresh based on HHE's operational model."
      },

      {
        "module_code": "MM",
        "module_name": "Materials Management",
        "relevance": "Critical",
        "fit_score": {
          "score": 3,
          "label": "Moderate Configuration",
          "rationale": "SAP MM handles standard procurement, inventory management, and batch tracking well. However, HHE's procurement model involves purchasing from 3,200+ smallholder farmers via mobile money — this is not a standard SAP procurement pattern. Standard MM assumes vendor master records with formal purchase orders, whereas HHE likely uses spot purchases at collection points with immediate mobile money payment. Batch management for cashew lot traceability is standard but requires careful configuration of batch classification, batch determination, and shelf life management for raw cashew."
        },
        "gap_analysis": [
          {
            "requirement": "Smallholder farmer procurement (3,200+ individual suppliers, spot purchases at farm gate)",
            "sap_standard_capability": "MM supports vendor master records and purchase order processing. For high-volume small purchases, simplified procurement via purchase orders without RFQ/contract is possible. One-time vendor functionality or vendor group master records can reduce master data burden.",
            "gap_type": "Extension Gap",
            "resolution_approach": "BTP extension",
            "clean_core_compliant": true,
            "effort_estimate": "High",
            "notes": "Standard PO processing for 3,200+ individual farmer purchases is impractical. Recommend a BTP-based mobile farmer intake app that captures purchase data (farmer ID, quantity, grade, price) and posts simplified material documents in S/4HANA. Business Partner master records for farmers should use a group/classification approach rather than individual full vendor masters. Consider SAP Rural Sourcing Management (RSM) if available, or a custom BTP application."
          },
          {
            "requirement": "Lot/batch traceability from farm gate to export container",
            "sap_standard_capability": "MM batch management supports batch creation at goods receipt, batch classification (cashew grade, moisture, origin region), batch determination for sales orders, and batch-level inventory valuation. Batch traceability reports are standard.",
            "gap_type": "Configuration Gap",
            "resolution_approach": "Standard config",
            "clean_core_compliant": true,
            "effort_estimate": "Medium",
            "notes": "Configure batch classification with cashew-specific characteristics: origin (region/farmer group), kernel grade (W240/W320/SW/LP), moisture content, whole/broken kernel count, outturn ratio, defect count. Set up batch determination strategies for sales order fulfillment."
          },
          {
            "requirement": "Mobile money payment to farmers upon delivery",
            "sap_standard_capability": "SAP FI-AP supports payment processing via payment programs (F110), but regional mobile money platforms are not a standard SAP payment method.",
            "gap_type": "Extension Gap",
            "resolution_approach": "BTP extension",
            "clean_core_compliant": true,
            "effort_estimate": "High",
            "notes": "Requires BTP Integration Suite to connect SAP payment run output to the regional mobile money provider or mobile money aggregator APIs. Payment file format mapping and reconciliation logic needed. This is the single most complex integration in the entire project."
          },
          {
            "requirement": "Inventory management across multiple storage stages (raw cashew nut intake, raw intake and drying, drying tables, processing facility, export warehouse)",
            "sap_standard_capability": "MM supports storage location-based inventory management with goods movements between locations. Material type configuration can handle the cashew transformation (raw cashew nut to shelled to graded kernel) using process orders or stock transfer with material change.",
            "gap_type": "Configuration Gap",
            "resolution_approach": "Standard config",
            "clean_core_compliant": true,
            "effort_estimate": "Medium",
            "notes": "Design decision: model cashew processing stages as storage location transfers (simpler, same material number) or as production/process orders with material conversion (more accurate costing but higher complexity). Recommend storage location approach for Phase 1 given company size."
          }
        ],
        "key_scope_items": [
          { "scope_item_id": "J45", "scope_item_name": "Procurement of Direct Materials", "activation_type": "Mandatory", "notes": "Raw cashew raw cashew nut procurement" },
          { "scope_item_id": "J58", "scope_item_name": "Inventory Management", "activation_type": "Mandatory", "notes": "Multi-stage cashew inventory" },
          { "scope_item_id": "1FL", "scope_item_name": "Batch Management", "activation_type": "Mandatory", "notes": "Cashew lot traceability" },
          { "scope_item_id": "2QR", "scope_item_name": "Simplified Procurement", "activation_type": "Recommended", "notes": "High-volume farmer purchases" },
          { "scope_item_id": "BMD", "scope_item_name": "Physical Inventory", "activation_type": "Recommended", "notes": "Warehouse stock counts" }
        ],
        "estimated_users": {
          "professional": 3,
          "limited_professional": 5,
          "developer": 0,
          "rationale": "Procurement lead + warehouse manager + collection station supervisor as Professional; field agents/collection point staff as Limited Professional (if mobile access is implemented)"
        },
        "license_implications": "MM is included in S/4HANA base. If a mobile farmer intake app is built on BTP, BTP licensing (Build Apps, Integration Suite) is incremental.",
        "implementation_notes": "MM is the most complex module for HHE due to the non-standard smallholder procurement model. Recommend a phased approach: Phase 1 with simplified goods receipt posting and manual farmer payment trigger, Phase 2 with full BTP mobile app and automated the regional mobile money provider integration.",
        "data_migration_complexity": "Medium",
        "data_migration_notes": "Farmer master data (3,200+ records) needs migration from Excel/WhatsApp records into Business Partner master. Material master setup for cashew varieties and grades. Opening stock balances at go-live."
      },

      {
        "module_code": "SD",
        "module_name": "Sales and Distribution",
        "relevance": "Critical",
        "fit_score": {
          "score": 3,
          "label": "Moderate Configuration",
          "rationale": "SAP SD handles export sales order processing, pricing, delivery, and billing as standard functionality. The moderate fit score reflects the complexity of international export documentation requirements (phytosanitary certificates, EU food-safety traceability certificates, weight notes, bills of lading) which go beyond standard SD output types. Foreign trade data in SD is well supported, but the specific document formats for Tanzanian cashew export require configuration and potentially custom form outputs."
        },
        "gap_analysis": [
          {
            "requirement": "Export sales order management for premium cashew (US, EU, Japan buyers)",
            "sap_standard_capability": "SD supports international sales orders with multi-currency pricing (USD, EUR, INR), Incoterms, payment terms, and foreign trade data. Standard sales order types (OR) with export-specific settings.",
            "gap_type": "Configuration Gap",
            "resolution_approach": "Standard config",
            "clean_core_compliant": true,
            "effort_estimate": "Low",
            "notes": "Straightforward SD configuration for export sales. Define sales org, distribution channel, and division structure. Configure pricing procedures for FOB/CIF pricing."
          },
          {
            "requirement": "Export documentation (phytosanitary certificates, EU food-safety traceability certificates, weight notes, bills of lading)",
            "sap_standard_capability": "SD output management supports document generation at delivery and billing. Standard packing list and delivery note are available. Specific Tanzanian export document formats (Tanzania Cashewnut Board forms, phytosanitary certificates from Ministry of Agriculture, Tanzania) are not pre-delivered.",
            "gap_type": "Configuration Gap",
            "resolution_approach": "Standard config",
            "clean_core_compliant": true,
            "effort_estimate": "Medium",
            "notes": "Custom Adobe Forms or SAP Forms by Adobe for export documents. Data is available in SD (weight, batch, foreign trade data) — forms need to be designed to match Tanzania Cashewnut Board and Ministry of Agriculture, Tanzania requirements. This is configuration-level effort, not modification."
          },
          {
            "requirement": "Batch-determined sales order fulfillment (customer orders specific lot/grade)",
            "sap_standard_capability": "SD batch determination allows automatic or manual batch assignment during delivery creation based on customer-specified characteristics (grade, origin, certification).",
            "gap_type": "Configuration Gap",
            "resolution_approach": "Standard config",
            "clean_core_compliant": true,
            "effort_estimate": "Medium",
            "notes": "Configure batch determination strategies linked to MM batch classification. For premium cashew, customers often request specific lots — manual batch assignment with batch info cockpit is appropriate."
          }
        ],
        "key_scope_items": [
          { "scope_item_id": "BD9", "scope_item_name": "Sell from Stock", "activation_type": "Mandatory", "notes": "Core export sales order to billing" },
          { "scope_item_id": "1MJ", "scope_item_name": "Foreign Trade / Customs (Export)", "activation_type": "Mandatory", "notes": "Export documentation and customs" },
          { "scope_item_id": "BKA", "scope_item_name": "Basic Credit Management", "activation_type": "Optional", "notes": "Only if buyer credit terms are offered" },
          { "scope_item_id": "1QE", "scope_item_name": "Batch-Specific Sales", "activation_type": "Recommended", "notes": "Lot-specific order fulfillment" }
        ],
        "estimated_users": {
          "professional": 2,
          "limited_professional": 1,
          "developer": 0,
          "rationale": "Export/sales manager + logistics coordinator as Professional; management reporting as Limited Professional"
        },
        "license_implications": "SD is included in S/4HANA base. Adobe Forms for export documents may need Forms by Adobe licensing — verify with SAP.",
        "implementation_notes": "SD is tightly integrated with MM (delivery references inventory) and FI-AR (billing creates accounting documents). Must be implemented in the same phase as MM and FI.",
        "data_migration_complexity": "Low",
        "data_migration_notes": "Customer master data (export buyers) from Excel. No open sales order migration needed for greenfield. Pricing condition records setup."
      },

      {
        "module_code": "QM",
        "module_name": "Quality Management",
        "relevance": "High",
        "fit_score": {
          "score": 4,
          "label": "Minor Configuration",
          "rationale": "SAP QM supports inspection planning, results recording, usage decisions, and quality certificates — all core to premium cashew quality management. The fit is strong because cashew quality attributes (kernel grading score, moisture, screen size, defect count, grade) map well to QM inspection characteristics. Minor configuration is needed for cashew-specific inspection plans, sampling procedures, and quality certificate generation for export buyers."
        },
        "gap_analysis": [
          {
            "requirement": "Digital quality records for cashew grading (kernel grading scores, moisture, defect count, screen size)",
            "sap_standard_capability": "QM inspection characteristics support numeric, text, and formula-based quality attributes. Inspection plans can define sampling procedures and acceptance criteria per quality characteristic. Results recording via Fiori apps or mobile.",
            "gap_type": "Configuration Gap",
            "resolution_approach": "Standard config",
            "clean_core_compliant": true,
            "effort_estimate": "Medium",
            "notes": "Define inspection characteristics for SCA kernel grading protocol (fragrance, aroma, flavor, aftertaste, acidity, body, uniformity, balance, clean cup, sweetness, overall, defects, final score). Set up inspection plans triggered at key processing stages: raw cashew nut intake, shelled after drying, graded kernel after processing facilitying, final pre-export."
          },
          {
            "requirement": "Full traceability linking quality records to batch/lot",
            "sap_standard_capability": "QM inspection lots are automatically linked to material documents (goods receipts, production orders) and thus to batches. Traceability from quality result to batch to sales order delivery is standard.",
            "gap_type": "No Gap",
            "resolution_approach": "Standard config",
            "clean_core_compliant": true,
            "effort_estimate": "Low",
            "notes": "Automatic inspection lot creation on goods receipt for batch-managed materials. No gap — this is core QM functionality."
          },
          {
            "requirement": "Quality certificates for export buyers",
            "sap_standard_capability": "QM supports quality certificate generation linked to delivery/batch. Certificate profiles can be configured to pull inspection results into formatted documents for customers.",
            "gap_type": "Configuration Gap",
            "resolution_approach": "Standard config",
            "clean_core_compliant": true,
            "effort_estimate": "Medium",
            "notes": "Configure certificate profiles and Adobe Form layout for cashew quality certificates. Specialty buyers typically expect lot-specific kernel grading reports and green analysis data."
          }
        ],
        "key_scope_items": [
          { "scope_item_id": "1NJ", "scope_item_name": "Quality Management for Procurement", "activation_type": "Mandatory", "notes": "Inspection at goods receipt" },
          { "scope_item_id": "2D7", "scope_item_name": "Quality Management in Inventory Management", "activation_type": "Recommended", "notes": "In-process quality during cashew processing stages" },
          { "scope_item_id": "2HL", "scope_item_name": "Quality Certificates", "activation_type": "Recommended", "notes": "Export buyer quality documentation" }
        ],
        "estimated_users": {
          "professional": 2,
          "limited_professional": 2,
          "developer": 0,
          "rationale": "Quality manager + head cupper as Professional; collection station quality checkers as Limited Professional"
        },
        "license_implications": "QM is included in S/4HANA base. No additional module licensing.",
        "implementation_notes": "QM should be implemented alongside MM to enable automatic inspection lot creation on goods receipt. Quality certificates should be designed alongside SD export documents for consistency.",
        "data_migration_complexity": "Low",
        "data_migration_notes": "No legacy quality data to migrate. Inspection plans and master inspection characteristics are new configuration. Historical kernel grading records from paper logs could optionally be loaded as reference data."
      },

      {
        "module_code": "WM",
        "module_name": "Warehouse Management (Basic) / Embedded EWM",
        "relevance": "Medium",
        "fit_score": {
          "score": 4,
          "label": "Minor Configuration",
          "rationale": "For a company of HHE's size, full EWM (Extended Warehouse Management) is overkill. Basic warehouse management using MM storage locations with goods movements is sufficient. If more granularity is needed (bin-level tracking within the processing facility or export warehouse), S/4HANA's embedded EWM provides this as a step-up from basic WM without requiring a separate EWM deployment. The fit is good because cashew warehouse management is relatively simple compared to discrete manufacturing or retail distribution."
        },
        "gap_analysis": [
          {
            "requirement": "Track inventory across collection station, drying tables, processing facility, and export warehouse",
            "sap_standard_capability": "MM storage locations provide location-level inventory tracking. Goods movements (MIGO) between storage locations track physical flow. For bin-level management, embedded EWM adds warehouse structure (storage types, storage sections, storage bins).",
            "gap_type": "No Gap",
            "resolution_approach": "Standard config",
            "clean_core_compliant": true,
            "effort_estimate": "Low",
            "notes": "Recommend starting with MM storage locations in Phase 1. Evaluate embedded EWM only if granular bin-level tracking is needed post go-live."
          }
        ],
        "key_scope_items": [
          { "scope_item_id": "1LJ", "scope_item_name": "Stock Transfer Between Plants/Storage Locations", "activation_type": "Mandatory", "notes": "Track cashew movement between processing stages" }
        ],
        "estimated_users": {
          "professional": 1,
          "limited_professional": 2,
          "developer": 0,
          "rationale": "Warehouse manager as Professional; warehouse staff as Limited Professional"
        },
        "license_implications": "Basic WM via MM storage locations is included. Embedded EWM is included in S/4HANA but adds configuration complexity.",
        "implementation_notes": "Do not over-engineer warehouse management for a 50-person company. MM storage locations with goods movements are sufficient for Phase 1.",
        "data_migration_complexity": "Low",
        "data_migration_notes": "Storage location master data is new configuration. Opening stock balances per storage location at go-live."
      },

      {
        "module_code": "GTS",
        "module_name": "Global Trade Services",
        "relevance": "Medium",
        "fit_score": {
          "score": 3,
          "label": "Moderate Configuration",
          "rationale": "SAP GTS provides comprehensive export compliance, customs management, and trade preference processing. For HHE, the relevant GTS functions are export license management, trade document generation, and sanctioned party screening. However, GTS is a separately licensed product with significant implementation effort relative to HHE's simple export model (single origin country, commodity product, well-established trade routes). The cost-benefit may not justify GTS for a company of this size."
        },
        "gap_analysis": [
          {
            "requirement": "Automated export documentation and compliance",
            "sap_standard_capability": "GTS Customs Management handles export declarations, license determination, and document generation. Integration with SD provides seamless document flow from sales order to customs declaration.",
            "gap_type": "No Gap",
            "resolution_approach": "Standard config",
            "clean_core_compliant": true,
            "effort_estimate": "High",
            "notes": "Technically no gap, but GTS is a full product deployment with its own organizational structure, master data, and processing logic. The effort is substantial for relatively simple export requirements."
          }
        ],
        "key_scope_items": [
          { "scope_item_id": "2VG", "scope_item_name": "Customs Management for Export", "activation_type": "Optional", "notes": "Full GTS deployment — evaluate cost-benefit" }
        ],
        "estimated_users": {
          "professional": 1,
          "limited_professional": 0,
          "developer": 0,
          "rationale": "Export compliance handled by export manager already counted in SD"
        },
        "license_implications": "GTS is a separately licensed SAP product — NOT included in S/4HANA base. Significant incremental licensing cost. For S/4HANA Cloud Public Edition, GTS functionality is limited to embedded foreign trade capabilities in SD.",
        "implementation_notes": "RECOMMENDATION: Defer GTS to a future phase. Use SD foreign trade data and custom Adobe Forms for export documentation in Phase 1. GTS is justified when export volume and complexity increase, or if regulatory requirements mandate automated compliance checking. If HHE exports to sanctioned or restricted markets in the future, GTS becomes more relevant.",
        "data_migration_complexity": "Low",
        "data_migration_notes": "No legacy GTS data. New setup of tariff classifications, export license master data, and trade partner profiles."
      },

      {
        "module_code": "PP",
        "module_name": "Production Planning",
        "relevance": "Low",
        "fit_score": {
          "score": 3,
          "label": "Moderate Configuration",
          "rationale": "Cashew processing (raw cashew nut intake, raw intake and drying, drying, processing facilitying, grading, blending, packaging) is a continuous/process manufacturing workflow, not discrete production. SAP PP supports this through process orders or repetitive manufacturing, but the complexity of PP is disproportionate to HHE's processing model. At 65 employees with a single collection station, a simplified approach using MM goods movements with material transformation is more appropriate than full PP deployment."
        },
        "gap_analysis": [
          {
            "requirement": "Track cashew processing from raw cashew nut to export-grade graded kernel",
            "sap_standard_capability": "PP/PI (Process Industry) supports bill of materials, routing, process orders, and yield management for agricultural processing.",
            "gap_type": "No Gap",
            "resolution_approach": "Standard config",
            "clean_core_compliant": true,
            "effort_estimate": "High",
            "notes": "Technically feasible but over-engineered for current scale. Recommend MM-based approach in Phase 1 (storage location transfers with material type changes). Evaluate PP only when HHE adds multiple processing lines or contract processing."
          }
        ],
        "key_scope_items": [],
        "estimated_users": {
          "professional": 0,
          "limited_professional": 0,
          "developer": 0,
          "rationale": "Not recommended for Phase 1. Processing tracked via MM goods movements."
        },
        "license_implications": "PP is included in S/4HANA base but adds significant configuration and training overhead.",
        "implementation_notes": "NOT RECOMMENDED for Phase 1. Cashew processing can be modeled using MM goods movements between storage locations with batch splitting/merging. Revisit PP if HHE builds multiple processing facilities or takes on contract processing for other exporters.",
        "data_migration_complexity": "N/A",
        "data_migration_notes": "N/A — module not recommended for initial deployment."
      },

      {
        "module_code": "PM",
        "module_name": "Plant Maintenance",
        "relevance": "Low",
        "fit_score": {
          "score": 4,
          "label": "Minor Configuration",
          "rationale": "SAP PM supports equipment maintenance, preventive maintenance scheduling, and maintenance order processing. HHE has limited equipment (collection station machinery, drying tables, processing facility, vehicles) that does not justify full PM deployment at this stage."
        },
        "gap_analysis": [],
        "key_scope_items": [],
        "estimated_users": {
          "professional": 0,
          "limited_professional": 0,
          "developer": 0,
          "rationale": "Not recommended for Phase 1. Equipment maintenance managed manually or via simple calendar reminders."
        },
        "license_implications": "PM is included in S/4HANA base.",
        "implementation_notes": "NOT RECOMMENDED for initial deployment. Limited equipment base does not justify PM module overhead. Revisit when HHE scales operations or acquires significant capital equipment.",
        "data_migration_complexity": "N/A",
        "data_migration_notes": "N/A"
      },

      {
        "module_code": "PS",
        "module_name": "Project System",
        "relevance": "Not Applicable",
        "fit_score": {
          "score": 5,
          "label": "Standard Fit",
          "rationale": "HHE is not a project-based business. Cashew export is a repetitive operational business model. PS is not applicable."
        },
        "gap_analysis": [],
        "key_scope_items": [],
        "estimated_users": { "professional": 0, "limited_professional": 0, "developer": 0, "rationale": "N/A" },
        "license_implications": "N/A",
        "implementation_notes": "NOT APPLICABLE. HHE does not have project-based revenue or cost management needs.",
        "data_migration_complexity": "N/A",
        "data_migration_notes": "N/A"
      },

      {
        "module_code": "HCM/SF",
        "module_name": "Human Capital Management / SuccessFactors",
        "relevance": "Low",
        "fit_score": {
          "score": 4,
          "label": "Minor Configuration",
          "rationale": "With approximately 65 employees, HHE's HR needs (payroll, time management, organizational management) can be served by lighter solutions. SuccessFactors Employee Central is a strong product but represents significant investment for a company of this size. SAP S/4HANA on-premise HCM is deprecated in favor of SuccessFactors."
        },
        "gap_analysis": [],
        "key_scope_items": [],
        "estimated_users": { "professional": 0, "limited_professional": 0, "developer": 0, "rationale": "N/A for Phase 1" },
        "license_implications": "SuccessFactors is separately licensed from S/4HANA. Significant incremental cost for 65 employees.",
        "implementation_notes": "NOT RECOMMENDED for Phase 1. Evaluate SuccessFactors Employee Central if HHE grows beyond 200 employees or has complex HR compliance requirements. In the interim, lightweight HR tools or local payroll software for Tanzania (e.g., WagePoint, local providers) are more cost-appropriate.",
        "data_migration_complexity": "N/A",
        "data_migration_notes": "N/A"
      },

      {
        "module_code": "BTP",
        "module_name": "SAP Business Technology Platform",
        "relevance": "High",
        "fit_score": {
          "score": 3,
          "label": "Moderate Configuration",
          "rationale": "BTP is not a traditional application module but is critical for HHE's Clean Core strategy. The the regional mobile money provider mobile money integration is the primary driver — SAP standard does not include mobile money payment methods, so a BTP Integration Suite-based connection is the Clean Core-compliant approach. Additionally, a mobile farmer intake application (for field agents capturing purchases at collection points) would be built on BTP Build Apps or SAP Build Work Zone. BTP is scored as Moderate Configuration because it requires development effort, not just configuration."
        },
        "gap_analysis": [
          {
            "requirement": "the regional mobile money provider mobile money integration for farmer payments",
            "sap_standard_capability": "SAP FI-AP payment program supports bank file formats but not mobile money APIs natively.",
            "gap_type": "Extension Gap",
            "resolution_approach": "BTP extension",
            "clean_core_compliant": true,
            "effort_estimate": "High",
            "notes": "Build a BTP Integration Suite iFlow that: (1) receives payment run output from S/4HANA, (2) transforms to the regional mobile money provider API format, (3) submits mobile money disbursements, (4) captures confirmation/failure responses, (5) updates payment status in S/4HANA. Requires the regional mobile money provider API documentation and test environment."
          },
          {
            "requirement": "Mobile farmer intake application for field agents",
            "sap_standard_capability": "SAP Fiori provides mobile-responsive UI but standard procurement Fiori apps are designed for professional buyers, not field agents at rural collection points with intermittent connectivity.",
            "gap_type": "Extension Gap",
            "resolution_approach": "BTP extension",
            "clean_core_compliant": true,
            "effort_estimate": "High",
            "notes": "Build a lightweight mobile app on SAP Build Apps (formerly AppGyver) or SAP Mobile Development Kit (MDK) that: captures farmer ID, weight, grade, price; works offline; syncs to S/4HANA MM when connectivity is available. This is a Phase 2 candidate."
          }
        ],
        "key_scope_items": [],
        "estimated_users": {
          "professional": 0,
          "limited_professional": 0,
          "developer": 1,
          "rationale": "One developer license for BTP extension development and maintenance"
        },
        "license_implications": "BTP is licensed separately. Requires at minimum: BTP Integration Suite (for the regional mobile money provider), potentially SAP Build Apps (for mobile app). BTP pricing is based on service consumption — estimate based on transaction volumes.",
        "implementation_notes": "BTP extensions should be planned alongside core module implementation but can be delivered incrementally. the regional mobile money provider integration is Phase 1 critical (farmers must be paid). Mobile farmer intake app is Phase 2.",
        "data_migration_complexity": "N/A",
        "data_migration_notes": "N/A — BTP is integration/extension platform, not a data store."
      }
    ],

    "integration_dependency_map": {
      "mandatory_bundles": [
        {
          "bundle_name": "Financial Core",
          "modules": ["FI", "CO"],
          "rationale": "FI and CO share the Universal Journal (ACDOCA) in S/4HANA. Every financial posting generates a corresponding CO posting. These modules cannot function independently.",
          "data_dependencies": ["Chart of accounts", "Cost center hierarchy", "Profit center hierarchy", "Company code settings"]
        },
        {
          "bundle_name": "Procure-to-Pay",
          "modules": ["MM", "FI"],
          "rationale": "Goods receipt in MM triggers automatic FI-AP invoice verification and payment processing. Purchase order commitment accounting posts to CO.",
          "data_dependencies": ["Vendor master (Business Partner)", "Material master", "G/L account determination for inventory posting", "Tax code assignment"]
        },
        {
          "bundle_name": "Order-to-Cash",
          "modules": ["SD", "FI"],
          "rationale": "Billing document creation in SD triggers automatic FI-AR accounting document posting. Revenue recognition, tax determination, and payment terms flow from SD to FI.",
          "data_dependencies": ["Customer master (Business Partner)", "Material master", "G/L account determination for revenue/COGS", "Tax code assignment", "Credit management"]
        },
        {
          "bundle_name": "Quality-Integrated Procurement",
          "modules": ["QM", "MM"],
          "rationale": "QM inspection lots are triggered by MM goods receipts. Quality decisions in QM update MM stock status (unrestricted, quality inspection, blocked). Batch quality data in QM is linked to MM batch master.",
          "data_dependencies": ["Material master (QM view)", "Inspection plans", "Batch classification"]
        }
      ],
      "optional_integrations": [
        {
          "source_module": "SD",
          "target_module": "QM",
          "integration_value": "Quality certificates attached to deliveries. Batch determination in SD can use QM inspection results to select only batches that pass quality criteria.",
          "can_defer": true,
          "deferral_impact": "Quality certificates would need to be generated manually outside SAP or as a separate process not linked to the delivery document."
        },
        {
          "source_module": "SD",
          "target_module": "GTS",
          "integration_value": "Automatic customs declaration and export compliance checking triggered by SD delivery. Sanctioned party screening on sales order creation.",
          "can_defer": true,
          "deferral_impact": "Export documentation handled manually via SD foreign trade fields and custom forms. No automated compliance screening."
        },
        {
          "source_module": "MM",
          "target_module": "WM",
          "integration_value": "Bin-level inventory management within storage locations. Pick/pack/ship processing for export containers.",
          "can_defer": true,
          "deferral_impact": "Inventory tracked at storage location level only (not bin level). Adequate for HHE's current scale."
        }
      ],
      "non_sap_interfaces": [
        {
          "external_system": "the regional mobile money provider (Mobile Money Gateway)",
          "interface_type": "Real-time API",
          "direction": "Outbound (payment instructions) + Inbound (confirmation/status)",
          "data_objects": ["Payment disbursement instructions", "Payment confirmation/failure status", "Mobile money transaction IDs"],
          "integration_technology": "BTP Integration Suite",
          "complexity": "High",
          "clean_core_compliant": true
        },
        {
          "external_system": "Banking system (for export revenue)",
          "interface_type": "Batch file",
          "direction": "Bidirectional",
          "data_objects": ["Bank statements (MT940/CAMT.053)", "Payment files", "FX rate feeds"],
          "integration_technology": "SAP standard bank communication management",
          "complexity": "Medium",
          "clean_core_compliant": true
        },
        {
          "external_system": "Tanzania Revenue Authority (URA) / EFRIS",
          "interface_type": "Real-time API",
          "direction": "Outbound",
          "data_objects": ["E-invoices", "Tax declarations"],
          "integration_technology": "BTP Integration Suite or SAP Document Compliance",
          "complexity": "Medium",
          "clean_core_compliant": true
        }
      ],
      "data_flow_diagram_description": "Key end-to-end flow — Cashew Purchase to Export Settlement: (1) Field agent records farmer purchase at collection point [BTP Mobile App or manual entry] -> (2) Goods receipt posted in MM with batch creation [MM] -> (3) Automatic inspection lot created for incoming quality check [QM] -> (4) Quality results recorded (moisture, defect count, preliminary grade) [QM] -> (5) Farmer payment triggered via accounts payable [FI-AP] -> (6) Payment disbursed to farmer mobile money account [BTP Integration Suite -> the regional mobile money provider] -> (7) Cashew moves through processing stages via storage location transfers [MM] -> (8) Final quality grading and kernel grading at processing facility [QM] -> (9) Export sales order created for buyer [SD] -> (10) Batch determination assigns specific lots to sales order [SD + MM] -> (11) Delivery created and export documentation generated [SD] -> (12) Billing document posted with FX conversion (USD/EUR/INR -> TZS) [SD -> FI-AR] -> (13) Revenue recognized and profitability posted to CO-PA [FI -> CO]."
    },

    "cross_module_considerations": {
      "organizational_structure": {
        "company_codes": { "count": 1, "rationale": "Single legal entity in Tanzania. One company code with TZS as local currency and USD as parallel currency for investor/group reporting." },
        "controlling_areas": { "count": 1, "rationale": "One controlling area mapped 1:1 to the single company code." },
        "plants": { "count": 2, "rationale": "Plant 1: Njombe HQ and collection station (processing facility). Plant 2: Export warehouse/processing facility (if physically separate). If co-located, single plant with multiple storage locations is sufficient." },
        "storage_locations": { "count": 5, "rationale": "Raw cashew nut intake, raw intake and drying (fermentation/washing), drying tables, processing facility/grading, export warehouse. Each stage is a storage location for inventory tracking." },
        "sales_organizations": { "count": 1, "rationale": "Single sales organization for all export markets. Distribution channels: 01-Export (primary), possibly 02-Domestic if local sales exist." },
        "distribution_channels": { "count": 1, "rationale": "Single distribution channel for direct export sales. Add domestic channel only if HHE sells within Tanzania." },
        "purchasing_organizations": { "count": 1, "rationale": "Centralized purchasing — all farmer procurement and supplier purchases through one purchasing organization." },
        "design_notes": "Enterprise structure is simple given HHE's single-entity, single-country model. Key design decision: whether the collection station and export warehouse are modeled as one plant or two. Recommend single plant with multiple storage locations for simplicity unless physical separation or distinct P&L tracking is needed."
      },
      "master_data_harmonization": [
        {
          "master_data_object": "Business Partner (Farmer/Supplier)",
          "current_state": "Excel/WhatsApp records for 3,200+ smallholder farmers. No standardized data structure.",
          "harmonization_effort": "High",
          "key_decisions": [
            "Model farmers as individual Business Partners or as grouped entities (e.g., by collection point or cooperative)?",
            "What minimum data is required per farmer (name, location, mobile money number, national ID)?",
            "How to handle farmers without formal identification?"
          ],
          "cross_module_impact": ["MM (vendor master for procurement)", "FI-AP (payment processing)", "BTP (mobile app farmer lookup)"]
        },
        {
          "master_data_object": "Business Partner (Export Buyer/Customer)",
          "current_state": "Small number of export buyers — likely under 50. Data exists in Excel or email records.",
          "harmonization_effort": "Low",
          "key_decisions": ["Customer classification by market (US, EU, Japan)", "Payment terms and Incoterms standardization"],
          "cross_module_impact": ["SD (customer master for sales orders)", "FI-AR (accounts receivable)"]
        },
        {
          "master_data_object": "Material Master",
          "current_state": "No formal material master. Cashew tracked informally by variety and grade.",
          "harmonization_effort": "Medium",
          "key_decisions": [
            "Material numbering scheme (by variety, processing method, grade?)",
            "How many distinct material numbers (raw cashew nut, shelled, graded kernel by grade)?",
            "Unit of measure standardization (kg for processing, 60kg bags for export)",
            "Batch management activation and classification characteristics"
          ],
          "cross_module_impact": ["MM (procurement and inventory)", "SD (sales)", "QM (inspection plans)", "CO (product costing)"]
        },
        {
          "master_data_object": "G/L Account Master / Chart of Accounts",
          "current_state": "No formal chart of accounts. Manual Excel-based tracking.",
          "harmonization_effort": "Medium",
          "key_decisions": [
            "Adopt SAP reference chart of accounts or design custom?",
            "Account structure for multi-currency postings",
            "Profit center structure (by product line, by market, or by farm region?)"
          ],
          "cross_module_impact": ["FI (all postings)", "CO (cost allocation)", "SD (revenue recognition)", "MM (inventory valuation)"]
        }
      ],
      "number_range_management": {
        "strategy": "Internal",
        "key_objects": ["Accounting documents", "Purchase orders", "Sales orders", "Deliveries", "Billing documents", "Material numbers", "Batch numbers", "Business partner numbers"],
        "notes": "Greenfield deployment — use SAP internal numbering for all objects. No legacy number ranges to maintain. Batch numbers should include a prefix indicating origin/processing stage for human readability."
      },
      "authorization_concept": {
        "complexity": "Simple",
        "key_considerations": [
          "Small user base (~15-20 total SAP users) simplifies role design",
          "Key segregation of duties: procurement approval vs. payment release, sales order vs. billing",
          "Field agent access (if mobile app) requires restricted data visibility",
          "Management dashboard access for investors/leadership"
        ],
        "role_count_estimate": 8
      }
    },

    "clean_core_compliance": {
      "overall_assessment": "B",
      "overall_assessment_label": "Clean Core with Extensions",
      "rationale": "HHE has a significant greenfield advantage — no legacy custom code, no existing modifications. The core S/4HANA deployment (FI, CO, MM, SD, QM) can be implemented using 90%+ standard processes. The two areas requiring BTP extensions (the regional mobile money provider mobile money integration and mobile farmer intake app) are cleanly separated as side-by-side extensions on BTP, fully compliant with Clean Core Level B. No classic ABAP modifications are recommended anywhere in this scope.",
      "per_module_assessment": [
        {
          "module_code": "FI",
          "clean_core_level": "A",
          "standard_process_adoption_rate": "95%",
          "extensions_needed": [],
          "modifications_flagged": []
        },
        {
          "module_code": "CO",
          "clean_core_level": "A",
          "standard_process_adoption_rate": "90%",
          "extensions_needed": [],
          "modifications_flagged": []
        },
        {
          "module_code": "MM",
          "clean_core_level": "B",
          "standard_process_adoption_rate": "75%",
          "extensions_needed": [
            {
              "extension_description": "Mobile farmer intake application for field collection points",
              "extension_type": "BTP Side-by-Side",
              "clean_core_impact": "None",
              "justification": "SAP standard procurement apps are designed for office-based buyers. Field agents at rural collection points need a simplified, offline-capable mobile interface."
            },
            {
              "extension_description": "Simplified farmer master data management for high-volume smallholder onboarding",
              "extension_type": "Key User App",
              "clean_core_impact": "Low",
              "justification": "Standard BP maintenance transaction is too complex for onboarding 3,200+ farmers with minimal data per record."
            }
          ],
          "modifications_flagged": []
        },
        {
          "module_code": "SD",
          "clean_core_level": "A",
          "standard_process_adoption_rate": "85%",
          "extensions_needed": [
            {
              "extension_description": "Custom Adobe Forms for Tanzanian export documentation (Tanzania Cashewnut Board certificates, phytosanitary forms)",
              "extension_type": "Key User App",
              "clean_core_impact": "None",
              "justification": "Form layout customization is standard practice and does not violate Clean Core. No modification to underlying SD logic."
            }
          ],
          "modifications_flagged": []
        },
        {
          "module_code": "QM",
          "clean_core_level": "A",
          "standard_process_adoption_rate": "90%",
          "extensions_needed": [],
          "modifications_flagged": []
        },
        {
          "module_code": "BTP",
          "clean_core_level": "B",
          "standard_process_adoption_rate": "N/A — extension platform",
          "extensions_needed": [
            {
              "extension_description": "the regional mobile money provider mobile money integration via BTP Integration Suite",
              "extension_type": "BTP Side-by-Side",
              "clean_core_impact": "None",
              "justification": "Core Clean Core pattern: S/4HANA core remains standard, integration with non-SAP payment platform handled entirely on BTP."
            }
          ],
          "modifications_flagged": []
        }
      ],
      "btp_extension_summary": {
        "total_extensions_recommended": 3,
        "extension_categories": ["Integration (the regional mobile money provider)", "Mobile App (Farmer Intake)", "Key User Extensibility (Export Forms, Farmer BP Management)"],
        "estimated_btp_services": ["BTP Integration Suite", "SAP Build Apps", "SAP Build Work Zone (standard edition)"],
        "btp_licensing_impact": "BTP consumption licensing adds approximately 15-25% to the S/4HANA subscription cost. The the regional mobile money provider integration iFlow is the primary cost driver due to high transaction volume (3,200+ farmer payments per harvest season). Evaluate BTP Enterprise Agreement vs. pay-as-you-go."
      }
    },

    "risk_assessment": {
      "overall_risk_level": "Medium",
      "per_module_risks": [
        {
          "module_code": "MM",
          "risk_level": "High",
          "risks": [
            {
              "risk_description": "Smallholder farmer procurement model is non-standard for SAP. High-volume, low-value spot purchases from 3,200+ individual suppliers do not match SAP's expected procurement patterns.",
              "risk_category": "Functional",
              "likelihood": "High",
              "impact": "High",
              "mitigation": "Prototype the farmer intake process early in the Explore phase. Conduct a 2-week spike to validate whether simplified PO processing or a BTP mobile app is the right approach. Engage SAP's Agribusiness industry team for reference architectures."
            },
            {
              "risk_description": "Farmer master data quality is likely very poor — inconsistent names, no formal IDs for some farmers, duplicate records across WhatsApp groups.",
              "risk_category": "Data",
              "likelihood": "High",
              "impact": "Medium",
              "mitigation": "Allocate 4-6 weeks for farmer master data cleansing and enrichment before go-live. Define minimum required fields for farmer BP records. Consider a field registration campaign with mobile app capturing farmer photo, GPS location, and national ID (where available)."
            }
          ]
        },
        {
          "module_code": "BTP",
          "risk_level": "High",
          "risks": [
            {
              "risk_description": "the regional mobile money provider API integration is a custom development effort with dependencies on a third-party payment platform. API changes, uptime, and transaction limits are outside HHE/SAP control.",
              "risk_category": "Integration",
              "likelihood": "Medium",
              "impact": "High",
              "mitigation": "Engage the regional mobile money provider technical team early for API documentation and sandbox access. Build robust error handling and retry logic. Implement a fallback manual payment process for system outages. Define SLA expectations with the regional mobile money provider."
            },
            {
              "risk_description": "Internet connectivity at rural collection points may be unreliable, affecting mobile farmer intake app and real-time data sync.",
              "risk_category": "Technical",
              "likelihood": "High",
              "impact": "Medium",
              "mitigation": "Design the mobile app with offline-first architecture. Data syncs when connectivity is available. Implement conflict resolution for concurrent offline edits."
            }
          ]
        },
        {
          "module_code": "FI",
          "risk_level": "Low",
          "risks": [
            {
              "risk_description": "Tanzania tax localization (EFRIS e-invoicing, withholding tax) may not be fully covered by SAP standard country version.",
              "risk_category": "Compliance",
              "likelihood": "Medium",
              "impact": "Medium",
              "mitigation": "Verify SAP Tanzania localization coverage in SAP Note 2793345 or current equivalent. If gaps exist, evaluate SAP Document Compliance or BTP-based integration with URA EFRIS portal."
            }
          ]
        }
      ],
      "cross_cutting_risks": [
        {
          "risk_description": "Change management: Moving from Excel and WhatsApp to SAP S/4HANA is a massive operational transformation for a 50-person company with no prior ERP experience. User adoption failure is the single biggest risk to project success.",
          "risk_category": "Organizational",
          "affected_modules": ["ALL"],
          "mitigation": "Invest heavily in change management and training. Identify 3-5 internal super users and train them intensively. Use Fiori's intuitive UX as a selling point. Consider a pilot deployment with the headquarters team before rolling out to field operations. Budget 15-20% of project cost for change management activities."
        },
        {
          "risk_description": "Scope creep: Budget is tight and investor-funded. Every additional module, extension, or customization increases cost. Risk of over-promising during scoping and under-delivering during implementation.",
          "risk_category": "Organizational",
          "affected_modules": ["ALL"],
          "mitigation": "Define a firm Phase 1 scope (FI, CO, MM, SD, QM core) and resist scope additions during implementation. Defer GTS, PP, PM, and advanced BTP extensions to Phase 2. Use MoSCoW prioritization for all requirements."
        },
        {
          "risk_description": "SAP may be over-engineered for a company of this size. SAP Business One or a cloud ERP alternative (Odoo, ERPNext, Xero + trade-specific add-ons) might deliver 80% of the value at 30% of the cost.",
          "risk_category": "Functional",
          "affected_modules": ["ALL"],
          "mitigation": "This is an important strategic question for the client. The Module Fit Analysis should be shared alongside a brief comparison with SAP Business One (which targets companies under $50M revenue). If revenue is under $5M, SAP Business One or SAP GROW with S/4HANA Cloud Public Edition starter package may be more appropriate. Recommend a cost-benefit comparison before proceeding to implementation roadmap."
        }
      ]
    },

    "sap_toolchain_integration": {
      "signavio_recommendations": [
        {
          "use_case": "Define target-state processes using SAP Best Practice process flows as starting templates. HHE has no existing processes to mine — focus is on target-state design, not current-state analysis.",
          "timing": "During Explore",
          "modules_affected": ["MM", "SD", "QM"],
          "value_proposition": "Signavio Process Navigator provides pre-built SAP Best Practice process diagrams for procurement, sales, and quality management. These can be used as the baseline for Fit-to-Standard workshops, reducing design effort by 30-40%."
        },
        {
          "use_case": "Process compliance monitoring post go-live — verify that actual usage matches designed processes.",
          "timing": "Post Go-Live",
          "modules_affected": ["ALL"],
          "value_proposition": "Signavio Process Intelligence can analyze SAP transaction logs to identify process deviations, bottlenecks, and automation opportunities after go-live."
        }
      ],
      "leanix_recommendations": [
        {
          "use_case": "Not recommended at this stage",
          "timing": "N/A",
          "value_proposition": "HHE's application landscape is minimal (Excel, the regional mobile money provider, WordPress). LeanIX application rationalization is not justified until the landscape grows significantly."
        }
      ],
      "cloud_alm_setup": {
        "requirements_to_track": 28,
        "solution_processes_to_configure": ["Procure-to-Pay (MM/FI)", "Order-to-Cash (SD/FI)", "Record-to-Report (FI/CO)", "Quality Management (QM/MM)"],
        "test_scope_implications": "Integration testing is critical for the MM-QM-SD-FI chain. End-to-end test scenarios should trace a cashew lot from farmer purchase through export sale and financial settlement.",
        "deployment_tracking_needs": "Single go-live cutover. Cloud ALM Deployment Management for transport tracking and go-live readiness assessment."
      }
    },

    "sizing_recommendation": {
      "recommended_deployment_model": "S/4HANA Cloud Public Edition",
      "sap_program": "SAP GROW",
      "rationale": "HHE's profile (sub-$10M revenue, 65 employees, greenfield, no existing SAP footprint, budget-conscious, willingness to adopt standard processes) aligns precisely with SAP GROW's target market. S/4HANA Cloud Public Edition via GROW provides: (1) lowest total cost of ownership, (2) pre-activated best practice scope items, (3) quarterly innovation cycle without upgrade projects, (4) Clean Core compliance by design (Public Edition enforces standard). The key constraint is that Public Edition scope items must cover HHE's needs — the module fit analysis above confirms they do for the core scope.",
      "alternative_considered": "SAP Business One (Cloud or On-Premise)",
      "alternative_rationale": "SAP Business One targets SMEs under $50M revenue and may be more cost-appropriate for HHE at its current size. Business One offers financials, procurement, inventory, sales, and basic production in a single, simpler package. However, Business One lacks the depth of batch management, QM, and the BTP extension ecosystem that HHE needs for premium cashew traceability. RECOMMENDATION: If budget analysis shows S/4HANA Cloud via GROW exceeds investor appetite, evaluate SAP Business One as a credible alternative. If HHE's growth trajectory is confirmed (7,000 farmers, new markets), S/4HANA via GROW is the better long-term investment.",
      "estimated_total_users": {
        "professional": 8,
        "limited_professional": 10,
        "developer": 1
      },
      "estimated_system_sizing": "XS",
      "high_availability_needs": "No",
      "disaster_recovery_needs": "No",
      "notes": "Total estimated users: 19 (8 Professional + 10 Limited Professional + 1 Developer). This is well within S/4HANA Cloud Public Edition minimum thresholds. SAP GROW starter packages typically begin at 20-30 Professional user equivalents. Actual sizing confirmation needed with SAP during the commercial proposal phase."
    },

    "downstream_handoff": {
      "ready_for_roadmap_generation": true,
      "ready_for_proposal_drafting": true,
      "module_priority_sequence": ["FI", "CO", "MM", "SD", "QM", "BTP", "WM", "GTS"],
      "key_decisions_needed_before_roadmap": [
        "Client confirmation of revenue range (drives product selection: S/4HANA GROW vs. Business One)",
        "Budget envelope confirmation from investor",
        "Confirmation of single plant vs. dual plant organizational structure",
        "Decision on Phase 1 the regional mobile money provider integration approach (full BTP integration vs. manual payment with Excel bridge)"
      ],
      "recommended_next_steps": [
        "1. Share this Module Fit Analysis with HHE stakeholders for validation",
        "2. Conduct a 2-hour workshop to resolve key design decisions (org structure, farmer master data strategy, the regional mobile money provider integration approach)",
        "3. Run SAP Digital Discovery Assessment (DDA) to validate scope item selection against S/4HANA Cloud Public Edition catalog",
        "4. Request SAP GROW commercial proposal based on estimated 19 users and confirmed module scope",
        "5. Proceed to Skill 03 (Implementation Roadmap Generator) with validated module scope and decisions"
      ],
      "signals_for_skill_03": {
        "phase_1_candidates": ["FI", "CO", "MM", "SD", "QM"],
        "phase_2_candidates": ["BTP (mobile farmer intake app)", "WM (embedded EWM upgrade)", "GTS"],
        "future_phase_candidates": ["PP", "PM", "HCM/SF"],
        "critical_path_modules": ["FI", "MM"]
      },
      "signals_for_skill_04": {
        "headline_value_drivers": [
          "End-to-end cashew lot traceability — from farmer to export buyer — enabling premium specialty pricing",
          "Automated multi-currency financial management replacing manual Excel reconciliation",
          "Scalable platform supporting growth from 3,200 to 7,000+ farmers without system replacement",
          "Investor-grade financial reporting (real-time P&L, balance sheet, cash flow)"
        ],
        "key_risk_messages": [
          "Change management is the primary risk — team has no ERP experience",
          "the regional mobile money provider mobile money integration is custom development — budget accordingly",
          "SAP Business One should be evaluated as a cost-effective alternative if budget is constrained"
        ],
        "investment_justification_data": [
          "Estimated 19 SAP users (8 Professional + 10 Limited Professional + 1 Developer)",
          "S/4HANA Cloud Public Edition via SAP GROW — lowest TCO deployment model",
          "Phase 1 scope: 5 core modules (FI, CO, MM, SD, QM) — achievable in 6-9 months with GROW accelerated methodology",
          "Phase 2 adds BTP extensions (mobile app, advanced the regional mobile money provider integration) and optional GTS"
        ]
      }
    }
  }
}
```

---

## Integration Points

| Downstream Skill | Data Consumed from Module Fit Analysis | How It Is Used |
|---|---|---|
| **03 Implementation Roadmap Generator** | `signals_for_skill_03` (phase candidates, critical path), `integration_dependency_map` (mandatory bundles), `sizing_recommendation` (deployment model), `risk_assessment` (complexity drivers) | Determines phase sequencing, milestone dates, resource requirements, and critical path scheduling. Mandatory bundles must be in the same phase. Risk levels calibrate timeline buffers. |
| **04 Executive Proposal Drafter** | `signals_for_skill_04` (value drivers, risk messages, investment data), `sizing_recommendation` (deployment model, user counts, SAP program), `module_assessment_matrix` (relevance and fit scores for executive summary) | Frames the business case narrative, structures the investment ask, articulates risks in executive language, and provides the quantitative foundation for the proposal. |
| **05 SAP Best Practices Fetcher** | `module_assessment_matrix` (key scope items per module), `clean_core_compliance` (extension requirements), `sizing_recommendation` (deployment model determines which scope item catalog to query) | Pulls detailed SAP Best Practice content for each identified scope item, retrieves process flow diagrams, and fetches configuration guides. Scope item IDs from this skill are the lookup keys for Skill 05. |

---

## Prompt Engineering Notes

### Key Design Decisions

1. **1-5 Fit Scoring Scale:** A five-point scale provides sufficient granularity to distinguish between "standard out-of-the-box" (5) and "SAP does not support this" (1) while remaining simple enough for non-technical stakeholders to interpret. Three-point scales (Red/Amber/Green) lose the distinction between "needs configuration" and "needs customization" — a difference that has significant cost implications. Scales above 5 add false precision without improving decision quality.

2. **Per-Module Clean Core Assessment:** Clean Core compliance is assessed per module rather than as a single aggregate score because different modules have different extension profiles. A client might be Clean Core Level A on FI/CO but Level C on MM due to a custom procurement workflow. Per-module assessment enables targeted remediation and helps Skill 03 sequence phases to prioritize Clean Core-compliant modules first.

3. **Mandatory Bundle Identification:** Identifying modules that must be implemented together prevents a common implementation anti-pattern: deploying FI without MM-FI integration, or SD without FI-AR integration, which leads to manual rekeying and reconciliation issues. The bundle concept directly informs Skill 03's phase design.

4. **SAP Business One Flagging:** For small companies (under 200 employees, sub-$50M revenue), including SAP Business One as an alternative recommendation is critical for consultant credibility. Recommending full S/4HANA to a 50-person company without acknowledging Business One would be a red flag to any experienced SAP advisor. This analysis preserves optionality rather than forcing a product decision prematurely.

5. **Scope Item ID References:** Including SAP Best Practice scope item IDs (e.g., "1YR", "J58", "BKP") creates a direct bridge to SAP's own catalog and enables Skill 05 to fetch detailed content. These IDs are the common language between this analysis and SAP's Digital Discovery Assessment tool.

6. **Integration Dependency Map as First-Class Object:** Many fit/gap analyses treat integration as an afterthought. By making the dependency map a core output section (not an appendix), this skill forces integration considerations into the scoping conversation early — when changes are cheap rather than during Realize phase when they are expensive.

7. **Sizing Recommendation Includes Product Alternative:** The sizing section does not just recommend a deployment model — it explicitly considers whether S/4HANA is the right product at all. This mirrors what a responsible SAP partner would do: right-sizing the solution to the client rather than pushing the largest possible deal.

### Iteration History

**v1 (Initial):** Simple module-by-module fit/gap table with Red/Amber/Green scoring. Problems: no integration dependency analysis, no Clean Core assessment, no sizing recommendation, no cross-module design considerations. Output was too thin to drive implementation planning.

**v2 (Current):** Expanded to include the 1-5 fit scoring scale, per-module Clean Core assessment, integration dependency map with mandatory bundles, cross-module organizational structure design, risk assessment, SAP toolchain integration points, and sizing recommendation with product alternative analysis. Added the downstream handoff section with explicit signals for Skills 03 and 04. The Highland Harvest Exports Ltd. example (a fictional benchmarking scenario) was built as a complete, realistic output to serve as a few-shot example for the LLM.

**Planned v3 improvements:**
- Add SAP Solution Manager / Focused Build work package estimation to map modules to implementation effort in person-days
- Incorporate SAP Roadmap Viewer data to flag modules where SAP's published roadmap includes planned features that could close current gaps (avoiding premature customization)
- Add a "Total Cost of Ownership" estimation section that aggregates licensing, implementation, BTP, and ongoing support costs per module
- Integrate with SAP Discovery Center to auto-validate scope item availability for the recommended deployment model
- Add competitive gap analysis section (how would this scope look on Oracle Cloud ERP, Microsoft Dynamics 365, or Odoo?)
