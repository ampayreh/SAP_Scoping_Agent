# Skill 03 Output: Implementation Roadmap — Highland Harvest Exports (HHE)

> **Fictional scenario.** This company, its founder, its facilities, its buyers, and every figure below are invented for benchmarking purposes. No resemblance to any real business is intended.

## Roadmap Metadata

| Field | Value |
|---|---|
| **Roadmap ID** | IR-20260217-HHE |
| **Source Brief** | DB-20260217-HHE |
| **Source Module Analysis** | MFA-20260217-HHE |
| **Created Date** | 2026-02-17 |
| **Confidence Level** | MEDIUM |
| **Roadmap Version** | 1.0 |

---

## Implementation Roadmap

```json
{
  "implementation_roadmap": {
    "metadata": {
      "roadmap_id": "IR-20260217-HHE",
      "created_date": "2026-02-17T00:00:00Z",
      "source_brief_id": "DB-20260217-HHE",
      "source_module_analysis_id": "MFA-20260217-HHE",
      "roadmap_version": "1.0",
      "confidence_level": "MEDIUM",
      "assumptions": [
        "Revenue in the $900K-$3.1M range (SAP GROW eligibility confirmed)",
        "19 named users across finance, operations, sales/export, quality, and management",
        "Internet connectivity at Njombe and Mafinga adequate for cloud access (to be validated during Discover)",
        "Investor funding approved with budget envelope of $98,000-$190,000 for Year 1",
        "Client can dedicate 3-4 staff members at 25-50% capacity to the project",
        "SAP GROW starter pack pricing applies with standard Public Cloud SLAs",
        "Single legal entity in Tanzania with multi-currency requirements (no intercompany)",
        "Regional implementation partner with East Africa presence available at $100-$150/hour blended rate",
        "Go-live targeted before October 2026 harvest season"
      ],
      "caveats": [
        "Budget estimates are ROM only — formal quotation requires SAP pricing engagement and partner SOW",
        "Timeline assumes no major regulatory or organizational disruptions",
        "Resource model assumes lean regional partner, not Big 4 pricing",
        "Several Skill 01 inputs were inferred (marked [INFERRED]) — timeline and budget ranges carry wider uncertainty",
        "Seasonal workforce training continuity at Mafinga is a known challenge — not fully mitigated in Phase 1"
      ]
    },

    "roadmap_summary": {
      "program_name": "Project Korosho — HHE S/4HANA Cloud Implementation",
      "recommended_edition": "S/4HANA Cloud Public Edition via SAP GROW",
      "transformation_type": "Greenfield",
      "go_live_strategy": "Big Bang (single wave)",
      "go_live_strategy_rationale": "Single-site operation with 19 users and compact module scope (FI/CO, MM, SD, QM). Phased rollout would add complexity and cost disproportionate to scale. All core modules are tightly interdependent — FI/CO is needed for MM posting, SD billing, and QM results. Separating them into waves would require temporary workarounds. Big bang risk is manageable at this scale with adequate hypercare.",
      "total_duration_months": 7.5,
      "number_of_waves": 1,
      "wave_summary": [
        {
          "wave_id": "W1",
          "name": "Core ERP Foundation",
          "scope_description": "FI/CO (multi-currency financial accounting and controlling), MM (farmer procurement and inventory with batch traceability), SD (export sales order management and billing), QM (cashew grading and traceability). Mobile money integration via BTP.",
          "target_go_live": "Week 30 from project kickoff (October 2026 target)",
          "duration_months": 7.5
        }
      ],
      "overall_program_risk": "MEDIUM",
      "clean_core_strategy": "Full compliance — greenfield implementation with no legacy customizations. All extensions via BTP side-by-side model.",
      "cloud_alm_project_type": "Implementation"
    },

    "phase_plan": [
      {
        "phase_name": "Discover",
        "sap_activate_phase": "Discover",
        "wave": "W0 (Pre-project)",
        "duration_weeks": 3,
        "start_offset_weeks": 0,
        "duration_rationale": "Standard 2-4 week baseline + 1 week for no prior SAP experience. HHE needs connectivity assessment at the Njombe station and SAP GROW eligibility confirmation.",
        "key_activities": [
          {
            "activity": "Scope Validation Workshop",
            "description": "Confirm module scope from Skill 02 analysis with Amina Cheyo and key stakeholders. Validate business process priorities and must-have vs. nice-to-have capabilities. Resolve SAP GROW vs. Business One product decision.",
            "responsible": "Solution Architect + Founder",
            "sap_tool": "Digital Discovery Assessment (DDA)"
          },
          {
            "activity": "Stakeholder Alignment Sessions",
            "description": "Identify and engage all key stakeholders. Establish governance structure, decision-making authority, escalation paths. Confirm who will serve as process owners for finance, operations, export, and quality.",
            "responsible": "Project Manager",
            "sap_tool": "None"
          },
          {
            "activity": "Infrastructure and Connectivity Assessment",
            "description": "Validate internet connectivity at the Njombe collection station and Mafinga processing facility. Test latency to SAP data center. Assess device availability for end users. Identify backup connectivity options.",
            "responsible": "Technical Consultant",
            "sap_tool": "None"
          },
          {
            "activity": "SAP GROW Eligibility Confirmation",
            "description": "Confirm SAP GROW starter pack applicability. Validate user count, edition eligibility, and pricing model with SAP account team.",
            "responsible": "Solution Architect",
            "sap_tool": "SAP for Me"
          }
        ],
        "deliverables": [
          "Signed scope statement and project charter",
          "Stakeholder register and RACI matrix",
          "Infrastructure readiness report (connectivity at Njombe and Mafinga)",
          "SAP GROW subscription confirmation (or Business One decision)",
          "Project governance framework",
          "Confirmed product selection: S/4HANA GROW vs. Business One"
        ],
        "staffing": [
          { "role": "Solution Architect", "source": "Partner", "fte": 0.5, "key_skills": ["SAP S/4HANA Cloud", "SAP GROW", "Agribusiness"] },
          { "role": "Project Manager", "source": "Partner", "fte": 0.5, "key_skills": ["SAP Activate", "Mid-market delivery"] },
          { "role": "Executive Sponsor", "source": "Client (Amina Cheyo)", "fte": 0.1, "key_skills": ["Decision authority", "Budget approval"] },
          { "role": "Project Champion", "source": "Client", "fte": 0.25, "key_skills": ["Operations knowledge", "Staff influence"] }
        ],
        "prerequisites": [
          "Client commitment to proceed (letter of intent or signed SOW)",
          "Key stakeholder availability confirmed for workshop dates",
          "Investor approval of Phase 1 budget envelope"
        ],
        "risks": [
          "Stakeholder misalignment on scope — mitigate with structured workshop facilitation",
          "Connectivity assessment reveals inadequate infrastructure — contingency: evaluate satellite internet, mobile hotspot, or offline-first architecture",
          "Product selection deadlock (GROW vs. B1) — mitigate with clear decision criteria in workshop"
        ],
        "phase_exit_criteria": [
          "Scope statement signed by Amina Cheyo",
          "Product selection confirmed (GROW or Business One)",
          "Infrastructure readiness confirmed (or remediation plan with timeline)",
          "SAP GROW subscription initiated (or B1 licensing)",
          "Project team identified and availability confirmed"
        ],
        "sap_tools_used": [
          { "tool": "Digital Discovery Assessment", "usage": "Validate scope items against S/4HANA Cloud Public Edition catalog" },
          { "tool": "SAP for Me", "usage": "Confirm licensing and subscription setup" }
        ]
      },

      {
        "phase_name": "Prepare",
        "sap_activate_phase": "Prepare",
        "wave": "W1",
        "duration_weeks": 5,
        "start_offset_weeks": 3,
        "duration_rationale": "Standard 4-8 week baseline, adjusted: +2 weeks for greenfield org structure design, -1 week for simple single-entity structure, +1 week limited IT capacity (1.1x multiplier). Net: 5 weeks.",
        "key_activities": [
          {
            "activity": "System Provisioning",
            "description": "Provision S/4HANA Cloud tenant (DEV, QAS, PRD). Configure initial system landscape. Set up Cloud ALM project workspace.",
            "responsible": "Technical Consultant",
            "sap_tool": "SAP Cloud ALM, SAP for Me"
          },
          {
            "activity": "Organizational Structure Design",
            "description": "Define company code (HH01), controlling area (HH01), plants (NJ01 Njombe, MA01 Mafinga), storage locations, sales organization (HH10), distribution channel, division. Map to HHE's operational reality.",
            "responsible": "Solution Architect + Finance Lead",
            "sap_tool": "S/4HANA Cloud Configuration"
          },
          {
            "activity": "Master Data Strategy",
            "description": "Define master data objects: farmer/vendor masters (~3,200 records), material masters for cashew grades, customer masters for export buyers (Baltic Nut Traders, Meridian Food Import, Casa do Caju, Northgate Commodities, Sunrise Ingredients), chart of accounts (HHCA). Plan data creation approach — manual entry with templates for greenfield.",
            "responsible": "Functional Consultant + Process Owners",
            "sap_tool": "None"
          },
          {
            "activity": "ERP Fundamentals Training",
            "description": "Foundational ERP concepts training for HHE team. Cover: what is an ERP, process thinking, master data concepts, transaction flow (PO → GR → IV → payment), reporting basics. Critical for a team with zero prior ERP experience.",
            "responsible": "Change Management Lead",
            "sap_tool": "SAP Learning Hub"
          },
          {
            "activity": "Project Plan Finalization",
            "description": "Detailed project plan with task assignments, milestones, and resource calendar. Set up Cloud ALM task boards and requirement tracking.",
            "responsible": "Project Manager",
            "sap_tool": "SAP Cloud ALM"
          }
        ],
        "deliverables": [
          "Provisioned S/4HANA Cloud landscape (DEV, QAS, PRD)",
          "Cloud ALM project workspace configured",
          "Organizational structure design document (dual-plant: Njombe + Mafinga)",
          "Master data strategy and templates",
          "Detailed project plan and resource calendar",
          "ERP fundamentals training completion for all process owners"
        ],
        "staffing": [
          { "role": "Project Manager", "source": "Partner", "fte": 0.75 },
          { "role": "Solution Architect", "source": "Partner", "fte": 0.5 },
          { "role": "Functional Consultant (FI/CO)", "source": "Partner", "fte": 0.5 },
          { "role": "Technical Consultant", "source": "Partner", "fte": 0.25 },
          { "role": "Change Management Lead", "source": "Partner", "fte": 0.25 },
          { "role": "Project Champion", "source": "Client", "fte": 0.5 },
          { "role": "Finance Lead", "source": "Client", "fte": 0.25 },
          { "role": "Operations Lead", "source": "Client", "fte": 0.25 }
        ],
        "phase_exit_criteria": [
          "All three system landscapes provisioned and accessible",
          "Organizational structure design approved by Amina Cheyo",
          "Master data templates ready for population",
          "Client team has completed ERP fundamentals training",
          "Cloud ALM project workspace operational"
        ]
      },

      {
        "phase_name": "Explore",
        "sap_activate_phase": "Explore",
        "wave": "W1",
        "duration_weeks": 8,
        "start_offset_weeks": 8,
        "duration_rationale": "Standard 8-16 week baseline. Applied multipliers: 1.2x for no prior ERP experience, 1.1x for Clean Core discipline, 0.9x for SAP GROW accelerators = ~10 weeks adjusted. Reduced to 8 weeks based on compact scope (4 core modules) and lean mid-market approach.",
        "key_activities": [
          {
            "activity": "Fit-to-Standard Workshops",
            "description": "Process-by-process workshops: (1) Procure-to-Pay — farmer raw-cashew procurement with mobile money payment, (2) Inventory Management — batch-managed cashew lots through 4 processing stages, (3) Order-to-Cash — export sales with grade-based pricing, (4) Record-to-Report — multi-currency financials and period-end close, (5) Quality Management — kernel grading protocol, inspection plans, certificates.",
            "responsible": "Functional Consultants + Process Owners",
            "sap_tool": "SAP Signavio (Value Accelerators)"
          },
          {
            "activity": "Gap Resolution Design",
            "description": "For each gap from Skill 02: (1) mobile money integration — BTP design, (2) Tanzania export documentation forms — Adobe Forms templates, (3) farmer lot traceability beyond standard batch — classification schema, (4) EU food-safety traceability geo-data capture — Key User Extensibility or BTP app.",
            "responsible": "Solution Architect + Functional Consultants",
            "sap_tool": "SAP BTP (design)"
          },
          {
            "activity": "Integration Architecture Design",
            "description": "Design integration for: mobile money REST API, Tanzania bank file interfaces, potential TRA e-invoicing. Define API specs, middleware approach (BTP Integration Suite), error handling, monitoring.",
            "responsible": "Solution Architect + Technical Consultant",
            "sap_tool": "SAP Integration Suite (BTP)"
          },
          {
            "activity": "Data Migration Approach",
            "description": "For greenfield: define reference data to load — farmer master data from Excel (~3,200 records), material masters (cashew grades), customer masters (export buyers), chart of accounts, opening balances. Design validation rules.",
            "responsible": "Data Migration Specialist + Process Owners",
            "sap_tool": "S/4HANA Cloud Migration Cockpit"
          },
          {
            "activity": "Security and Authorization Design",
            "description": "5 business roles: Finance, Operations/Procurement, Sales/Export, Quality, Management/Reporting. Map to SAP standard business roles for Public Cloud edition.",
            "responsible": "Solution Architect",
            "sap_tool": "S/4HANA Cloud"
          }
        ],
        "deliverables": [
          "Fit-to-Standard workshop documentation (5 process areas)",
          "Gap list with approved resolution approach for each gap",
          "Business process master list (BPML) in Cloud ALM",
          "Integration architecture document (mobile money, bank, TRA)",
          "Data migration plan and templates",
          "Security role design document"
        ],
        "staffing": [
          { "role": "Project Manager", "source": "Partner", "fte": 0.75 },
          { "role": "Solution Architect", "source": "Partner", "fte": 0.5 },
          { "role": "Functional Consultant (FI/CO)", "source": "Partner", "fte": 0.75 },
          { "role": "Functional Consultant (MM/SD)", "source": "Partner", "fte": 0.75 },
          { "role": "Functional Consultant (QM)", "source": "Partner", "fte": 0.5 },
          { "role": "Technical Consultant", "source": "Partner", "fte": 0.25 },
          { "role": "Finance Lead (Process Owner)", "source": "Client", "fte": 0.5 },
          { "role": "Operations Lead (Process Owner)", "source": "Client", "fte": 0.5 },
          { "role": "Export Manager (Process Owner)", "source": "Client", "fte": 0.5 },
          { "role": "Project Champion", "source": "Client", "fte": 0.5 }
        ],
        "phase_exit_criteria": [
          "All Fit-to-Standard workshops completed with sign-off",
          "Gap list finalized with approved resolution for each gap",
          "Integration architecture approved",
          "Data migration templates populated with sample data",
          "No unresolved critical design decisions"
        ]
      },

      {
        "phase_name": "Realize",
        "sap_activate_phase": "Realize",
        "wave": "W1",
        "duration_weeks": 10,
        "start_offset_weeks": 16,
        "duration_rationale": "Standard 12-24 week baseline for mid-market. Applied: 1.2x for no ERP experience, 1.1x for multi-currency (6 currencies), 0.9x for Clean Core (less custom development). Compressed to 10 weeks for lean scope — 4 core modules, single geography, small user base.",
        "key_activities": [
          {
            "activity": "System Configuration",
            "description": "Configure all in-scope processes: multi-currency FI/CO, farmer procurement with batch management (MM), export sales order processing (SD), quality inspection plans for kernel grading (QM). Use self-service configuration in Public Cloud.",
            "responsible": "Functional Consultants",
            "sap_tool": "S/4HANA Cloud Self-Service Configuration"
          },
          {
            "activity": "BTP Extension Development",
            "description": "Build mobile money integration on BTP Integration Suite. Develop farmer intake mobile app (offline-capable) if approved in Explore. Follow Clean Core side-by-side extension model.",
            "responsible": "Technical Consultant + Solution Architect",
            "sap_tool": "SAP BTP, SAP Build, SAP Integration Suite"
          },
          {
            "activity": "Data Migration Execution",
            "description": "Load master data: farmer/vendor masters (~3,200 records), material masters (cashew grades), customer masters (5+ export buyers), chart of accounts, opening balances.",
            "responsible": "Data Migration Specialist + Process Owners",
            "sap_tool": "S/4HANA Cloud Migration Cockpit"
          },
          {
            "activity": "Unit Testing",
            "description": "Test each configured process end-to-end in isolation. Verify: multi-currency transactions, batch traceability flows, export document generation, quality inspection recording, financial posting accuracy.",
            "responsible": "Functional Consultants",
            "sap_tool": "SAP Cloud ALM (test management)"
          },
          {
            "activity": "Integration Testing",
            "description": "Test cross-module flows: farmer procurement (MM) → quality inspection (QM) → batch update → inventory transfer → export sale (SD) → billing (FI-AR) → month-end close. Test mobile money payment flow end-to-end.",
            "responsible": "All Consultants + Process Owners",
            "sap_tool": "SAP Cloud ALM (test orchestration)"
          },
          {
            "activity": "User Acceptance Testing (UAT)",
            "description": "Client process owners and key users execute test scenarios with real business data — actual farmer names, cashew grades, buyer contracts. Log defects in Cloud ALM.",
            "responsible": "Process Owners + Key Users (client-led)",
            "sap_tool": "SAP Cloud ALM (defect management)"
          }
        ],
        "deliverables": [
          "Fully configured S/4HANA Cloud system (QAS environment)",
          "BTP extensions deployed (mobile money integration, mobile apps if scoped)",
          "Master data loaded and validated",
          "Unit test results — all test cases passed",
          "Integration test results — all cross-module flows validated",
          "UAT sign-off from all process owners",
          "Defect log with all critical/high defects resolved"
        ],
        "staffing": [
          { "role": "Project Manager", "source": "Partner", "fte": 1.0 },
          { "role": "Solution Architect", "source": "Partner", "fte": 0.25 },
          { "role": "Functional Consultant (FI/CO)", "source": "Partner", "fte": 1.0 },
          { "role": "Functional Consultant (MM/SD)", "source": "Partner", "fte": 1.0 },
          { "role": "Functional Consultant (QM)", "source": "Partner", "fte": 0.5 },
          { "role": "Technical Consultant", "source": "Partner", "fte": 0.5 },
          { "role": "Data Migration Specialist", "source": "Partner", "fte": 0.5 },
          { "role": "Finance Lead", "source": "Client", "fte": 0.5 },
          { "role": "Operations Lead", "source": "Client", "fte": 0.5 },
          { "role": "Export Manager", "source": "Client", "fte": 0.5 },
          { "role": "Key Users (2-3)", "source": "Client", "fte": 0.25 }
        ],
        "phase_exit_criteria": [
          "All configuration tested and signed off",
          "BTP extensions functional and integration-tested",
          "Master data loaded and validated by process owners",
          "UAT completed with zero critical defects, fewer than 5 high defects open",
          "Process owners have signed UAT completion forms",
          "Production configuration transport tested"
        ]
      },

      {
        "phase_name": "Deploy",
        "sap_activate_phase": "Deploy",
        "wave": "W1",
        "duration_weeks": 4,
        "start_offset_weeks": 26,
        "duration_rationale": "Standard 4-8 weeks. 4 weeks for single-site, small user base. +1 week absorbed for limited IT capacity multiplier (1.1x). Training compressed to 2 weeks with role-based approach.",
        "key_activities": [
          {
            "activity": "End-User Training",
            "description": "Role-based training for all 19 users. Finance team: FI/CO transactions and reporting. Operations team: procurement, inventory, batch management. Export team: sales orders, billing, export documentation. Quality team: inspection recording and certificates. Management: dashboards and analytics. Training approach: hands-on workshops (not classroom lectures), 3-4 hours/day morning sessions.",
            "responsible": "Change Management Lead + Functional Consultants",
            "sap_tool": "SAP Learning Hub"
          },
          {
            "activity": "Training Materials Production",
            "description": "Produce laminated quick reference cards (A4, durable) for each role. English primary text with key terms in Swahili for field staff. Step-by-step process guides with screenshots. Video recordings of training sessions.",
            "responsible": "Change Management Lead",
            "sap_tool": "None"
          },
          {
            "activity": "Cutover Planning and Rehearsal",
            "description": "Define cutover sequence: freeze Excel operations, final data reconciliation, opening balance load to production, production configuration activation, mobile money integration go-live. One cutover rehearsal in QAS environment.",
            "responsible": "Project Manager + All Leads",
            "sap_tool": "SAP Cloud ALM (deployment management)"
          },
          {
            "activity": "Go-Live Readiness Assessment",
            "description": "Formal go/no-go assessment: all users trained, all critical defects resolved, cutover rehearsal successful, hypercare support confirmed, rollback plan documented.",
            "responsible": "Project Manager + Amina Cheyo",
            "sap_tool": "SAP Cloud ALM"
          },
          {
            "activity": "Go-Live Execution",
            "description": "Execute cutover plan. Activate production system. Verify first transactions: farmer payment, quality inspection, export order, financial posting. Confirm all integrations operational.",
            "responsible": "Full project team",
            "sap_tool": "S/4HANA Cloud Production"
          }
        ],
        "deliverables": [
          "Training completion records (all 19 users trained)",
          "Laminated reference cards produced and distributed",
          "Cutover plan (hour-by-hour for go-live weekend)",
          "Cutover rehearsal results",
          "Go/No-Go decision document signed by Amina Cheyo",
          "Production system live and operational"
        ],
        "staffing": [
          { "role": "Project Manager", "source": "Partner", "fte": 1.0 },
          { "role": "Solution Architect", "source": "Partner", "fte": 0.25 },
          { "role": "Functional Consultant (FI/CO)", "source": "Partner", "fte": 0.75 },
          { "role": "Functional Consultant (MM/SD)", "source": "Partner", "fte": 0.75 },
          { "role": "Technical Consultant", "source": "Partner", "fte": 0.5 },
          { "role": "Change Management Lead", "source": "Partner", "fte": 0.5 },
          { "role": "All Client Leads", "source": "Client", "fte": 0.75 }
        ],
        "phase_exit_criteria": [
          "Production system live and processing transactions",
          "All end users trained (100% completion rate)",
          "First business cycle verified (farmer purchase → quality inspection → export order → financial posting)",
          "Hypercare support structure activated"
        ]
      },

      {
        "phase_name": "Run (Hypercare)",
        "sap_activate_phase": "Run",
        "wave": "W1",
        "duration_weeks": 8,
        "start_offset_weeks": 30,
        "duration_rationale": "Extended from standard 4-6 weeks to 8 weeks because HHE has no prior ERP experience. First-time ERP users need intensive support through at least two complete month-end close cycles.",
        "key_activities": [
          {
            "activity": "Intensive Support (Weeks 1-4)",
            "description": "On-site support at Njombe and Mafinga during first purchasing cycle. Daily triage calls. Rapid issue resolution. User adoption monitoring. Floor walking during first transactions.",
            "responsible": "Partner team (reduced) + Client leads",
            "sap_tool": "SAP Cloud ALM (incident management)"
          },
          {
            "activity": "First Month-End Close Support",
            "description": "Guided support through first full financial close. Validate: multi-currency revaluation, period-end closing, FX gains/losses posting, financial report generation, bank reconciliation.",
            "responsible": "Functional Consultant (FI/CO)",
            "sap_tool": "S/4HANA Cloud"
          },
          {
            "activity": "Stabilization and Optimization (Weeks 5-8)",
            "description": "Address recurring issues. Fine-tune configurations. Optimize reports and dashboards for Amina and the investor. Begin knowledge transfer for ongoing administration.",
            "responsible": "Functional Consultants + Client Key Users",
            "sap_tool": "SAP Cloud ALM"
          },
          {
            "activity": "Knowledge Transfer and Handover",
            "description": "Formal knowledge transfer for day-to-day operations. Document standard operating procedures (SOPs). Establish SAP support channel access. Define ongoing support model (managed services agreement).",
            "responsible": "Partner team + Client super users",
            "sap_tool": "SAP for Me (support portal)"
          },
          {
            "activity": "Phase 2 Planning",
            "description": "Assess Phase 2 candidates: GTS for EU food-safety export compliance, advanced BTP mobile apps, farmer portal, analytics dashboards, potential Dar es Salaam retail line POS integration.",
            "responsible": "Solution Architect + Amina Cheyo",
            "sap_tool": "None"
          }
        ],
        "deliverables": [
          "Hypercare support log with all issues resolved",
          "Two month-end closes completed successfully",
          "Standard operating procedures (SOPs) for all core processes",
          "Knowledge transfer documentation",
          "System administration guide for designated super user",
          "Phase 2 roadmap recommendations",
          "Project closure report"
        ],
        "staffing": [
          { "role": "Project Manager", "source": "Partner", "fte": 0.25 },
          { "role": "Functional Consultant (FI/CO)", "source": "Partner", "fte": 0.5 },
          { "role": "Functional Consultant (MM/SD)", "source": "Partner", "fte": 0.25 },
          { "role": "Technical Consultant", "source": "Partner", "fte": 0.1 },
          { "role": "All Client Leads", "source": "Client", "fte": 0.25 }
        ],
        "phase_exit_criteria": [
          "Two consecutive month-end closes completed without critical issues",
          "Open incident count below threshold (< 5 medium, 0 critical)",
          "Client team self-sufficient for day-to-day operations",
          "Knowledge transfer signed off by designated client super user",
          "Project closure report accepted by Amina Cheyo"
        ]
      }
    ],

    "risk_register": [
      {
        "risk_id": "R01",
        "category": "Organizational",
        "description": "Change management resistance — staff accustomed to Excel and WhatsApp resist adopting SAP. Field workers at Njombe and seasonal workers at Mafinga may have limited technology exposure.",
        "probability": "HIGH",
        "impact": "HIGH",
        "risk_score": "CRITICAL",
        "mitigation_strategy": "Invest 15-20% of project budget in change management. Identify 3-5 internal super users and train intensively. Role-specific training with laminated reference cards in English + Swahili. On-site floor support during first harvest cycle.",
        "contingency_plan": "If adoption is critically low at go-live, implement a parallel-run period where both Excel and SAP are used for 4-6 weeks. Gradually sunset Excel process by process as confidence builds.",
        "risk_owner": "Amina Cheyo (Founder)",
        "monitoring_trigger": "Training completion rate below 80% two weeks before go-live; post-go-live transaction counts below 50% of expected volume"
      },
      {
        "risk_id": "R02",
        "category": "Technical",
        "description": "Internet connectivity at the Njombe collection station (rural Southern Highlands Zone) may be unreliable for cloud-based SAP access.",
        "probability": "HIGH",
        "impact": "MEDIUM",
        "risk_score": "HIGH",
        "mitigation_strategy": "Connectivity assessment during Discover phase. Budget for ISP upgrade or secondary connection. Design mobile apps with offline-first architecture. Identify backup connectivity (satellite, mobile hotspot).",
        "contingency_plan": "Deploy dedicated mobile hotspot (satellite or local ISP) at Njombe. For critical periods, pre-load data and sync batch when connected.",
        "risk_owner": "Technical Consultant",
        "monitoring_trigger": "Connectivity assessment shows <1 Mbps sustained or >30% downtime during business hours"
      },
      {
        "risk_id": "R03",
        "category": "Resource",
        "description": "No internal IT capacity — HHE has no IT staff to support an enterprise system post-implementation.",
        "probability": "MEDIUM",
        "impact": "HIGH",
        "risk_score": "HIGH",
        "mitigation_strategy": "Designate or hire a part-time IT coordinator / super user before go-live. Include comprehensive admin training in project scope. Establish Year 1 managed services agreement with implementation partner ($6,500/year budgeted).",
        "contingency_plan": "Extend managed services agreement to Year 2-3 if internal capacity is not established.",
        "risk_owner": "Amina Cheyo",
        "monitoring_trigger": "No IT coordinator identified by Explore phase; managed services agreement not signed by Deploy phase"
      },
      {
        "risk_id": "R04",
        "category": "Scope",
        "description": "Farmer procurement model is non-standard for SAP — 3,200+ individual smallholder suppliers with mobile money payments and quality-based differential pricing at point of purchase.",
        "probability": "HIGH",
        "impact": "MEDIUM",
        "risk_score": "HIGH",
        "mitigation_strategy": "Prototype farmer intake process in first 2 weeks of Explore. Validate: simplified PO processing vs. BTP mobile app. Engage SAP Agribusiness industry team for reference architectures.",
        "contingency_plan": "If standard MM proves unworkable for farmer procurement, implement a BTP-native intake application that feeds summarized data to SAP (aggregated POs per collection period rather than per-farmer transactions).",
        "risk_owner": "Solution Architect",
        "monitoring_trigger": "Prototype results from Explore show >50% deviation from standard MM process flow"
      },
      {
        "risk_id": "R05",
        "category": "Technical",
        "description": "Mobile money API integration is custom development with third-party dependency — API changes, uptime, and transaction limits outside HHE/SAP control.",
        "probability": "MEDIUM",
        "impact": "HIGH",
        "risk_score": "HIGH",
        "mitigation_strategy": "Engage the mobile money provider's technical team during Discover for API documentation and sandbox access. Build robust error handling and retry logic. Define SLA expectations with the provider. Proof-of-concept in Explore phase.",
        "contingency_plan": "Manual payment fallback process: export payment instructions from SAP, process through the provider's dashboard manually, import confirmation file. Eliminates automation but maintains operations.",
        "risk_owner": "Technical Consultant",
        "monitoring_trigger": "Provider sandbox not available by Explore phase; API response times >5 seconds during load testing"
      },
      {
        "risk_id": "R06",
        "category": "Financial",
        "description": "Budget overrun — tight investor-funded budget with limited contingency. Scope additions or timeline extensions could exceed approved envelope.",
        "probability": "MEDIUM",
        "impact": "MEDIUM",
        "risk_score": "MEDIUM",
        "mitigation_strategy": "Strict scope governance with formal change request process. Phase 2 parking lot for valid but non-critical requirements. 15-20% contingency approved upfront. Weekly budget burn rate tracking.",
        "contingency_plan": "If budget threshold reached at 80% with work remaining, present trade-off options to Amina: reduce scope (defer BTP mobile app), extend timeline (spread partner costs), or request additional investor funding.",
        "risk_owner": "Project Manager",
        "monitoring_trigger": "Actual spend exceeds 110% of planned spend at any phase gate"
      },
      {
        "risk_id": "R07",
        "category": "Scope",
        "description": "Scope creep — pressure to add features during workshops (e.g., farmer CRM, weather integration, certification tracking) that expand beyond Phase 1 core.",
        "probability": "MEDIUM",
        "impact": "MEDIUM",
        "risk_score": "MEDIUM",
        "mitigation_strategy": "Define firm Phase 1 scope before Explore begins. Use MoSCoW prioritization. Maintain Phase 2 backlog in Cloud ALM. Solution Architect has design authority to reject scope additions.",
        "contingency_plan": "If Amina insists on additional scope, present timeline and budget impact analysis before approving. Never add scope without adjusting one of: budget, timeline, or other scope items.",
        "risk_owner": "Solution Architect + Project Manager",
        "monitoring_trigger": "More than 3 change requests submitted during Explore; any change request estimated at >2 weeks effort"
      },
      {
        "risk_id": "R08",
        "category": "Technical",
        "description": "Farmer master data quality — Excel-based farmer records likely have inconsistent names, missing IDs, duplicates, and no standardized format.",
        "probability": "HIGH",
        "impact": "MEDIUM",
        "risk_score": "MEDIUM",
        "mitigation_strategy": "Begin data cleansing during Prepare phase. Define minimum required fields. Data cleansing sprint (4-6 weeks) with process owner validation. Consider field registration campaign.",
        "contingency_plan": "If data quality is too poor for full migration, migrate only verified/active farmers (~800 core suppliers) and add remaining farmers progressively during hypercare.",
        "risk_owner": "Data Migration Specialist + Operations Lead",
        "monitoring_trigger": "Dry run 1 shows >20% duplicate rate or >30% missing required fields"
      },
      {
        "risk_id": "R09",
        "category": "Resource",
        "description": "Client staff availability — process owners have day jobs running HHE operations and may not be available at the 50% allocation the project requires during Explore and Realize.",
        "probability": "MEDIUM",
        "impact": "MEDIUM",
        "risk_score": "MEDIUM",
        "mitigation_strategy": "Flexible workshop scheduling (2-3 days per week, morning sessions). Secure Amina's commitment to staff release. Consider hiring temporary replacements for key roles during peak project periods.",
        "contingency_plan": "Extend Explore phase by 2 weeks if client availability drops below 30%. Reschedule workshops rather than conducting them without process owner input.",
        "risk_owner": "Amina Cheyo + Project Manager",
        "monitoring_trigger": "Workshop attendance below 75% for any process area; UAT participation below 100% for process owners"
      },
      {
        "risk_id": "R10",
        "category": "Organizational",
        "description": "Seasonal workforce training continuity — 50-70 seasonal workers at Mafinga need training but are only present during harvest/processing season.",
        "probability": "MEDIUM",
        "impact": "LOW",
        "risk_score": "MEDIUM",
        "mitigation_strategy": "Time go-live to coincide with harvest season when seasonal workers are present. Focus seasonal worker training on limited transactions (goods receipt, basic quality recording). Laminated cards + video recordings for re-training each season.",
        "contingency_plan": "If seasonal workers are not present at go-live, permanent staff handle their SAP transactions initially. Train seasonal workers when they arrive with abbreviated 2-day program.",
        "risk_owner": "Change Management Lead",
        "monitoring_trigger": "Go-live date slips past October, missing seasonal worker availability window"
      },
      {
        "risk_id": "R11",
        "category": "External",
        "description": "Tanzania tax localization — VFD e-invoicing and withholding tax configuration may not be fully covered in SAP standard Tanzania country version.",
        "probability": "LOW",
        "impact": "MEDIUM",
        "risk_score": "LOW",
        "mitigation_strategy": "Verify SAP Tanzania localization coverage during Discover phase. Check current SAP Notes. If gaps, evaluate SAP Document Compliance or BTP-based TRA integration.",
        "contingency_plan": "Manual TRA portal submission as interim solution until SAP localization or BTP integration is available.",
        "risk_owner": "Functional Consultant (FI/CO)",
        "monitoring_trigger": "SAP Tanzania localization review reveals >2 critical tax compliance gaps"
      },
      {
        "risk_id": "R12",
        "category": "External",
        "description": "SAP GROW Public Edition scope item limitations — some HHE requirements may not be available as scope items in the Public Edition catalog.",
        "probability": "LOW",
        "impact": "MEDIUM",
        "risk_score": "LOW",
        "mitigation_strategy": "Run DDA during Discover to validate all required scope items against the catalog. Identify alternatives for any missing items (Key User Extensibility, BTP extensions).",
        "contingency_plan": "If critical scope items are unavailable, evaluate SAP S/4HANA Cloud Private Edition (more flexible but higher cost) or SAP Business One.",
        "risk_owner": "Solution Architect",
        "monitoring_trigger": "DDA reveals >3 required scope items not available in Public Edition"
      }
    ],

    "change_management_plan": {
      "ocm_approach": "ADKAR-aligned (Awareness → Desire → Knowledge → Ability → Reinforcement), adapted for a rural agricultural workforce with limited enterprise technology exposure. Emphasis on hands-on learning, visual materials, and leveraging existing communication channels (WhatsApp groups, physical notice boards).",
      "change_readiness_assessment": "LOW-MEDIUM. Executive sponsorship is strong (Amina Cheyo is personally driving transformation). However, the operational team has zero ERP experience, limited IT infrastructure exposure, and a mix of permanent and seasonal workers across two facilities. The jump from Excel/WhatsApp to SAP is the largest change management challenge in this project.",
      "stakeholder_engagement_strategy": "Amina Cheyo as active sponsor — visible, vocal, present at key milestones. 3-5 internal super users identified during Prepare, trained intensively, and empowered as first-line support. Monthly all-staff communication from Amina on project progress and benefits.",
      "communication_plan": {
        "audiences": ["Amina Cheyo (Founder)", "Lead Investor", "Process Owners (4)", "Njombe permanent staff (28)", "Mafinga seasonal workers (50-70)", "Export buyers (informational)"],
        "channels": ["WhatsApp groups (existing — primary for field staff)", "Physical notice boards at Njombe and Mafinga", "Monthly email update (Amina + Investor)", "Weekly project team meeting (Cloud ALM)"],
        "frequency": "Weekly for project team; bi-weekly for investor; monthly for all staff",
        "key_messages_by_phase": {
          "discover_prepare": "Why we are changing — HHE is growing and needs better tools to serve our farmers and buyers. SAP will help us track every kilo of cashew from farm to container.",
          "explore": "What will change for you — your specific role and daily tasks will look like this in the new system. Your input is shaping how the system works.",
          "realize": "How you will work — hands-on practice with the actual system using real HHE data. Your cashews, your farmers, your buyers.",
          "deploy": "You are ready — you have been trained, you have practiced, and support is available. This is our system now.",
          "run": "We are here to help — support is available every day. Tell us what is working and what needs adjustment."
        }
      },
      "training_plan": {
        "approach": "Direct Training (team too small for train-the-trainer)",
        "training_environments": "Dedicated training client (sandbox) with realistic HHE data — actual farmer names, cashew grades, buyer contracts",
        "training_schedule": "Deploy phase: 2 weeks of role-based training, 3-4 hours/day (morning sessions to accommodate afternoon operations)",
        "training_materials": [
          "Role-specific laminated quick reference cards (A4, durable, water-resistant for field use)",
          "English primary text with key terms in Swahili where helpful",
          "Step-by-step process guides with screenshots for each core transaction",
          "Video recordings of training sessions for seasonal worker re-training",
          "SAP Learning Hub access for self-paced reinforcement"
        ],
        "role_based_curricula": [
          "Finance team: FI postings, multi-currency transactions, period-end close, financial reports, bank reconciliation",
          "Operations team: create purchase orders/goods receipts, batch assignment, inventory transfers, stock overview",
          "Export/Sales team: create sales orders, delivery processing, billing, export documentation",
          "Quality team: create inspection lots, record grading results, quality certificates, batch classification",
          "Management: dashboard navigation, standard reports, analytics overview"
        ]
      },
      "go_live_readiness_criteria": [
        "100% of system users have completed role-based training (attendance + practical assessment)",
        "All process owners have signed UAT completion forms",
        "Cutover rehearsal completed with no critical issues",
        "Hypercare support structure confirmed (support hours, contact channels, escalation)",
        "First-week transaction scripts prepared and validated",
        "Rollback plan documented (revert to Excel for critical processes if catastrophic failure)"
      ]
    },

    "budget_framework": {
      "disclaimer": "Rough order-of-magnitude estimates for planning purposes only. Not a binding quotation. Actual costs depend on SAP GROW pricing (varies by region and negotiation), implementation partner rates (East Africa market), and client-specific factors. All figures in USD.",
      "currency": "USD",
      "cost_categories": [
        {
          "category": "SAP Licensing (Year 1)",
          "subcategories": ["SAP GROW starter pack", "S/4HANA Cloud Public Edition subscription", "BTP credits for mobile money integration"],
          "estimated_range_low": 16000,
          "estimated_range_high": 31000,
          "assumptions": ["SAP GROW starter pack for 15-20 named users", "Includes standard FI/CO, MM, SD, QM scope items", "BTP credits (~$3,000-$5,500/year)"],
          "phase_allocation": "Annual subscription — begins at system provisioning (Prepare phase)"
        },
        {
          "category": "Implementation Partner",
          "subcategories": ["Project management", "Solution architecture", "Functional consulting (FI/CO, MM/SD, QM)", "Technical consulting (BTP, integration)", "Change management and training"],
          "estimated_range_low": 52000,
          "estimated_range_high": 92000,
          "assumptions": ["Blended rate $100-$150/hour (East Africa regional partner)", "4-5 person core team over 7-month engagement", "Mix of onsite and remote delivery"],
          "phase_allocation": "Distributed across all phases; peak during Explore and Realize"
        },
        {
          "category": "Client Internal Resources",
          "subcategories": ["Process owner time", "Project champion time", "Executive sponsor time", "End-user training time"],
          "estimated_range_low": 10000,
          "estimated_range_high": 20000,
          "assumptions": ["Loaded cost of staff time at Tanzania salary levels", "Includes opportunity cost of day-job backfill"],
          "phase_allocation": "Explore and Realize = 60% of client resource cost"
        },
        {
          "category": "Infrastructure and Connectivity",
          "subcategories": ["Internet connectivity upgrade", "End-user devices (laptops/tablets)", "Backup power (UPS/generator)"],
          "estimated_range_low": 3000,
          "estimated_range_high": 8000,
          "assumptions": ["May need ISP upgrade at Njombe", "5-8 additional workstations or tablets", "Cloud infrastructure included in GROW subscription"],
          "phase_allocation": "One-time cost during Prepare phase"
        },
        {
          "category": "Data Migration",
          "subcategories": ["Data cleansing", "Master data preparation", "Opening balance preparation"],
          "estimated_range_low": 2000,
          "estimated_range_high": 5000,
          "assumptions": ["Greenfield — no complex legacy extraction", "Farmer master data cleansing from Excel (~3,200 records)", "Manual effort with process owner validation"],
          "phase_allocation": "Prepare and Realize phases"
        },
        {
          "category": "Training",
          "subcategories": ["Training facility setup", "Training materials production (laminated cards)", "SAP Learning Hub licenses"],
          "estimated_range_low": 2000,
          "estimated_range_high": 5000,
          "assumptions": ["Direct training delivery included in partner costs", "Materials production and printing", "Learning Hub for 15-20 users"],
          "phase_allocation": "Deploy phase"
        },
        {
          "category": "Contingency",
          "subcategories": ["Scope buffer", "Timeline buffer", "Unforeseen costs"],
          "estimated_range_low": 13000,
          "estimated_range_high": 29000,
          "assumptions": ["15-20% of total implementation cost", "Higher percentage reflects first-time ERP risk and inferred inputs"],
          "phase_allocation": "Held in reserve — released against approved change requests"
        }
      ],
      "total_estimated_range": {
        "low": 98000,
        "high": 190000
      },
      "annual_recurring_costs": {
        "licensing": 19000,
        "support": 6500,
        "infrastructure": 3000,
        "total_annual": 28500
      },
      "cost_optimization_recommendations": [
        "Leverage SAP GROW starter pack — purpose-built for mid-market with simplified pricing",
        "Use regional implementation partner with East Africa presence — significantly lower rates than Big 4",
        "Maximize remote delivery — onsite for workshops and training only",
        "Adopt SAP standard processes (Fit-to-Standard) to minimize custom development",
        "Phase advanced capabilities (GTS, analytics) to Phase 2 to keep initial investment manageable"
      ],
      "roi_considerations": [
        "Inventory traceability: reduce shrinkage — estimated 3-5% improvement in realized revenue per lot",
        "Financial reporting: reduce month-end close from ~5 days to ~1 day — free finance staff for analysis",
        "Multi-currency: reduce FX losses — estimated 1-2% improvement on international transactions",
        "Export documentation: reduce preparation time by 60-70% — faster shipment turnaround",
        "Scalability: system supports 7,000+ farmers without proportional headcount increase",
        "Investor confidence: professional-grade financial reporting supports future funding rounds"
      ]
    },

    "critical_path": {
      "critical_path_activities": [
        { "activity": "Scope validation and SAP GROW confirmation", "phase": "Discover", "duration_weeks": 3, "predecessors": [], "float_days": 0, "on_critical_path": true },
        { "activity": "System provisioning", "phase": "Prepare", "duration_weeks": 2, "predecessors": ["SAP GROW confirmation"], "float_days": 0, "on_critical_path": true },
        { "activity": "Org structure design", "phase": "Prepare", "duration_weeks": 3, "predecessors": ["Scope validation"], "float_days": 5, "on_critical_path": false },
        { "activity": "ERP fundamentals training", "phase": "Prepare", "duration_weeks": 2, "predecessors": ["Project kickoff"], "float_days": 10, "on_critical_path": false },
        { "activity": "Fit-to-Standard workshops", "phase": "Explore", "duration_weeks": 6, "predecessors": ["System provisioning", "Org structure design"], "float_days": 0, "on_critical_path": true },
        { "activity": "Integration architecture design", "phase": "Explore", "duration_weeks": 3, "predecessors": ["FtS workshops (week 2)"], "float_days": 10, "on_critical_path": false },
        { "activity": "Gap resolution design", "phase": "Explore", "duration_weeks": 2, "predecessors": ["FtS workshops"], "float_days": 0, "on_critical_path": true },
        { "activity": "System configuration", "phase": "Realize", "duration_weeks": 6, "predecessors": ["Gap resolution design"], "float_days": 0, "on_critical_path": true },
        { "activity": "BTP extension development", "phase": "Realize", "duration_weeks": 5, "predecessors": ["Integration architecture"], "float_days": 5, "on_critical_path": false },
        { "activity": "Data migration execution", "phase": "Realize", "duration_weeks": 3, "predecessors": ["System config (week 4)"], "float_days": 5, "on_critical_path": false },
        { "activity": "Integration testing", "phase": "Realize", "duration_weeks": 3, "predecessors": ["System config", "BTP extensions", "Data migration"], "float_days": 0, "on_critical_path": true },
        { "activity": "UAT", "phase": "Realize", "duration_weeks": 3, "predecessors": ["Integration testing"], "float_days": 0, "on_critical_path": true },
        { "activity": "End-user training", "phase": "Deploy", "duration_weeks": 2, "predecessors": ["UAT sign-off"], "float_days": 0, "on_critical_path": true },
        { "activity": "Cutover execution", "phase": "Deploy", "duration_weeks": 1, "predecessors": ["Training", "Cutover rehearsal"], "float_days": 0, "on_critical_path": true },
        { "activity": "Go-live", "phase": "Deploy", "duration_weeks": 0, "predecessors": ["Cutover execution"], "float_days": 0, "on_critical_path": true }
      ],
      "key_milestones": [
        { "milestone": "Project Kickoff", "target_date_offset_weeks": 0, "gate_type": "Phase Gate", "decision_maker": "Amina Cheyo" },
        { "milestone": "Discover Complete / Scope Confirmed", "target_date_offset_weeks": 3, "gate_type": "Phase Gate", "decision_maker": "Steering Committee" },
        { "milestone": "System Landscape Provisioned", "target_date_offset_weeks": 5, "gate_type": "Phase Gate", "decision_maker": "Project Manager" },
        { "milestone": "Prepare Complete", "target_date_offset_weeks": 8, "gate_type": "Phase Gate", "decision_maker": "Steering Committee" },
        { "milestone": "Fit-to-Standard Complete", "target_date_offset_weeks": 14, "gate_type": "Phase Gate", "decision_maker": "Solution Architect" },
        { "milestone": "Explore Complete / Design Approved", "target_date_offset_weeks": 16, "gate_type": "Steering Committee", "decision_maker": "Steering Committee" },
        { "milestone": "Configuration Complete", "target_date_offset_weeks": 22, "gate_type": "Phase Gate", "decision_maker": "Solution Architect" },
        { "milestone": "UAT Complete / Sign-Off", "target_date_offset_weeks": 26, "gate_type": "Go/No-Go", "decision_maker": "Process Owners + Amina" },
        { "milestone": "Go-Live", "target_date_offset_weeks": 30, "gate_type": "Go/No-Go", "decision_maker": "Steering Committee" },
        { "milestone": "Hypercare Complete / Project Closure", "target_date_offset_weeks": 38, "gate_type": "Phase Gate", "decision_maker": "Steering Committee" }
      ],
      "external_dependencies": [
        "SAP GROW subscription processing and tenant provisioning (2-3 weeks lead time)",
        "Mobile money provider API documentation and sandbox access (engage during Discover)",
        "Tanzania Revenue Authority e-invoicing requirements (clarify during Explore)",
        "Internet connectivity upgrade at Njombe (schedule during Prepare)",
        "Client staff availability around harvest season (Sep-Jan — plan Explore/Realize to avoid or accommodate)"
      ],
      "schedule_buffer": "5 days distributed: 2 days between Explore and Realize (design stabilization), 3 days between Realize and Deploy (defect resolution overflow). Additional: 2-week extension clause in SOW for Realize phase if UAT defect resolution requires additional cycles."
    },

    "sap_toolchain_usage_plan": [
      { "tool": "SAP for Me", "phases_used": ["Discover", "Prepare"], "specific_usage": "GROW subscription initiation, license management, tenant provisioning", "license_required": true, "setup_timing": "Activate during Discover" },
      { "tool": "Digital Discovery Assessment", "phases_used": ["Discover"], "specific_usage": "Validate scope items against S/4HANA Cloud Public Edition catalog", "license_required": false, "setup_timing": "Run during Discover workshops" },
      { "tool": "SAP Cloud ALM", "phases_used": ["Prepare", "Explore", "Realize", "Deploy", "Run"], "specific_usage": "Project workspace, requirements, test management, defect tracking, deployment management, incident management", "license_required": true, "setup_timing": "Configure first week of Prepare" },
      { "tool": "SAP Signavio", "phases_used": ["Explore"], "specific_usage": "Value Accelerators for Fit-to-Standard workshops. Process diagrams for procurement, sales, quality. No process mining (no digital processes to mine).", "license_required": true, "setup_timing": "Provision 1-2 weeks before Explore" },
      { "tool": "SAP Integration Suite (BTP)", "phases_used": ["Explore", "Realize"], "specific_usage": "Integration architecture design (Explore). Mobile money iFlow development, API management (Realize).", "license_required": true, "setup_timing": "BTP subaccount during Prepare; Integration Suite during Explore" },
      { "tool": "S/4HANA Cloud Migration Cockpit", "phases_used": ["Realize"], "specific_usage": "Master data migration using standard templates", "license_required": false, "setup_timing": "Configure migration objects during Realize" },
      { "tool": "Joule for Consultants (J4C)", "phases_used": ["Explore", "Realize"], "specific_usage": "Configuration guidance for multi-currency, batch management, QM inspection plans", "license_required": true, "setup_timing": "Available with SAP partner credentials" },
      { "tool": "SAP Learning Hub", "phases_used": ["Prepare", "Deploy"], "specific_usage": "ERP fundamentals (Prepare). Role-based training reinforcement (Deploy).", "license_required": true, "setup_timing": "Licenses during Prepare" }
    ]
  }
}
```

---

## Timeline Visual Summary

```
Week:  0    3    5    8         14   16         22   26  28  30         38
       |    |    |    |          |    |          |    |   |   |          |
       |-Discover-|    |          |    |          |    |   |   |          |
            |--Prepare--|          |    |          |    |   |   |          |
                 |------Explore-------|    |          |    |   |   |          |
                                       |------Realize-------|   |   |          |
                                                             |-Deploy-|          |
                                                                  |---Hypercare--|

Milestones:
  W0  = Project Kickoff (May 2026)
  W3  = Scope Confirmed
  W5  = System Provisioned
  W8  = Prepare Complete
  W14 = Fit-to-Standard Done
  W16 = Explore Complete
  W22 = Configuration Complete
  W26 = UAT Sign-Off
  W30 = GO-LIVE (October 2026)
  W38 = Project Closure (January 2027)
```

---

## Go-Live Timing Recommendation

**Target: October 2026** — aligned with the start of the main cashew harvest purchasing season.

Rationale:
- HHE's highest-volume operations occur during harvest (October–January). Going live before the harvest ensures the system is tested under real production conditions with on-site support available.
- Seasonal workers at Mafinga are present during harvest — they can be trained during the Deploy phase and immediately use the system.
- If go-live slips past October, the next viable window is March-April 2027 (post-harvest lull), adding 4-5 months to the timeline.
- Kickoff in May 2026 provides a comfortable 7.5-month runway to October go-live, with buffer.

---

*Generated by SAP S/4HANA Implementation Scoping Agent — Skill 03: Implementation Roadmap Generator*
*Source data completeness: 74% (Skill 01) | Roadmap confidence: MEDIUM*
