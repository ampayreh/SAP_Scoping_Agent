# Skill 01 Output: Client Discovery Intake -- Constellation Satellite Systems (CSS)

## Input Sources
- Client brief (Scenario B raw input)
- SAP ECC 6.0 EHP8 system profile and custom code inventory
- Stakeholder interview notes (CEO, CFO, CIO, CISO, VP Manufacturing)
- Parent company SAP landscape alignment requirements
- ITAR/EAR regulatory compliance context
- Aerospace and defense industry reference architecture (SAP for A&D)

---

## Structured Discovery Brief

```json
{
  "discovery_brief": {
    "metadata": {
      "brief_id": "DB-20260222-CSS",
      "created_date": "2026-02-22T00:00:00Z",
      "data_completeness_score": "90%",
      "confidence_level": "HIGH",
      "missing_information_flags": [
        "IMPORTANT: Exact count of legal entities not stated; subsidiary relationship to parent conglomerate implies at least 2 (CSS + parent), but intercompany structure needs confirmation",
        "IMPORTANT: Number of active SAP user licenses by type (Professional vs. Limited Professional vs. Developer) not broken out",
        "IMPORTANT: Data volume and database size for current ECC instance not specified; critical for system conversion sizing",
        "HELPFUL: Detailed integration architecture diagrams for the 12 custom middleware interfaces not provided",
        "HELPFUL: Specific SAP Basis support model post-conversion (in-house vs. AMS partner) not discussed",
        "HELPFUL: Parent company intercompany accounting requirements and consolidation approach not detailed"
      ],
      "clarifying_questions": [
        "1. What is the current ECC database size (TB)? This directly impacts system conversion duration, downtime window planning, and infrastructure sizing for S/4HANA Cloud Private Edition.",
        "2. How many legal entities does CSS operate? Is there intercompany billing between CSS and the parent conglomerate, or between CSS sites (Redmond, Huntsville, Cape Canaveral)?",
        "3. Of the 2,400 custom ABAP objects, has CSS conducted any preliminary analysis using SAP Custom Code Migration Worklist or ABAP Test Cockpit (ATC)? Any prior classification of custom code (must-keep vs. retire vs. refactor)?",
        "4. What is the scope of ITAR-controlled data within SAP? Specifically, which master data objects and transactions carry ITAR classification, and how is access currently enforced?",
        "5. What is the parent company's timeline and expectation for CSS to align on S/4HANA Cloud Private Edition? Is there a shared managed service provider or hosting partner?",
        "6. For the 12 custom middleware interfaces, which integration middleware is in use (SAP PI/PO, MuleSoft, Boomi, custom)? Is SAP Integration Suite (BTP) the target middleware?",
        "7. What is the current SAP archiving strategy? Are there data retention requirements driven by ITAR, DCAA audit, or contract close-out that affect the conversion scope?",
        "8. Has the organization conducted a formal change readiness assessment following the two failed IT projects? Is there an active organizational change management (OCM) program?"
      ]
    },

    "client_profile": {
      "company_name": "Constellation Satellite Systems (CSS)",
      "industry": "High Tech / Aerospace and Defense (SAP Industry: A&D / HT)",
      "sub_industry": "Satellite Manufacturing, LEO Constellation Deployment and Launch Services",
      "revenue_range": "~$1.2B annually",
      "employee_count": "~2,500 across all sites",
      "sap_user_count": "~800 active SAP users (Professional + Limited Professional licenses)",
      "geographic_footprint": {
        "headquarters": "Redmond, WA, USA",
        "manufacturing_sites": ["Redmond, WA (satellite manufacturing)", "Huntsville, AL (manufacturing)"],
        "launch_operations": "Cape Canaveral, FL",
        "operating_countries": ["United States"],
        "legal_entities": "[INFERRED: 1 primary entity; parent conglomerate structure implies additional intercompany relationships. Needs confirmation.]",
        "currencies": ["USD (primary)", "EUR [INFERRED: European supplier payments for space-grade components]"]
      },
      "ownership_structure": "Subsidiary of a larger aerospace conglomerate (parent uses S/4HANA Cloud Private Edition)",
      "growth_trajectory": "Rapid growth: scaling satellite production from 5/month to 15/month within 18 months (3x increase) to support constellation deployment schedule"
    },

    "current_landscape": {
      "erp_current": {
        "system": "SAP ECC 6.0 EHP8",
        "version": "EHP8 (installed 2015)",
        "deployment": "On-premise",
        "customization_level": "Heavy",
        "estimated_custom_objects": "~2,400 custom ABAP objects (reports, enhancements, interfaces) plus 47 custom transactions",
        "basis_team": "4 FTEs dedicated SAP Basis",
        "maintenance_status": "SAP ECC mainstream maintenance ends 2027; extended maintenance available to 2030",
        "modules_in_use": ["FI", "CO", "MM", "SD", "PP", "QM", "PM", "PS", "GTS (partial)"],
        "pain_points": [
          "Heavy customization (2,400 objects) creates upgrade barriers; 3 enhancement packs skipped",
          "BOM management disconnect: engineering BOMs in Teamcenter PLM do not sync cleanly with manufacturing BOMs in SAP PP; as-built BOMs tracked manually outside SAP",
          "Project System (PS) used for satellite program tracking but earned value management (EVM) performed in Excel outside SAP",
          "ITAR compliance managed through fragmented combination of partial GTS implementation, manual processes, and a separate access control database",
          "MES-to-SAP integration has 4-hour data lag; no real-time manufacturing visibility",
          "Financial close cycle is 12 business days (target: 5 days)",
          "Supply chain has no predictive visibility for long-lead components (18+ month lead times for space-grade electronics)",
          "Revenue recognition for long-term contracts (IFRS 15/ASC 606) not properly configured; milestone-based recognition handled manually",
          "47 custom transactions increase training burden and complicate support"
        ]
      },
      "adjacent_systems": [
        {
          "category": "PLM",
          "product": "Siemens Teamcenter",
          "integration_method": "Custom middleware interface",
          "data_quality": "Fair [INFERRED: engineering BOM data is authoritative but sync to SAP PP is lossy]",
          "notes": "Primary source for engineering BOMs; critical integration point for BOM lifecycle management"
        },
        {
          "category": "MES",
          "product": "Apriso (Dassault Systemes)",
          "integration_method": "Custom middleware interface (4-hour lag)",
          "data_quality": "Fair [INFERRED: MES data is operationally current but SAP lags by 4 hours]",
          "notes": "Shop floor execution; real-time integration is a key transformation requirement"
        },
        {
          "category": "CRM",
          "product": "Salesforce",
          "integration_method": "Custom middleware interface [INFERRED]",
          "data_quality": "Unknown",
          "notes": "Customer and contract management; integration with SD for order processing"
        },
        {
          "category": "HCM",
          "product": "Workday",
          "integration_method": "Custom middleware interface [INFERRED]",
          "data_quality": "Unknown",
          "notes": "HR and payroll; no HCM in SAP scope. Cost center/employee master sync needed."
        },
        {
          "category": "Planning",
          "product": "Anaplan",
          "integration_method": "Custom middleware interface [INFERRED]",
          "data_quality": "Unknown",
          "notes": "Financial and operational planning; integration with CO/FI and PP for actuals vs. plan"
        },
        {
          "category": "Middleware",
          "product": "12 custom middleware interfaces (technology not specified)",
          "integration_method": "Custom",
          "data_quality": "Unknown",
          "notes": "Integration backbone connecting SAP to PLM, MES, CRM, HCM, Anaplan, and other systems. Middleware modernization is a critical workstream."
        }
      ],
      "data_landscape": {
        "master_data_quality": "Fair [INFERRED: 10+ years of ECC usage with heavy customization suggests data quality challenges; BOM synchronization issues confirm master data inconsistencies]",
        "data_governance_maturity": "Emerging [INFERRED: large-scale ECC with dedicated Basis team suggests some governance; but manual processes and Excel workarounds indicate gaps]",
        "estimated_data_volume": "High [INFERRED: $1.2B revenue, 800 users, 10+ years of transactional data, complex BOM structures for satellite manufacturing, ITAR-controlled data]"
      },
      "existing_sap_footprint": {
        "has_sap": true,
        "products": ["SAP ECC 6.0 EHP8 (FI/CO, MM, SD, PP, QM, PM, PS, GTS partial)"],
        "btp_usage": "No [INFERRED: not mentioned; parent may have BTP access]",
        "signavio_usage": "Planned (parent company mandate)",
        "leanix_usage": "Planned (parent company mandate)"
      }
    },

    "business_requirements": {
      "primary_drivers": [
        "Board-mandated S/4HANA migration before ECC mainstream maintenance end (December 2028 go-live deadline)",
        "Digital factory: real-time production visibility, predictive quality analytics, AI-assisted supply chain planning (CEO priority)",
        "Financial close reduction from 12 days to 5 days with program-level profitability analysis (CFO priority)",
        "Integrated BOM lifecycle management: single source of truth from engineering through manufacturing through as-built configuration (VP Manufacturing priority)",
        "Full ITAR/EAR compliance via complete GTS implementation replacing fragmented manual controls (CISO priority)",
        "60% custom code reduction aligned with SAP Clean Core principles (CIO priority)",
        "Parent company alignment on S/4HANA Cloud Private Edition, Signavio, and LeanIX"
      ],
      "process_pain_points": [
        {
          "process_area": "Record-to-Report (Financial Close)",
          "current_state": "12-business-day close cycle driven by manual reconciliations, Excel-based EVM consolidation, and multi-step intercompany processing",
          "desired_state": "5-day close with automated reconciliations, real-time program profitability, embedded EVM within PS/CO, and streamlined period-end processing",
          "impact": "High",
          "sap_module_relevance": ["FI", "CO", "PS"]
        },
        {
          "process_area": "Revenue Recognition (IFRS 15/ASC 606)",
          "current_state": "Milestone-based revenue recognition for long-term satellite and launch service contracts handled manually outside SAP; FI configuration does not support contract-based revenue recognition",
          "desired_state": "Automated revenue recognition using S/4HANA Revenue Accounting and Reporting (RAR) with milestone, percentage-of-completion, and deliverable-based recognition methods",
          "impact": "High",
          "sap_module_relevance": ["FI", "SD", "PS", "RAR"]
        },
        {
          "process_area": "Engineering and Manufacturing BOM Management",
          "current_state": "Engineering BOMs authored in Teamcenter PLM; manufacturing BOMs maintained separately in SAP PP with lossy synchronization; as-built BOMs tracked manually. Three disconnected BOM representations create traceability gaps and rework.",
          "desired_state": "Integrated BOM lifecycle from engineering (Teamcenter) through manufacturing BOM (PP) to as-built configuration, with bi-directional sync, engineering change management, and full serialized traceability per satellite unit",
          "impact": "High",
          "sap_module_relevance": ["PP", "PLM integration", "QM"]
        },
        {
          "process_area": "ITAR/EAR Export Control Compliance",
          "current_state": "Partial GTS implementation supplemented by manual processes and a separate access control database; compliance enforcement is fragmented and audit-risky",
          "desired_state": "Fully integrated GTS with automated screening (denied party, embargo, license determination), document-level ITAR classification, access control enforcement within SAP authorization model, and audit-ready compliance reporting",
          "impact": "High",
          "sap_module_relevance": ["GTS", "SD", "MM", "Security/Authorization"]
        },
        {
          "process_area": "Production Planning and Shop Floor Integration",
          "current_state": "MES (Apriso) to SAP integration has 4-hour data lag; no real-time production visibility; scaling from 5 to 15 satellites/month requires tighter planning and execution integration",
          "desired_state": "Real-time or near-real-time MES integration; digital factory visibility with live production status, predictive quality analytics, and yield tracking per satellite unit",
          "impact": "High",
          "sap_module_relevance": ["PP", "QM", "MES integration"]
        },
        {
          "process_area": "Supply Chain Planning for Long-Lead Components",
          "current_state": "No predictive tracking for space-grade electronic components with 18+ month lead times; supply chain disruptions discovered reactively; demand planning disconnected from production schedule",
          "desired_state": "Integrated demand and supply planning with long-lead component visibility, supplier collaboration, predictive risk analytics, and alignment with 3x production ramp schedule",
          "impact": "High",
          "sap_module_relevance": ["MM", "PP", "Anaplan integration", "IBP potential"]
        },
        {
          "process_area": "Plant Maintenance (Predictive)",
          "current_state": "Standard preventive maintenance scheduling in PM; no predictive maintenance capabilities for manufacturing equipment",
          "desired_state": "Predictive maintenance leveraging IoT sensor data from manufacturing equipment to reduce unplanned downtime during production ramp",
          "impact": "Medium",
          "sap_module_relevance": ["PM", "BTP/IoT"]
        },
        {
          "process_area": "Custom Code and Technical Debt Management",
          "current_state": "2,400 custom ABAP objects and 47 custom transactions; 3 enhancement packs skipped due to custom code conflicts; high total cost of ownership and support burden on 4 FTE Basis team",
          "desired_state": "60% custom code reduction; remaining custom extensions moved to BTP (key user extensibility, side-by-side extensions) aligned with Clean Core strategy; standard S/4HANA functionality adopted where custom code replicated standard features",
          "impact": "High",
          "sap_module_relevance": ["Basis/Technical", "BTP", "All modules"]
        }
      ],
      "must_have_capabilities": [
        "System Conversion (Brownfield) path preserving 10+ years of transactional and master data history",
        "S/4HANA Cloud Private Edition deployment aligned with parent company platform",
        "Full GTS implementation for ITAR/EAR compliance (non-negotiable for defense prime contractor requirements)",
        "Revenue Accounting and Reporting (RAR) for IFRS 15/ASC 606 contract-based revenue recognition",
        "5-day financial close enablement with automated reconciliation and period-end workflows",
        "Integrated BOM management with Teamcenter PLM bi-directional synchronization",
        "Real-time or near-real-time MES (Apriso) integration replacing 4-hour batch lag",
        "Serialized traceability per satellite unit (as-built configuration management)",
        "ABAP custom code remediation and Clean Core alignment",
        "Signavio process mining and LeanIX enterprise architecture adoption (parent mandate)"
      ],
      "nice_to_have_capabilities": [
        "SAP Integrated Business Planning (IBP) for long-lead component demand/supply planning",
        "Predictive quality analytics for satellite manufacturing (AI/ML on quality inspection data)",
        "Predictive maintenance for manufacturing equipment (IoT integration via BTP)",
        "SAP Analytics Cloud (SAC) for real-time operational and financial dashboards",
        "Digital twin integration for satellite configuration management",
        "Supplier collaboration portal for space-grade component suppliers"
      ],
      "explicit_exclusions": [
        "HCM: Workday is the HCM system of record; no SuccessFactors in scope",
        "CRM: Salesforce is the CRM system of record; no SAP Sales Cloud in scope"
      ]
    },

    "compliance_and_regulatory": {
      "regulatory_frameworks": [
        "ITAR (International Traffic in Arms Regulations) -- satellite systems classified as defense articles under USML Category XV; controls technical data access, export, and foreign person access",
        "EAR (Export Administration Regulations) -- certain components and technologies controlled under CCL",
        "SOX (Sarbanes-Oxley Act) [INFERRED: $1.2B subsidiary of publicly traded aerospace conglomerate likely subject to SOX compliance for financial reporting controls]",
        "IFRS 15 / ASC 606 -- Revenue from Contracts with Customers; requires milestone-based and percentage-of-completion recognition for long-term satellite and launch contracts",
        "DCAA (Defense Contract Audit Agency) audit requirements [INFERRED: if CSS holds US government/DoD contracts, DCAA cost accounting compliance is required]",
        "FAR/DFARS compliance [INFERRED: federal acquisition regulation compliance for government contracts]"
      ],
      "industry_standards": [
        "AS9100 (Aerospace Quality Management System) [INFERRED: standard requirement for aerospace manufacturing]",
        "NASA-STD-8739 (Workmanship Standards) [INFERRED: if CSS supports NASA missions]",
        "MIL-STD specifications for space-grade component qualification [INFERRED]",
        "CMMC (Cybersecurity Maturity Model Certification) [INFERRED: if CSS handles Controlled Unclassified Information (CUI)]"
      ],
      "audit_requirements": [
        "SOX compliance for financial controls and reporting [INFERRED]",
        "DCAA cost accounting compliance for government contracts [INFERRED]",
        "ITAR compliance audits (DDTC registration and annual reporting)",
        "AS9100 quality system audits [INFERRED]",
        "Parent company internal audit and consolidation reporting"
      ],
      "data_residency_requirements": [
        "ITAR-controlled technical data must reside on US-person-accessible systems within US jurisdiction",
        "CMMC may require FedRAMP-authorized infrastructure [INFERRED: if DoD contracts require CMMC Level 2+]"
      ],
      "export_control_considerations": "CRITICAL: Satellites are ITAR-controlled defense articles (USML Category XV). Full GTS implementation is non-negotiable. Must support: denied party screening, license determination and tracking, technology control plans, foreign person access restrictions within SAP, ITAR classification at document and BOM item level, and audit trail for all export-controlled data access."
    },

    "transformation_context": {
      "transformation_type": "System Conversion (Brownfield) -- preserves existing configuration, master data, and transactional history from 10+ years of ECC operation. Recommended over greenfield given: (a) mature SAP footprint with 7 active modules, (b) need to retain historical data for ITAR audit trails and DCAA compliance, (c) organizational change fatigue favoring incremental transformation over wholesale process redesign.",
      "deployment_preference": "S/4HANA Cloud Private Edition -- driven by parent company platform alignment mandate. Private Edition supports: (a) ITAR data residency requirements (dedicated tenant), (b) custom code migration path for retained ABAP objects, (c) parent company Signavio and LeanIX tool integration, (d) system conversion approach from ECC 6.0.",
      "clean_core_readiness": {
        "awareness": "High (CIO has explicitly stated 60% custom code reduction target aligned with Clean Core)",
        "willingness_to_adopt_standard": "Medium -- CIO is committed but 2,400 custom objects include ITAR-driven, manufacturing-specific, and integration-critical customizations that may not all have standard equivalents. Expect tension between Clean Core aspiration and operational necessity.",
        "estimated_custom_code_to_evaluate": "~2,400 ABAP objects + 47 custom transactions",
        "clean_core_maturity_assessment": "Level C/D [INFERRED: heavy customization, 3 skipped enhancement packs, partial GTS implementation, and manual workarounds indicate significant distance from Clean Core. CIO's 60% reduction target suggests awareness that Level A/B is not achievable in initial conversion; target should be Level B post-remediation.]",
        "recommended_approach": "Phase 1: Run SAP Custom Code Migration Worklist and ABAP Test Cockpit (ATC) to classify all 2,400 objects into categories: (a) retire (standard S/4HANA replaces), (b) adapt (simplification adjustments needed), (c) retain on-stack (no standard equivalent, business-critical), (d) move to BTP (side-by-side extension). Phase 2: Execute remediation in waves aligned with module go-live sequence."
      },
      "timeline_signals": {
        "target_go_live": "December 2028 for core finance + operations (board-mandated)",
        "hard_deadline": true,
        "driver": "Board mandate driven by ECC mainstream maintenance ending 2027 and extended maintenance ending 2030. December 2028 provides 2-year buffer before extended maintenance end.",
        "recommended_approach": "Multi-wave implementation over 18 to 24 months: Wave 1 (core finance, controlling, GTS/ITAR) targets Q2 2028; Wave 2 (manufacturing, supply chain, project systems) targets Q4 2028; Wave 3 (advanced analytics, predictive capabilities, optimization) targets H1 2029."
      },
      "budget_signals": {
        "range_indicated": "$15-25M allocated for the transformation program",
        "funding_approved": "Yes -- budget allocated at board level",
        "budget_owner": "[INFERRED: CIO or CFO as program sponsor; board-level oversight given mandate]",
        "budget_validation": "REASONABLE for scope. $15-25M for a brownfield S/4HANA conversion at a $1.2B high-tech manufacturer with 800 users, heavy customization, and complex integrations is within expected range. Comparable projects typically run $12K-$25K per SAP user for conversions of this complexity. At 800 users, the $15-25M range ($18.75K-$31.25K per user) is aggressive but achievable if: (a) scope is phased across waves, (b) custom code remediation achieves the 60% reduction (reducing testing effort), and (c) existing integrations are modernized rather than rebuilt. Risk: budget may be tight if significant BTP development is required for retained custom extensions."
      },
      "change_management_readiness": {
        "executive_sponsorship": "Strong -- board mandate with clear executive alignment (CEO, CFO, CIO, CISO, VP Manufacturing all have stated objectives tied to S/4HANA)",
        "prior_erp_experience": "Mixed -- original ECC implementation (2015) was successful, but two recent IT project failures (MES upgrade, PLM migration) have created organizational skepticism",
        "organizational_change_capacity": "Low to Medium -- TOP RISK FACTOR. Two failed IT projects in the past 3 years have generated change fatigue and skepticism about large technology programs. This must be addressed proactively with: (a) dedicated OCM workstream with change champions at each site, (b) early wins strategy to build credibility, (c) transparent communication about how this program differs from prior failures, (d) formal lessons-learned analysis from MES and PLM projects to avoid repeating mistakes.",
        "training_infrastructure": "[INFERRED: Established -- 800 existing SAP users suggests training programs and SAP competency exist. However, significant retraining needed for S/4HANA Fiori UX, new workflows, and processes modified during custom code retirement.]",
        "multi_site_considerations": "Three geographically dispersed sites (Redmond WA, Huntsville AL, Cape Canaveral FL) require coordinated change management, site-specific go-live planning, and consideration of manufacturing continuity during cutover."
      }
    },

    "stakeholder_map": {
      "executive_sponsor": "[INFERRED: CEO or CIO -- board mandate suggests C-level sponsorship. Recommend confirming single accountable executive sponsor.]",
      "project_champion": "[INFERRED: CIO -- stated 60% custom code reduction and Clean Core objective indicates active engagement and transformation ownership]",
      "it_leadership": "CIO (transformation lead) + SAP Basis team (4 FTEs) + CISO (ITAR/security requirements)",
      "key_business_process_owners": [
        "CFO: Financial close, revenue recognition (IFRS 15/ASC 606), program profitability (FI/CO/PS)",
        "VP Manufacturing: BOM management, production planning, MES integration, digital factory (PP/QM/PM)",
        "CISO: ITAR/EAR compliance, GTS implementation, access control, data security",
        "CIO: Technical architecture, custom code remediation, Clean Core, integration modernization",
        "[INFERRED: VP Supply Chain / Procurement: long-lead component management, supplier collaboration (MM)]",
        "[INFERRED: VP Programs / Project Management: satellite program tracking, EVM, contract management (PS)]",
        "[INFERRED: Controller: financial close, SOX compliance, consolidation with parent (FI/CO)]"
      ],
      "known_resistors_or_risks": [
        "CRITICAL: Organizational change fatigue from 2 failed IT projects (MES upgrade, PLM migration) in past 3 years. Expect skepticism from middle management and shop floor personnel.",
        "Manufacturing teams may resist process changes during 3x production ramp (5 to 15 satellites/month); timing conflict between operational scaling and system transformation.",
        "Custom code owners (power users who designed the 47 custom transactions) may resist retirement of their processes. Early engagement and co-design sessions are essential.",
        "Huntsville and Cape Canaveral sites may feel secondary to Redmond HQ in program planning; ensure equitable site representation in design workshops.",
        "[INFERRED: Parent company governance may impose constraints that conflict with CSS operational needs; balance parent alignment with CSS autonomy.]"
      ]
    },

    "initial_module_signals": {
      "high_relevance": [
        "FI (Financial Accounting) -- 5-day close target, multi-entity consolidation, IFRS 15/ASC 606 revenue recognition via RAR, SOX compliance, parent company reporting alignment",
        "CO (Controlling) -- program-level profitability analysis, cost center accounting, earned value management integration with PS, product costing for satellite manufacturing",
        "MM (Materials Management) -- space-grade component procurement, long-lead item tracking (18+ month lead times), supplier management, inventory management across 3 sites",
        "SD (Sales & Distribution) -- satellite and launch services sales, milestone billing, contract management, integration with Salesforce CRM",
        "PP (Production Planning) -- manufacturing BOM management, production scheduling for 15 satellites/month target, MES (Apriso) integration, shop floor control",
        "QM (Quality Management) -- aerospace quality (AS9100), serialized inspection per satellite, supplier quality, in-process quality with MES integration",
        "PM (Plant Maintenance) -- manufacturing equipment maintenance, cleanroom infrastructure, launch facility equipment; predictive maintenance potential with BTP/IoT",
        "PS (Project System) -- satellite program tracking, earned value management (WBS-based), milestone tracking, program-level cost collection, integration with CO for profitability",
        "GTS (Global Trade Services) -- ITAR/EAR compliance (NON-NEGOTIABLE). Denied party screening, license management, export classification, technology control plan enforcement, foreign person access control. This is the single highest-compliance-risk module."
      ],
      "medium_relevance": [
        "RAR (Revenue Accounting and Reporting) -- IFRS 15/ASC 606 automated revenue recognition for long-term satellite contracts; may be classified as high if separate module activation is required",
        "BTP (Business Technology Platform) -- target platform for retained custom extensions (Clean Core), MES real-time integration, IoT/predictive maintenance, Teamcenter PLM integration modernization",
        "SAP Integration Suite (BTP) -- modernization of 12 custom middleware interfaces; target architecture for Teamcenter, Apriso, Salesforce, Workday, and Anaplan integrations",
        "IBP (Integrated Business Planning) -- long-lead supply chain planning, demand sensing for constellation deployment schedule [evaluate vs. existing Anaplan investment]",
        "SAC (SAP Analytics Cloud) -- real-time operational dashboards, financial reporting, manufacturing analytics [INFERRED: aligns with CEO digital factory vision]"
      ],
      "low_relevance": [
        "EWM (Extended Warehouse Management) -- standard MM warehouse functions likely sufficient for satellite component warehousing; evaluate if Huntsville or Redmond have complex warehouse operations",
        "TM (Transportation Management) -- satellite transport to launch site is specialized (not standard logistics); likely handled outside SAP",
        "SuccessFactors -- excluded; Workday is HCM system of record",
        "SAP Sales Cloud / Service Cloud -- excluded; Salesforce is CRM system of record"
      ],
      "rationale": "CSS requires activation of virtually all currently deployed SAP modules (FI/CO, MM, SD, PP, QM, PM, PS) in S/4HANA, plus full GTS implementation as the single most compliance-critical addition. The transformation is not about adding new modules; it is about modernizing and deepening the existing footprint while eliminating custom code through standard S/4HANA functionality. GTS elevation from partial to full implementation is non-negotiable given ITAR exposure. RAR is new scope required for IFRS 15/ASC 606. BTP is critical infrastructure for Clean Core strategy (hosting retained extensions) and integration modernization (replacing 12 custom middleware interfaces). IBP should be evaluated against the existing Anaplan investment; if Anaplan is retained, IBP may be deferred. The CEO's digital factory vision and the CFO's 5-day close target are the two transformation narratives that will resonate with the board and help overcome organizational skepticism."
    },

    "downstream_handoff": {
      "ready_for_module_fit_analysis": true,
      "recommended_next_steps": [
        "1. Proceed to Skill 02 (Module Fit Analyzer) with this brief at 90% completeness; sufficient detail for comprehensive fit/gap analysis across all 9 in-scope modules plus GTS and RAR.",
        "2. Engage SAP Custom Code Migration Worklist immediately: analyze all 2,400 ABAP objects and 47 custom transactions. Classify into retire/adapt/retain/move-to-BTP categories. This is the critical path activity for both timeline and budget.",
        "3. Deploy SAP Signavio for current-state process mining on ECC (parent company mandate). Focus on: financial close process, BOM change management, procurement cycle for long-lead components, and ITAR compliance workflows.",
        "4. Deploy LeanIX for application portfolio rationalization (parent company mandate). Map all 12 middleware interfaces, Teamcenter, Apriso, Salesforce, Workday, and Anaplan integration points. Define target integration architecture.",
        "5. Conduct formal change readiness assessment addressing the 2 failed IT project legacy. Commission independent OCM baseline survey across all 3 sites. This is a prerequisite for program launch.",
        "6. Validate ITAR data scope and access control requirements with CISO. GTS implementation design must begin in parallel with technical conversion planning.",
        "7. Engage parent company S/4HANA Cloud PE managed service provider for infrastructure sizing and tenant provisioning requirements.",
        "8. Schedule executive alignment workshop: confirm single accountable executive sponsor, validate wave structure, and secure commitment to OCM investment."
      ],
      "information_to_gather_before_proceeding": [
        "ECC database size (TB) for conversion sizing",
        "Custom code preliminary classification (if any prior analysis exists)",
        "Legal entity structure and intercompany requirements",
        "ITAR data scope within SAP (which objects, transactions, and master data carry classification)",
        "Parent company managed service provider and hosting requirements for S/4HANA Cloud PE",
        "Integration middleware inventory (SAP PI/PO, MuleSoft, Boomi, or custom) for the 12 interfaces",
        "Change readiness baseline from the 2 failed IT project post-mortems"
      ],
      "sap_tools_to_engage": {
        "cloud_alm": "Strongly recommended: establish project governance, requirements tracking, and test management from program initiation. Use Cloud ALM for deployment management across multi-wave approach.",
        "signavio": "Required (parent company mandate): deploy for current-state process mining on ECC production system. Priority process domains: financial close (Record-to-Report), BOM lifecycle (Design-to-Operate), procurement (Source-to-Pay), ITAR compliance flows. Benchmark against SAP Best Practices for Aerospace and Defense.",
        "leanix": "Required (parent company mandate): map current application portfolio including all integration points. Use for integration architecture target-state design and application rationalization (evaluate Anaplan vs. IBP, middleware consolidation).",
        "dda": "Highly recommended: run Digital Discovery Assessment to validate scope item selection against S/4HANA Cloud Private Edition catalog. Use DDA output to confirm module fit and identify scope items requiring custom development on BTP.",
        "custom_code_migration_worklist": "CRITICAL PATH: run immediately against ECC production to classify 2,400 ABAP objects. Feed results into Skill 02 for custom code impact analysis per module.",
        "abap_test_cockpit": "Required: ATC analysis of all custom code for S/4HANA compatibility (simplification items, deprecated APIs, new data model impacts)."
      }
    }
  }
}
```

---

## Key Observations and Risk Summary

| Dimension | Assessment | Detail |
|---|---|---|
| **Data Completeness** | 90% | Exceptionally detailed input covering all critical dimensions; minor gaps in database sizing, legal entity structure, and integration architecture specifics |
| **Recommended Approach** | System Conversion (Brownfield) | Preserves 10+ years of ECC data, reduces change impact (addresses fatigue risk), retains configuration investment, and aligns with ITAR audit trail requirements |
| **Deployment Target** | S/4HANA Cloud Private Edition | Parent company alignment mandate; supports ITAR data residency, custom code migration path, and system conversion approach |
| **Clean Core Maturity** | Level C/D (current); Level B (target) | 2,400 custom objects and 47 custom transactions; CIO targets 60% reduction. Expect ~960 objects retained post-remediation; BTP required for side-by-side extensions. |
| **Top Risk: Change Fatigue** | HIGH | Two failed IT projects (MES upgrade, PLM migration) in 3 years have created organizational skepticism. Dedicated OCM workstream with early wins strategy is essential to program success. |
| **Top Risk: Production Ramp Conflict** | HIGH | 3x production ramp (5 to 15 satellites/month) overlaps with S/4HANA conversion timeline. Manufacturing continuity during cutover must be explicitly planned. |
| **Budget Adequacy** | Reasonable but Tight | $15-25M for 800-user brownfield conversion with heavy customization and complex integrations. At $18.75K to $31.25K per user, achievable with phased scope and successful custom code reduction. |
| **Timeline Feasibility** | Achievable with Risk | 18 to 24 month program to hit December 2028 deadline. Multi-wave approach required. Custom code remediation is the critical path. |
| **ITAR/GTS** | Non-negotiable Phase 1 | ITAR compliance gaps are the single highest regulatory risk. Full GTS must be in Wave 1 scope alongside core finance. |
| **Module Count** | 9 current + 2 new (GTS full, RAR) | All existing modules carry forward plus GTS elevation and RAR activation. BTP is critical infrastructure, not optional. |
