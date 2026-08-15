# Skill 03: Implementation Roadmap Generator

## Purpose

Consume the structured discovery brief (Skill 01) and module fit analysis (Skill 02) to produce a phased implementation roadmap aligned to SAP Activate methodology. The roadmap covers the full project lifecycle from Discover through Run, with calibrated timelines, resource models, risk registers, change management strategy, budget framework, and Clean Core compliance planning. This is the deliverable that transforms analytical findings into an actionable project plan.

**SAP Ecosystem Positioning:** This skill generates the implementation roadmap that would typically be created in SAP Cloud ALM's project planning module. Cloud ALM provides the governance framework — task management, requirements tracking, test orchestration, deployment coordination — but it requires a human architect to define the project phases, wave structure, resource plan, and critical path. This skill automates that initial planning, producing output structured for direct import into Cloud ALM's project workspace. It also references where SAP Signavio's Value Accelerators would be used during the Explore phase for Fit-to-Standard process validation, and where Joule for Consultants would accelerate configuration during Realize.

---

## Inputs

| Source | Data Consumed | Key Fields Used |
|---|---|---|
| **Skill 01 — Discovery Brief** | Client context, organizational readiness, constraints | `client_profile` (size, geography, industry), `transformation_context` (timeline, budget, change readiness, deployment preference), `stakeholder_map`, `compliance_and_regulatory` |
| **Skill 02 — Module Fit Analysis** | Module scope, integration complexity, sizing | `module_assessment_matrix` (confirmed modules, fit scores, gap counts), `integration_dependencies` (cross-module and third-party), `sizing_recommendation` (edition, user counts, infrastructure) |
| **Skill 05 — SAP Best Practices** (optional) | Industry-specific implementation patterns | Relevant SAP best practice scope items, industry-specific process variants, reference timelines from SAP Model Company |

---

## Output: Implementation Roadmap

```json
{
  "implementation_roadmap": {
    "metadata": {
      "roadmap_id": "IR-{YYYYMMDD}-{CLIENT_SHORT}",
      "created_date": "ISO 8601",
      "source_brief_id": "DB-{ref}",
      "source_module_analysis_id": "MFA-{ref}",
      "roadmap_version": "1.0",
      "confidence_level": "HIGH | MEDIUM | LOW",
      "assumptions": ["list of planning assumptions"],
      "caveats": ["limitations and conditions"]
    },

    "roadmap_summary": {
      "program_name": "",
      "recommended_edition": "S/4HANA Cloud Public Edition | Private Edition | On-Premise | SAP GROW",
      "transformation_type": "Greenfield | Brownfield | Bluefield | System Conversion",
      "go_live_strategy": "Big Bang | Phased (by module) | Phased (by geography) | Parallel Run",
      "go_live_strategy_rationale": "",
      "total_duration_months": 0,
      "number_of_waves": 0,
      "wave_summary": [
        {
          "wave_id": "W1",
          "name": "",
          "scope_description": "",
          "target_go_live": "",
          "duration_months": 0
        }
      ],
      "overall_program_risk": "HIGH | MEDIUM | LOW",
      "clean_core_strategy": "Full compliance | Pragmatic compliance | Managed extensions",
      "cloud_alm_project_type": "Implementation | Upgrade | Migration"
    },

    "phase_plan": [
      {
        "phase_name": "Discover",
        "sap_activate_phase": "Discover",
        "wave": "W0 (Pre-project)",
        "duration_weeks": 0,
        "start_offset_weeks": 0,
        "key_activities": [
          {
            "activity": "",
            "description": "",
            "responsible": "",
            "sap_tool": ""
          }
        ],
        "deliverables": [],
        "staffing": [
          {
            "role": "",
            "source": "Client | Partner | SAP",
            "fte": 0.0,
            "key_skills": []
          }
        ],
        "prerequisites": [],
        "risks": [],
        "phase_exit_criteria": [],
        "sap_tools_used": {
          "tool": "",
          "usage": ""
        }
      }
    ],

    "wave_release_strategy": {
      "strategy_rationale": "",
      "waves": [
        {
          "wave_id": "W1",
          "name": "",
          "modules_in_scope": [],
          "processes_in_scope": [],
          "geographic_scope": [],
          "user_count": 0,
          "go_live_criteria": [],
          "dependencies_on_prior_waves": [],
          "key_risks": []
        }
      ],
      "inter_wave_dependencies": [],
      "regression_testing_strategy": ""
    },

    "resource_plan": {
      "client_team": {
        "structure_notes": "",
        "roles": [
          {
            "role": "",
            "name_or_tbd": "",
            "fte_by_phase": {
              "discover": 0.0,
              "prepare": 0.0,
              "explore": 0.0,
              "realize": 0.0,
              "deploy": 0.0,
              "run": 0.0
            },
            "critical_success_factors": [],
            "backfill_required": true
          }
        ]
      },
      "partner_team": {
        "structure_notes": "",
        "roles": [
          {
            "role": "",
            "fte_by_phase": {
              "discover": 0.0,
              "prepare": 0.0,
              "explore": 0.0,
              "realize": 0.0,
              "deploy": 0.0,
              "run": 0.0
            },
            "seniority": "Principal | Senior | Consultant | Analyst",
            "onsite_remote": "Onsite | Remote | Hybrid"
          }
        ]
      },
      "total_fte_by_phase": {
        "discover": { "client": 0.0, "partner": 0.0 },
        "prepare": { "client": 0.0, "partner": 0.0 },
        "explore": { "client": 0.0, "partner": 0.0 },
        "realize": { "client": 0.0, "partner": 0.0 },
        "deploy": { "client": 0.0, "partner": 0.0 },
        "run": { "client": 0.0, "partner": 0.0 }
      },
      "resource_risks": []
    },

    "risk_register": [
      {
        "risk_id": "R01",
        "category": "Organizational | Technical | Scope | Resource | External | Financial",
        "description": "",
        "probability": "HIGH | MEDIUM | LOW",
        "impact": "HIGH | MEDIUM | LOW",
        "risk_score": "CRITICAL | HIGH | MEDIUM | LOW",
        "mitigation_strategy": "",
        "contingency_plan": "",
        "risk_owner": "",
        "monitoring_trigger": ""
      }
    ],

    "change_management_plan": {
      "ocm_approach": "",
      "change_readiness_assessment": "",
      "stakeholder_engagement_strategy": "",
      "communication_plan": {
        "audiences": [],
        "channels": [],
        "frequency": "",
        "key_messages_by_phase": {}
      },
      "training_plan": {
        "approach": "Train-the-Trainer | Direct Training | Blended | Self-Service",
        "training_environments": "",
        "training_schedule": "",
        "training_materials": [],
        "role_based_curricula": []
      },
      "go_live_readiness_criteria": [],
      "organizational_design_considerations": []
    },

    "budget_framework": {
      "disclaimer": "Rough order-of-magnitude estimates for planning purposes only. Not a binding quotation.",
      "currency": "USD",
      "cost_categories": [
        {
          "category": "",
          "subcategories": [],
          "estimated_range_low": 0,
          "estimated_range_high": 0,
          "assumptions": [],
          "phase_allocation": ""
        }
      ],
      "total_estimated_range": {
        "low": 0,
        "high": 0
      },
      "annual_recurring_costs": {
        "licensing": 0,
        "support": 0,
        "infrastructure": 0,
        "total_annual": 0
      },
      "cost_optimization_recommendations": [],
      "roi_considerations": []
    },

    "critical_path": {
      "critical_path_activities": [
        {
          "activity": "",
          "phase": "",
          "duration_weeks": 0,
          "predecessors": [],
          "float_days": 0,
          "on_critical_path": true
        }
      ],
      "key_milestones": [
        {
          "milestone": "",
          "target_date_offset_weeks": 0,
          "gate_type": "Phase Gate | Steering Committee | Go/No-Go",
          "decision_maker": ""
        }
      ],
      "external_dependencies": [],
      "schedule_buffer": ""
    },

    "sap_toolchain_usage_plan": [
      {
        "tool": "",
        "phases_used": [],
        "specific_usage": "",
        "license_required": true,
        "setup_timing": ""
      }
    ]
  }
}
```

---

## Step-by-Step Behavior

### Step 1: Input Validation and Prerequisite Check

- Verify that the module fit analysis (Skill 02) and discovery brief (Skill 01) are present and structurally complete
- Check for critical fields required for roadmap generation:
  - **From Skill 01:** `client_profile.employee_count`, `transformation_context.deployment_preference`, `transformation_context.change_management_readiness`, `transformation_context.timeline_signals`, `transformation_context.budget_signals`
  - **From Skill 02:** `module_assessment_matrix` (at least one module scored), `sizing_recommendation.recommended_edition`, `integration_dependencies`
- If critical fields are missing, generate a structured list of blockers and request the information before proceeding
- If fields are present but marked `[INFERRED]` from Skill 01, carry forward the inference tags and increase uncertainty ranges in timeline and budget estimates
- Log any data quality concerns that affect planning confidence

### Step 2: Program Structure Determination

Determine the overall program structure — single wave vs. multi-wave — based on the following decision logic:

| Factor | Single Wave Indicator | Multi-Wave Indicator |
|---|---|---|
| **Module count** | 3-5 core modules | 6+ modules or complex scope items |
| **User count** | < 200 named users | > 200 named users or 3+ distinct user communities |
| **Geographic scope** | Single country | Multi-country with localization requirements |
| **Integration complexity** | < 5 integration points | 5+ integration points or complex middleware |
| **Client change capacity** | Medium-High readiness | Low readiness or no prior ERP experience |
| **Regulatory complexity** | Single jurisdiction | Multi-jurisdictional compliance requirements |
| **Data migration complexity** | Greenfield or minimal legacy data | Large legacy dataset requiring cleansing and migration |
| **Risk appetite** | Client accepts big-bang risk | Client prefers incremental de-risking |

For each wave, determine:
- Module scope and process scope
- Geographic scope (if multi-geography rollout)
- User communities affected
- Go-live strategy (Big Bang for single-wave; Phased or Parallel Run for multi-wave)
- Buffer time between waves for stabilization

### Step 3: Phase Duration Calibration

Adjust standard SAP Activate phase durations based on client-specific factors. Start from baseline ranges and apply multipliers:

**Baseline Durations (S/4HANA Cloud Public Edition, mid-market):**

| Phase | Baseline Range | Adjustment Factors |
|---|---|---|
| **Discover** | 2-4 weeks | +1-2 weeks if multi-geography; +1 week if no prior SAP experience |
| **Prepare** | 4-8 weeks | +2-4 weeks if greenfield (org structure design); +2 weeks if complex master data strategy |
| **Explore** | 8-16 weeks | +4 weeks per additional wave; +2-4 weeks if heavy Fit-to-Standard gap resolution; -2-4 weeks if SAP Model Company accelerator used |
| **Realize** | 12-24 weeks | +4-8 weeks if complex integrations; +4 weeks if data migration from multiple sources; +2-4 weeks per BTP extension |
| **Deploy** | 4-8 weeks | +2-4 weeks if parallel run strategy; +2 weeks if multi-site cutover |
| **Run (Hypercare)** | 4-12 weeks | +4 weeks if first ERP (high support demand); duration scales with organizational complexity |

**Complexity Multipliers:**

| Client Characteristic | Multiplier Effect |
|---|---|
| No prior ERP experience | 1.2x on Explore + Realize (steeper learning curve) |
| Multi-currency (3+ currencies) | 1.1x on Realize (additional configuration and testing) |
| Regulatory-heavy industry | 1.15x on Explore + Realize (compliance validation) |
| Limited IT capacity | 1.1x on Prepare + Deploy (more partner support needed) |
| Aggressive Clean Core target | 0.9x on Realize (less custom development) but 1.1x on Explore (more Fit-to-Standard discipline) |

Apply multipliers cumulatively and round to nearest week. Document all adjustments in the `assumptions` field.

### Step 4: Resource Modeling

Estimate team composition based on module scope, client capacity, and project scale. Use the following resource model archetypes:

**Small Implementation (< 100 users, 3-5 modules, single geography):**

| Role | Client | Partner |
|---|---|---|
| Executive Sponsor | 0.1 FTE | — |
| Project Manager | 0.5-1.0 FTE | 0.5-1.0 FTE |
| Solution Architect | — | 0.25-0.5 FTE |
| Functional Consultant (per module) | — | 0.5-1.0 FTE |
| Process Owner (per process area) | 0.25-0.5 FTE | — |
| Key User (per process area) | 0.25-0.5 FTE | — |
| Technical / Basis Consultant | — | 0.25 FTE |
| Data Migration Specialist | 0.25 FTE | 0.25-0.5 FTE |
| Change Management / Training | 0.25 FTE | 0.25-0.5 FTE |

**Medium Implementation (100-500 users, 5-8 modules, 1-3 countries):**
Scale partner team by ~1.5-2x. Add dedicated test manager, integration architect, and cutover manager. Client team needs dedicated project manager and expanded key user network.

**Large Implementation (500+ users, 8+ modules, multi-geography):**
Scale partner team by ~3-5x. Add program director, multiple workstream leads, dedicated security consultant, organizational change management workstream, and regional rollout coordinators. Client PMO with 3-5 dedicated FTEs.

Resource allocation follows a characteristic curve across phases:
- **Discover:** Lean team (architect + PM)
- **Prepare:** Ramp-up begins (core team onboards)
- **Explore:** Full team engaged (peak functional consultant utilization)
- **Realize:** Peak staffing (all roles active, testing team added)
- **Deploy:** Transition from build to support (training team peaks, consultants begin ramp-down)
- **Run:** Hypercare team (reduced partner presence, client team takes ownership)

### Step 5: Risk Assessment

Identify and score implementation risks using a structured framework. Generate the top 10-15 risks by evaluating the following risk categories against the client profile:

| Risk Category | Assessment Inputs | Typical Risks |
|---|---|---|
| **Organizational** | Change readiness, executive sponsorship, prior ERP experience | Inadequate change management, stakeholder resistance, decision-making delays |
| **Technical** | Current landscape, IT capacity, infrastructure readiness | Integration failures, data quality issues, performance problems, connectivity gaps |
| **Scope** | Module count, gap analysis results, customization appetite | Scope creep, underestimated gap resolution effort, Clean Core deviations |
| **Resource** | Client staffing capacity, partner availability, key person dependencies | Client resource availability (day-job vs. project), consultant turnover, knowledge transfer gaps |
| **External** | Regulatory changes, vendor dependencies, market conditions | SAP release cycle changes, third-party API changes, regulatory shifts |
| **Financial** | Budget signals, contingency adequacy, licensing cost structure | Budget overrun, unplanned licensing costs, infrastructure cost escalation |

Scoring matrix:
- **Probability:** HIGH (>60%), MEDIUM (30-60%), LOW (<30%)
- **Impact:** HIGH (go-live delay >4 weeks or >20% budget overrun), MEDIUM (2-4 week delay or 10-20% overrun), LOW (manageable within buffer)
- **Risk Score:** Probability x Impact mapped to CRITICAL / HIGH / MEDIUM / LOW

Each risk must include a mitigation strategy (proactive action to reduce probability/impact) and a contingency plan (reactive action if the risk materializes).

### Step 6: Change Management Planning

Design the organizational change management (OCM) approach based on the stakeholder map and organizational readiness assessment from Skill 01:

1. **Change Impact Assessment** — Map each SAP module to affected roles and quantify the degree of change (process change, tool change, organizational change)
2. **Stakeholder Engagement Strategy** — Based on the stakeholder map, define engagement cadence for sponsors, champions, process owners, end users, and known resistors
3. **Communication Plan** — Multi-channel communication plan with phase-appropriate messaging:
   - Discover/Prepare: "Why we are changing" (awareness)
   - Explore: "What will change for you" (understanding)
   - Realize: "How you will work in the new system" (capability)
   - Deploy: "You are ready" (confidence)
   - Run: "We are here to help" (reinforcement)
4. **Training Plan** — Role-based training curricula, delivery method (train-the-trainer vs. direct, classroom vs. e-learning vs. blended), training environment provisioning timeline, and SAP Enable Now / SAP Learning Hub usage
5. **Go-Live Readiness Criteria** — Measurable criteria that must be met before cutover authorization (training completion rates, UAT defect closure rates, data migration validation, cutover rehearsal success)

### Step 7: Budget Framework Generation

Produce rough order-of-magnitude (ROM) cost estimates across standard SAP implementation cost categories. These are directional estimates for planning purposes, not binding quotations.

**Cost Categories:**

| Category | Estimation Method | Typical Range (% of total) |
|---|---|---|
| **SAP Licensing** | Based on Skill 02 sizing recommendation (edition, user types, user counts) | 15-25% of year-1 cost |
| **Implementation Partner** | FTE count x blended rate x duration per phase | 40-55% of year-1 cost |
| **Client Internal Resources** | FTE count x loaded cost x allocation percentage | 10-20% of year-1 cost |
| **Infrastructure / Cloud** | Based on deployment model (BTP, hyperscaler, on-premise) | 5-10% of year-1 cost |
| **Data Migration** | Complexity-based (greenfield = low, multi-source legacy = high) | 5-10% of year-1 cost |
| **Training** | User count x training cost per user (varies by delivery method) | 3-8% of year-1 cost |
| **Contingency** | Standard 15-25% of total implementation cost | 15-25% of implementation |

Also estimate **annual recurring costs** (licensing, support, infrastructure, ongoing optimization) to give a 3-year total cost of ownership (TCO) view.

Include ROI considerations specific to the client profile: operational efficiency gains, working capital improvements, compliance cost reduction, scalability value, and reporting/decision-making acceleration.

### Step 8: Output Assembly with Critical Path Analysis

Assemble all components into the structured roadmap JSON:

1. Map all activities to a timeline and identify the **critical path** — the longest chain of dependent activities that determines the minimum project duration
2. Calculate float for non-critical activities
3. Identify **key milestones** (phase gates, steering committee reviews, go/no-go decisions, go-live dates)
4. Map **external dependencies** (SAP system provisioning lead times, partner resource availability, client fiscal calendar, regulatory deadlines)
5. Define **schedule buffer** strategy (concentrated at end vs. distributed across phases)
6. Compile the **SAP toolchain usage plan** showing when each SAP tool is activated across the project lifecycle
7. Final quality check: validate internal consistency (timeline vs. resource capacity, scope vs. budget, risk mitigations vs. resource plan)

---

## Constraints and Failure Modes

| Constraint | Handling |
|---|---|
| **Unrealistic timeline expectations** | If the client's target go-live date is less than 70% of the calculated minimum duration, flag as HIGH risk and present both the target timeline (with required trade-offs) and the recommended timeline. Never silently compress phases below safe minimums. |
| **Budget mismatch with scope** | If the budget signals from Skill 01 are < 60% of the ROM estimate, present a phased scope reduction option: identify which modules/processes could move to a later wave to fit within budget. Flag clearly that budget is a binding constraint. |
| **Insufficient client staffing** | If the client cannot provide the minimum required process owners and key users (at least 0.25 FTE per in-scope process area), flag as CRITICAL risk. Propose mitigation: increased partner staffing (at higher cost), extended timeline, or reduced scope. |
| **Aggressive Clean Core timeline** | If the client has heavy customization (from Skill 02 gap analysis) but insists on Clean Core compliance in Wave 1, quantify the Fit-to-Standard effort realistically and propose a pragmatic Clean Core roadmap (core compliance in W1, full compliance over 2-3 waves). |
| **Multi-geography complexity** | If the module fit analysis includes multi-country rollout, ensure the roadmap includes localization effort per country (chart of accounts, tax configuration, language, legal entity setup). Add 2-4 weeks per additional country in Realize phase. |
| **Missing integration partner** | If the module fit analysis identifies third-party integrations but no integration partner is confirmed, flag as a schedule risk and add a "partner selection" activity in the Prepare phase with a 4-6 week lead time assumption. |
| **No prior ERP experience** | If the client has never operated an ERP system (as flagged in Skill 01), apply the 1.2x complexity multiplier and add explicit "ERP fundamentals" training in the Prepare phase. Recommend extended hypercare (8-12 weeks vs. standard 4-6 weeks). |
| **Data quality unknown** | If master data quality is rated "Poor" or "Unknown" in Skill 01, add a dedicated data cleansing sprint (2-4 weeks) in the Prepare phase and increase data migration effort estimate by 1.5x. |

---

## Example Usage

### Input Summary (from Skills 01 and 02)

**From Skill 01 — Highland Harvest Exports Ltd. Discovery Brief:**
- 65-employee premium cashew exporter, Njombe, Tanzania
- No existing ERP (Excel + WhatsApp + the regional mobile money provider)
- Multi-currency (TZS, USD, EUR, INR)
- Key drivers: inventory traceability, export documentation, financial reporting, quality management
- Greenfield deployment, Public Cloud preferred, budget-sensitive with investor backing
- No prior ERP experience, limited IT capacity, change management is a significant concern

**From Skill 02 — Module Fit Analysis:**
- Recommended edition: S/4HANA Cloud Public Edition via SAP GROW
- Core modules: FI/CO, MM, SD, QM
- Extension candidates: GTS (Phase 2), BTP (mobile/the regional mobile money provider integration)
- 15-20 named users estimated
- Integration points: the regional mobile money provider (mobile money), bank connectivity, Tanzania Revenue Authority (tax), potential certification body APIs
- Clean Core alignment: HIGH (greenfield advantage, no legacy customizations)

### Sample Output

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
        "Revenue in the $1-5M USD range based on company size and industry (SAP GROW eligibility confirmed)",
        "15-20 named users across finance, operations, sales/export, quality, and management roles",
        "Reliable internet connectivity available at Njombe office and collection station (to be validated)",
        "Investor funding approved with a budget envelope of $80,000-$150,000 for year-1 implementation",
        "Client can dedicate 2-3 staff members at 50% capacity to the project",
        "SAP GROW starter pack pricing applies with standard Public Cloud SLAs",
        "Single legal entity in Tanzania with multi-currency requirements (no intercompany)"
      ],
      "caveats": [
        "Budget estimates are ROM only — formal quotation requires SAP pricing engagement",
        "Timeline assumes no major regulatory or organizational disruptions",
        "Resource model assumes a lean regional implementation partner with East Africa experience",
        "Several Skill 01 inputs were inferred — timeline and budget ranges carry wider uncertainty bands"
      ]
    },

    "roadmap_summary": {
      "program_name": "Project Korosho — Highland Harvest Exports Ltd. S/4HANA Implementation",
      "recommended_edition": "S/4HANA Cloud Public Edition via SAP GROW",
      "transformation_type": "Greenfield",
      "go_live_strategy": "Big Bang (single wave)",
      "go_live_strategy_rationale": "Single-site operation with < 20 users and a compact module scope (FI/CO, MM, SD, QM). Phased rollout would add complexity and cost disproportionate to the scale. Big Bang is appropriate because the user community is small, co-located, and can be trained as a single cohort. The risk of a big-bang approach at this scale is manageable with adequate hypercare planning.",
      "total_duration_months": 7,
      "number_of_waves": 1,
      "wave_summary": [
        {
          "wave_id": "W1",
          "name": "Core ERP Foundation",
          "scope_description": "FI/CO (multi-currency financial accounting and controlling), MM (farmer procurement and inventory with batch traceability), SD (export sales order management and billing), QM (cashew quality grading and traceability). the regional mobile money provider integration via BTP for mobile money payments.",
          "target_go_live": "Month 7 from project kickoff",
          "duration_months": 7
        }
      ],
      "overall_program_risk": "MEDIUM",
      "clean_core_strategy": "Full compliance — greenfield implementation with no legacy customizations. All extensions via BTP side-by-side model. the regional mobile money provider integration built as a BTP application, not an in-app modification.",
      "cloud_alm_project_type": "Implementation"
    },

    "phase_plan": [
      {
        "phase_name": "Discover",
        "sap_activate_phase": "Discover",
        "wave": "W0 (Pre-project)",
        "duration_weeks": 3,
        "start_offset_weeks": 0,
        "key_activities": [
          {
            "activity": "Scope Validation Workshop",
            "description": "Confirm module scope from Skill 02 analysis with client stakeholders. Validate business process priorities and must-have vs. nice-to-have capabilities.",
            "responsible": "Solution Architect + Client Executive Sponsor",
            "sap_tool": "Digital Discovery Assessment (DDA)"
          },
          {
            "activity": "Stakeholder Alignment Sessions",
            "description": "Identify and engage all key stakeholders. Establish governance structure, decision-making authority, and escalation paths.",
            "responsible": "Project Manager",
            "sap_tool": "None"
          },
          {
            "activity": "Infrastructure and Connectivity Assessment",
            "description": "Validate internet connectivity at Njombe office and collection station. Test latency to SAP data center (EU or Middle East region). Assess device availability for end users.",
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
          "Infrastructure readiness report",
          "SAP GROW subscription confirmation",
          "Project governance framework"
        ],
        "staffing": [
          { "role": "Solution Architect", "source": "Partner", "fte": 0.5, "key_skills": ["SAP S/4HANA Cloud", "SAP GROW", "Agribusiness"] },
          { "role": "Project Manager", "source": "Partner", "fte": 0.5, "key_skills": ["SAP Activate", "Mid-market delivery"] },
          { "role": "Executive Sponsor", "source": "Client", "fte": 0.1, "key_skills": ["Decision authority", "Budget approval"] },
          { "role": "Project Champion", "source": "Client", "fte": 0.25, "key_skills": ["Operations knowledge", "Staff influence"] }
        ],
        "prerequisites": [
          "Client commitment to proceed (letter of intent or signed SOW)",
          "Key stakeholder availability confirmed for workshop dates"
        ],
        "risks": [
          "Stakeholder misalignment on scope or priority — mitigate with structured workshop facilitation",
          "Connectivity assessment reveals inadequate infrastructure — contingency: evaluate satellite internet or Private Edition"
        ],
        "phase_exit_criteria": [
          "Scope statement signed by executive sponsor",
          "Infrastructure readiness confirmed (or remediation plan in place)",
          "SAP GROW subscription initiated",
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
        "key_activities": [
          {
            "activity": "System Provisioning",
            "description": "Provision S/4HANA Cloud tenant (development, quality, production). Configure initial system landscape. Set up Cloud ALM project.",
            "responsible": "Technical Consultant",
            "sap_tool": "SAP Cloud ALM, SAP for Me"
          },
          {
            "activity": "Organizational Structure Design",
            "description": "Define company code, controlling area, plant, storage locations, sales organization, distribution channel, and division. Map to Highland Harvest Exports Ltd.'s organizational reality.",
            "responsible": "Solution Architect + Finance Lead",
            "sap_tool": "S/4HANA Cloud Configuration"
          },
          {
            "activity": "Master Data Strategy",
            "description": "Define master data objects (farmer/vendor masters, material masters for cashew grades, customer masters for export buyers, chart of accounts). Plan data creation approach (manual entry for greenfield — no migration required from Excel).",
            "responsible": "Functional Consultant + Process Owners",
            "sap_tool": "None"
          },
          {
            "activity": "ERP Fundamentals Training",
            "description": "Foundational ERP concepts training for client team. Cover process thinking, master data concepts, transaction flow, and reporting basics. Critical for a team with no prior ERP experience.",
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
          "Organizational structure design document",
          "Master data strategy and templates",
          "Detailed project plan and resource calendar",
          "ERP fundamentals training completion certificates"
        ],
        "staffing": [
          { "role": "Project Manager", "source": "Partner", "fte": 0.75, "key_skills": ["SAP Activate", "Cloud ALM"] },
          { "role": "Solution Architect", "source": "Partner", "fte": 0.5, "key_skills": ["Org structure design", "S/4HANA Cloud"] },
          { "role": "Functional Consultant (FI/CO)", "source": "Partner", "fte": 0.5, "key_skills": ["Chart of accounts", "Multi-currency"] },
          { "role": "Technical Consultant", "source": "Partner", "fte": 0.25, "key_skills": ["System provisioning", "Cloud ALM setup"] },
          { "role": "Change Management Lead", "source": "Partner", "fte": 0.25, "key_skills": ["Training design", "Stakeholder engagement"] },
          { "role": "Project Champion", "source": "Client", "fte": 0.5, "key_skills": ["Internal coordination"] },
          { "role": "Finance Lead", "source": "Client", "fte": 0.25, "key_skills": ["Chart of accounts input", "Financial processes"] },
          { "role": "Operations Lead", "source": "Client", "fte": 0.25, "key_skills": ["Procurement and inventory processes"] }
        ],
        "prerequisites": [
          "Signed project charter from Discover phase",
          "SAP GROW subscription activated",
          "Client team members identified and onboarded to project"
        ],
        "risks": [
          "System provisioning delays — mitigate by initiating SAP subscription in Discover phase",
          "Client team unfamiliar with ERP concepts — mitigate with dedicated ERP fundamentals training"
        ],
        "phase_exit_criteria": [
          "All three system landscapes provisioned and accessible",
          "Cloud ALM project operational with requirements baseline loaded",
          "Organizational structure design approved by client",
          "Master data templates ready for population",
          "Client team has completed ERP fundamentals training"
        ],
        "sap_tools_used": [
          { "tool": "SAP Cloud ALM", "usage": "Project setup, task management, requirements tracking" },
          { "tool": "SAP Learning Hub", "usage": "ERP fundamentals training for client team" },
          { "tool": "SAP for Me", "usage": "Subscription and tenant management" }
        ]
      },

      {
        "phase_name": "Explore",
        "sap_activate_phase": "Explore",
        "wave": "W1",
        "duration_weeks": 8,
        "start_offset_weeks": 8,
        "key_activities": [
          {
            "activity": "Fit-to-Standard Workshops",
            "description": "Process-by-process workshops comparing client requirements to SAP standard processes. Cover: Procure-to-Pay (farmer procurement), Inventory Management (batch-managed cashew lots), Order-to-Cash (export sales), Record-to-Report (multi-currency financials), Quality Management (grading and traceability). Use SAP Signavio Value Accelerators to benchmark against best practices.",
            "responsible": "Functional Consultants + Process Owners",
            "sap_tool": "SAP Signavio, S/4HANA Cloud"
          },
          {
            "activity": "Gap Resolution Design",
            "description": "For each identified gap (e.g., the regional mobile money provider mobile money integration, Tanzania-specific export documentation, farmer lot traceability beyond standard batch management), design resolution approach: standard configuration, BTP extension, or process workaround.",
            "responsible": "Solution Architect + Functional Consultants",
            "sap_tool": "SAP BTP (design phase)"
          },
          {
            "activity": "Integration Architecture Design",
            "description": "Design integration architecture for the regional mobile money provider (mobile money), bank file interfaces (Tanzania bank formats), and potential Tanzania Revenue Authority e-invoicing. Define API specifications, middleware approach (SAP Integration Suite on BTP), error handling, and monitoring.",
            "responsible": "Solution Architect + Technical Consultant",
            "sap_tool": "SAP Integration Suite (BTP)"
          },
          {
            "activity": "Data Migration Approach Finalization",
            "description": "For greenfield: define which reference data will be loaded (opening balances, farmer master data from Excel, material master data for cashew grades, customer master data for export buyers). Design data templates and validation rules.",
            "responsible": "Data Migration Specialist + Process Owners",
            "sap_tool": "S/4HANA Cloud Migration Cockpit"
          },
          {
            "activity": "Security and Authorization Design",
            "description": "Define role-based access: Finance role, Procurement/Operations role, Sales/Export role, Quality role, Management/Reporting role. Map to SAP standard business roles for Public Cloud.",
            "responsible": "Solution Architect",
            "sap_tool": "S/4HANA Cloud"
          }
        ],
        "deliverables": [
          "Fit-to-Standard workshop documentation (per process area)",
          "Gap list with resolution approach for each gap",
          "Business process master list (BPML) in Cloud ALM",
          "Integration architecture document",
          "Data migration plan and templates",
          "Security role design document",
          "Updated scope and change request log"
        ],
        "staffing": [
          { "role": "Project Manager", "source": "Partner", "fte": 0.75, "key_skills": ["Workshop facilitation", "Scope management"] },
          { "role": "Solution Architect", "source": "Partner", "fte": 0.5, "key_skills": ["Integration architecture", "BTP", "Clean Core"] },
          { "role": "Functional Consultant (FI/CO)", "source": "Partner", "fte": 0.75, "key_skills": ["Multi-currency", "Financial close", "Controlling"] },
          { "role": "Functional Consultant (MM/SD)", "source": "Partner", "fte": 0.75, "key_skills": ["Batch management", "Procurement", "Export sales"] },
          { "role": "Functional Consultant (QM)", "source": "Partner", "fte": 0.5, "key_skills": ["Quality inspection", "Certificate management"] },
          { "role": "Technical Consultant", "source": "Partner", "fte": 0.25, "key_skills": ["Integration Suite", "API design"] },
          { "role": "Finance Lead (Process Owner)", "source": "Client", "fte": 0.5, "key_skills": ["Current financial processes", "Reporting requirements"] },
          { "role": "Operations Lead (Process Owner)", "source": "Client", "fte": 0.5, "key_skills": ["Procurement, inventory, quality processes"] },
          { "role": "Export Manager (Process Owner)", "source": "Client", "fte": 0.5, "key_skills": ["Export documentation, sales processes"] },
          { "role": "Project Champion", "source": "Client", "fte": 0.5, "key_skills": ["Decision-making, internal coordination"] }
        ],
        "prerequisites": [
          "System landscapes provisioned and configured with org structure",
          "Client process owners identified and available at 50% allocation",
          "Master data templates prepared"
        ],
        "risks": [
          "Process owners unable to dedicate 50% time — mitigate with flexible workshop scheduling (2-3 days per week)",
          "Excessive gaps identified beyond standard — mitigate with strict Fit-to-Standard discipline and Clean Core commitment",
          "Integration complexity with the regional mobile money provider underestimated — mitigate with early API assessment and proof-of-concept"
        ],
        "phase_exit_criteria": [
          "All Fit-to-Standard workshops completed with sign-off",
          "Gap list finalized with approved resolution approach for each gap",
          "Integration design approved",
          "Data migration templates populated with sample data and validated",
          "Business process master list baselined in Cloud ALM",
          "No unresolved critical design decisions"
        ],
        "sap_tools_used": [
          { "tool": "SAP Signavio", "usage": "Value Accelerators for Fit-to-Standard benchmarking against SAP best practice processes" },
          { "tool": "SAP Cloud ALM", "usage": "Requirements management, business process documentation, test case generation" },
          { "tool": "SAP Integration Suite", "usage": "Integration architecture design and API specification" },
          { "tool": "Joule for Consultants", "usage": "Configuration guidance for complex scenarios (multi-currency, batch management)" }
        ]
      },

      {
        "phase_name": "Realize",
        "sap_activate_phase": "Realize",
        "wave": "W1",
        "duration_weeks": 10,
        "start_offset_weeks": 16,
        "key_activities": [
          {
            "activity": "System Configuration",
            "description": "Configure all in-scope processes in the S/4HANA Cloud development tenant. Multi-currency FI/CO setup, procurement workflows for farmer payments, batch-managed inventory, export sales order processing, quality inspection procedures. Use self-service configuration tools in Public Cloud.",
            "responsible": "Functional Consultants",
            "sap_tool": "S/4HANA Cloud Self-Service Configuration"
          },
          {
            "activity": "BTP Extension Development",
            "description": "Build the regional mobile money provider mobile money integration on BTP using SAP Integration Suite. Develop any custom Fiori apps for mobile field operations (farmer payment confirmation, lot quality capture). Follow Clean Core side-by-side extension model.",
            "responsible": "Technical Consultant + Solution Architect",
            "sap_tool": "SAP BTP, SAP Build, SAP Integration Suite"
          },
          {
            "activity": "Data Migration Execution",
            "description": "Load master data: farmer/vendor masters (~3,200 records), material masters (cashew grades and variants), customer masters (export buyers), chart of accounts, opening balances. Use Migration Cockpit with prepared templates.",
            "responsible": "Data Migration Specialist + Process Owners",
            "sap_tool": "S/4HANA Cloud Migration Cockpit"
          },
          {
            "activity": "Unit Testing",
            "description": "Test each configured process end-to-end in isolation. Verify multi-currency transactions, batch traceability flows, export document generation, quality inspection recording, and financial posting accuracy.",
            "responsible": "Functional Consultants",
            "sap_tool": "SAP Cloud ALM (test management)"
          },
          {
            "activity": "Integration Testing",
            "description": "Test cross-module flows: farmer procurement (MM) triggering payment (FI-AP) via the regional mobile money provider integration; export sales order (SD) with quality certificate (QM) and financial billing (FI-AR); month-end close across all modules.",
            "responsible": "All Consultants + Process Owners",
            "sap_tool": "SAP Cloud ALM (test orchestration)"
          },
          {
            "activity": "User Acceptance Testing (UAT)",
            "description": "Client process owners and key users execute test scenarios based on real business data. Test all critical business processes with realistic volumes. Log defects in Cloud ALM.",
            "responsible": "Process Owners + Key Users (client-led)",
            "sap_tool": "SAP Cloud ALM (defect management)"
          }
        ],
        "deliverables": [
          "Fully configured S/4HANA Cloud system (QAS environment)",
          "BTP extensions deployed (the regional mobile money provider integration, mobile apps)",
          "Master data loaded and validated",
          "Unit test results (all test cases passed)",
          "Integration test results (all cross-module flows validated)",
          "UAT sign-off from process owners",
          "Defect log with all critical/high defects resolved"
        ],
        "staffing": [
          { "role": "Project Manager", "source": "Partner", "fte": 1.0, "key_skills": ["Test coordination", "Defect management"] },
          { "role": "Solution Architect", "source": "Partner", "fte": 0.25, "key_skills": ["Design authority", "Integration oversight"] },
          { "role": "Functional Consultant (FI/CO)", "source": "Partner", "fte": 1.0, "key_skills": ["Configuration", "Multi-currency testing"] },
          { "role": "Functional Consultant (MM/SD)", "source": "Partner", "fte": 1.0, "key_skills": ["Configuration", "Batch management"] },
          { "role": "Functional Consultant (QM)", "source": "Partner", "fte": 0.5, "key_skills": ["Quality inspection config", "Certificate setup"] },
          { "role": "Technical Consultant", "source": "Partner", "fte": 0.5, "key_skills": ["BTP development", "Integration Suite"] },
          { "role": "Data Migration Specialist", "source": "Partner", "fte": 0.5, "key_skills": ["Migration Cockpit", "Data validation"] },
          { "role": "Finance Lead", "source": "Client", "fte": 0.5, "key_skills": ["UAT execution", "Financial validation"] },
          { "role": "Operations Lead", "source": "Client", "fte": 0.5, "key_skills": ["UAT execution", "Procurement/inventory validation"] },
          { "role": "Export Manager", "source": "Client", "fte": 0.5, "key_skills": ["UAT execution", "Export process validation"] },
          { "role": "Key Users (2-3)", "source": "Client", "fte": 0.25, "key_skills": ["UAT execution from end-user perspective"] }
        ],
        "prerequisites": [
          "Explore phase exit criteria met — all designs approved",
          "QAS system available and configured with org structure",
          "Master data templates finalized and populated"
        ],
        "risks": [
          "the regional mobile money provider API integration complexity — mitigate with early proof-of-concept in Explore and technical spike in first week of Realize",
          "UAT delays due to client availability — mitigate with pre-scheduled UAT calendar and dedicated client time allocation",
          "Data quality issues in farmer master data migration — mitigate with data validation rules and cleansing cycle before load"
        ],
        "phase_exit_criteria": [
          "All configuration items tested and signed off",
          "All BTP extensions functional and integration-tested",
          "Master data loaded and validated by process owners",
          "UAT completed with zero open critical defects and fewer than 5 open high defects",
          "Process owners have signed UAT completion forms",
          "Production system configuration transport tested"
        ],
        "sap_tools_used": [
          { "tool": "S/4HANA Cloud Self-Service Configuration", "usage": "Process configuration and business rule setup" },
          { "tool": "SAP BTP", "usage": "the regional mobile money provider integration development, mobile extensions" },
          { "tool": "SAP Integration Suite", "usage": "API-based integration with the regional mobile money provider and bank interfaces" },
          { "tool": "SAP Cloud ALM", "usage": "Test management, defect tracking, transport orchestration" },
          { "tool": "S/4HANA Cloud Migration Cockpit", "usage": "Master data and opening balance migration" },
          { "tool": "Joule for Consultants", "usage": "Configuration troubleshooting and best practice validation" }
        ]
      },

      {
        "phase_name": "Deploy",
        "sap_activate_phase": "Deploy",
        "wave": "W1",
        "duration_weeks": 4,
        "start_offset_weeks": 26,
        "key_activities": [
          {
            "activity": "End-User Training",
            "description": "Role-based training for all 15-20 users. Finance team: FI/CO transactions and reporting. Operations team: procurement, inventory, batch management. Export team: sales orders, billing, export documentation. Quality team: inspection recording and certificates. Management: dashboards and analytics.",
            "responsible": "Change Management Lead + Functional Consultants",
            "sap_tool": "SAP Enable Now (optional), SAP Learning Hub"
          },
          {
            "activity": "Cutover Planning and Rehearsal",
            "description": "Define the cutover sequence: freeze Excel operations, final data reconciliation, opening balance load to production, production configuration activation, integration go-live with the regional mobile money provider. Conduct one cutover rehearsal in QAS.",
            "responsible": "Project Manager + All Leads",
            "sap_tool": "SAP Cloud ALM (deployment management)"
          },
          {
            "activity": "Production Readiness Checks",
            "description": "Verify production system configuration, security roles, integration endpoints (the regional mobile money provider production API), print/output management, backup/recovery procedures.",
            "responsible": "Technical Consultant",
            "sap_tool": "SAP Cloud ALM"
          },
          {
            "activity": "Go-Live Readiness Assessment",
            "description": "Formal go/no-go assessment against predefined readiness criteria. Steering committee decision with documented risk acceptance.",
            "responsible": "Project Manager + Executive Sponsor",
            "sap_tool": "SAP Cloud ALM"
          },
          {
            "activity": "Go-Live Execution",
            "description": "Execute cutover plan. Activate production system. Verify first transactions (farmer payment, export order, financial posting). Confirm all integrations operational.",
            "responsible": "Full project team",
            "sap_tool": "S/4HANA Cloud Production, SAP Cloud ALM"
          }
        ],
        "deliverables": [
          "Training completion records (all users trained and certified)",
          "Cutover plan (detailed, hour-by-hour for go-live weekend)",
          "Cutover rehearsal results",
          "Go/no-go decision document signed by steering committee",
          "Production system live and operational",
          "First transaction verification report"
        ],
        "staffing": [
          { "role": "Project Manager", "source": "Partner", "fte": 1.0, "key_skills": ["Cutover management", "Go-live coordination"] },
          { "role": "Solution Architect", "source": "Partner", "fte": 0.25, "key_skills": ["Go-live verification", "Escalation support"] },
          { "role": "Functional Consultant (FI/CO)", "source": "Partner", "fte": 0.75, "key_skills": ["Opening balance load", "Production verification"] },
          { "role": "Functional Consultant (MM/SD)", "source": "Partner", "fte": 0.75, "key_skills": ["Master data verification", "Process verification"] },
          { "role": "Technical Consultant", "source": "Partner", "fte": 0.5, "key_skills": ["Production readiness", "Integration go-live"] },
          { "role": "Change Management Lead", "source": "Partner", "fte": 0.5, "key_skills": ["Training delivery", "Go-live communication"] },
          { "role": "All Client Leads", "source": "Client", "fte": 0.75, "key_skills": ["Training participation", "Cutover validation"] }
        ],
        "prerequisites": [
          "UAT sign-off from all process owners",
          "All critical and high defects resolved",
          "End-user training scheduled and resources allocated",
          "Cutover plan reviewed and approved"
        ],
        "risks": [
          "Training effectiveness for non-technical users — mitigate with hands-on workshops, not classroom lectures; provide quick reference cards",
          "Cutover weekend issues — mitigate with rehearsal and rollback plan",
          "Internet connectivity disruption at go-live — mitigate with backup connectivity plan and offline procedures for critical period"
        ],
        "phase_exit_criteria": [
          "Production system live and processing transactions",
          "All end users have completed training",
          "First business cycle completed successfully (farmer purchase, quality inspection, export order, financial posting)",
          "Hypercare support structure activated"
        ],
        "sap_tools_used": [
          { "tool": "SAP Cloud ALM", "usage": "Deployment management, cutover tracking, go-live checklist" },
          { "tool": "SAP Learning Hub", "usage": "Training content and certification" }
        ]
      },

      {
        "phase_name": "Run (Hypercare)",
        "sap_activate_phase": "Run",
        "wave": "W1",
        "duration_weeks": 8,
        "start_offset_weeks": 30,
        "key_activities": [
          {
            "activity": "Intensive Support (Weeks 1-4)",
            "description": "On-site or dedicated remote support during first month-end close. Daily triage calls. Rapid issue resolution. Performance monitoring. User adoption tracking.",
            "responsible": "Partner team (reduced) + Client leads",
            "sap_tool": "SAP Cloud ALM (incident management)"
          },
          {
            "activity": "First Month-End Close Support",
            "description": "Guided support through first full financial close cycle. Validate multi-currency revaluation, period-end closing, financial report generation, and reconciliation with bank statements.",
            "responsible": "Functional Consultant (FI/CO)",
            "sap_tool": "S/4HANA Cloud"
          },
          {
            "activity": "Stabilization and Optimization (Weeks 5-8)",
            "description": "Address recurring issues. Fine-tune configurations based on live usage patterns. Optimize reports and dashboards. Begin knowledge transfer for ongoing administration.",
            "responsible": "Functional Consultants + Client Key Users",
            "sap_tool": "SAP Cloud ALM"
          },
          {
            "activity": "Knowledge Transfer and Handover",
            "description": "Formal knowledge transfer sessions for client team to manage day-to-day operations independently. Document standard operating procedures. Establish SAP support channel access.",
            "responsible": "Partner team + Client IT/Key Users",
            "sap_tool": "SAP for Me (support portal)"
          },
          {
            "activity": "Phase 2 Planning (Future)",
            "description": "Assess Phase 2 candidates: GTS for export compliance automation, advanced analytics, farmer portal/mobile app expansion, certification tracking. Feed learnings back into roadmap.",
            "responsible": "Solution Architect + Client Management",
            "sap_tool": "None"
          }
        ],
        "deliverables": [
          "Hypercare support log with all issues resolved",
          "First month-end close completed successfully",
          "Standard operating procedures (SOPs) for all processes",
          "Knowledge transfer documentation",
          "System administration guide for client team",
          "Phase 2 roadmap recommendations",
          "Project closure report"
        ],
        "staffing": [
          { "role": "Project Manager", "source": "Partner", "fte": 0.25, "key_skills": ["Hypercare coordination", "Project closure"] },
          { "role": "Functional Consultant (FI/CO)", "source": "Partner", "fte": 0.5, "key_skills": ["Month-end close support", "Financial reporting"] },
          { "role": "Functional Consultant (MM/SD)", "source": "Partner", "fte": 0.25, "key_skills": ["Process optimization", "User support"] },
          { "role": "Technical Consultant", "source": "Partner", "fte": 0.1, "key_skills": ["Performance monitoring", "Integration monitoring"] },
          { "role": "All Client Leads", "source": "Client", "fte": 0.25, "key_skills": ["Issue triage", "User support within teams"] }
        ],
        "prerequisites": [
          "Production system live",
          "Hypercare support agreement in place",
          "Incident management process defined in Cloud ALM"
        ],
        "risks": [
          "High support demand from users unfamiliar with ERP — mitigate with extended hypercare (8 weeks vs. standard 4) and on-site floor support",
          "Partner consultant availability for hypercare period — mitigate with contractual commitment and knowledge transfer during Realize"
        ],
        "phase_exit_criteria": [
          "Two consecutive month-end closes completed without critical issues",
          "Open incident count below threshold (< 5 medium, 0 critical)",
          "Client team self-sufficient for day-to-day operations",
          "Knowledge transfer sign-off from client IT lead",
          "Project closure report accepted by steering committee"
        ],
        "sap_tools_used": [
          { "tool": "SAP Cloud ALM", "usage": "Incident management, monitoring, health dashboards" },
          { "tool": "SAP for Me", "usage": "SAP support channel access, knowledge base" }
        ]
      }
    ],

    "wave_release_strategy": {
      "strategy_rationale": "Single-wave big-bang recommended for Highland Harvest Exports Ltd.. The compact module scope (FI/CO, MM, SD, QM), small user base (15-20), and single-site operation make a phased approach unnecessarily complex. All core modules are tightly interdependent — FI/CO is needed for MM posting, SD posting, and QM results recording. Separating them into waves would require extensive temporary workarounds. A Phase 2 is recommended 6-12 months post-go-live for GTS (export compliance automation) and advanced BTP extensions.",
      "waves": [
        {
          "wave_id": "W1",
          "name": "Core ERP Foundation",
          "modules_in_scope": ["FI", "CO", "MM", "SD", "QM"],
          "processes_in_scope": [
            "Record-to-Report (multi-currency financial accounting and period-end close)",
            "Procure-to-Pay (farmer cashew procurement with mobile money payment)",
            "Inventory Management (batch-tracked cashew from farm gate through processing)",
            "Order-to-Cash (export sales, pricing in USD/EUR/INR, billing)",
            "Quality Management (grading, kernel grading score recording, quality certificates)"
          ],
          "geographic_scope": ["Tanzania (single country)"],
          "user_count": 18,
          "go_live_criteria": [
            "UAT signed off by all process owners with zero critical defects",
            "All end users trained and certified on their role-specific processes",
            "Master data loaded and validated (farmer masters, material masters, customer masters, chart of accounts)",
            "Opening financial balances loaded and reconciled",
            "the regional mobile money provider integration tested in production with live transactions",
            "Cutover rehearsal completed successfully",
            "Steering committee go/no-go approval documented"
          ],
          "dependencies_on_prior_waves": [],
          "key_risks": ["First ERP for entire organization — high change management demand"]
        }
      ],
      "inter_wave_dependencies": [],
      "regression_testing_strategy": "Not applicable for single-wave. Standard regression testing included in quarterly SAP Cloud update cycles post-go-live, managed via Cloud ALM feature lifecycle management."
    },

    "resource_plan": {
      "client_team": {
        "structure_notes": "Lean client team appropriate for a 65-employee company. No dedicated IT function exists, so the Project Champion role is critical. Process Owners must be empowered to make design decisions without excessive escalation. Backfill consideration: these individuals have day jobs running the business — their project allocation must be realistic.",
        "roles": [
          {
            "role": "Executive Sponsor",
            "name_or_tbd": "CEO / Managing Director (TBD)",
            "fte_by_phase": { "discover": 0.1, "prepare": 0.05, "explore": 0.05, "realize": 0.05, "deploy": 0.1, "run": 0.05 },
            "critical_success_factors": ["Visible commitment to the project", "Timely decision-making on escalations", "Budget authority"],
            "backfill_required": false
          },
          {
            "role": "Project Champion / Internal PM",
            "name_or_tbd": "Operations Manager or Senior Staff (TBD)",
            "fte_by_phase": { "discover": 0.25, "prepare": 0.5, "explore": 0.5, "realize": 0.5, "deploy": 0.75, "run": 0.25 },
            "critical_success_factors": ["Respected by staff", "Understands all business processes end-to-end", "Can bridge between partner team and staff"],
            "backfill_required": true
          },
          {
            "role": "Finance Process Owner",
            "name_or_tbd": "Finance Manager / Accountant (TBD)",
            "fte_by_phase": { "discover": 0.1, "prepare": 0.25, "explore": 0.5, "realize": 0.5, "deploy": 0.5, "run": 0.25 },
            "critical_success_factors": ["Owns chart of accounts decisions", "Can validate multi-currency processing", "Month-end close authority"],
            "backfill_required": true
          },
          {
            "role": "Operations / Procurement Process Owner",
            "name_or_tbd": "Collection Station Manager or Procurement Lead (TBD)",
            "fte_by_phase": { "discover": 0.1, "prepare": 0.25, "explore": 0.5, "realize": 0.5, "deploy": 0.5, "run": 0.25 },
            "critical_success_factors": ["Understands farmer procurement workflows", "Can define quality grading standards", "Inventory management authority"],
            "backfill_required": true
          },
          {
            "role": "Export / Sales Process Owner",
            "name_or_tbd": "Export Manager (TBD)",
            "fte_by_phase": { "discover": 0.1, "prepare": 0.1, "explore": 0.5, "realize": 0.5, "deploy": 0.5, "run": 0.25 },
            "critical_success_factors": ["Knows export documentation requirements", "Customer relationship context", "Pricing and billing authority"],
            "backfill_required": true
          }
        ]
      },
      "partner_team": {
        "structure_notes": "Lean partner team sized for a SAP GROW mid-market engagement. Solution Architect provides oversight across phases but is not full-time (shared across engagements). Functional consultants cover multiple modules where skill overlap exists (MM/SD consultant, FI/CO consultant). One technical consultant handles BTP extensions and integration. Change management lead doubles as training lead. This is a 4-5 person core team with fractional allocation.",
        "roles": [
          {
            "role": "Project Manager / Engagement Lead",
            "fte_by_phase": { "discover": 0.5, "prepare": 0.75, "explore": 0.75, "realize": 1.0, "deploy": 1.0, "run": 0.25 },
            "seniority": "Senior",
            "onsite_remote": "Hybrid (onsite for workshops, remote for execution)"
          },
          {
            "role": "Solution Architect",
            "fte_by_phase": { "discover": 0.5, "prepare": 0.5, "explore": 0.5, "realize": 0.25, "deploy": 0.25, "run": 0.1 },
            "seniority": "Principal",
            "onsite_remote": "Hybrid (onsite for Discover and key Explore workshops)"
          },
          {
            "role": "Functional Consultant — FI/CO",
            "fte_by_phase": { "discover": 0.0, "prepare": 0.5, "explore": 0.75, "realize": 1.0, "deploy": 0.75, "run": 0.5 },
            "seniority": "Senior",
            "onsite_remote": "Hybrid"
          },
          {
            "role": "Functional Consultant — MM/SD/QM",
            "fte_by_phase": { "discover": 0.0, "prepare": 0.25, "explore": 0.75, "realize": 1.0, "deploy": 0.75, "run": 0.25 },
            "seniority": "Consultant",
            "onsite_remote": "Hybrid"
          },
          {
            "role": "Technical Consultant — BTP / Integration",
            "fte_by_phase": { "discover": 0.0, "prepare": 0.25, "explore": 0.25, "realize": 0.5, "deploy": 0.5, "run": 0.1 },
            "seniority": "Consultant",
            "onsite_remote": "Remote (onsite for integration testing)"
          },
          {
            "role": "Change Management / Training Lead",
            "fte_by_phase": { "discover": 0.0, "prepare": 0.25, "explore": 0.25, "realize": 0.25, "deploy": 0.5, "run": 0.1 },
            "seniority": "Consultant",
            "onsite_remote": "Hybrid (onsite for training delivery)"
          }
        ]
      },
      "total_fte_by_phase": {
        "discover": { "client": 0.65, "partner": 1.0 },
        "prepare": { "client": 1.15, "partner": 2.5 },
        "explore": { "client": 2.05, "partner": 3.25 },
        "realize": { "client": 2.3, "partner": 4.0 },
        "deploy": { "client": 2.6, "partner": 3.75 },
        "run": { "client": 1.05, "partner": 1.3 }
      },
      "resource_risks": [
        "Client process owners cannot sustain 50% project allocation during peak harvest season (typically Oct-Feb) — schedule Explore/Realize phases to avoid peak harvest if possible",
        "No internal IT function means the partner carries all technical responsibility — increases dependency on partner and complicates long-term support handover",
        "Single points of failure: each client process owner covers an entire domain with no backup — illness or departure creates critical project risk",
        "Partner team sourcing: requires consultants with both SAP GROW experience and East Africa / agribusiness domain knowledge — limited talent pool"
      ]
    },

    "risk_register": [
      {
        "risk_id": "R01",
        "category": "Organizational",
        "description": "Change management failure — staff accustomed to Excel and WhatsApp may resist structured ERP processes, leading to workarounds, shadow systems, or low adoption",
        "probability": "HIGH",
        "impact": "HIGH",
        "risk_score": "CRITICAL",
        "mitigation_strategy": "Dedicated change management workstream from Prepare phase. ERP fundamentals training before Fit-to-Standard workshops. Identify and empower 2-3 change champions among staff. Communicate benefits in terms relevant to daily work, not technology.",
        "contingency_plan": "If adoption metrics are below 70% at Week 4 of hypercare, extend hypercare by 4 weeks with additional on-site floor support.",
        "risk_owner": "Change Management Lead + Executive Sponsor",
        "monitoring_trigger": "Training assessment scores below 60%, UAT participation below 80%, post-go-live support ticket volume exceeding 5 per user per week"
      },
      {
        "risk_id": "R02",
        "category": "Technical",
        "description": "Internet connectivity insufficient for cloud ERP at collection station or field operations — latency, outages, or bandwidth limitations degrade user experience",
        "probability": "MEDIUM",
        "impact": "HIGH",
        "risk_score": "HIGH",
        "mitigation_strategy": "Conduct connectivity assessment during Discover phase. Test latency to SAP data center. Evaluate backup ISP options (fiber, 4G/5G backup, satellite). Design offline-capable mobile workflows for field operations via BTP.",
        "contingency_plan": "If connectivity is inadequate: evaluate SAP S/4HANA Cloud Private Edition (single-tenant with potential for regional hosting) or implement local caching layer on BTP.",
        "risk_owner": "Technical Consultant",
        "monitoring_trigger": "Connectivity assessment shows >200ms latency or >2% packet loss during business hours"
      },
      {
        "risk_id": "R03",
        "category": "Resource",
        "description": "Client process owners unavailable at required allocation — day-job demands (especially during harvest season) conflict with project needs",
        "probability": "HIGH",
        "impact": "MEDIUM",
        "risk_score": "HIGH",
        "mitigation_strategy": "Schedule project timeline to avoid peak harvest season overlap with Explore/Realize phases. Pre-agree process owner allocation with executive sponsor. Designate backup key users for each process area.",
        "contingency_plan": "If process owners are consistently below 25% allocation, extend Explore phase by 2-4 weeks and shift to condensed workshop format (2 full days per week instead of daily sessions).",
        "risk_owner": "Project Manager",
        "monitoring_trigger": "Process owner attendance below 60% for two consecutive weeks"
      },
      {
        "risk_id": "R04",
        "category": "Technical",
        "description": "the regional mobile money provider mobile money integration more complex than anticipated — API limitations, transaction reconciliation challenges, or mobile money provider changes",
        "probability": "MEDIUM",
        "impact": "MEDIUM",
        "risk_score": "MEDIUM",
        "mitigation_strategy": "Conduct the regional mobile money provider API assessment and proof-of-concept in Explore phase. Engage the regional mobile money provider technical team early. Design integration with fallback to manual payment reconciliation.",
        "contingency_plan": "If the regional mobile money provider integration is not achievable in Wave 1 timeline, implement bank file upload integration as an interim solution and defer real-time mobile money integration to Phase 2.",
        "risk_owner": "Technical Consultant",
        "monitoring_trigger": "Proof-of-concept not completed by end of Explore phase"
      },
      {
        "risk_id": "R05",
        "category": "Financial",
        "description": "Total cost exceeds investor budget envelope — scope additions, extended timeline, or unplanned licensing costs push costs beyond approved funding",
        "probability": "MEDIUM",
        "impact": "HIGH",
        "risk_score": "HIGH",
        "mitigation_strategy": "Strict scope management with formal change request process. Fixed-price SOW for core implementation. Monthly budget reviews with steering committee. Contingency buffer built into estimates.",
        "contingency_plan": "If budget is exceeded by >15%, present scope reduction options to steering committee: defer QM to Phase 2, simplify the regional mobile money provider integration, reduce training scope.",
        "risk_owner": "Project Manager + Executive Sponsor",
        "monitoring_trigger": "Actual spend exceeds 80% of budget with <60% of work completed"
      },
      {
        "risk_id": "R06",
        "category": "Scope",
        "description": "Scope creep driven by discovered requirements during Fit-to-Standard workshops — client identifies new needs not captured in Skill 01 discovery",
        "probability": "MEDIUM",
        "impact": "MEDIUM",
        "risk_score": "MEDIUM",
        "mitigation_strategy": "Strict change request process. All new requirements logged in Cloud ALM and assessed for timeline/cost impact before approval. 'Phase 2 parking lot' for non-critical requirements.",
        "contingency_plan": "If scope increases exceed 20% of original scope, re-baseline timeline and budget with steering committee approval.",
        "risk_owner": "Project Manager + Solution Architect",
        "monitoring_trigger": "More than 5 approved change requests or any single change request estimated at >2 weeks of effort"
      },
      {
        "risk_id": "R07",
        "category": "Technical",
        "description": "Data quality issues during master data creation — farmer master data in Excel is incomplete, inconsistent, or duplicated, causing migration failures",
        "probability": "HIGH",
        "impact": "LOW",
        "risk_score": "MEDIUM",
        "mitigation_strategy": "Data profiling exercise in Prepare phase. Define data quality rules and validation checks. Iterative cleansing approach with process owner involvement.",
        "contingency_plan": "If farmer master data cannot be cleaned to acceptable quality, start with a subset of active farmers (e.g., top 500 by volume) and migrate remaining farmers in batches during hypercare.",
        "risk_owner": "Data Migration Specialist + Operations Process Owner",
        "monitoring_trigger": "Data profiling reveals >30% records with critical field gaps"
      },
      {
        "risk_id": "R08",
        "category": "External",
        "description": "SAP Cloud release cycle introduces breaking changes — quarterly S/4HANA Cloud Public Edition updates may affect configured processes or BTP extensions",
        "probability": "LOW",
        "impact": "MEDIUM",
        "risk_score": "LOW",
        "mitigation_strategy": "Subscribe to SAP Cloud ALM feature lifecycle management notifications. Conduct regression testing after each quarterly update. Follow SAP Clean Core guidelines to minimize update impact.",
        "contingency_plan": "If a quarterly update causes regression, engage SAP support and temporarily defer the update cycle (limited flexibility in Public Cloud).",
        "risk_owner": "Technical Consultant",
        "monitoring_trigger": "SAP quarterly release notes flag changes to in-scope processes"
      },
      {
        "risk_id": "R09",
        "category": "Organizational",
        "description": "No internal IT capacity for post-go-live system administration — no one in the organization can manage user accounts, run reports, or troubleshoot basic issues independently",
        "probability": "HIGH",
        "impact": "MEDIUM",
        "risk_score": "HIGH",
        "mitigation_strategy": "Identify and develop a 'super user' within the client team during Realize phase. Include system administration training in the training plan. Evaluate managed services agreement with implementation partner for ongoing support.",
        "contingency_plan": "If no suitable internal candidate emerges, negotiate a 12-month managed services contract with the implementation partner covering basic administration, quarterly updates, and incident support.",
        "risk_owner": "Project Manager + Executive Sponsor",
        "monitoring_trigger": "No super user candidate identified by mid-Realize phase"
      },
      {
        "risk_id": "R10",
        "category": "External",
        "description": "Regulatory changes — Tanzania Revenue Authority, Tanzania Cashewnut Board, or international trade regulation changes during implementation require scope adjustments",
        "probability": "LOW",
        "impact": "MEDIUM",
        "risk_score": "LOW",
        "mitigation_strategy": "Monitor Tanzania regulatory landscape during implementation. Build flexibility into tax configuration and export documentation processes. Use SAP standard localization packages where available.",
        "contingency_plan": "If regulatory change impacts in-scope processes, assess as a change request with timeline and cost impact. SAP Cloud updates typically incorporate regulatory changes for supported countries.",
        "risk_owner": "Solution Architect + Finance Process Owner",
        "monitoring_trigger": "New regulatory requirement published that affects financial reporting, tax, or export processes"
      }
    ],

    "change_management_plan": {
      "ocm_approach": "Prosci ADKAR-aligned approach adapted for a small organization with no prior ERP experience. Focus on Awareness (why change) and Desire (what is in it for me) before diving into Knowledge (how to use SAP). The key challenge is bridging the gap from informal Excel/WhatsApp workflows to structured ERP processes without creating a perception that the system is bureaucratic overhead.",
      "change_readiness_assessment": "LOW-MEDIUM. The team has no ERP experience, limited formal IT systems exposure, and operates in an informal-process culture. However, the small team size enables direct engagement with every affected user, and growth-driven urgency creates a natural case for change. Executive sponsor commitment (investor backing) provides top-down support.",
      "stakeholder_engagement_strategy": "Engage every user personally — at 65 employees and 15-20 system users, individual engagement is feasible and more effective than corporate communications. Identify 2-3 early adopters as change champions. Conduct bi-weekly 'open house' sessions where staff can ask questions and see system demos.",
      "communication_plan": {
        "audiences": ["Executive team (3-5)", "Process owners (3-4)", "End users (15-20)", "Non-system users (30+, awareness only)"],
        "channels": ["WhatsApp group (familiar channel)", "Team meetings (weekly)", "Physical notice board at collection station", "Hands-on demo sessions"],
        "frequency": "Weekly updates during active phases; bi-weekly during Discover/Run",
        "key_messages_by_phase": {
          "discover": "We are evaluating a system to help us grow to 7,000 farmers. Your input is critical to getting this right.",
          "prepare": "We have committed to SAP. Here is what this means for our company and your role. Training starts soon.",
          "explore": "We are designing how the new system will work. Process owners: your expertise shapes the outcome.",
          "realize": "The system is being built. You will start testing it soon. Here is what to expect.",
          "deploy": "Go-live is approaching. You are trained and ready. We have support in place for any issues.",
          "run": "We are live. Use the system for all transactions. Help is available — ask your change champion or call the support line."
        }
      },
      "training_plan": {
        "approach": "Direct Training (no train-the-trainer — team too small to justify intermediate layer)",
        "training_environments": "Dedicated training client (sandbox) with realistic data. Physical training at Njombe office — classroom with projector and individual workstations.",
        "training_schedule": "Deploy phase: 2 weeks of role-based training, 3-4 hours per day (morning sessions to accommodate afternoon operations). Hands-on exercises using real business scenarios (actual farmer names, cashew grades, export buyer data).",
        "training_materials": [
          "Role-specific quick reference cards (laminated, A4, English with key terms in Swahili where helpful)",
          "Step-by-step process guides with screenshots for each core transaction",
          "Video recordings of training sessions for future reference",
          "SAP Learning Hub access for self-paced reinforcement"
        ],
        "role_based_curricula": [
          "Finance team: FI postings, multi-currency transactions, period-end close, financial reports, bank reconciliation",
          "Operations team: create purchase orders, goods receipt, batch assignment, inventory transfers, stock overview",
          "Export/Sales team: create sales orders, delivery processing, billing, export documentation",
          "Quality team: create inspection lots, record results, quality certificates, batch classification",
          "Management: dashboard navigation, standard reports, analytics overview"
        ]
      },
      "go_live_readiness_criteria": [
        "100% of system users have completed role-based training (attendance + practical assessment)",
        "All process owners have signed UAT completion forms",
        "Cutover rehearsal completed with no critical issues",
        "Hypercare support structure confirmed (support hours, contact channels, escalation path)",
        "First-week transaction scripts prepared and validated",
        "Rollback plan documented and approved (revert to Excel for critical processes if catastrophic failure)"
      ],
      "organizational_design_considerations": [
        "No new roles required — SAP processes map to existing job functions",
        "Operations team will need to adopt more structured workflows (formal purchase orders vs. WhatsApp messages)",
        "Finance team workload may shift from data entry to analysis as manual reconciliation is automated",
        "A 'super user' role should be formally established for ongoing system administration"
      ]
    },

    "budget_framework": {
      "disclaimer": "Rough order-of-magnitude estimates for planning purposes only. Not a binding quotation. Actual costs depend on SAP GROW pricing (varies by region and negotiation), implementation partner rates (East Africa market), and client-specific factors. All figures in USD.",
      "currency": "USD",
      "cost_categories": [
        {
          "category": "SAP Licensing (Year 1)",
          "subcategories": ["SAP GROW starter pack", "S/4HANA Cloud Public Edition subscription", "BTP credits for the regional mobile money provider integration"],
          "estimated_range_low": 15000,
          "estimated_range_high": 30000,
          "assumptions": ["SAP GROW starter pack pricing for 15-20 named users", "Includes standard FI/CO, MM, SD, QM scope items", "BTP credits for integration workload (~$3,000-$7,000/year)"],
          "phase_allocation": "Annual subscription — begins at system provisioning (Prepare phase)"
        },
        {
          "category": "Implementation Partner",
          "subcategories": ["Project management", "Solution architecture", "Functional consulting (FI/CO, MM/SD, QM)", "Technical consulting (BTP, integration)", "Change management and training"],
          "estimated_range_low": 50000,
          "estimated_range_high": 90000,
          "assumptions": ["Blended partner rate of $100-$150/hour (East Africa regional partner)", "4-5 person core team over 7-month engagement", "Mix of onsite and remote delivery", "Rate assumption reflects regional partner, not Big 4 pricing"],
          "phase_allocation": "Distributed across all phases; peak spend during Explore and Realize"
        },
        {
          "category": "Client Internal Resources",
          "subcategories": ["Process owner time allocation", "Project champion time", "Executive sponsor time", "End-user training time"],
          "estimated_range_low": 10000,
          "estimated_range_high": 20000,
          "assumptions": ["Loaded cost of client staff time allocated to project", "Based on estimated salaries for Tanzania-based professional staff", "Includes opportunity cost of day-job backfill"],
          "phase_allocation": "Explore and Realize phases represent 60% of client resource cost"
        },
        {
          "category": "Infrastructure and Connectivity",
          "subcategories": ["Internet connectivity upgrade", "End-user devices (laptops/tablets)", "Backup power (UPS/generator if needed)"],
          "estimated_range_low": 3000,
          "estimated_range_high": 8000,
          "assumptions": ["May need ISP upgrade or secondary connection at collection station", "5-8 additional workstations or tablets for system access", "Cloud infrastructure included in SAP GROW subscription"],
          "phase_allocation": "One-time cost during Prepare phase"
        },
        {
          "category": "Data Migration",
          "subcategories": ["Data cleansing", "Master data preparation", "Opening balance preparation"],
          "estimated_range_low": 2000,
          "estimated_range_high": 5000,
          "assumptions": ["Greenfield implementation — no complex legacy data extraction", "Farmer master data cleansing from Excel (~3,200 records)", "Manual effort with process owner validation"],
          "phase_allocation": "Prepare and Realize phases"
        },
        {
          "category": "Training",
          "subcategories": ["Training facility setup", "Training materials production", "SAP Learning Hub licenses"],
          "estimated_range_low": 2000,
          "estimated_range_high": 5000,
          "assumptions": ["Direct training delivery (included in partner costs above)", "Materials production and printing", "SAP Learning Hub access for 15-20 users"],
          "phase_allocation": "Deploy phase"
        },
        {
          "category": "Contingency",
          "subcategories": ["Scope buffer", "Timeline buffer", "Unforeseen costs"],
          "estimated_range_low": 12000,
          "estimated_range_high": 25000,
          "assumptions": ["15-20% of total implementation cost", "Covers scope additions, extended timelines, additional training needs", "Higher contingency percentage reflects first-time ERP risk and inferred inputs"],
          "phase_allocation": "Held in reserve — released against approved change requests"
        }
      ],
      "total_estimated_range": {
        "low": 94000,
        "high": 183000
      },
      "annual_recurring_costs": {
        "licensing": 18000,
        "support": 6000,
        "infrastructure": 3000,
        "total_annual": 27000
      },
      "cost_optimization_recommendations": [
        "Leverage SAP GROW starter pack — purpose-built for mid-market with simplified pricing and pre-configured best practices",
        "Use a regional implementation partner with East Africa presence — significantly lower rates than global system integrators",
        "Maximize remote delivery — onsite presence for workshops and training only, remote for configuration and development",
        "Adopt SAP standard processes (Fit-to-Standard) to minimize custom development costs and maintain Clean Core",
        "Phase advanced capabilities (GTS, advanced analytics) to Phase 2 to keep initial investment manageable"
      ],
      "roi_considerations": [
        "Inventory traceability: reduce shrinkage and quality disputes — estimated 3-5% improvement in realized revenue per lot",
        "Financial reporting: reduce month-end close from ~5 days manual to ~1 day automated — free finance staff for analysis",
        "Multi-currency: reduce FX losses from manual tracking — estimated 1-2% improvement on international transactions",
        "Export documentation: reduce document preparation time by 60-70% — faster shipment turnaround",
        "Scalability: system supports growth to 7,000+ farmers without proportional headcount increase",
        "Investor confidence: professional-grade financial reporting supports future funding rounds"
      ]
    },

    "critical_path": {
      "critical_path_activities": [
        { "activity": "Scope validation and SAP GROW confirmation", "phase": "Discover", "duration_weeks": 3, "predecessors": [], "float_days": 0, "on_critical_path": true },
        { "activity": "System provisioning", "phase": "Prepare", "duration_weeks": 2, "predecessors": ["SAP GROW confirmation"], "float_days": 0, "on_critical_path": true },
        { "activity": "Organizational structure design", "phase": "Prepare", "duration_weeks": 3, "predecessors": ["Scope validation"], "float_days": 5, "on_critical_path": false },
        { "activity": "ERP fundamentals training", "phase": "Prepare", "duration_weeks": 2, "predecessors": ["Project kickoff"], "float_days": 10, "on_critical_path": false },
        { "activity": "Fit-to-Standard workshops", "phase": "Explore", "duration_weeks": 6, "predecessors": ["System provisioning", "Org structure design"], "float_days": 0, "on_critical_path": true },
        { "activity": "Integration architecture design", "phase": "Explore", "duration_weeks": 3, "predecessors": ["Fit-to-Standard workshops (week 2)"], "float_days": 10, "on_critical_path": false },
        { "activity": "Gap resolution design", "phase": "Explore", "duration_weeks": 2, "predecessors": ["Fit-to-Standard workshops"], "float_days": 0, "on_critical_path": true },
        { "activity": "System configuration", "phase": "Realize", "duration_weeks": 6, "predecessors": ["Gap resolution design"], "float_days": 0, "on_critical_path": true },
        { "activity": "BTP extension development", "phase": "Realize", "duration_weeks": 5, "predecessors": ["Integration architecture design"], "float_days": 5, "on_critical_path": false },
        { "activity": "Data migration execution", "phase": "Realize", "duration_weeks": 3, "predecessors": ["System configuration (week 4)"], "float_days": 5, "on_critical_path": false },
        { "activity": "Integration testing", "phase": "Realize", "duration_weeks": 3, "predecessors": ["System configuration", "BTP extensions", "Data migration"], "float_days": 0, "on_critical_path": true },
        { "activity": "UAT", "phase": "Realize", "duration_weeks": 3, "predecessors": ["Integration testing"], "float_days": 0, "on_critical_path": true },
        { "activity": "End-user training", "phase": "Deploy", "duration_weeks": 2, "predecessors": ["UAT sign-off"], "float_days": 0, "on_critical_path": true },
        { "activity": "Cutover execution", "phase": "Deploy", "duration_weeks": 1, "predecessors": ["End-user training", "Cutover rehearsal"], "float_days": 0, "on_critical_path": true },
        { "activity": "Go-live", "phase": "Deploy", "duration_weeks": 0, "predecessors": ["Cutover execution"], "float_days": 0, "on_critical_path": true }
      ],
      "key_milestones": [
        { "milestone": "Project Kickoff", "target_date_offset_weeks": 0, "gate_type": "Phase Gate", "decision_maker": "Executive Sponsor" },
        { "milestone": "Discover Phase Complete / Scope Confirmed", "target_date_offset_weeks": 3, "gate_type": "Phase Gate", "decision_maker": "Steering Committee" },
        { "milestone": "System Landscape Provisioned", "target_date_offset_weeks": 5, "gate_type": "Phase Gate", "decision_maker": "Project Manager" },
        { "milestone": "Prepare Phase Complete / Detailed Plan Approved", "target_date_offset_weeks": 8, "gate_type": "Phase Gate", "decision_maker": "Steering Committee" },
        { "milestone": "Fit-to-Standard Workshops Complete", "target_date_offset_weeks": 14, "gate_type": "Phase Gate", "decision_maker": "Solution Architect" },
        { "milestone": "Explore Phase Complete / Design Approved", "target_date_offset_weeks": 16, "gate_type": "Steering Committee", "decision_maker": "Steering Committee" },
        { "milestone": "Configuration Complete", "target_date_offset_weeks": 22, "gate_type": "Phase Gate", "decision_maker": "Solution Architect" },
        { "milestone": "UAT Complete / Sign-Off", "target_date_offset_weeks": 26, "gate_type": "Go/No-Go", "decision_maker": "Process Owners + Executive Sponsor" },
        { "milestone": "Go-Live", "target_date_offset_weeks": 30, "gate_type": "Go/No-Go", "decision_maker": "Steering Committee" },
        { "milestone": "Hypercare Complete / Project Closure", "target_date_offset_weeks": 38, "gate_type": "Phase Gate", "decision_maker": "Steering Committee" }
      ],
      "external_dependencies": [
        "SAP GROW subscription processing and tenant provisioning (allow 2-3 weeks lead time)",
        "the regional mobile money provider API documentation and sandbox access (engage during Discover phase)",
        "Tanzania Revenue Authority e-invoicing requirements (clarify during Explore phase)",
        "Internet connectivity upgrade at collection station (schedule during Prepare phase)",
        "Client staff availability around harvest season (Oct-Feb typically — plan Explore/Realize to avoid or accommodate)"
      ],
      "schedule_buffer": "5 days of buffer distributed: 2 days between Explore and Realize (design stabilization), 3 days between Realize and Deploy (defect resolution overflow). Additional contingency: 2-week extension clause in SOW for Realize phase if UAT defect resolution requires additional cycles."
    },

    "sap_toolchain_usage_plan": [
      {
        "tool": "SAP for Me",
        "phases_used": ["Discover", "Prepare"],
        "specific_usage": "SAP GROW subscription initiation, license management, tenant provisioning requests, support access setup",
        "license_required": true,
        "setup_timing": "Activate during Discover phase — required before system provisioning"
      },
      {
        "tool": "Digital Discovery Assessment (DDA)",
        "phases_used": ["Discover"],
        "specific_usage": "Validate module scope selections against S/4HANA Cloud Public Edition scope item catalog. Confirm that selected processes are available in the GROW edition.",
        "license_required": false,
        "setup_timing": "Run during Discover phase workshops"
      },
      {
        "tool": "SAP Cloud ALM",
        "phases_used": ["Prepare", "Explore", "Realize", "Deploy", "Run"],
        "specific_usage": "Project workspace setup (Prepare). Requirements management, business process master list, and test case generation (Explore). Test orchestration, defect management, and transport tracking (Realize). Deployment management, cutover checklist, and go-live readiness (Deploy). Incident management, monitoring dashboards, and feature lifecycle management for quarterly updates (Run).",
        "license_required": true,
        "setup_timing": "Configure during first week of Prepare phase — becomes the central project governance tool"
      },
      {
        "tool": "SAP Signavio",
        "phases_used": ["Explore"],
        "specific_usage": "Value Accelerators used during Fit-to-Standard workshops to benchmark client requirements against SAP reference processes. Process diagrams generated for each in-scope process area. Not used for process mining (no existing digital processes to mine).",
        "license_required": true,
        "setup_timing": "Provision Signavio workspace 1-2 weeks before Explore workshops begin"
      },
      {
        "tool": "SAP Integration Suite (BTP)",
        "phases_used": ["Explore", "Realize"],
        "specific_usage": "Integration architecture design for the regional mobile money provider and bank connectivity (Explore). Integration flow development, API management, and monitoring setup (Realize).",
        "license_required": true,
        "setup_timing": "BTP subaccount provisioned during Prepare phase; Integration Suite activated during Explore"
      },
      {
        "tool": "S/4HANA Cloud Migration Cockpit",
        "phases_used": ["Realize"],
        "specific_usage": "Master data migration (farmer/vendor masters, material masters, customer masters, chart of accounts, opening balances) using standard migration templates.",
        "license_required": false,
        "setup_timing": "Available within S/4HANA Cloud tenant — configure migration objects during Realize"
      },
      {
        "tool": "Joule for Consultants (J4C)",
        "phases_used": ["Explore", "Realize"],
        "specific_usage": "Deep-dive configuration guidance for complex scenarios: multi-currency setup, batch management configuration, quality inspection plan design. Used by functional consultants as an in-context knowledge assistant.",
        "license_required": true,
        "setup_timing": "Available to consultants with SAP partner credentials — no separate setup required"
      },
      {
        "tool": "SAP Learning Hub",
        "phases_used": ["Prepare", "Deploy"],
        "specific_usage": "ERP fundamentals training content (Prepare). Role-based training reinforcement and self-paced learning (Deploy and ongoing).",
        "license_required": true,
        "setup_timing": "Learning Hub licenses activated during Prepare phase for client team"
      }
    ]
  }
}
```

---

## Integration Points

| Downstream Skill | How This Skill's Output Is Used |
|---|---|
| **04 Executive Proposal Drafter** | Consumes `roadmap_summary` (program duration, wave structure, go-live strategy), `budget_framework` (ROM estimates for pricing section), `risk_register` (top risks for executive summary), and `resource_plan` (team structure for staffing section). The proposal drafter uses the roadmap as the backbone of the "Approach" section and the budget framework as the basis for the commercial proposal. |
| **05 SAP Best Practices Fetcher** | The `sap_toolchain_usage_plan` identifies when Signavio Value Accelerators and J4C are needed, triggering Skill 05 to fetch relevant best practice content. The `phase_plan` Explore activities reference SAP best practice processes that Skill 05 can retrieve for Fit-to-Standard workshop preparation. |

| Upstream Skill | How This Skill Consumes Its Output |
|---|---|
| **01 Client Discovery Intake** | `client_profile` drives resource model sizing and geographic complexity assessment. `transformation_context` provides timeline, budget, and change readiness inputs for phase calibration. `stakeholder_map` informs change management planning. `compliance_and_regulatory` flags localization effort. |
| **02 Module Fit Analyzer** | `module_assessment_matrix` determines which modules appear in the wave scope. `integration_dependencies` drive integration architecture activities and BTP extension planning. `sizing_recommendation` determines the SAP edition, user count, and licensing model that feeds into the budget framework. Gap analysis results drive Realize phase duration estimation. |

---

## Prompt Engineering Notes

### Key Design Decisions

1. **SAP Activate phase alignment as the structural backbone.** The entire roadmap is organized around the six SAP Activate phases (Discover, Prepare, Explore, Realize, Deploy, Run) rather than generic project phases. This is deliberate: SAP Activate is the mandatory delivery methodology for S/4HANA Cloud implementations, Cloud ALM project templates are structured around these phases, and every SAP implementation partner plans their engagements using this framework. Deviating from Activate would produce a roadmap that consultants cannot operationalize. The phase names, sequencing, and exit criteria in this skill directly mirror the SAP Activate Methodology documentation (publicly available on help.sap.com).

2. **Timeline estimation through calibrated baselines, not AI hallucination.** Duration estimates start from well-established SAP Activate baseline ranges and are adjusted using explicit multipliers tied to client characteristics. This approach is essential because SAP implementation timelines are not arbitrary — they are constrained by real-world factors like SAP Cloud provisioning lead times, quarterly release cycles, and the pace at which humans can absorb process change. The multiplier system makes the estimation logic transparent and auditable, preventing the model from generating unrealistically optimistic or pessimistic timelines.

3. **Realistic resource modeling vs. over-engineering for small clients.** A major failure mode in SAP implementation planning is applying large-enterprise resource models to mid-market clients. A 65-person company does not need a 20-person implementation team. The resource archetypes (Small / Medium / Large) explicitly scale the team size, and the example output demonstrates a lean 4-5 person partner team appropriate for a SAP GROW engagement. This reflects real delivery patterns: regional SAP partners serving the mid-market in Africa and emerging markets commonly deploy teams of this size. Over-resourcing would produce a budget estimate that immediately disqualifies the engagement.

4. **Change management as a first-class planning concern, not an afterthought.** For organizations moving from Excel to ERP (a common pattern in emerging markets), change management is the single biggest determinant of implementation success or failure. The roadmap explicitly includes ERP fundamentals training in the Prepare phase (before Fit-to-Standard workshops), change champion identification, and communication plans adapted to the client's actual communication channels (WhatsApp groups, physical notice boards). This reflects the reality that a rural cashew collection station in the Southern Highlands of Tanzania operates differently from a corporate headquarters.

5. **Budget framework as directional guidance, not a quotation.** The budget section is deliberately framed as rough order-of-magnitude with explicit disclaimers. SAP licensing costs are commercially sensitive and negotiation-dependent, and implementation partner pricing varies significantly by market. The value of this section is establishing whether the investment is in the $50K, $150K, or $500K+ range — directional guidance that allows the client and investor to make an informed go/no-go decision before entering formal commercial negotiations. The ROM also includes annual recurring costs to frame total cost of ownership, which is critical for investor-backed clients evaluating multi-year ROI.

6. **SAP toolchain integration rather than replacement.** The SAP toolchain usage plan explicitly maps when each SAP tool is activated across the project lifecycle. This positions the skills pack as an orchestration layer that feeds into SAP's tools (Cloud ALM for governance, Signavio for process benchmarking, Integration Suite for connectivity) rather than replacing them. This is strategically important: the skills pack adds value by automating the planning that precedes tool usage, not by competing with SAP's own capabilities.

### Iteration History

**v1 (Initial):** Simple phase-by-phase timeline with fixed durations. Problem: no calibration for client size/complexity, no resource model, no risk register. Output was generic and not actionable for a real engagement.

**v2 (Current):** Added complexity multipliers for phase calibration, three-tier resource model archetypes, structured risk register with scoring matrix, ADKAR-aligned change management plan, ROM budget framework with TCO view, critical path analysis, and comprehensive SAP toolchain usage plan. The example output demonstrates the full schema for a realistic mid-market engagement, showing how each component adapts to a specific client context.

**Planned v3 improvements:**
- Add multi-wave example (e.g., Scenario B: high-tech manufacturing with Wave 1 core finance/logistics, Wave 2 production planning, Wave 3 advanced analytics)
- Incorporate SAP RISE vs. GROW decision framework output from Skill 02 to auto-select the correct licensing and deployment model
- Add integration with Cloud ALM API schema to enable direct project import (eliminating manual transcription)
- Enhance budget framework with regional rate card data (Big 4 vs. regional partner vs. offshore rates)
- Add earned value management (EVM) tracking framework for in-flight project monitoring
- Include SAP S/4HANA Cloud quarterly release calendar alignment to ensure go-live timing does not conflict with mandatory update windows
