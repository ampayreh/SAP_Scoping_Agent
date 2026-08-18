# Skill 01: Client Discovery Intake Agent

## Purpose

Transform unstructured client information into a standardized, structured discovery brief that serves as the foundation for all downstream scoping skills. This skill replicates the work an SAP Enterprise Architect performs during the **Discover phase** of SAP Activate — gathering context, identifying gaps in understanding, and producing a normalized intake document that multiple workstreams can consume.

**SAP Ecosystem Positioning:** This skill operates upstream of SAP's Digital Discovery Assessment (DDA) tool and Joule for Consultants (J4C). While DDA evaluates requirements against scope items and J4C retrieves implementation guidance, neither captures and structures the raw client context that feeds those tools. The structured discovery brief produced here could be exported into SAP Cloud ALM as project context or used to seed a LeanIX application inventory.

---

## Inputs

The agent accepts **any combination** of the following, in any format (narrative text, bullet points, meeting notes, email threads, RFP excerpts):

| Input Category | Description | Examples |
|---|---|---|
| **Company Profile** | Basic firmographics | Industry, revenue, employee count, geographies, legal entities |
| **Current IT Landscape** | Existing systems and tools | ERP (SAP ECC, Oracle, Odoo, spreadsheets), CRM, WMS, BI tools, custom applications |
| **Pain Points** | Business problems driving the initiative | Manual processes, data silos, compliance gaps, reporting delays, scalability issues |
| **Strategic Objectives** | What the client wants to achieve | Digital transformation, cloud migration, M&A integration, IPO readiness, operational efficiency |
| **Compliance & Regulatory** | Industry/geography-specific requirements | SOX, GDPR, IFRS, FDA, export controls, local tax regulations |
| **Budget & Timeline Signals** | Any indications of constraints | Fiscal year deadlines, board-mandated timelines, budget ranges |
| **Stakeholder Context** | Decision-making dynamics | Executive sponsor, IT leadership maturity, change readiness, prior failed implementations |
| **Process Landscape** | Key business processes | Order-to-cash, procure-to-pay, record-to-report, plan-to-produce, hire-to-retire |

**Minimum viable input:** The agent can work with as little as a company name and industry, but will flag all missing dimensions and generate clarifying questions.

---

## Output: Structured Discovery Brief

The agent produces a structured JSON-compatible discovery brief with the following schema:

```json
{
  "discovery_brief": {
    "metadata": {
      "brief_id": "DB-{YYYYMMDD}-{CLIENT_SHORT}",
      "created_date": "ISO 8601",
      "data_completeness_score": "0-100%",
      "confidence_level": "HIGH | MEDIUM | LOW",
      "missing_information_flags": ["list of gaps"],
      "clarifying_questions": ["prioritized questions to fill gaps"]
    },

    "client_profile": {
      "company_name": "",
      "industry": "{SAP industry code + description}",
      "sub_industry": "",
      "revenue_range": "",
      "employee_count": "",
      "geographic_footprint": {
        "headquarters": "",
        "operating_countries": [],
        "legal_entities": 0,
        "currencies": []
      },
      "ownership_structure": "Public | Private | PE-backed | Family-owned | Government",
      "growth_trajectory": "Stable | Growing | Rapid growth | Contracting | M&A active"
    },

    "current_landscape": {
      "erp_current": {
        "system": "",
        "version": "",
        "deployment": "On-premise | Cloud | Hybrid",
        "customization_level": "Minimal | Moderate | Heavy",
        "estimated_custom_objects": "",
        "pain_points": []
      },
      "adjacent_systems": [
        {
          "category": "CRM | WMS | BI | HR | MES | PLM | Other",
          "product": "",
          "integration_method": "API | File | Manual | None",
          "data_quality": "Good | Fair | Poor | Unknown"
        }
      ],
      "data_landscape": {
        "master_data_quality": "Good | Fair | Poor | Unknown",
        "data_governance_maturity": "Established | Emerging | None",
        "estimated_data_volume": ""
      },
      "existing_sap_footprint": {
        "has_sap": true,
        "products": [],
        "btp_usage": "Yes | No | Planned",
        "signavio_usage": "Yes | No | Planned",
        "leanix_usage": "Yes | No | Planned"
      }
    },

    "business_requirements": {
      "primary_drivers": [],
      "process_pain_points": [
        {
          "process_area": "{SAP standard process name}",
          "current_state": "",
          "desired_state": "",
          "impact": "High | Medium | Low",
          "sap_module_relevance": []
        }
      ],
      "must_have_capabilities": [],
      "nice_to_have_capabilities": [],
      "explicit_exclusions": []
    },

    "compliance_and_regulatory": {
      "regulatory_frameworks": [],
      "industry_standards": [],
      "audit_requirements": [],
      "data_residency_requirements": [],
      "export_control_considerations": ""
    },

    "transformation_context": {
      "transformation_type": "Greenfield | Brownfield | Bluefield | System Conversion",
      "deployment_preference": "Public Cloud | Private Cloud | On-Premise | Hybrid",
      "clean_core_readiness": {
        "awareness": "High | Medium | Low | None",
        "willingness_to_adopt_standard": "High | Medium | Low",
        "estimated_custom_code_to_evaluate": ""
      },
      "timeline_signals": {
        "target_go_live": "",
        "hard_deadline": true,
        "driver": "Contract expiration | Fiscal year | Regulatory | Board mandate | Other"
      },
      "budget_signals": {
        "range_indicated": "",
        "funding_approved": "Yes | Partial | Not yet",
        "budget_owner": ""
      },
      "change_management_readiness": {
        "executive_sponsorship": "Strong | Moderate | Weak | Unknown",
        "prior_erp_experience": "Successful | Mixed | Failed | None",
        "organizational_change_capacity": "High | Medium | Low | Unknown",
        "training_infrastructure": ""
      }
    },

    "stakeholder_map": {
      "executive_sponsor": "",
      "project_champion": "",
      "it_leadership": "",
      "key_business_process_owners": [],
      "known_resistors_or_risks": []
    },

    "initial_module_signals": {
      "high_relevance": [],
      "medium_relevance": [],
      "low_relevance": [],
      "rationale": ""
    },

    "downstream_handoff": {
      "ready_for_module_fit_analysis": true,
      "recommended_next_steps": [],
      "information_to_gather_before_proceeding": [],
      "sap_tools_to_engage": {
        "cloud_alm": "Recommended for project setup once scope is confirmed",
        "signavio": "Recommended if client needs process mining of current state",
        "leanix": "Recommended if client has complex application portfolio to rationalize",
        "dda": "Recommended for scope item validation against S/4HANA Cloud catalog"
      }
    }
  }
}
```

---

## Step-by-Step Behavior

### Step 1: Input Parsing and Normalization

- Accept input in any format (free text, bullets, tables, meeting notes)
- Extract all identifiable facts and categorize them against the discovery brief schema
- Normalize industry terminology to SAP industry classification codes (e.g., "cashew export" → "Consumer Products — Agricultural Commodities" / SAP Industry: CP)
- Normalize process terminology to SAP standard process names (e.g., "shipping and invoicing" → "Order-to-Cash (OTC)" with sub-processes "Outbound Delivery" and "Billing")

### Step 2: Completeness Assessment

- Score data completeness (0-100%) across all schema fields
- Flag every missing field with severity:
  - **Critical (blocks downstream analysis):** Industry, employee count, current ERP, primary drivers
  - **Important (reduces accuracy):** Revenue range, geographic footprint, compliance requirements, timeline
  - **Helpful (improves richness):** Stakeholder map, budget signals, change readiness, data quality
- Generate **prioritized clarifying questions** for all Critical and Important gaps, ordered by impact on downstream skill accuracy

### Step 3: Inference and Enrichment

Where explicit data is missing, make reasonable inferences based on available context. Always mark inferences clearly:

- **Industry-based inference:** If an agricultural export company in East Africa is mentioned, infer multi-currency requirements (local currency, USD, EUR), export compliance needs, agricultural commodity-specific processes
- **Size-based inference:** Employee count and revenue drive assumptions about module complexity, user licensing, and implementation timeline
- **Geography-based inference:** Operating countries drive tax localization, language, and data residency requirements
- **Current landscape inference:** If "Excel-based" processes are mentioned, infer low digitization maturity, significant change management need, and greenfield transformation type

All inferences must be flagged with `[INFERRED]` tags and the reasoning documented.

### Step 4: Initial Module Signal Generation

Based on the parsed and enriched data, generate preliminary module relevance signals:

- Map stated business requirements to SAP S/4HANA modules
- Use SAP standard module abbreviations: FI, CO, MM, SD, PP, QM, PM, PS, WM/EWM, HCM/SuccessFactors, TM, GTS, RE-FX, etc.
- Classify as High / Medium / Low relevance with brief rationale
- Note: This is a directional signal only — detailed fit/gap is performed by Skill 02

### Step 5: Clean Core Pre-Assessment

Evaluate the client's readiness and alignment with SAP's Clean Core strategy:

- Assess current customization level and willingness to adopt standard processes
- Flag potential Clean Core challenges (heavy custom ABAP, non-standard integrations, regulatory-driven customizations)
- Note where BTP extensions may be needed to preserve Clean Core compliance
- Reference SAP's 4-level Clean Core maturity model (A through D)

### Step 6: SAP Toolchain Recommendations

Based on the client profile, recommend which SAP tools should be engaged and when:

- **SAP Cloud ALM:** Always — for project governance once scope is confirmed
- **SAP Signavio:** If the client needs process mining of their current state or wants to benchmark against SAP best practices (5,000+ reference processes)
- **SAP LeanIX:** If the client has a complex application portfolio that needs rationalization before migration
- **Digital Discovery Assessment (DDA):** For scope item validation against the S/4HANA Cloud catalog
- **Joule for Consultants (J4C):** For deep-dive configuration questions during Explore phase

### Step 7: Output Assembly and Quality Check

- Assemble the complete discovery brief in the structured schema
- Validate internal consistency (e.g., timeline expectations vs. scope complexity)
- Flag any contradictions in client input (e.g., "minimal budget" + "aggressive timeline" + "large scope")
- Generate the `downstream_handoff` section with explicit readiness assessment for Skill 02

---

## Constraints and Failure Modes

| Constraint | Handling |
|---|---|
| **Insufficient input** | If data completeness < 30%, return a partial brief with prominent warning and list of must-answer questions before proceeding |
| **Off-topic / non-SAP request** | If the input has no plausible connection to an SAP implementation (e.g., a marketing campaign, unrelated software request, general business advice), decline concisely in 2-3 sentences: state that this is an SAP scoping agent, name what it does instead, and stop. Do not produce a discovery brief, do not speculate about hypothetical SAP angles on the request, and do not generate deliverables from the off-topic domain (no campaign plans, no creative concepts, no unrelated advice) — even partially or as an illustration. |
| **Contradictory input** | Flag contradictions explicitly (e.g., "Client states both 'no budget constraints' and '$500K total budget'") and ask for clarification |
| **Industry not recognized** | Map to nearest SAP industry classification and flag for human review |
| **Ambiguous scope** | Default to broader scope with explicit flags (better to over-scope at discovery than miss modules) |
| **Client using non-SAP terminology** | Translate to SAP standard terms with a terminology mapping appendix |
| **Input contains PII or sensitive data** | Process the data for scoping purposes but flag any fields that should be redacted in shared documents |
| **Over-reliance on inference** | If >50% of the brief is inferred rather than stated, set confidence_level to LOW and strongly recommend a client validation workshop |

---

## Example Usage

> **Fictional scenario.** This company, its founder, and every figure below are invented for benchmarking purposes. No resemblance to any real business is intended.

### Sample Input

```
We're a raw cashew export company based in the Southern Highlands of Tanzania called
Highland Harvest Exports (we sell under the brand "Mlima"). About 65 permanent employees,
scaling to 110+ in peak season. We buy raw cashew nuts from 3,200+ smallholder farmers
across the region, process them at our facilities, and export to specialty buyers in
Europe, North America, and Asia.

Currently everything runs on Excel spreadsheets and WhatsApp groups. We use a regional
mobile money provider for farmer collections and have a basic Wix website. No ERP at all.

Our biggest pain points:
- We can't track inventory from farm gate to export container accurately
- Currency management is a nightmare (TZS for farmer payments, USD for exports, EUR for
  some European buyers, plus CAD, KRW, and INR occasionally)
- Export documentation takes forever — phytosanitary certificates, weight notes,
  bills of lading, EU food-safety traceability forms
- We have no real financial reporting — everything is reconciled manually at month end
- Kernel-grade traceability is critical for premium buyers but we're doing it on paper
- We want to scale to 7,000 farmers in the next 2 years but our systems can't handle
  the current volume

We've heard about SAP but honestly don't know if it's the right fit for a company our
size. Budget is tight but our lead investor is willing to fund technology if the ROI is clear.
```

### Sample Output

```json
{
  "discovery_brief": {
    "metadata": {
      "brief_id": "DB-20260217-HHE",
      "created_date": "2026-02-17T00:00:00Z",
      "data_completeness_score": "62%",
      "confidence_level": "MEDIUM",
      "missing_information_flags": [
        "CRITICAL: Revenue range not provided — needed for licensing model recommendation",
        "CRITICAL: No timeline or go-live target indicated",
        "IMPORTANT: No compliance/regulatory details beyond export documentation",
        "IMPORTANT: No IT staffing or technical capability assessment",
        "IMPORTANT: Investor structure and budget range not quantified",
        "HELPFUL: No stakeholder map — who makes the final decision?",
        "HELPFUL: No current technology infrastructure details (servers, internet reliability, mobile coverage)"
      ],
      "clarifying_questions": [
        "1. What is Highland Harvest Exports's annual revenue range? (This determines whether S/4HANA Cloud Public Edition, Private Edition, or an alternative like SAP Business One or SAP Grow is the right fit)",
        "2. Is there a target go-live date or external deadline driving this initiative?",
        "3. Who is the executive sponsor and final decision-maker for this technology investment?",
        "4. What is the investor's budget envelope for technology — are we talking $50K, $200K, $500K+?",
        "5. What does your current IT infrastructure look like? Reliable internet connectivity? On-site servers or fully cloud-based? Staff with technical skills?",
        "6. Are there specific regulatory requirements from the Tanzania Cashewnut Board or export licensing bodies that must be supported?",
        "7. Do you currently export under any certification programs (Fairtrade, Rainforest Alliance, Organic)? These drive traceability requirements.",
        "8. How many concurrent users would need system access? (Field agents, collection station staff, office staff, management)"
      ]
    },

    "client_profile": {
      "company_name": "Highland Harvest Exports Ltd. (HHE)",
      "industry": "Consumer Products — Agricultural Commodities (SAP Industry: CP)",
      "sub_industry": "Raw Cashew Nut Processing and Export",
      "revenue_range": "[UNKNOWN — CRITICAL GAP]",
      "employee_count": "~65 permanent, up to 110+ in peak season",
      "geographic_footprint": {
        "headquarters": "Southern Highlands Zone, Tanzania",
        "operating_countries": ["Tanzania"],
        "operating_regions": ["Southern Highlands (sourcing)", "Europe, North America, Asia (export markets)"],
        "legal_entities": "[INFERRED: 1 — single entity assumed unless stated otherwise]",
        "currencies": ["TZS", "USD", "EUR", "CAD", "KRW", "INR"]
      },
      "ownership_structure": "[INFERRED: Private, investor-backed]",
      "growth_trajectory": "Rapid growth — targeting 2.2x farmer base expansion (3,200 → 7,000) in 2 years"
    },

    "current_landscape": {
      "erp_current": {
        "system": "None — Excel spreadsheets",
        "version": "N/A",
        "deployment": "N/A",
        "customization_level": "N/A (no ERP)",
        "estimated_custom_objects": "N/A",
        "pain_points": [
          "No inventory traceability from farm gate to export",
          "Manual multi-currency management",
          "Paper-based export documentation",
          "Manual month-end financial reconciliation",
          "Paper-based kernel-grade traceability",
          "Systems cannot scale to support growth targets"
        ]
      },
      "adjacent_systems": [
        {
          "category": "Payment Processing",
          "product": "Regional mobile money provider (farmer collections)",
          "integration_method": "Manual [INFERRED]",
          "data_quality": "Unknown"
        },
        {
          "category": "Web Presence",
          "product": "Wix",
          "integration_method": "None",
          "data_quality": "N/A"
        },
        {
          "category": "Communication",
          "product": "WhatsApp (operational coordination)",
          "integration_method": "Manual",
          "data_quality": "Poor [INFERRED — no structured data capture]"
        }
      ],
      "data_landscape": {
        "master_data_quality": "Poor [INFERRED — Excel-based with no governance]",
        "data_governance_maturity": "None [INFERRED]",
        "estimated_data_volume": "Low [INFERRED — 65 employees, 3,200 farmers]"
      },
      "existing_sap_footprint": {
        "has_sap": false,
        "products": [],
        "btp_usage": "No",
        "signavio_usage": "No",
        "leanix_usage": "No"
      }
    },

    "business_requirements": {
      "primary_drivers": [
        "End-to-end inventory traceability (farm gate to export container)",
        "Multi-currency financial management",
        "Export documentation automation",
        "Financial reporting and month-end close",
        "Kernel-grade traceability for premium buyers",
        "Scalability to support 2.2x growth"
      ],
      "process_pain_points": [
        {
          "process_area": "Inventory Management / Warehouse Management",
          "current_state": "Excel tracking, no farm-to-container traceability",
          "desired_state": "Full lot traceability with batch management from farmer purchase through processing, grading, and export",
          "impact": "High",
          "sap_module_relevance": ["MM", "WM", "QM", "SD"]
        },
        {
          "process_area": "Financial Accounting — Multi-Currency",
          "current_state": "Manual currency conversion, manual reconciliation",
          "desired_state": "Automated multi-currency processing with real-time FX handling for TZS/USD/EUR/CAD/KRW/INR",
          "impact": "High",
          "sap_module_relevance": ["FI", "CO"]
        },
        {
          "process_area": "Foreign Trade / Export Management",
          "current_state": "Manual document preparation (phytosanitary, weight notes, bills of lading, EU food-safety forms)",
          "desired_state": "Automated export documentation with compliance checks",
          "impact": "High",
          "sap_module_relevance": ["SD", "GTS"]
        },
        {
          "process_area": "Record-to-Report",
          "current_state": "Manual month-end reconciliation from spreadsheets",
          "desired_state": "Automated financial close with real-time reporting",
          "impact": "High",
          "sap_module_relevance": ["FI", "CO"]
        },
        {
          "process_area": "Quality Management",
          "current_state": "Paper-based quality tracking",
          "desired_state": "Digital quality records with full traceability (outturn ratio, moisture, whole/broken kernel count, defect rate)",
          "impact": "High",
          "sap_module_relevance": ["QM"]
        },
        {
          "process_area": "Procurement — Farmer Payments",
          "current_state": "Mobile money, WhatsApp coordination",
          "desired_state": "Integrated procurement with mobile money payment processing for 7,000+ smallholder farmers",
          "impact": "Medium",
          "sap_module_relevance": ["MM", "FI-AP"]
        }
      ],
      "must_have_capabilities": [
        "Batch/lot traceability",
        "Multi-currency (minimum TZS, USD, EUR)",
        "Export documentation support",
        "Financial reporting (P&L, balance sheet, cash flow)",
        "Mobile access for field operations [INFERRED]"
      ],
      "nice_to_have_capabilities": [
        "Farmer relationship management (CRM-like)",
        "Certification tracking (Fairtrade, Organic, etc.) [INFERRED]",
        "Weather/harvest forecasting integration [INFERRED]",
        "Mobile money integration"
      ],
      "explicit_exclusions": []
    },

    "compliance_and_regulatory": {
      "regulatory_frameworks": [
        "Tanzania Cashewnut Board regulations [INFERRED]",
        "Export licensing — Tanzania Revenue Authority [INFERRED]",
        "Phytosanitary compliance — Ministry of Agriculture, Tanzania [INFERRED]",
        "EU food-safety import traceability documentation [STATED] — general import documentation, not EUDR (which does not cover cashew)"
      ],
      "industry_standards": [
        "[CLARIFICATION NEEDED: Fairtrade, Rainforest Alliance, Organic certifications?]"
      ],
      "audit_requirements": [
        "[INFERRED: Investor reporting requirements]"
      ],
      "data_residency_requirements": [
        "[UNKNOWN — need to confirm Tanzania Personal Data Protection Act, 2022 requirements]"
      ],
      "export_control_considerations": "Agricultural commodity export — phytosanitary, origin certificates, weight/quality documentation"
    },

    "transformation_context": {
      "transformation_type": "Greenfield [INFERRED — no existing ERP]",
      "deployment_preference": "Public Cloud [INFERRED — no IT infrastructure, budget-conscious, rapid deployment needed]",
      "clean_core_readiness": {
        "awareness": "None [INFERRED — no SAP experience]",
        "willingness_to_adopt_standard": "High [INFERRED — no existing customizations to protect; greenfield advantage]",
        "estimated_custom_code_to_evaluate": "N/A — greenfield"
      },
      "timeline_signals": {
        "target_go_live": "[UNKNOWN — CRITICAL GAP]",
        "hard_deadline": "[UNKNOWN]",
        "driver": "[UNKNOWN — possibly growth-driven: need systems before scaling to 7,000 farmers]"
      },
      "budget_signals": {
        "range_indicated": "Tight — but investor willing to fund with clear ROI",
        "funding_approved": "Partial — contingent on ROI business case",
        "budget_owner": "[UNKNOWN — likely investor + management]"
      },
      "change_management_readiness": {
        "executive_sponsorship": "Unknown",
        "prior_erp_experience": "None [INFERRED]",
        "organizational_change_capacity": "Unknown — significant concern given jump from Excel to ERP",
        "training_infrastructure": "[INFERRED: Limited — rural operations, potential connectivity challenges]"
      }
    },

    "stakeholder_map": {
      "executive_sponsor": "[UNKNOWN — CLARIFICATION NEEDED]",
      "project_champion": "[UNKNOWN]",
      "it_leadership": "[INFERRED: May not exist — no IT function mentioned]",
      "key_business_process_owners": [
        "[INFERRED: Operations/Collection Station Manager]",
        "[INFERRED: Finance/Accounting Lead]",
        "[INFERRED: Export/Logistics Manager]",
        "[INFERRED: Farmer Relations/Sourcing Lead]"
      ],
      "known_resistors_or_risks": [
        "[INFERRED: Field staff may resist digital tools if connectivity is unreliable]",
        "[INFERRED: Jump from Excel to SAP is significant — change management is a major risk factor]"
      ]
    },

    "initial_module_signals": {
      "high_relevance": [
        "FI (Financial Accounting) — multi-currency, financial reporting, month-end close",
        "CO (Controlling) — cost center accounting, profitability analysis by lot/buyer/region",
        "MM (Materials Management) — farmer procurement, inventory management, batch tracking",
        "SD (Sales & Distribution) — export sales order management, pricing, billing",
        "QM (Quality Management) — cashew kernel grading, outturn ratio, moisture, defect tracking"
      ],
      "medium_relevance": [
        "WM/EWM (Warehouse Management) — collection station and processing facility inventory",
        "GTS (Global Trade Services) — export compliance, trade documentation [if budget allows]",
        "BTP (Business Technology Platform) — mobile extensions, mobile money integration"
      ],
      "low_relevance": [
        "PP (Production Planning) — cashew processing is relatively simple vs. discrete manufacturing",
        "PM (Plant Maintenance) — limited equipment base at this scale",
        "PS (Project System) — not project-driven business",
        "HCM/SuccessFactors — 65 employees can be managed with lighter solution"
      ],
      "rationale": "Core scope centers on agricultural commodity procurement (MM), batch-managed inventory with full traceability (MM+QM), multi-currency financial management (FI/CO), and export order processing (SD). The company's growth ambitions and investor requirements drive the need for robust financial reporting. GTS is relevant but may be cost-prohibitive for a company this size — manual export doc handling may be acceptable in Phase 1. IMPORTANT NOTE: Given the company size (~65 employees) and budget sensitivity, SAP Business One or SAP S/4HANA Cloud Public Edition via SAP GROW should be evaluated as potentially better-fit alternatives to a full S/4HANA deployment."
    },

    "downstream_handoff": {
      "ready_for_module_fit_analysis": true,
      "recommended_next_steps": [
        "1. Client validation workshop to confirm inferences and fill Critical gaps (revenue, timeline, budget range, stakeholders)",
        "2. Proceed to Skill 02 (Module Fit Analyzer) with this brief — sufficient data for directional analysis",
        "3. Flag for sizing discussion: SAP S/4HANA Cloud vs. SAP Business One vs. SAP GROW for mid-market",
        "4. Assess IT infrastructure readiness (internet connectivity at collection station and field operations)"
      ],
      "information_to_gather_before_proceeding": [
        "Annual revenue range (determines product fit and licensing)",
        "Target go-live date or external deadline",
        "Confirmed budget envelope from investor",
        "Number of expected concurrent users by role",
        "Internet connectivity assessment at all operating locations"
      ],
      "sap_tools_to_engage": {
        "cloud_alm": "Recommended once scope is confirmed — set up project structure and requirements tracking",
        "signavio": "Not recommended at this stage — no existing processes to mine; focus on defining target-state processes using SAP best practices",
        "leanix": "Not recommended — application landscape is minimal (Excel, mobile money, Wix)",
        "dda": "Highly recommended — run Digital Discovery Assessment to validate scope item selection against S/4HANA Cloud Public Edition catalog and evaluate SAP GROW eligibility"
      }
    }
  }
}
```

---

## Integration Points

| Downstream Skill | How This Skill's Output Is Used |
|---|---|
| **02 Module Fit Analyzer** | Consumes the `business_requirements`, `initial_module_signals`, and `current_landscape` sections to perform detailed fit/gap scoring per module |
| **03 Implementation Roadmap** | Uses `transformation_context` (timeline, budget, change readiness) and `client_profile` (size, geography) to calibrate phasing and resource estimates |
| **04 Executive Proposal Drafter** | Uses `client_profile`, `primary_drivers`, and `stakeholder_map` to frame the narrative for the appropriate audience |
| **05 SAP Best Practices Fetcher** | Uses `industry`, `sub_industry`, and `initial_module_signals` to pull relevant SAP best practice scope items and industry-specific reference content |

---

## Prompt Engineering Notes

### Key Design Decisions

1. **Structured JSON output** rather than narrative: Ensures downstream skills can programmatically consume the brief without parsing ambiguity. Also mirrors how SAP Cloud ALM stores project artifacts.

2. **Explicit inference tagging** (`[INFERRED]`): Critical for trust and transparency. Consultants must be able to distinguish stated facts from AI assumptions. This also enables a feedback loop where clients can correct inferences.

3. **SAP terminology normalization**: Translating client language ("shipping") into SAP process names ("Outbound Delivery") early in the pipeline ensures consistency across all downstream skills and aligns with SAP Activate deliverable standards.

4. **Completeness scoring**: Quantifying data quality at intake prevents garbage-in-garbage-out problems in downstream skills. The score also serves as a signal to the consultant about whether to proceed or gather more data.

5. **SAP toolchain recommendations**: Including explicit guidance on when to use SAP's own tools (Cloud ALM, Signavio, LeanIX, DDA) positions this skills pack as complementary rather than competitive, and helps consultants make better tooling decisions.

### Iteration History

**v1 (Initial):** Simple extraction of facts into categories. Problem: no inference, no gap detection, no SAP terminology mapping. Output was too thin to drive downstream analysis.

**v2 (Current):** Added completeness scoring, inference engine with explicit tagging, SAP terminology normalization, initial module signals, Clean Core pre-assessment, and SAP toolchain recommendations. Significantly richer output that enables Skill 02 to run without additional client interaction in most cases.

**Planned v3 improvements:**
- Add SAP industry solution map alignment (e.g., SAP for Agribusiness scope items)
- Incorporate SAP GROW vs. RISE decision framework based on company size/maturity
- Add competitive landscape context (what if client is also evaluating Oracle Cloud, Dynamics 365, or Odoo?)
