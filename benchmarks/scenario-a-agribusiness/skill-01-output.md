# Skill 01 Output: Client Discovery Intake — Highland Harvest Exports (HHE)

> **Fictional scenario.** This company, its founder, its facilities, its buyers, and every figure below are invented for benchmarking purposes. No resemblance to any real business is intended.

## Input Sources
- Client brief (original scenario text)
- HHE website (mlima-cashew.example — placeholder domain) — farmer engagement articles
- Regional trade press — profile of founder Amina Cheyo
- Specialty importer product pages (fictional: Baltic Nut Traders EE, Meridian Food Import KR, Casa do Caju PT, Northgate Commodities CA, Sunrise Ingredients IN)
- Tanzania Cashewnut Board recognition coverage

---

## Structured Discovery Brief

```json
{
  "discovery_brief": {
    "metadata": {
      "brief_id": "DB-20260217-HHE",
      "created_date": "2026-02-17T00:00:00Z",
      "data_completeness_score": "74%",
      "confidence_level": "MEDIUM-HIGH",
      "missing_information_flags": [
        "CRITICAL: Exact annual revenue not disclosed — must estimate from container volume and market pricing",
        "IMPORTANT: Total farmer count not precisely stated — sources reference 1,800+ (trade press) and 3,200+ (original brief); actual number needs confirmation",
        "IMPORTANT: No formal IT infrastructure assessment — internet connectivity at Njombe collection station is unknown",
        "IMPORTANT: Budget envelope not quantified beyond 'tight but investor-funded'",
        "HELPFUL: No org chart or formal stakeholder map beyond founder Amina Cheyo",
        "HELPFUL: Certification status unclear — no Organic, Fairtrade, or Rainforest Alliance certifications mentioned in any source"
      ],
      "clarifying_questions": [
        "1. What is HHE's annual revenue? (With 20-35 containers/year at premium RCN pricing of $1.20-$2.10/kg FOB, estimated $900K-$3.1M — this determines SAP Business One vs. S/4HANA Cloud fit)",
        "2. How many active smallholder farmers currently supply HHE? (Sources conflict: 1,800+ vs. 3,200+ — this affects procurement module complexity)",
        "3. What is the internet connectivity situation at the Njombe collection station and Mafinga processing facility? (Determines cloud vs. hybrid deployment, offline capability needs)",
        "4. What is the investor's budget envelope for technology investment? ($60K, $180K, $350K+?)",
        "5. Does HHE hold or pursue any sustainability certifications (Organic, Fairtrade, Rainforest Alliance)? (Drives traceability and compliance module requirements)",
        "6. Who are the key decision-makers beyond founder Amina Cheyo? Is there a CFO, operations manager, or investor representative who needs to approve technology decisions?",
        "7. What is the target go-live date? Is it tied to a specific harvest season (October-December)?",
        "8. How many concurrent users would need system access? (Njombe station staff ~28, Mafinga facility 50-70 seasonal, office/management, field agents)"
      ]
    },

    "client_profile": {
      "company_name": "Highland Harvest Exports Ltd. (HHE)",
      "brand_name": "Mlima (Swahili word meaning 'mountain')",
      "industry": "Consumer Products — Agricultural Commodities (SAP Industry: CP)",
      "sub_industry": "Raw Cashew Nut Processing and Export",
      "revenue_range": "[ESTIMATED: $900K-$3.1M annually — based on 20-35 containers of raw cashew nuts at $1.20-$2.10/kg FOB. Premium pricing confirmed by presence with specialty import buyers in Europe and Asia]",
      "employee_count": {
        "njombe_collection_station": "~28 direct employees plus indirect (transporters)",
        "mafinga_processing_facility": "50-70 seasonal workers",
        "total_estimated": "~65 permanent, up to 110+ during peak season"
      },
      "geographic_footprint": {
        "headquarters": "Njombe area, Southern Highlands Zone, Tanzania",
        "processing_facility": "Mafinga area, Iringa Region, Tanzania",
        "sourcing_region": "Southern Highlands smallholder cashew belt, Tanzania (altitude 900-1,600 masl)",
        "operating_countries": ["Tanzania"],
        "export_markets": ["Estonia (Baltic Nut Traders)", "South Korea (Meridian Food Import)", "Portugal (Casa do Caju)", "Canada (Northgate Commodities)", "India (Sunrise Ingredients)", "Additional EU and North American buyers"],
        "legal_entities": "[INFERRED: 1 — single Tanzanian entity]",
        "currencies": ["TZS (farmer payments, local operations)", "USD (primary export currency)", "EUR (European buyers)", "CAD (Canadian buyers)", "KRW (South Korean buyers)", "INR (Indian buyers)"]
      },
      "ownership_structure": "Private, investor-backed",
      "founder": "Amina Cheyo (age ~42), entered cashew industry 2018, established HHE ~2020",
      "growth_trajectory": "Rapid growth — scaling from 20-35 containers/year with plans to expand farmer base from ~3,200 to 7,000 in 2 years; also planning a domestic retail line for the Dar es Salaam market"
    },

    "current_landscape": {
      "erp_current": {
        "system": "None — Excel spreadsheets, WhatsApp groups for operational coordination",
        "version": "N/A",
        "deployment": "N/A",
        "customization_level": "N/A (no ERP)",
        "estimated_custom_objects": "N/A",
        "pain_points": [
          "No inventory traceability from farm gate to export container",
          "Manual multi-currency management across 6 currencies",
          "Paper-based export documentation (phytosanitary, weight notes, bills of lading, EU food-safety traceability forms)",
          "Manual month-end financial reconciliation",
          "Paper-based kernel-grade traceability (outturn ratio, moisture, count — critical for premium buyers)",
          "Systems cannot scale to support 2.2x farmer base growth",
          "No lot-level cost tracking from farmer delivery through processing stages to export"
        ]
      },
      "adjacent_systems": [
        {
          "category": "Payment Processing",
          "product": "Regional mobile money provider (farmer payment collections)",
          "integration_method": "Manual [INFERRED]",
          "data_quality": "Unknown — likely transaction records available via provider dashboard"
        },
        {
          "category": "Web Presence / Brand",
          "product": "mlima-cashew.example (Wix)",
          "integration_method": "None",
          "data_quality": "N/A — marketing site only"
        },
        {
          "category": "Communication / Operations",
          "product": "WhatsApp (farmer coordination, field operations, logistics)",
          "integration_method": "Manual",
          "data_quality": "Poor [INFERRED — unstructured message-based coordination]"
        },
        {
          "category": "B2B Sales Channel",
          "product": "Direct relationships with international specialty importers",
          "integration_method": "Manual (email, WhatsApp)",
          "data_quality": "Unknown"
        }
      ],
      "data_landscape": {
        "master_data_quality": "Poor [INFERRED — Excel-based with no governance; farmer records likely incomplete]",
        "data_governance_maturity": "None [INFERRED]",
        "estimated_data_volume": "Low-Medium [1,800-3,200+ farmer records, seasonal purchase transactions, lot tracking through 4 processing stages]"
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
        "End-to-end lot traceability from farmer delivery through 4 processing stages (raw intake → drying → shelling → grading/export) to container shipment",
        "Multi-currency financial management (TZS, USD, EUR, CAD, KRW, INR)",
        "Export documentation automation (phytosanitary certificates, weight notes, bills of lading, EU food-safety traceability forms)",
        "Financial reporting for investor requirements and operational visibility",
        "Kernel-grade traceability to protect premium pricing (outturn ratio, moisture, whole/broken kernel count)",
        "Scalability to support 2.2x farmer base growth (3,200 → 7,000 farmers)",
        "EU food-safety import traceability compliance for European export market [INFERRED — EU market represents a meaningful share of HHE sales]"
      ],
      "process_pain_points": [
        {
          "process_area": "Agricultural Commodity Procurement (Procure-to-Pay variant)",
          "current_state": "Smallholder farmers deliver raw cashew nuts to collection points; purchased via mobile money; pricing based on quality grade with premium above market rate; no digital records of farmer-level transactions",
          "desired_state": "Digitized farmer procurement with mobile money integration, farmer master data with geo-coordinates (traceability), quality-linked differential pricing, batch creation at point of purchase",
          "impact": "High",
          "sap_module_relevance": ["MM", "FI-AP", "QM"]
        },
        {
          "process_area": "Inventory Management with Lot/Batch Traceability",
          "current_state": "Excel tracking; 4 processing stages (raw intake → drying → shelling → grading/export) tracked manually; no lot-level cost or quality linkage",
          "desired_state": "Full batch management with split valuation per lot; processing stage tracking via stock transfers; batch characteristics (origin region, moisture at intake, kernel count/size grade, outturn ratio, defect rate)",
          "impact": "High",
          "sap_module_relevance": ["MM", "WM", "QM"]
        },
        {
          "process_area": "Quality Management — Kernel Grading",
          "current_state": "Paper-based grading evaluations; quality records not linked to lots; difficult to prove traceability to premium buyers who require it for grade-based contracts",
          "desired_state": "Digital quality inspection at each processing stage; kernel grade records linked to batch; Certificate of Quality generation for buyers; defect tracking per industry grading standard",
          "impact": "High",
          "sap_module_relevance": ["QM"]
        },
        {
          "process_area": "Financial Accounting — Multi-Currency",
          "current_state": "Manual currency conversion across 6 currencies; manual month-end reconciliation from spreadsheets; no real-time visibility into profitability by lot, buyer, or market",
          "desired_state": "Automated multi-currency processing; real-time FX; profitability analysis by lot/buyer/region; investor-grade financial reporting (P&L, balance sheet, cash flow)",
          "impact": "High",
          "sap_module_relevance": ["FI", "CO"]
        },
        {
          "process_area": "Export Sales — Order-to-Cash",
          "current_state": "Manual sales orders via email/WhatsApp with international specialty importers; manual export documentation; pricing negotiated per contract with differential pricing by grade",
          "desired_state": "Structured export sales order management; automated export documentation (phytosanitary, EU food-safety forms, bills of lading, weight certificates); contract-based pricing with grade differentials",
          "impact": "High",
          "sap_module_relevance": ["SD", "GTS"]
        },
        {
          "process_area": "Farmer Payments via Mobile Money",
          "current_state": "Mobile money disbursements to farmers; no integration with financial records; reconciliation is manual",
          "desired_state": "Integrated mobile money payment processing; automated vendor payment runs triggering disbursements; automatic FI-AP clearing",
          "impact": "Medium",
          "sap_module_relevance": ["FI-AP", "BTP"]
        }
      ],
      "must_have_capabilities": [
        "Batch/lot traceability with batch characteristics (origin, moisture, grade, outturn ratio)",
        "Multi-currency (minimum TZS, USD, EUR — ideally all 6 active currencies)",
        "Export documentation support (phytosanitary, EU food-safety forms, weight notes, bills of lading)",
        "Financial reporting (P&L, balance sheet, cash flow — investor grade)",
        "Quality management with kernel-grade tracking and Certificate of Quality generation",
        "Export-traceability data capture (farmer geo-coordinates, plot size, harvest date) [INFERRED]"
      ],
      "nice_to_have_capabilities": [
        "Mobile access for field operations (cherry... raw nut collection, quality inspection at collection station)",
        "Farmer relationship management (CRM-like — payment history, quality history, incentive tracking)",
        "Certification tracking (Organic, Fairtrade, Rainforest Alliance) — if HHE pursues these",
        "Domestic sales management for planned Dar es Salaam retail line",
        "Weather/harvest forecasting integration",
        "Mobile money integration"
      ],
      "explicit_exclusions": []
    },

    "compliance_and_regulatory": {
      "regulatory_frameworks": [
        "Tanzania Cashewnut Board regulations — HHE recognized as a model smallholder-sourcing project",
        "Export licensing — Tanzania Revenue Authority",
        "Phytosanitary compliance — Ministry of Agriculture, Tanzania",
        "EU food-safety import traceability documentation — required for shipments into the European Union; enforcement is administrative rather than commodity-specific like EUDR [INFERRED — relevant given HHE's EU buyer base]",
        "Tanzania Personal Data Protection Act, 2022 [INFERRED — farmer personal data]"
      ],
      "industry_standards": [
        "AFI (African Cashew Initiative) grading guidance — HHE kernels graded to premium whole-kernel standard",
        "Tanzania Cashewnut Board quality benchmarks",
        "[CLARIFICATION NEEDED: Does HHE hold or pursue Organic, Fairtrade, or Rainforest Alliance certifications?]"
      ],
      "audit_requirements": [
        "Investor reporting requirements [STATED — investor funding conditional on ROI]",
        "Tanzania Cashewnut Board reporting as a model sourcing project [INFERRED]"
      ],
      "data_residency_requirements": [
        "EU food-safety import rules require traceability data to be available on request [INFERRED]",
        "Tanzania Personal Data Protection Act compliance for farmer personal data [INFERRED]"
      ],
      "export_control_considerations": "Agricultural commodity export — phytosanitary certificates, weight/quality documentation, EU food-safety traceability paperwork for European market"
    },

    "transformation_context": {
      "transformation_type": "Greenfield [CONFIRMED — no existing ERP]",
      "deployment_preference": "Public Cloud [INFERRED — no IT infrastructure, budget-conscious, rapid deployment needed; rural location favors cloud with offline sync capability]",
      "clean_core_readiness": {
        "awareness": "None [INFERRED — no SAP experience]",
        "willingness_to_adopt_standard": "High [INFERRED — greenfield with no legacy processes to protect; HHE's quality-focused culture suggests openness to best practices]",
        "estimated_custom_code_to_evaluate": "N/A — greenfield"
      },
      "timeline_signals": {
        "target_go_live": "[UNKNOWN — recommend alignment with harvest season: go-live before October harvest season start]",
        "hard_deadline": "[UNKNOWN]",
        "driver": "Growth-driven — need systems before scaling to 7,000 farmers; also EU food-safety compliance urgency for European market"
      },
      "budget_signals": {
        "range_indicated": "Tight — investor willing to fund with clear ROI",
        "funding_approved": "Partial — contingent on ROI business case",
        "budget_owner": "[INFERRED: Amina Cheyo (Founder) + lead investor]"
      },
      "change_management_readiness": {
        "executive_sponsorship": "Strong [INFERRED — founder Amina Cheyo is directly driving business transformation; Cashewnut Board model-project recognition shows leadership commitment]",
        "prior_erp_experience": "None [CONFIRMED]",
        "organizational_change_capacity": "Medium-Low [INFERRED — rural workforce; seasonal workers at Mafinga; BUT strong founder leadership and quality culture suggest change can be championed effectively]",
        "training_infrastructure": "[INFERRED: Limited — rural operations, potential connectivity challenges; mobile-first training approach likely needed]"
      }
    },

    "stakeholder_map": {
      "executive_sponsor": "Amina Cheyo — Founder (age ~42; entered cashew industry 2018; corporate background before agribusiness)",
      "project_champion": "[INFERRED: Amina Cheyo — likely the sole strategic decision-maker at this company size]",
      "it_leadership": "[INFERRED: Does not exist — no IT function mentioned in any source]",
      "key_business_process_owners": [
        "Njombe Collection Station Manager (quality intake, farmer procurement)",
        "Mafinga Processing Facility Supervisor (drying, shelling, grading, export prep)",
        "Finance/Accounting Lead [INFERRED — handles multi-currency, investor reporting]",
        "Export/Logistics Manager [INFERRED — manages buyer relationships, shipping]",
        "Farmer Relations Lead [INFERRED — manages 1,800-3,200+ smallholder relationships, incentive programs]"
      ],
      "known_resistors_or_risks": [
        "Field and seasonal workers may resist digital tools if connectivity is unreliable at rural sites",
        "Jump from Excel/WhatsApp to ERP is massive — highest change management risk",
        "No IT staff to manage system post-implementation — ongoing support model critical",
        "Seasonal workforce at Mafinga (50-70 workers) creates training continuity challenge"
      ]
    },

    "initial_module_signals": {
      "high_relevance": [
        "FI (Financial Accounting) — multi-currency (6 currencies), financial reporting, investor reporting, month-end close automation",
        "CO (Controlling) — profitability analysis by lot/buyer/region/grade; cost tracking through 4 processing stages",
        "MM (Materials Management) — farmer procurement, batch-managed inventory, processing stage tracking via stock transfers",
        "SD (Sales & Distribution) — export sales order management, contract pricing with grade differentials, buyer management",
        "QM (Quality Management) — kernel-grade tracking, moisture/defect analysis, Certificate of Quality, quality-linked batch characteristics"
      ],
      "medium_relevance": [
        "WM (Warehouse Management — embedded) — collection station and processing facility bin management; multi-location (Njombe + Mafinga)",
        "GTS (Global Trade Services) — export compliance documentation automation [if budget allows; significant value for EU food-safety compliance]",
        "BTP (Business Technology Platform) — mobile money integration, mobile field apps for cashew collection/quality inspection, traceability geo-data capture"
      ],
      "low_relevance": [
        "PP (Production Planning) — cashew processing is stage-based (intake→drying→shelling→grading), not discrete/process manufacturing; standard inventory movements may suffice",
        "PM (Plant Maintenance) — limited equipment base (drying racks, shelling machines, grading tables)",
        "PS (Project System) — not a project-driven business",
        "HCM/SuccessFactors — ~65 permanent + 70 seasonal employees; lighter solution sufficient"
      ],
      "rationale": "Core scope: agricultural commodity procurement with batch traceability (MM+QM), multi-currency financial management (FI/CO), and export sales processing (SD). HHE's premium-grade positioning makes quality management (QM) unusually important — it's not a compliance checkbox, it's a revenue driver. GTS is strategically important for EU food-safety documentation but may be cost-prohibitive in Phase 1. BTP is needed for mobile money integration and mobile field capabilities. CRITICAL SIZING NOTE: At ~$900K-$3.1M revenue and ~65 permanent employees, HHE is at the boundary between SAP Business One and S/4HANA Cloud Public Edition via SAP GROW. Recommend evaluating both options — S/4HANA may be justified if the 2.2x growth plan materializes and export-compliance requirements need GTS-level capability."
    },

    "downstream_handoff": {
      "ready_for_module_fit_analysis": true,
      "recommended_next_steps": [
        "1. Client validation session with Amina Cheyo to confirm: exact farmer count, revenue range, budget envelope, go-live timeline, certification status",
        "2. Proceed to Skill 02 (Module Fit Analyzer) — sufficient data for directional analysis at 74% completeness",
        "3. Critical decision point: SAP Business One vs. S/4HANA Cloud Public Edition (GROW) — revenue and growth trajectory are the deciding factors",
        "4. Assess IT infrastructure: internet connectivity at Njombe and Mafinga; mobile network coverage for field operations",
        "5. EU food-safety compliance urgency assessment — if EU buyers require enhanced traceability documentation, this accelerates timeline and may push toward S/4HANA (GTS module not available in Business One)"
      ],
      "information_to_gather_before_proceeding": [
        "Confirmed annual revenue range",
        "Exact active farmer count",
        "Target go-live date (recommend before October harvest)",
        "Budget envelope from investor",
        "Internet/mobile connectivity assessment at operating locations",
        "Certification status (Organic, Fairtrade, etc.)",
        "Number of expected concurrent users by role and location"
      ],
      "sap_tools_to_engage": {
        "cloud_alm": "Recommended once scope is confirmed — set up project structure and requirements tracking",
        "signavio": "Not recommended at this stage — no existing processes to mine; define target-state processes using SAP best practices for agricultural commodity trading",
        "leanix": "Not recommended — application landscape is minimal (Excel, mobile money, Wix, WhatsApp)",
        "dda": "Highly recommended — run Digital Discovery Assessment to validate scope item selection against S/4HANA Cloud Public Edition catalog and evaluate SAP GROW eligibility"
      }
    }
  }
}
```

---

## Key Enrichments from Support Materials

The scenario data significantly enriched the discovery brief compared to the generic prompt:

| Dimension | Generic Scenario | Enriched with Scenario Data |
|---|---|---|
| **Founder** | Unknown | Amina Cheyo, ~42, entered cashew industry 2018, corporate background |
| **Brand** | Unknown | "Mlima" — Swahili word meaning "mountain" |
| **Processing stages** | Assumed basic | 4 stages confirmed: raw intake, drying, shelling, grading/export prep |
| **Quality metrics** | Unknown | Outturn ratio (KOR), moisture percentage, whole/broken kernel count |
| **Export markets** | Generic "EU, North America, Asia" | Specific fictional buyers: Baltic Nut Traders (EE), Meridian Food Import (KR), Casa do Caju (PT), Northgate Commodities (CA), Sunrise Ingredients (IN) |
| **Currencies** | 3 (TZS, USD, EUR) | 6 confirmed: TZS, USD, EUR, CAD, KRW, INR |
| **Facilities** | "processing facility" | Njombe collection station + Mafinga processing facility |
| **Staff model** | "~65 employees" | ~28 permanent (Njombe) + 50-70 seasonal (Mafinga) + indirect |
| **Production volume** | Unknown | 20-35 containers/year raw cashew |
| **Recognition** | Unknown | Tanzania Cashewnut Board model sourcing project |
| **Export compliance** | Not mentioned | Inferred as important — EU buyers require food-safety traceability documentation |
| **Revenue estimate** | Unknown | $900K-$3.1M estimated from container volume × premium pricing |
| **Domestic plans** | Unknown | Dar es Salaam retail line planned |
