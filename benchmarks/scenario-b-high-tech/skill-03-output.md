# Skill 03 Output: Implementation Roadmap -- Constellation Satellite Systems (CSS)

## Roadmap Metadata

| Field | Value |
|---|---|
| **Roadmap ID** | IR-20260222-CSS |
| **Source Brief** | DB-20260222-CSS |
| **Source Module Analysis** | MFA-20260222-CSS |
| **Created Date** | 2026-02-22 |
| **Confidence Level** | HIGH |
| **Roadmap Version** | 1.0 |

---

## Implementation Roadmap

```json
{
  "implementation_roadmap": {
    "metadata": {
      "roadmap_id": "IR-20260222-CSS",
      "created_date": "2026-02-22T00:00:00Z",
      "source_brief_id": "DB-20260222-CSS",
      "source_module_analysis_id": "MFA-20260222-CSS",
      "roadmap_version": "1.0",
      "confidence_level": "HIGH",
      "assumptions": [
        "Revenue at ~$1.2B annually with growth trajectory tied to constellation deployment schedule",
        "~800 active SAP users (Professional + Limited Professional licenses) across 3 US sites",
        "Board-mandated go-live deadline of December 2028 for core finance and operations",
        "Budget envelope of $15M-$25M allocated for the full transformation program",
        "Parent company alignment to S/4HANA Cloud Private Edition is a firm requirement, not optional",
        "Custom code remediation can begin as a pre-project initiative (Wave 0) without waiting for full program approval",
        "Siemens Teamcenter PLM and Dassault Apriso MES remain as best-of-breed systems; integration redesign, not replacement",
        "CSS can dedicate 10-15 internal FTEs to the program alongside implementation partner resources",
        "SAP Basis team of 4 FTEs transitions to Cloud PE operations role post-conversion",
        "ITAR compliance constraints will require dedicated security architecture workstream",
        "Satellite production rate scales from 5/month to 15/month during the program timeline, requiring careful cutover planning"
      ],
      "caveats": [
        "Budget estimates are ROM (Rough Order of Magnitude) -- formal quotation requires SAP pricing engagement, partner SOW, and infrastructure sizing",
        "System conversion duration estimates depend on database size (not specified in discovery); large databases (>5TB) may extend downtime windows",
        "Custom code analysis results may shift wave boundaries if critical objects require Wave 1 remediation",
        "MES and PLM integration architectures require dedicated technical discovery workshops beyond this roadmap",
        "Two failed IT projects (MES upgrade, PLM migration) create elevated organizational risk that may slow adoption",
        "Parent company alignment timeline may impose additional constraints on go-live sequencing",
        "ITAR-controlled data handling during system conversion requires specialized security clearance for some partner resources"
      ]
    },

    "roadmap_summary": {
      "program_name": "Project Polaris -- CSS S/4HANA Transformation",
      "recommended_edition": "S/4HANA Cloud Private Edition (RISE with SAP)",
      "transformation_type": "System Conversion (Brownfield)",
      "go_live_strategy": "Phased (by module group, 3 waves)",
      "go_live_strategy_rationale": "A big bang approach carries unacceptable risk for an enterprise of this complexity with 2,400 custom objects, critical ITAR compliance requirements, and organizational change fatigue from two recent failed IT projects. Phasing by module group allows: (1) early wins with finance to build organizational confidence; (2) GTS/ITAR compliance addressed in Wave 1 to remove the highest-severity regulatory risk; (3) manufacturing modules in Wave 2 aligned to the production scale-up timeline; (4) advanced capabilities in Wave 3 after the organization has absorbed core changes. A geographic phasing alternative was considered but rejected because all three sites share a single SAP instance and the same process landscape.",
      "total_duration_months": 22,
      "number_of_waves": 3,
      "wave_summary": [
        {
          "wave_id": "W0",
          "name": "Pre-Project Preparation",
          "scope_description": "Custom code analysis and classification (ATC/CCM), Clean Core assessment, Signavio process discovery, LeanIX application rationalization, system conversion readiness assessment, program governance setup, OCM baseline",
          "target_go_live": "N/A (preparation phase)",
          "duration_months": 4
        },
        {
          "wave_id": "W1",
          "name": "Core Finance and Compliance",
          "scope_description": "FI/CO conversion with Universal Journal migration, IFRS 15/ASC 606 revenue recognition, GTS full implementation for ITAR/EAR compliance, basic MM/SD conversion, custom code remediation (Phase 1: critical objects)",
          "target_go_live": "Month 14 from program start",
          "duration_months": 10
        },
        {
          "wave_id": "W2",
          "name": "Manufacturing and Supply Chain",
          "scope_description": "PP conversion with enhanced BOM management, QM conversion with space-grade quality inspection plans, PM conversion with calibration management, PLM integration redesign (Teamcenter), MES integration redesign (Apriso), supply chain visibility enhancements",
          "target_go_live": "Month 20 from program start",
          "duration_months": 6
        },
        {
          "wave_id": "W3",
          "name": "Advanced Capabilities and Optimization",
          "scope_description": "PS enhancement with earned value management, advanced analytics and embedded reporting, remaining custom code retirement (Phase 2), Cloud ALM steady-state operations, integration cleanup and middleware decommissioning",
          "target_go_live": "Month 22 from program start",
          "duration_months": 4
        }
      ],
      "overall_program_risk": "HIGH",
      "clean_core_strategy": "Pragmatic compliance -- target Clean Core Level B from current Level D. Remediate custom code in two phases: Phase 1 (Wave 0/W1) addresses critical and high-priority objects; Phase 2 (W3) retires remaining objects. Extensions via BTP side-by-side model for net-new requirements. Accept managed exceptions for ITAR-specific customizations where no Clean Core alternative exists.",
      "cloud_alm_project_type": "Migration"
    },

    "phase_plan": [
      {
        "phase_name": "Discover and Prepare",
        "sap_activate_phase": "Discover + Prepare",
        "wave": "W0 (Pre-Project Preparation)",
        "duration_weeks": 16,
        "start_offset_weeks": 0,
        "duration_rationale": "Extended Discover/Prepare for a heavily customized brownfield conversion. 4 months allows proper custom code analysis (2,400 objects), Signavio process mining, LeanIX application rationalization, and program governance setup. Also provides time for OCM baseline assessment to address organizational change fatigue.",
        "key_activities": [
          {
            "activity": "Custom Code Analysis and Classification",
            "description": "Run SAP Custom Code Migration Worklist and ABAP Test Cockpit (ATC) against all 2,400 custom objects and 47 custom transactions. Classify each object: (1) Retire -- no longer needed, can be deleted; (2) Refactor -- needed but must be rewritten for S/4HANA compatibility; (3) Retain -- compatible with S/4HANA, keep as-is; (4) Replace -- standard S/4HANA functionality now covers this. Target: 60% reduction aligned to CIO mandate.",
            "responsible": "SAP Technical Architect + CSS Basis Team",
            "sap_tool": "SAP Custom Code Migration Worklist, ABAP Test Cockpit (ATC), Simplification Item Catalog"
          },
          {
            "activity": "Signavio Process Discovery",
            "description": "Deploy SAP Signavio Process Intelligence to mine current ECC transaction logs. Map actual process execution patterns for Order-to-Cash, Procure-to-Pay, Plan-to-Produce, and Record-to-Report. Identify process variants, bottlenecks, and deviation from SAP standard. Output feeds Explore phase Fit-to-Standard workshops.",
            "responsible": "Process Architect + Business Process Owners",
            "sap_tool": "SAP Signavio Process Intelligence, Value Accelerators"
          },
          {
            "activity": "LeanIX Application Rationalization",
            "description": "Map the full CSS application landscape including all 12 custom middleware interfaces, Teamcenter, Apriso, Salesforce, Workday, Anaplan. Identify redundancies, retirement candidates, and integration architecture target state. Align with parent company enterprise architecture standards.",
            "responsible": "Enterprise Architect + CIO Office",
            "sap_tool": "LeanIX Enterprise Architecture Management"
          },
          {
            "activity": "System Conversion Readiness Assessment",
            "description": "Evaluate technical readiness for system conversion: database size assessment, Unicode compliance check, add-on compatibility analysis, dual-stack to single-stack requirements, OS/DB migration needs if applicable. Assess downtime window requirements against production schedule (satellite manufacturing cannot tolerate extended outages).",
            "responsible": "SAP Technical Architect + Basis Team Lead",
            "sap_tool": "SAP Readiness Check, SAP Maintenance Planner"
          },
          {
            "activity": "Clean Core Maturity Assessment",
            "description": "Evaluate current Clean Core maturity level across all 5 dimensions: custom code, integrations, extensions, processes, data. Current state assessed at Level D (heavily customized with 2,400 objects, 12 custom interfaces, partial GTS). Target state: Level B (pragmatic compliance with managed extensions for ITAR-specific requirements).",
            "responsible": "SAP Solution Architect + Technical Architect",
            "sap_tool": "SAP Clean Core Dashboard, Custom Code Migration Worklist"
          },
          {
            "activity": "ITAR Security Architecture Design",
            "description": "Design the security architecture for ITAR-controlled data in S/4HANA Cloud Private Edition. Define data classification taxonomy, role-based access controls, deemed export controls for non-US-person access, audit trail requirements. Engage SAP and hosting partner on ITAR-compliant infrastructure (FedRAMP or equivalent).",
            "responsible": "CISO + SAP Security Architect",
            "sap_tool": "SAP GTS License Management, S/4HANA Authorization Framework"
          },
          {
            "activity": "Program Governance Setup",
            "description": "Establish steering committee (CIO sponsor, CFO co-sponsor, VP Manufacturing, CISO), program management office (PMO), and wave delivery teams. Define RACI, escalation paths, and decision-making authority. Address organizational skepticism head-on: present lessons learned from failed MES and PLM projects, define how this program is structured differently.",
            "responsible": "Program Director + CIO",
            "sap_tool": "SAP Cloud ALM (project setup, task management)"
          },
          {
            "activity": "OCM Baseline and Change Readiness Assessment",
            "description": "Conduct formal change readiness assessment across all 3 sites. Identify change champions and resistors. Assess impact of 2 failed IT projects on organizational willingness to adopt. Design targeted communication strategy that acknowledges past failures and differentiates this program. Establish change agent network.",
            "responsible": "OCM Lead + HR Business Partners",
            "sap_tool": "SAP Signavio Process Governance (communication of process changes)"
          }
        ],
        "deliverables": [
          "Custom Code Analysis Report (2,400 objects classified with remediation recommendations)",
          "Process Discovery Report (Signavio output with variant analysis and Fit-to-Standard readiness)",
          "Application Landscape Map (LeanIX output with target state architecture)",
          "System Conversion Readiness Report (technical assessment with risk items)",
          "Clean Core Maturity Assessment (Level D current state with Level B target roadmap)",
          "ITAR Security Architecture Design Document",
          "Program Charter with governance structure and RACI",
          "Change Readiness Assessment Report with OCM strategy",
          "Updated budget estimate (ROM narrowed to +/-20% based on custom code analysis results)"
        ],
        "staffing": [
          {"role": "Program Director", "source": "Partner", "fte": 1.0, "key_skills": ["SAP program management", "aerospace/defense industry", "brownfield conversions"]},
          {"role": "SAP Solution Architect", "source": "Partner", "fte": 1.0, "key_skills": ["S/4HANA Cloud PE architecture", "system conversion", "Clean Core"]},
          {"role": "SAP Technical Architect", "source": "Partner", "fte": 1.0, "key_skills": ["ABAP analysis", "ATC/CCM", "S/4HANA conversion tools"]},
          {"role": "Process Architect", "source": "Partner", "fte": 0.5, "key_skills": ["Signavio", "process mining", "Fit-to-Standard"]},
          {"role": "Enterprise Architect", "source": "Client", "fte": 0.5, "key_skills": ["LeanIX", "integration architecture"]},
          {"role": "Security Architect", "source": "Partner", "fte": 0.5, "key_skills": ["ITAR compliance", "SAP GTS", "S/4HANA authorization"]},
          {"role": "OCM Lead", "source": "Partner", "fte": 0.5, "key_skills": ["Organizational change management", "stakeholder engagement"]},
          {"role": "CSS Internal Team (part-time)", "source": "Client", "fte": 3.0, "key_skills": ["SAP Basis", "business process knowledge", "functional SMEs"]}
        ],
        "prerequisites": [
          "Board approval for $15-25M program budget",
          "CIO sponsor confirmed and empowered for cross-functional decisions",
          "Implementation partner selected (ideally with A&D industry experience and ITAR clearance)",
          "SAP RISE with SAP contract negotiated (Private Edition sizing, licensing)",
          "Parent company alignment confirmed (hosting partner, Signavio/LeanIX licensing)"
        ],
        "risks": [
          {"risk": "Custom code analysis reveals higher remediation effort than estimated", "severity": "HIGH", "mitigation": "Early ATC/CCM analysis in Week 1-4; build contingency of 20% into remediation estimates"},
          {"risk": "ITAR security requirements constrain hosting partner selection", "severity": "HIGH", "mitigation": "Engage SAP and hosting partner early on ITAR-compliant infrastructure options (FedRAMP, IL4/IL5)"},
          {"risk": "Organizational resistance based on failed MES/PLM projects", "severity": "HIGH", "mitigation": "Address head-on in program charter; demonstrate structural differences from prior projects; quick wins in Wave 1"},
          {"risk": "Parent company imposes constraints that conflict with CSS operational needs", "severity": "MEDIUM", "mitigation": "Establish alignment governance with parent IT leadership; document CSS-specific requirements that justify deviations"}
        ],
        "phase_exit_criteria": [
          "Custom code analysis completed for all 2,400 objects with classification results",
          "Signavio process discovery completed with variant analysis for top 10 processes",
          "System conversion readiness assessment completed with no P1 blockers",
          "ITAR security architecture approved by CISO",
          "Program governance established with steering committee charter signed",
          "Budget estimate refined to +/-20% accuracy",
          "Implementation partner SOW executed"
        ]
      },
      {
        "phase_name": "Explore (Wave 1)",
        "sap_activate_phase": "Explore",
        "wave": "W1 -- Core Finance and Compliance",
        "duration_weeks": 8,
        "start_offset_weeks": 16,
        "duration_rationale": "8-week Explore for Wave 1 covers FI/CO, GTS, and basic MM/SD. Finance and GTS are the most complex functional areas for CSS. Signavio Value Accelerators used to accelerate Fit-to-Standard workshops. Additional complexity from IFRS 15/ASC 606 configuration requirements.",
        "key_activities": [
          {
            "activity": "Fit-to-Standard Workshops -- Finance",
            "description": "Conduct Fit-to-Standard workshops for FI/CO covering: Universal Journal migration impact, IFRS 15/ASC 606 revenue recognition for long-term satellite contracts, program-level profitability analysis (CO-PA), milestone billing, intercompany with parent conglomerate, financial close process redesign (12 days to 5 days target). Use Signavio Value Accelerators for Record-to-Report process alignment.",
            "responsible": "FI/CO Solution Architect + CFO Office",
            "sap_tool": "SAP Signavio Value Accelerators, Fit-to-Standard Workshop Templates"
          },
          {
            "activity": "Fit-to-Standard Workshops -- GTS/ITAR",
            "description": "Conduct Fit-to-Standard workshops for GTS covering: ITAR/EAR license management, denied party screening, deemed export controls, trade preference management, product classification (ECCN/USML). Map current manual and fragmented processes to GTS standard. Define custom extension requirements for CSS-specific ITAR workflows.",
            "responsible": "GTS Solution Architect + CISO + Legal/Compliance",
            "sap_tool": "SAP GTS Best Practice Content, Fit-to-Standard Workshop Templates"
          },
          {
            "activity": "Fit-to-Standard Workshops -- MM/SD (Basic)",
            "description": "Conduct Fit-to-Standard for core procurement (MM) and sales order management (SD). Focus areas: long-lead component procurement (18+ month lead times), supplier collaboration, milestone billing for satellite programs, Salesforce CRM integration architecture.",
            "responsible": "MM/SD Solution Architect + Procurement/Sales SMEs",
            "sap_tool": "SAP Signavio Value Accelerators for Procure-to-Pay and Order-to-Cash"
          },
          {
            "activity": "Custom Code Remediation Planning (Phase 1)",
            "description": "Based on W0 analysis results, develop detailed remediation plan for critical and high-priority custom objects required for Wave 1 go-live. Estimate: ~400-600 objects in Phase 1 remediation scope (retire, refactor, or replace). Assign to development sprints during Realize phase.",
            "responsible": "Technical Architect + ABAP Development Lead",
            "sap_tool": "SAP Custom Code Migration Worklist, ABAP Test Cockpit"
          },
          {
            "activity": "Integration Architecture Design -- Wave 1",
            "description": "Design integration architecture for Wave 1 scope: SAP Integration Suite (BTP) as target middleware replacing custom interfaces. Wave 1 integrations: Workday HCM (payroll posting), Salesforce CRM (opportunity-to-order), Anaplan (financial planning data exchange), parent company consolidation.",
            "responsible": "Integration Architect + CIO Office",
            "sap_tool": "SAP Integration Suite (BTP), SAP API Business Hub"
          }
        ],
        "deliverables": [
          "Fit-to-Standard documentation for FI/CO, GTS, MM, SD",
          "Gap list with disposition (standard, configuration, BTP extension, managed exception)",
          "IFRS 15/ASC 606 configuration design document",
          "GTS/ITAR compliance architecture (detailed)",
          "Custom code remediation plan -- Phase 1 (400-600 objects)",
          "Integration architecture design -- Wave 1",
          "Solution design document for Wave 1 scope",
          "Updated risk register"
        ],
        "staffing": [
          {"role": "Program Director", "source": "Partner", "fte": 1.0, "key_skills": ["Program management", "A&D industry"]},
          {"role": "SAP Solution Architect", "source": "Partner", "fte": 1.0, "key_skills": ["S/4HANA architecture", "Fit-to-Standard facilitation"]},
          {"role": "FI/CO Solution Architect", "source": "Partner", "fte": 1.0, "key_skills": ["Universal Journal", "IFRS 15", "CO-PA"]},
          {"role": "GTS Solution Architect", "source": "Partner", "fte": 1.0, "key_skills": ["SAP GTS", "ITAR/EAR compliance"]},
          {"role": "MM/SD Consultant", "source": "Partner", "fte": 1.0, "key_skills": ["Procurement", "sales order management"]},
          {"role": "Technical Architect", "source": "Partner", "fte": 1.0, "key_skills": ["ABAP", "custom code remediation", "conversion tools"]},
          {"role": "Integration Architect", "source": "Partner", "fte": 0.5, "key_skills": ["SAP Integration Suite", "BTP", "middleware"]},
          {"role": "OCM Lead", "source": "Partner", "fte": 0.5, "key_skills": ["Change management", "stakeholder engagement"]},
          {"role": "CSS Business SMEs", "source": "Client", "fte": 4.0, "key_skills": ["Finance", "compliance", "procurement", "sales"]}
        ],
        "phase_exit_criteria": [
          "All Fit-to-Standard workshops completed with sign-off from process owners",
          "Gap list approved by steering committee with disposition for each gap",
          "ITAR security architecture validated by CISO",
          "Custom code remediation Phase 1 plan approved",
          "Integration architecture design approved by CIO",
          "Solution design document baselined"
        ]
      },
      {
        "phase_name": "Realize (Wave 1)",
        "sap_activate_phase": "Realize",
        "wave": "W1 -- Core Finance and Compliance",
        "duration_weeks": 16,
        "start_offset_weeks": 24,
        "duration_rationale": "16-week Realize for Wave 1. FI/CO configuration includes Universal Journal migration, IFRS 15 setup, and CO-PA redesign. GTS full implementation is a major workstream. Custom code remediation Phase 1 runs in parallel. Includes 2 cycles of integration testing and 1 cycle of UAT.",
        "key_activities": [
          {
            "activity": "FI/CO Configuration and Conversion",
            "description": "Configure S/4HANA finance: Universal Journal activation, New Asset Accounting migration, IFRS 15/ASC 606 revenue recognition for long-term satellite contracts (milestone-based POC method), program-level CO-PA for satellite programs, intercompany accounting with parent conglomerate, financial close process optimization (target 5-day close). Joule for Consultants (J4C) used for configuration acceleration.",
            "responsible": "FI/CO Solution Architect + Finance Business SMEs",
            "sap_tool": "S/4HANA Configuration, Joule for Consultants (J4C), SAP Cloud ALM"
          },
          {
            "activity": "GTS Full Implementation",
            "description": "Implement SAP GTS for comprehensive ITAR/EAR compliance: license management for export licenses and agreements, denied party screening (DPS) with daily list updates, product classification (ECCN and USML categories), deemed export controls for non-US-person access, trade compliance document generation, audit trail and reporting for DDTC/BIS. This is the most complex workstream in Wave 1.",
            "responsible": "GTS Solution Architect + Legal/Compliance + CISO",
            "sap_tool": "SAP GTS, S/4HANA Integration with GTS"
          },
          {
            "activity": "MM/SD Basic Conversion",
            "description": "Convert core procurement and sales processes to S/4HANA. Procurement: supplier master migration, purchase order conversion, goods receipt. Sales: sales order conversion, milestone billing configuration, output management. Integration: Salesforce CRM opportunity-to-order flow via SAP Integration Suite.",
            "responsible": "MM/SD Consultant + Procurement/Sales SMEs",
            "sap_tool": "S/4HANA Configuration, SAP Data Migration Cockpit"
          },
          {
            "activity": "Custom Code Remediation -- Phase 1",
            "description": "Execute Phase 1 custom code remediation: retire unnecessary objects, refactor critical custom code for S/4HANA compatibility, replace custom functionality with standard S/4HANA features where available. Target: 400-600 objects addressed (retire ~250, refactor ~100, replace ~100-250 with standard). Development sprints with bi-weekly code review.",
            "responsible": "Technical Architect + ABAP Development Team",
            "sap_tool": "ABAP Test Cockpit (ATC), SAP Custom Code Migration Worklist, Eclipse ADT"
          },
          {
            "activity": "System Conversion Technical Execution",
            "description": "Execute the technical system conversion using SAP Software Update Manager (SUM) with Database Migration Option (DMO). Includes: database migration (to SAP HANA if not already), S/4HANA conversion, data migration and cleansing, technical testing. Plan for 2-3 dress rehearsal conversions before production cutover.",
            "responsible": "Technical Architect + SAP Basis Team",
            "sap_tool": "SUM/DMO, SAP Readiness Check, SAP Maintenance Planner"
          },
          {
            "activity": "Integration Development -- Wave 1",
            "description": "Build Wave 1 integrations on SAP Integration Suite (BTP): Workday HCM payroll posting, Salesforce CRM opportunity-to-order, Anaplan financial planning data exchange, parent company consolidation data feed. Retire corresponding custom middleware interfaces.",
            "responsible": "Integration Architect + Integration Developers",
            "sap_tool": "SAP Integration Suite (BTP), SAP API Business Hub"
          },
          {
            "activity": "Testing (SIT, Integration, UAT)",
            "description": "2 cycles of system integration testing (SIT), 1 cycle of integration testing with connected systems (Workday, Salesforce, Anaplan), 1 cycle of user acceptance testing (UAT). GTS/ITAR compliance testing requires specialized test scenarios with CISO sign-off. Defect management via SAP Cloud ALM.",
            "responsible": "Test Manager + Business SMEs + CISO (GTS testing)",
            "sap_tool": "SAP Cloud ALM (test management, defect tracking)"
          }
        ],
        "deliverables": [
          "Configured S/4HANA system (Wave 1 scope: FI/CO, GTS, MM, SD)",
          "Custom code remediation Phase 1 completed (400-600 objects)",
          "Wave 1 integrations built and tested on SAP Integration Suite",
          "System conversion dress rehearsal results (2-3 cycles)",
          "Test results: SIT, integration testing, UAT with sign-off",
          "GTS/ITAR compliance validation report (CISO approved)",
          "IFRS 15/ASC 606 parallel run results",
          "Cutover plan for Wave 1 go-live",
          "End-user training materials for Wave 1 scope"
        ],
        "staffing": [
          {"role": "Program Director", "source": "Partner", "fte": 1.0, "key_skills": ["Program management"]},
          {"role": "FI/CO Solution Architect", "source": "Partner", "fte": 1.0, "key_skills": ["Universal Journal", "IFRS 15"]},
          {"role": "GTS Solution Architect", "source": "Partner", "fte": 1.0, "key_skills": ["SAP GTS", "ITAR/EAR"]},
          {"role": "MM/SD Consultant", "source": "Partner", "fte": 1.0, "key_skills": ["Procurement", "sales"]},
          {"role": "Technical Architect", "source": "Partner", "fte": 1.0, "key_skills": ["System conversion", "SUM/DMO"]},
          {"role": "ABAP Developers (2-3)", "source": "Partner", "fte": 2.5, "key_skills": ["ABAP", "S/4HANA", "custom code remediation"]},
          {"role": "Integration Developers (2)", "source": "Partner", "fte": 2.0, "key_skills": ["SAP Integration Suite", "BTP"]},
          {"role": "Test Manager", "source": "Partner", "fte": 1.0, "key_skills": ["SAP testing", "Cloud ALM"]},
          {"role": "OCM Lead", "source": "Partner", "fte": 1.0, "key_skills": ["Change management", "training"]},
          {"role": "CSS Business SMEs", "source": "Client", "fte": 6.0, "key_skills": ["Finance", "compliance", "procurement", "sales"]},
          {"role": "CSS Basis Team", "source": "Client", "fte": 2.0, "key_skills": ["SAP Basis", "system administration"]}
        ],
        "phase_exit_criteria": [
          "All Wave 1 configuration completed and unit tested",
          "Custom code remediation Phase 1 completed with ATC clean results",
          "GTS/ITAR compliance validated by CISO and legal",
          "IFRS 15/ASC 606 parallel run successful for 2 reporting periods",
          "System conversion dress rehearsal completed within acceptable downtime window",
          "UAT completed with business sign-off (>95% test cases passed)",
          "Wave 1 integrations tested end-to-end",
          "End-user training delivered for finance and compliance users",
          "Go/No-Go decision by steering committee"
        ]
      },
      {
        "phase_name": "Deploy (Wave 1) and Explore (Wave 2)",
        "sap_activate_phase": "Deploy + Explore",
        "wave": "W1 Deploy + W2 Explore (overlapping)",
        "duration_weeks": 8,
        "start_offset_weeks": 40,
        "duration_rationale": "Wave 1 Deploy (4 weeks cutover + hypercare) overlaps with Wave 2 Explore (8 weeks). This parallelism is possible because W2 Explore is primarily workshop-based and does not conflict with W1 production cutover. Overlap saves 4 weeks on the critical path.",
        "key_activities": [
          {
            "activity": "Wave 1 Production Cutover",
            "description": "Execute production system conversion during a planned downtime window. Sequence: final data migration and cleansing, production system conversion via SUM/DMO, integration switchover to SAP Integration Suite, GTS activation with ITAR controls, financial data validation, smoke testing, user access provisioning. Cutover window: target 48-72 hours (weekend + buffer).",
            "responsible": "Technical Architect + Basis Team + Cutover Manager",
            "sap_tool": "SUM/DMO, SAP Cloud ALM (cutover management)"
          },
          {
            "activity": "Wave 1 Hypercare (4 weeks)",
            "description": "Intensive post-go-live support for finance and compliance users. Dedicated support team on-site at all 3 locations. Priority focus: financial posting accuracy, GTS compliance verification, integration monitoring, performance optimization. Daily triage calls, weekly steering committee updates.",
            "responsible": "All Wave 1 consultants + CSS super users",
            "sap_tool": "SAP Cloud ALM (incident management, monitoring)"
          },
          {
            "activity": "Fit-to-Standard Workshops -- Manufacturing (PP, QM, PM)",
            "description": "Conduct Fit-to-Standard workshops for Wave 2 manufacturing modules. PP: BOM management (engineering, manufacturing, as-built), production planning for 15 satellites/month, MRP for long-lead components. QM: space-grade quality inspection plans, non-conformance management. PM: calibration management, clean room equipment maintenance. Use Signavio Value Accelerators for Plan-to-Produce.",
            "responsible": "PP/QM/PM Solution Architects + VP Manufacturing + Production SMEs",
            "sap_tool": "SAP Signavio Value Accelerators for Plan-to-Produce"
          },
          {
            "activity": "PLM and MES Integration Architecture Design",
            "description": "Design the target integration architecture for Teamcenter PLM and Apriso MES with S/4HANA. PLM: engineering BOM to manufacturing BOM synchronization via SAP Integration Suite (replacing custom middleware; target: real-time or near-real-time sync). MES: Apriso to S/4HANA shop floor integration (replacing 4-hour lag with real-time confirmation posting). As-built BOM capture architecture.",
            "responsible": "Integration Architect + PLM/MES Technical SMEs",
            "sap_tool": "SAP Integration Suite, SAP API Business Hub"
          }
        ],
        "deliverables": [
          "Wave 1 production go-live (FI/CO, GTS, MM, SD)",
          "Hypercare closure report with stabilization metrics",
          "Fit-to-Standard documentation for PP, QM, PM",
          "PLM integration architecture design (Teamcenter)",
          "MES integration architecture design (Apriso)",
          "Wave 2 solution design document",
          "Updated risk register reflecting Wave 1 lessons learned"
        ],
        "staffing": [
          {"role": "Program Director", "source": "Partner", "fte": 1.0, "key_skills": ["Program management"]},
          {"role": "Wave 1 Support Team", "source": "Partner", "fte": 4.0, "key_skills": ["FI/CO", "GTS", "MM/SD", "Basis"]},
          {"role": "PP/QM/PM Solution Architect", "source": "Partner", "fte": 1.0, "key_skills": ["Manufacturing", "quality", "maintenance"]},
          {"role": "Integration Architect", "source": "Partner", "fte": 1.0, "key_skills": ["PLM/MES integration", "SAP Integration Suite"]},
          {"role": "OCM Lead", "source": "Partner", "fte": 0.5, "key_skills": ["Change management"]},
          {"role": "CSS Manufacturing SMEs", "source": "Client", "fte": 4.0, "key_skills": ["Production planning", "quality", "maintenance"]}
        ],
        "phase_exit_criteria": [
          "Wave 1 hypercare closed with <5 P1 incidents open",
          "Finance team operating independently on S/4HANA",
          "GTS compliance verified for first month of live ITAR transactions",
          "Wave 2 Fit-to-Standard completed with sign-off",
          "PLM and MES integration architectures approved",
          "Wave 2 Realize scope and timeline confirmed"
        ]
      },
      {
        "phase_name": "Realize and Deploy (Wave 2)",
        "sap_activate_phase": "Realize + Deploy",
        "wave": "W2 -- Manufacturing and Supply Chain",
        "duration_weeks": 20,
        "start_offset_weeks": 48,
        "duration_rationale": "20 weeks for Wave 2 Realize (16 weeks) plus Deploy (4 weeks). Manufacturing modules (PP, QM, PM) are the highest complexity workstream due to BOM management, PLM integration, and MES integration. The production scale-up (5 to 15 satellites/month) adds operational risk to cutover planning.",
        "key_activities": [
          {
            "activity": "PP Configuration -- BOM Management",
            "description": "Configure S/4HANA PP for integrated BOM lifecycle management. Engineering BOM (sourced from Teamcenter PLM, synchronized via Integration Suite), Manufacturing BOM (derived from eBOM with production-specific components, routings, work centers), As-Built BOM (captured from MES confirmations via Apriso integration). Enable BOM comparison and change management. Configure MRP for long-lead component planning (18+ month horizons).",
            "responsible": "PP Solution Architect + Manufacturing Engineering",
            "sap_tool": "S/4HANA PP Configuration, Joule for Consultants"
          },
          {
            "activity": "QM Configuration -- Space-Grade Quality",
            "description": "Configure QM for aerospace quality requirements: incoming inspection plans for space-grade components (AS9100 compliance), in-process inspection at satellite assembly stages, final inspection and test before launch delivery. Non-conformance management with MRB (Material Review Board) workflow. Certificate of Conformance generation. Calibration management for test and measurement equipment.",
            "responsible": "QM Solution Architect + Quality Engineering",
            "sap_tool": "S/4HANA QM Configuration"
          },
          {
            "activity": "PM Configuration -- Calibration and Clean Room",
            "description": "Configure PM for manufacturing asset maintenance: calibration management for test equipment (traceability to NIST standards), clean room environment monitoring and maintenance, preventive maintenance scheduling aligned to production shifts.",
            "responsible": "PM Consultant + Facilities/Maintenance SMEs",
            "sap_tool": "S/4HANA PM Configuration"
          },
          {
            "activity": "PLM Integration Build (Teamcenter)",
            "description": "Build the Teamcenter PLM to S/4HANA integration on SAP Integration Suite. Engineering BOM synchronization with change management (ECN/ECO workflow). Target: near-real-time BOM sync replacing current custom middleware with 4+ hour lag. Material master harmonization between PLM and ERP.",
            "responsible": "Integration Architect + PLM Technical Team",
            "sap_tool": "SAP Integration Suite, Teamcenter Gateway for SAP"
          },
          {
            "activity": "MES Integration Build (Apriso)",
            "description": "Build the Apriso MES to S/4HANA integration on SAP Integration Suite. Production order download, confirmation posting (real-time replacing 4-hour lag), goods movement posting, as-built BOM capture. Enable real-time manufacturing visibility -- the CEO's 'digital factory' requirement.",
            "responsible": "Integration Architect + MES Technical Team",
            "sap_tool": "SAP Integration Suite"
          },
          {
            "activity": "Supply Chain Visibility Enhancement",
            "description": "Configure enhanced supply chain visibility for long-lead components. Supplier collaboration portal, delivery schedule monitoring, predictive delivery tracking using SAP IBP (Integrated Business Planning) or embedded analytics. Focus on the 18+ month lead time space-grade electronics pipeline.",
            "responsible": "MM Solution Architect + Supply Chain SMEs",
            "sap_tool": "S/4HANA Embedded Analytics, SAP IBP (if licensed)"
          },
          {
            "activity": "Wave 2 Testing and Cutover",
            "description": "Manufacturing-specific testing: BOM lifecycle testing (eBOM to mBOM to as-built), MRP run validation, quality inspection workflow testing, PLM sync testing, MES integration testing. UAT with production floor users. Cutover plan must account for satellite manufacturing schedule -- zero tolerance for production disruption during cutover weekend.",
            "responsible": "Test Manager + Manufacturing SMEs",
            "sap_tool": "SAP Cloud ALM (test management)"
          }
        ],
        "deliverables": [
          "Configured S/4HANA manufacturing modules (PP, QM, PM)",
          "PLM integration live (Teamcenter to S/4HANA via Integration Suite)",
          "MES integration live (Apriso to S/4HANA -- real-time)",
          "BOM lifecycle management operational (eBOM, mBOM, as-built)",
          "Wave 2 production go-live (manufacturing and supply chain)",
          "Real-time manufacturing visibility dashboard (CEO 'digital factory')",
          "Wave 2 hypercare closure report"
        ],
        "staffing": [
          {"role": "Program Director", "source": "Partner", "fte": 1.0, "key_skills": ["Program management"]},
          {"role": "PP Solution Architect", "source": "Partner", "fte": 1.0, "key_skills": ["S/4HANA PP", "BOM management", "MRP"]},
          {"role": "QM Solution Architect", "source": "Partner", "fte": 1.0, "key_skills": ["S/4HANA QM", "AS9100", "aerospace quality"]},
          {"role": "PM Consultant", "source": "Partner", "fte": 0.5, "key_skills": ["S/4HANA PM", "calibration"]},
          {"role": "Integration Architects (2)", "source": "Partner", "fte": 2.0, "key_skills": ["PLM integration", "MES integration", "SAP Integration Suite"]},
          {"role": "Integration Developers (2)", "source": "Partner", "fte": 2.0, "key_skills": ["SAP Integration Suite", "iFlow development"]},
          {"role": "ABAP Developers (1-2)", "source": "Partner", "fte": 1.5, "key_skills": ["Custom code remediation", "BOM extensions"]},
          {"role": "Test Manager", "source": "Partner", "fte": 1.0, "key_skills": ["Manufacturing testing", "integration testing"]},
          {"role": "OCM Lead", "source": "Partner", "fte": 1.0, "key_skills": ["Shop floor change management"]},
          {"role": "CSS Manufacturing SMEs", "source": "Client", "fte": 6.0, "key_skills": ["Production planning", "quality", "maintenance", "PLM", "MES"]}
        ],
        "phase_exit_criteria": [
          "PP, QM, PM configured and tested",
          "PLM integration live with BOM sync validated",
          "MES integration live with real-time confirmation posting",
          "As-built BOM capture validated for 3+ satellite assemblies",
          "MRP run validated for long-lead components",
          "Wave 2 UAT passed with manufacturing sign-off",
          "Cutover completed within planned downtime window",
          "Wave 2 hypercare closed with <3 P1 incidents open"
        ]
      },
      {
        "phase_name": "Realize and Deploy (Wave 3)",
        "sap_activate_phase": "Realize + Deploy",
        "wave": "W3 -- Advanced Capabilities and Optimization",
        "duration_weeks": 12,
        "start_offset_weeks": 68,
        "duration_rationale": "12 weeks for Wave 3 covering PS enhancement, analytics, remaining custom code retirement, and integration cleanup. Lighter scope than W1/W2 because core modules are already live. Focus is on optimization and technical debt reduction.",
        "key_activities": [
          {
            "activity": "PS Enhancement -- Earned Value Management",
            "description": "Enhance Project System for satellite program management with proper earned value management (EVM) in SAP rather than Excel. Configure WBS structures for satellite programs, earned value calculation methods, program-level reporting. Integrate with CO-PA for program profitability analysis.",
            "responsible": "PS Consultant + Program Management Office",
            "sap_tool": "S/4HANA PS Configuration"
          },
          {
            "activity": "Advanced Analytics and Reporting",
            "description": "Deploy embedded analytics for operational visibility: real-time financial dashboards (CFO), manufacturing KPI dashboards (VP Manufacturing, CEO 'digital factory'), supply chain visibility dashboards, compliance reporting (CISO). Configure SAP Analytics Cloud (SAC) for executive reporting and predictive analytics.",
            "responsible": "Analytics Consultant + Business Intelligence Team",
            "sap_tool": "S/4HANA Embedded Analytics, SAP Analytics Cloud (SAC)"
          },
          {
            "activity": "Custom Code Retirement -- Phase 2",
            "description": "Complete the custom code remediation program. Phase 2 targets the remaining ~800-1,000 objects not addressed in Phase 1. Focus on retirement (removing unused custom transactions) and replacement with standard S/4HANA functionality. Target: achieve 60% total reduction from original 2,400 objects (CIO mandate). Final Clean Core Level B assessment.",
            "responsible": "Technical Architect + ABAP Development Team",
            "sap_tool": "ABAP Test Cockpit, Custom Code Migration Worklist"
          },
          {
            "activity": "Integration Cleanup and Middleware Decommission",
            "description": "Retire remaining custom middleware interfaces now replaced by SAP Integration Suite. Decommission legacy PI/PO or custom middleware. Validate all 12 original custom interfaces have been migrated or retired. Final integration architecture documentation for LeanIX.",
            "responsible": "Integration Architect + CIO Office",
            "sap_tool": "SAP Integration Suite, LeanIX"
          },
          {
            "activity": "Cloud ALM Steady-State Setup",
            "description": "Configure SAP Cloud ALM for steady-state operations: monitoring, incident management, change management, release management. Transition from project mode to operations mode. Train CSS IT team on Cloud ALM operations.",
            "responsible": "Solution Architect + CSS IT Operations",
            "sap_tool": "SAP Cloud ALM (operations)"
          }
        ],
        "deliverables": [
          "PS earned value management live and operational",
          "Executive dashboards deployed (SAP Analytics Cloud)",
          "Custom code reduced by 60% (target: ~960 objects remaining from 2,400)",
          "All 12 custom middleware interfaces migrated or retired",
          "Cloud ALM configured for steady-state operations",
          "Clean Core Level B assessment completed and documented",
          "Final program closure report",
          "Lessons learned document for parent company reference"
        ],
        "staffing": [
          {"role": "Program Director", "source": "Partner", "fte": 0.5, "key_skills": ["Program closure"]},
          {"role": "PS Consultant", "source": "Partner", "fte": 1.0, "key_skills": ["S/4HANA PS", "earned value management"]},
          {"role": "Analytics Consultant", "source": "Partner", "fte": 1.0, "key_skills": ["SAC", "embedded analytics"]},
          {"role": "Technical Architect", "source": "Partner", "fte": 0.5, "key_skills": ["Custom code remediation", "Clean Core"]},
          {"role": "ABAP Developer", "source": "Partner", "fte": 1.0, "key_skills": ["ABAP", "code retirement"]},
          {"role": "Integration Architect", "source": "Partner", "fte": 0.5, "key_skills": ["Middleware decommission"]},
          {"role": "Cloud ALM Consultant", "source": "Partner", "fte": 0.5, "key_skills": ["Cloud ALM operations"]},
          {"role": "OCM Lead", "source": "Partner", "fte": 0.5, "key_skills": ["Change management"]},
          {"role": "CSS IT Operations", "source": "Client", "fte": 4.0, "key_skills": ["SAP operations", "Basis"]}
        ],
        "phase_exit_criteria": [
          "PS earned value management validated with 2+ satellite programs",
          "Executive dashboards live with automated data refresh",
          "Custom code count at or below 960 objects (60% reduction achieved)",
          "All custom middleware interfaces decommissioned",
          "Cloud ALM steady-state operational with CSS IT team trained",
          "Clean Core Level B confirmed",
          "Program closure approved by steering committee",
          "Transition to AMS (Application Management Services) completed"
        ]
      }
    ],

    "risk_register": [
      {
        "risk_id": "R01",
        "category": "Organizational",
        "description": "Change fatigue from 2 failed IT projects (MES upgrade, PLM migration) creates resistance to the S/4HANA transformation program",
        "probability": "HIGH",
        "impact": "HIGH",
        "severity": "CRITICAL",
        "mitigation": "Address head-on in program charter. Demonstrate structural differences: dedicated OCM workstream, wave-based delivery with early wins, steering committee with C-level accountability, lessons learned from failed projects incorporated. Invest in change champion network at each site. Celebrate Wave 1 go-live as proof point.",
        "owner": "OCM Lead + CIO",
        "phase": "All phases"
      },
      {
        "risk_id": "R02",
        "category": "Technical",
        "description": "Custom code remediation for 2,400 objects is more complex than estimated, extending timeline and budget",
        "probability": "MEDIUM",
        "impact": "HIGH",
        "severity": "HIGH",
        "mitigation": "Early ATC/CCM analysis in Wave 0 (first 4 weeks). Build 20% contingency into remediation estimates. Phase remediation across W0/W1 (Phase 1: critical) and W3 (Phase 2: remaining). Accept that some objects may need to be retained as managed exceptions if remediation is cost-prohibitive.",
        "owner": "Technical Architect",
        "phase": "W0, W1, W3"
      },
      {
        "risk_id": "R03",
        "category": "Compliance",
        "description": "ITAR compliance requirements constrain hosting partner selection, partner staffing, and data handling, potentially delaying deployment",
        "probability": "MEDIUM",
        "impact": "HIGH",
        "severity": "HIGH",
        "mitigation": "Engage SAP and hosting partner early on ITAR-compliant infrastructure (FedRAMP, GovCloud options). Require ITAR clearance for partner resources accessing controlled data. Design data classification taxonomy in Wave 0. CISO sign-off gate at each phase exit.",
        "owner": "CISO + Program Director",
        "phase": "W0, W1"
      },
      {
        "risk_id": "R04",
        "category": "Integration",
        "description": "PLM (Teamcenter) and MES (Apriso) integration redesign is more complex than architectural direction suggests, requiring extended technical discovery",
        "probability": "MEDIUM",
        "impact": "MEDIUM",
        "severity": "MEDIUM",
        "mitigation": "Dedicated integration architecture design workshops in W2 Explore. Engage Siemens (Teamcenter) and Dassault (Apriso) integration specialists. Plan for 2-3 integration prototype sprints before committing to final architecture. Fallback: retain current integration patterns with incremental improvement if full redesign is too risky.",
        "owner": "Integration Architect",
        "phase": "W2"
      },
      {
        "risk_id": "R05",
        "category": "Operational",
        "description": "Satellite production scale-up (5 to 15/month) during the transformation program creates competing priorities and resource constraints",
        "probability": "HIGH",
        "impact": "MEDIUM",
        "severity": "HIGH",
        "mitigation": "Wave 2 cutover timing aligned to production schedule windows. Dedicated client SMEs allocated at agreed FTE levels (contract with business unit leaders). Manufacturing modules deployed after production team has absorbed Wave 1 changes. Hypercare staffing plan for Wave 2 accounts for production surge.",
        "owner": "VP Manufacturing + Program Director",
        "phase": "W2"
      },
      {
        "risk_id": "R06",
        "category": "Financial",
        "description": "Program cost exceeds $25M allocated budget due to scope creep, extended remediation, or integration complexity",
        "probability": "LOW",
        "impact": "HIGH",
        "severity": "MEDIUM",
        "mitigation": "ROM budget estimate of $18M-$23M provides $2M-$7M buffer within allocated range. Strict scope governance with change request process. Wave 3 scope can be deferred if budget pressure requires it (PS enhancement and analytics are valuable but not time-critical). Monthly budget tracking with steering committee visibility.",
        "owner": "Program Director + CFO",
        "phase": "All phases"
      },
      {
        "risk_id": "R07",
        "category": "Technical",
        "description": "System conversion downtime window insufficient for database size, requiring extended production outage",
        "probability": "MEDIUM",
        "impact": "HIGH",
        "severity": "HIGH",
        "mitigation": "Assess database size in Wave 0. Plan for 2-3 dress rehearsal conversions to validate downtime requirements. Near-zero downtime conversion options (SUM/DMO with nZDM) if database size exceeds planning parameters. Production schedule planning for cutover weekends.",
        "owner": "Technical Architect + Basis Team Lead",
        "phase": "W0, W1"
      },
      {
        "risk_id": "R08",
        "category": "Organizational",
        "description": "Parent company alignment requirements impose constraints that conflict with CSS operational timelines or priorities",
        "probability": "MEDIUM",
        "impact": "MEDIUM",
        "severity": "MEDIUM",
        "mitigation": "Establish parent company alignment governance committee. Document CSS-specific requirements that justify deviations from parent standards. Negotiate shared hosting and licensing terms early. Regular sync meetings with parent IT leadership.",
        "owner": "CIO + Program Director",
        "phase": "All phases"
      }
    ],

    "budget_framework": {
      "total_estimated_range": "$18,000,000 to $23,000,000",
      "budget_validation": "Within allocated range of $15M-$25M. ROM estimate based on: system conversion scope (not greenfield), 2,400 custom code objects, 3-wave delivery, 22-month duration, enterprise partner rates. Low end assumes efficient custom code remediation and clean PLM/MES integration. High end includes extended remediation, complex integration prototyping, and additional OCM investment.",
      "cost_breakdown": [
        {
          "category": "SAP Licensing (RISE with SAP -- Private Edition)",
          "estimated_range": "$2,500,000 to $3,500,000",
          "notes": "Annual subscription for ~800 users. Includes S/4HANA Cloud PE, SAP Integration Suite, Cloud ALM. Signavio and LeanIX licensed through parent company agreement. 3-year initial term assumed."
        },
        {
          "category": "Implementation Partner Services",
          "estimated_range": "$10,000,000 to $13,000,000",
          "notes": "15-20 partner FTEs over 22 months at blended rate of $250-$350/hour. Includes all waves: solution architecture, configuration, custom code remediation, integration development, testing, training, OCM. Rate assumption based on Tier 1/Tier 2 partner with A&D industry experience and ITAR clearance."
        },
        {
          "category": "Infrastructure and Hosting",
          "estimated_range": "$1,500,000 to $2,000,000",
          "notes": "RISE with SAP hosting costs for Private Edition. Includes development, quality, and production landscapes. ITAR-compliant hosting may carry premium. BTP runtime costs for integrations and extensions."
        },
        {
          "category": "Internal CSS Resources (Opportunity Cost)",
          "estimated_range": "$2,000,000 to $2,500,000",
          "notes": "10-15 CSS FTEs at varying allocation levels over 22 months. Includes business SME time, Basis team, IT operations. Not typically counted in external spend but represents real program cost."
        },
        {
          "category": "Contingency (15%)",
          "estimated_range": "$2,000,000 to $3,000,000",
          "notes": "Standard 15% contingency for enterprise transformation programs. Primary contingency drivers: custom code remediation overrun, PLM/MES integration complexity, ITAR hosting requirements, OCM investment increase."
        }
      ],
      "roi_timeline": "24 to 36 months post-Wave 3 go-live",
      "roi_drivers": [
        "Financial close reduction from 12 to 5 days (CFO target) -- estimated $500K-$1M annual value in reduced period-end resource costs and faster decision-making",
        "Custom code maintenance reduction (60% object retirement) -- estimated $800K-$1.2M annual savings in Basis and development support costs",
        "Real-time manufacturing visibility (elimination of 4-hour MES lag) -- estimated $1M-$2M annual value in production efficiency and quality improvement",
        "ITAR compliance automation via GTS (replacing manual processes) -- estimated $300K-$500K annual savings plus regulatory risk reduction (non-compliance penalties can reach $1M+ per violation)",
        "Middleware decommissioning (12 custom interfaces replaced by Integration Suite) -- estimated $400K-$600K annual savings in maintenance and support",
        "Parent company alignment (shared hosting, tools, processes) -- estimated $500K-$800K annual savings through economies of scale"
      ]
    },

    "change_management_strategy": {
      "approach": "Intensive, evidence-based OCM program designed to overcome organizational skepticism from 2 failed IT projects. The strategy acknowledges past failures explicitly and demonstrates how this program is structurally different.",
      "key_principles": [
        "Transparency: Acknowledge the MES and PLM project failures openly. Share what went wrong and how Project Polaris addresses those failure modes.",
        "Early wins: Wave 1 delivers visible improvements (faster financial close, automated ITAR compliance) that build credibility before tackling the higher-risk manufacturing scope in Wave 2.",
        "Site-specific engagement: Each of the 3 sites (Redmond, Huntsville, Cape Canaveral) has different roles, cultures, and concerns. OCM activities are tailored to site context.",
        "Manufacturing floor credibility: VP Manufacturing is the most influential stakeholder for Wave 2 adoption. Engage manufacturing leadership as co-owners of the solution design, not recipients of IT decisions.",
        "Measurable outcomes: Define and track adoption KPIs (login rates, transaction volumes, process compliance) weekly during hypercare and monthly thereafter."
      ],
      "ocm_workstreams": [
        {
          "workstream": "Leadership Alignment",
          "activities": ["Steering committee charter with defined decision authority", "Monthly executive briefings with progress metrics", "CEO-sponsored town halls at each site before each wave go-live", "Lessons learned sessions referencing prior failed projects"],
          "target_audience": "C-suite, VP level, parent company IT leadership"
        },
        {
          "workstream": "Change Champion Network",
          "activities": ["Identify 2-3 change champions per site (total 6-9)", "Train champions on S/4HANA navigation and key process changes", "Champions participate in UAT and provide peer feedback", "Champions serve as first-line support during hypercare"],
          "target_audience": "Mid-level managers and respected individual contributors at each site"
        },
        {
          "workstream": "Training Program",
          "activities": ["Role-based training curriculum (finance, compliance, procurement, manufacturing, management)", "Hands-on simulation in sandbox environment", "Quick reference guides for the 47 custom transactions being retired (mapped to S/4HANA standard equivalents)", "SAP Enable Now for on-screen guided tours"],
          "target_audience": "All 800 SAP users"
        },
        {
          "workstream": "Communication",
          "activities": ["Program newsletter (monthly)", "Site visit days where leadership observes training progress", "Intranet portal with FAQs, timeline, and feedback channel", "Anonymous feedback mechanism to surface concerns without fear of attribution"],
          "target_audience": "All CSS employees (not just SAP users)"
        }
      ]
    },

    "timeline_visualization": {
      "program_start": "Month 0",
      "wave_0_start": "Month 0",
      "wave_0_end": "Month 4",
      "wave_1_explore_start": "Month 4",
      "wave_1_explore_end": "Month 6",
      "wave_1_realize_start": "Month 6",
      "wave_1_realize_end": "Month 10",
      "wave_1_deploy_start": "Month 10",
      "wave_1_golive": "Month 14",
      "wave_2_explore_start": "Month 10",
      "wave_2_realize_start": "Month 12",
      "wave_2_deploy_start": "Month 18",
      "wave_2_golive": "Month 20",
      "wave_3_realize_start": "Month 18",
      "wave_3_deploy_start": "Month 20",
      "wave_3_golive": "Month 22",
      "program_end": "Month 22",
      "board_deadline": "December 2028",
      "notes": "Waves 2 and 3 Explore/Realize phases overlap with prior wave Deploy/Hypercare to compress timeline. Total program duration of 22 months fits within the board's December 2028 mandate assuming program start by March 2027."
    }
  }
}
```

---

## Roadmap Narrative Summary

### Program Overview

Project Polaris is a 22-month, 3-wave S/4HANA transformation program for Constellation Satellite Systems (CSS). The program converts the existing SAP ECC 6.0 EHP8 system to S/4HANA Cloud Private Edition (RISE with SAP), aligning CSS with the parent company's SAP strategy while addressing critical operational challenges in financial management, ITAR compliance, and manufacturing visibility.

The system conversion (brownfield) approach preserves CSS's existing investment in SAP master data, configuration, and business process knowledge while enabling modernization. This decision was driven by the scale of the existing SAP footprint (800 users, 7+ modules) and the need to minimize business disruption during a period of rapid production scale-up.

### Wave Structure Rationale

**Wave 0 (Months 0 to 4): Pre-Project Preparation.** This is the most critical planning phase. With 2,400 custom ABAP objects, CSS must understand its custom code landscape before committing to wave boundaries and timelines. The ATC/CCM analysis output directly shapes the remediation plan and may shift scope between waves. Signavio process mining and LeanIX application rationalization provide the analytical foundation for Fit-to-Standard workshops in subsequent waves.

**Wave 1 (Months 4 to 14): Core Finance and Compliance.** Finance first for three reasons: (1) the CFO's 5-day close target is achievable with S/4HANA Universal Journal and delivers a visible early win; (2) IFRS 15/ASC 606 revenue recognition is a compliance requirement that must be addressed; (3) GTS full implementation for ITAR/EAR compliance is non-negotiable and must precede manufacturing go-live (ITAR controls must be in place before any production data flows through the converted system). Wave 1 also includes basic MM/SD conversion to ensure procurement and sales processes remain functional.

**Wave 2 (Months 10 to 20): Manufacturing and Supply Chain.** The highest complexity wave. BOM lifecycle management (engineering, manufacturing, as-built) is the hardest integration challenge. PLM (Teamcenter) and MES (Apriso) integration redesigns transform CSS's manufacturing data flows from batch-lag to near-real-time. This wave delivers the CEO's "digital factory" vision. Timing accounts for the satellite production scale-up -- cutover planning must avoid disrupting the ramp from 5 to 15 satellites per month.

**Wave 3 (Months 18 to 22): Advanced Capabilities and Optimization.** PS earned value management moves program tracking from Excel into SAP. Executive analytics dashboards provide the real-time visibility demanded by leadership. The remaining custom code retirement (Phase 2) achieves the CIO's 60% reduction target. Integration cleanup decommissions the 12 legacy custom middleware interfaces.

### Critical Success Factors

1. **OCM investment is proportional to organizational risk.** The 2 failed IT projects make change management the single most important workstream. Budget for OCM at 8 to 10% of total program cost, not the typical 3 to 5%.

2. **Custom code analysis drives everything.** The Wave 0 ATC/CCM results will validate or challenge every timeline and budget estimate in this roadmap. If analysis reveals that 30%+ of objects require refactoring (vs. retirement or replacement), both timeline and budget should be adjusted upward.

3. **ITAR constrains partner selection.** Not all SAP implementation partners have the clearances and infrastructure to handle ITAR-controlled data. The partner selection process must include ITAR capability as a non-negotiable criterion.

4. **Production schedule alignment for Wave 2 cutover.** The satellite production scale-up cannot be interrupted. Wave 2 cutover must be planned around production windows, potentially requiring extended parallel-run periods.

5. **Parent company alignment governance.** Regular synchronization with parent company IT leadership prevents late-stage conflicts over architecture, hosting, or process standards.

### Key Metrics

| Metric | Current State | Target State (Post-Wave 3) |
|---|---|---|
| Financial close cycle | 12 business days | 5 business days |
| Custom ABAP objects | 2,400 | Less than 960 (60% reduction) |
| MES-to-SAP data lag | 4 hours | Real-time |
| ITAR compliance coverage | Partial (GTS + manual) | Full (SAP GTS automated) |
| Revenue recognition | Manual (Excel) | Automated (IFRS 15/ASC 606) |
| Clean Core maturity | Level D | Level B |
| BOM management | Disconnected (PLM/SAP/manual) | Integrated lifecycle (eBOM/mBOM/as-built) |
| Earned value management | Excel outside SAP | S/4HANA PS integrated |
| Custom middleware interfaces | 12 custom | SAP Integration Suite (standard) |
| Satellite production rate | 5/month | 15/month (supported by digital factory) |

---

## Cross-Skill Consistency Verification

| Data Point | Skill 01 Value | Skill 02 Value | Skill 03 Value |
|---|---|---|---|
| Employee count | ~2,500 | ~2,500 | ~2,500 |
| Revenue | ~$1.2B | ~$1.2B | ~$1.2B |
| SAP users | ~800 | ~800 | ~800 |
| Custom objects | ~2,400 + 47 transactions | 2,400 objects, 47 transactions | 2,400 objects |
| Budget range | $15M-$25M allocated | $15M-$25M | $18M-$23M (ROM within allocated range) |
| Timeline | Board deadline Dec 2028 | 18-24 months recommended | 22 months (fits Dec 2028 with Mar 2027 start) |
| Recommended edition | S/4HANA Cloud PE (RISE) | S/4HANA Cloud PE (RISE) | S/4HANA Cloud PE (RISE) |
| Transformation type | System Conversion | System Conversion | System Conversion (Brownfield) |
| Critical modules | FI/CO, PP, GTS | FI (3.5), PP (2.5), GTS (2.0) | W1: FI/CO + GTS, W2: PP + QM + PM |
| Clean Core | Level D current | Level D current, Level B target | Level D to Level B, pragmatic compliance |
| Top risk | Change fatigue | Custom code (2,400 objects) | Change fatigue (R01, CRITICAL) |
| Parent alignment | S/4HANA Cloud PE, Signavio, LeanIX | Signavio, LeanIX, Cloud ALM | Signavio, LeanIX, Cloud ALM referenced |
