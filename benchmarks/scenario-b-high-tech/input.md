# Scenario B: High-Tech Manufacturing Enterprise — Client Brief

## Client Input (Raw — to be fed into Skill 01)

Constellation Satellite Systems (CSS) is a satellite manufacturing and launch services
company headquartered in Redmond, WA with manufacturing facilities in Redmond, WA and
Huntsville, AL, plus a launch operations center in Cape Canaveral, FL.

We have approximately 2,500 employees across all sites. Annual revenue is ~$1.2B.
We manufacture Low Earth Orbit (LEO) communication satellites — currently producing
at a rate of 5 satellites per month with plans to scale to 15/month within 18 months
to support our constellation deployment timeline.

Current SAP landscape:
- SAP ECC 6.0 EHP8 on-premise (installed 2015, heavily customized)
- ~800 active SAP users (Professional + Limited Professional licenses)
- Modules in use: FI/CO, MM, SD, PP, QM, PM, PS
- ~2,400 custom ABAP objects (reports, enhancements, interfaces)
- 47 custom transactions
- Integration with: Teamcenter PLM (Siemens), MES system (Apriso/Dassault),
  Salesforce CRM, Workday HCM, Anaplan (planning), and 12 custom middleware interfaces
- SAP Basis team of 4 FTEs
- Maintenance ending: SAP ECC mainstream maintenance ends 2027, extended to 2030

Key pain points:
- ECC system is heavily customized and increasingly difficult to maintain
- Custom code creates upgrade barriers — we've skipped 3 enhancement packs
- BOM management is a nightmare — engineering BOMs in Teamcenter don't sync
  cleanly with manufacturing BOMs in SAP PP. As-built BOMs are tracked manually
- Project System (PS) is used for satellite program tracking but earned value
  management is done in Excel outside SAP
- ITAR compliance is managed through a combination of GTS (partial implementation),
  manual processes, and a separate access control database
- No real-time manufacturing visibility — MES-to-SAP integration has 4-hour lag
- Financial close takes 12 business days — target is 5 days
- Supply chain visibility is poor — long-lead components (18+ month lead times
  for space-grade electronics) have no predictive tracking
- We need to support IFRS 15/ASC 606 revenue recognition for long-term contracts
  but current FI configuration doesn't handle milestone-based recognition properly

Strategic drivers:
- Board has mandated S/4HANA migration by end of 2028 (before ECC maintenance ends)
- CEO wants "digital factory" capabilities — real-time production visibility, predictive
  quality, AI-assisted supply chain planning
- CFO wants to reduce close from 12 days to 5 days and implement proper program-level
  profitability analysis
- VP Manufacturing wants integrated BOM management (single source of truth from
  engineering through as-built)
- CISO is concerned about ITAR compliance gaps and wants GTS fully implemented
- CIO wants to reduce total custom code by 60% and move to Clean Core

Additional context:
- We're a subsidiary of a larger aerospace conglomerate that uses SAP S/4HANA Cloud
  (Private Edition) — there's pressure to align
- The parent company uses SAP Signavio for process management and LeanIX for
  enterprise architecture — we're expected to adopt these tools
- Budget: $15-25M has been allocated for the transformation program
- Timeline: Board deadline is December 2028 go-live for core finance + operations
- We've had two failed IT projects in the past 3 years (MES upgrade, PLM migration)
  which has created organizational skepticism about large IT programs

## Scenario Characteristics

| Dimension | Value |
|---|---|
| Company Size | ~2,500 employees, ~800 SAP users |
| Industry | High Tech / Aerospace & Defense |
| Current ERP | SAP ECC 6.0 EHP8 (heavily customized) |
| Transformation Type | System Conversion (Brownfield) |
| Complexity | Very High |
| Key Challenge | Custom code remediation (2,400 objects), BOM integration, ITAR compliance |
| Budget | $15-25M allocated |
| Geographic | US multi-site (WA, AL, FL) |
| Currencies | USD (primary), potentially EUR for European suppliers |
| Regulatory | ITAR/EAR export controls, IFRS 15/ASC 606, SOX |
| SAP Ecosystem | Parent uses S/4HANA Cloud PE, Signavio, LeanIX |

## Evaluation Focus Areas

1. Does the agent recommend System Conversion (Brownfield) given existing ECC investment?
2. Is custom code analysis prominently featured (2,400 objects is a red flag)?
3. Does it correctly assess Clean Core maturity as Level C/D with remediation plan?
4. Is ITAR/GTS flagged as non-negotiable Phase 1 scope?
5. Does it recommend S/4HANA Cloud Private Edition (parent alignment)?
6. Does it reference Signavio for process mining and LeanIX for app rationalization?
7. Is the timeline 18-24 months with multi-wave approach?
8. Does it flag organizational change fatigue from failed projects as top risk?
9. Is the $15-25M budget validated (not just echoed)?
10. Does the proposal address both the board mandate AND organizational skepticism?
