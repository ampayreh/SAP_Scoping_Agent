# Skill 05: SAP Best Practices Fetcher (MCP Tool)

## Purpose

An MCP (Model Context Protocol) tool that retrieves and synthesizes relevant SAP best practices, scope items, reference architectures, industry solution maps, and known implementation patterns. This skill grounds all other skills' outputs in SAP's official guidance rather than relying solely on the AI model's training data. It acts as the knowledge backbone of the entire skills pack, ensuring that every recommendation, timeline estimate, and module selection traces back to SAP's published methodology.

### SAP Ecosystem Positioning

This skill is the closest analog to **Joule for Consultants (J4C)** in the skills pack. J4C draws on 9+ TB of SAP content -- Implementation Guide (IMG), Simplification List, SAP Notes, Best Practice Explorer, and 200K+ pages of documentation -- via Anthropic Claude on Amazon Bedrock. This skill cannot replicate that proprietary knowledge base, but it can:

1. Reference SAP's publicly available best practice scope items and process flows from the SAP Best Practice Explorer
2. Provide industry-specific implementation patterns based on SAP's industry solution maps and industry cloud portfolio
3. Surface known gotchas, common configuration patterns, and architecture decisions drawn from publicly available SAP Community knowledge
4. Serve as a structured knowledge retrieval layer that other skills can query programmatically via the MCP protocol
5. Demonstrate the MCP integration pattern -- showing how this skills pack could connect to SAP's actual knowledge APIs (BTP, Signavio, LeanIX) via A2A/MCP protocols in a production implementation

### Future Vision: A2A and MCP Integration

In a production deployment, this skill would be replaced by actual MCP server connections to:

- **SAP BTP API** -- scope item catalog, configuration guides, extension metadata
- **SAP Signavio API** -- best practice process models, Value Accelerators, process mining benchmarks
- **SAP LeanIX API** -- reference architectures, application portfolio data, industry benchmarks
- **SAP Cloud ALM API** -- project templates, task libraries, implementation roadmap templates
- **SAP Help Portal** -- implementation guides, SAP Notes, KBAs, release information
- **SAP API Business Hub** -- API specifications, sandbox environments, integration content packages

This aligns with SAP's A2A protocol (co-developed with Google Cloud, announced at TechEd 2025) and the MCP support announced for SAP HANA Cloud. The architecture is designed so that swapping the curated knowledge base for live API connections requires changes only to the retrieval layer, not to the consuming skills or the tool interface contract.

---

## MCP Tool Specification

```json
{
  "tool": {
    "name": "sap_best_practices_fetcher",
    "description": "Retrieves SAP S/4HANA best practices, scope items, reference architectures, and industry-specific implementation patterns to ground scoping recommendations in SAP official guidance.",
    "input_schema": {
      "type": "object",
      "properties": {
        "query_type": {
          "type": "string",
          "enum": [
            "scope_items",
            "process_flow",
            "industry_map",
            "reference_architecture",
            "clean_core_guidance",
            "migration_pattern",
            "integration_pattern",
            "sizing_guidance",
            "licensing_guidance",
            "change_management_pattern"
          ],
          "description": "The type of SAP best practice information to retrieve"
        },
        "module": {
          "type": "string",
          "description": "SAP module code (FI, CO, MM, SD, PP, QM, PM, PS, WM, EWM, GTS, TM, HCM, SF, BTP, etc.)"
        },
        "industry": {
          "type": "string",
          "description": "SAP industry classification (e.g., Consumer Products, High Tech, Aerospace and Defense, Utilities, Retail, Public Sector, Oil and Gas, Banking, Life Sciences)"
        },
        "deployment_model": {
          "type": "string",
          "enum": ["public_cloud", "private_cloud", "on_premise", "hybrid"],
          "description": "Target deployment model — determines which scope items and configuration options are available"
        },
        "company_size": {
          "type": "string",
          "enum": ["small", "midmarket", "large_enterprise"],
          "description": "Company size category for sizing and scoping guidance"
        },
        "source_system": {
          "type": "string",
          "description": "Current ERP system if migrating (e.g., SAP ECC 6.0, SAP R/3, Oracle E-Business Suite, Microsoft Dynamics, Legacy/Custom)"
        },
        "specific_topic": {
          "type": "string",
          "description": "Free-text topic for targeted retrieval (e.g., multi-currency configuration, batch management for agricultural products, export compliance documentation, intercompany elimination)"
        }
      },
      "required": ["query_type"]
    },
    "output_schema": {
      "type": "object",
      "properties": {
        "results": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "title": { "type": "string" },
              "category": { "type": "string" },
              "sap_reference_id": { "type": "string", "description": "SAP scope item ID, note number, or reference document ID" },
              "content": { "type": "string" },
              "relevance_score": { "type": "number", "minimum": 0, "maximum": 1 },
              "source": { "type": "string" },
              "applicability_notes": { "type": "string" },
              "prerequisites": { "type": "array", "items": { "type": "string" }, "description": "Scope items or configurations that must be in place before this applies" },
              "deployment_availability": { "type": "array", "items": { "type": "string" }, "description": "Which deployment models support this capability" }
            }
          }
        },
        "metadata": {
          "type": "object",
          "properties": {
            "query_type": { "type": "string" },
            "total_results": { "type": "number" },
            "knowledge_currency": { "type": "string", "description": "Indicates how current the knowledge base is relative to SAP release cycles" },
            "confidence_level": { "type": "string", "enum": ["high", "medium", "low"], "description": "Confidence that results are accurate and current" },
            "gaps_identified": { "type": "array", "items": { "type": "string" }, "description": "Topics where the knowledge base has insufficient depth" },
            "disclaimer": { "type": "string" }
          }
        }
      }
    }
  }
}
```

---

## Inputs

| Input | Description | Required | Used By |
|---|---|---|---|
| `query_type` | Type of best practice to retrieve (scope_items, process_flow, industry_map, reference_architecture, clean_core_guidance, migration_pattern, integration_pattern, sizing_guidance, licensing_guidance, change_management_pattern) | Yes | All queries |
| `module` | SAP module code for module-specific queries (FI, CO, MM, SD, PP, QM, PM, PS, WM, EWM, GTS, TM, HCM, SF, BTP) | No | scope_items, process_flow, integration_pattern |
| `industry` | SAP industry classification for industry-specific guidance | No | industry_map, scope_items, sizing_guidance |
| `deployment_model` | Target deployment model (public_cloud, private_cloud, on_premise, hybrid) | No | reference_architecture, scope_items, licensing_guidance |
| `company_size` | Size category (small, midmarket, large_enterprise) | No | sizing_guidance, licensing_guidance |
| `source_system` | Current ERP system if migrating | No | migration_pattern |
| `specific_topic` | Free-text topic for targeted searches | No | All queries |

---

## Output: Best Practice Knowledge Package

The output contains retrieved knowledge organized by relevance, including:

1. **Scope Items** -- SAP best practice scope items with IDs (e.g., "1YR - Accounts Receivable", "2QN - Quality Management in Procurement"), descriptions, prerequisite scope items, configuration complexity ratings, and deployment model availability

2. **Process Flows** -- SAP standard process flows with BPMN-level descriptions, including process steps, decision points, integration touchpoints, variant configurations, and expected transaction codes

3. **Industry Patterns** -- Industry-specific implementation patterns including common module configurations, regulatory compliance approaches, industry benchmarks, and typical customization areas

4. **Reference Architectures** -- Standard SAP architecture patterns for the given deployment model, including integration architecture, data architecture, security architecture, and infrastructure sizing

5. **Clean Core Guidance** -- SAP's extensibility framework recommendations, ABAP Cloud model guidance, approved extension points, and custom code migration strategies

6. **Migration Patterns** -- System conversion vs. new implementation vs. selective data migration guidance, including data volume considerations and cutover planning

7. **Implementation Guidance** -- Known best practices, common pitfalls, critical success factors, and lessons learned from SAP's implementation knowledge base

---

## Knowledge Base Structure

Since this is a demonstration MCP tool (not connected to live SAP APIs), the skill maintains a curated knowledge base covering the most commonly needed best practices across two tiers of depth.

### Tier 1: Core Module Best Practices (Deep Coverage)

#### Financial Accounting (FI)

**Key Scope Items:**
- 1FC -- General Ledger Accounting: Universal Journal (ACDOCA), document splitting, real-time integration with CO, segment reporting
- 1YR -- Accounts Receivable: Customer invoicing, dunning, credit management, payment processing, dispute management
- 1YS -- Accounts Payable: Vendor invoicing, payment program (F110), automatic payment methods, evaluated receipt settlement
- 2FM -- Asset Accounting: New asset accounting (fully integrated with Universal Journal from S/4HANA), parallel valuation areas, asset lifecycle management
- 1NX -- Bank Account Management: Bank communication management (BCM), electronic bank statement processing, cash pool management
- J58 -- Multi-Currency Valuation: Foreign currency valuation, translation methods, parallel currencies (local/group/hard)

**Standard Process Flows:**
- Record-to-Report (R2R): Journal entry posting through financial close, including automated accruals, allocations, and reporting
- Period-End Close: Closing cockpit (transaction FCLM_CLC), task scheduling, parallel close execution, fast-close methodology
- Intercompany Reconciliation: ICR monitor, matching logic, automated clearing, elimination entries for consolidation

**Configuration Patterns:**
- Chart of accounts strategy: Country-specific CoA (statutory requirements) plus group CoA (consolidated reporting), with account group determination rules
- Parallel ledger approach: Leading ledger (0L) for group reporting, non-leading ledgers for local GAAP or management reporting, with posting logic rules (all ledgers vs. specific ledger)
- Currency types: Currency type 10 (company code currency), 30 (group currency), 40 (hard currency) -- configure all three from Day 1 even if only one is needed initially
- Payment program configuration: Payment method/country combinations, house bank and account determination, automatic vs. semi-automatic payment, DME file formats for local banking

**Common Pitfalls:**
- Underestimating chart of accounts harmonization effort across entities (typically 3-6 months for multi-entity clients)
- Inadequate parallel currency planning -- retrofitting currency types after go-live is extremely disruptive
- Tax integration complexity, especially for multi-country deployments with VAT, WHT, and US state tax requirements
- Not leveraging the Universal Journal (ACDOCA) for reporting, resulting in unnecessary custom reports

#### Controlling (CO)

**Key Scope Items:**
- 1FS -- Cost Center Accounting: Cost center hierarchy, planning, actual postings, allocation cycles
- 2NR -- Profitability Analysis: Account-based CO-PA (required in S/4HANA), margin analysis, top-down distribution
- 1FT -- Internal Orders: Overhead orders, investment orders, statistical vs. real orders
- 2QH -- Product Costing: Material cost estimates, standard costing, activity-based costing, actual cost component split

**Standard Process Flows:**
- Plan-to-Actual: Budget planning, cost center planning, periodic actuals comparison, variance analysis
- Cost Allocation: Assessment, distribution, periodic reposting, template allocation with sender/receiver logic
- Margin Analysis: Profitability segment definition, value field mapping, real-time margin calculation via ACDOCA

**Configuration Patterns:**
- CO-PA: S/4HANA mandates account-based CO-PA -- costing-based CO-PA is deprecated. Design profitability segments using existing FI dimensions (profit center, functional area, customer group, material group) rather than creating numerous custom characteristics
- Cost center hierarchy: Design reflects organizational structure with additional analytical levels. Standard depth is 4-5 levels (area, department, cost center group, cost center)
- Allocation cycle design: Minimize allocation cycles (target fewer than 10 per period close). Use template allocation for activity-dependent allocations

**Common Pitfalls:**
- Over-complex CO-PA characteristics creating a combinatorial explosion of profitability segments
- Misaligned cost element structure between FI GL accounts and CO cost elements (in S/4HANA these are unified, but migration from ECC requires careful mapping)
- Not leveraging Universal Journal for CO reporting, building redundant custom reporting instead

#### Materials Management (MM)

**Key Scope Items:**
- 1A2 -- Purchasing: Purchase requisitions, purchase orders, contracts, scheduling agreements, source determination
- 1NM -- Inventory Management: Goods receipt, goods issue, stock transfers, physical inventory, batch management
- 2QN -- Quality Management in Procurement: Quality inspection at goods receipt, vendor evaluation, certificate management
- 2C8 -- Subcontracting: Provision of components to subcontractor, receipt of finished goods, subcontractor stock management
- 4H3 -- Simplified Purchasing: Simplified flows for lower-value or routine procurement (relevant for smallholder farmer procurement in agribusiness)

**Standard Process Flows:**
- Procure-to-Pay (P2P): Purchase requisition through invoice verification and payment, including three-way match
- Source-to-Contract: Vendor selection, RFQ processing, contract creation, spend analysis
- Inventory Management: Goods movements (101/102/201/202/301/302), stock determination, batch management, shelf life monitoring

**Configuration Patterns:**
- Purchasing organization structure: Central vs. plant-level purchasing, purchasing groups by commodity category
- Material type strategy: Standard material types (ROH, HALB, FERT, HAWA) plus custom types for industry-specific needs (e.g., agricultural commodity material types with batch and quality attributes)
- Batch management: Batch level (material, plant, or client level), batch classification with custom characteristics, automatic batch determination in sales
- Valuation approach: Standard price vs. moving average price, split valuation by batch for commodity tracking

**Common Pitfalls:**
- Master data quality in material master -- incomplete or inconsistent material records derail procurement processes
- Vendor master harmonization across plants and purchasing organizations
- Batch management complexity for agricultural products (origin tracking, quality grades, moisture content, certification status)
- Underestimating the effort for invoice verification configuration, especially with OCR/ML-based automation

#### Sales and Distribution (SD)

**Key Scope Items:**
- 1B5 -- Sales Order Management: Order types, item categories, scheduling, availability check, output determination
- 1CN -- Billing: Invoice types, billing plans, revenue recognition triggers, intercompany billing
- 2QM -- Sales Scheduling: Delivery scheduling, transportation scheduling, route determination
- 1D8 -- Export Processing: Export declarations, customs documentation, trade compliance screening
- 2K4 -- Credit Management: Credit exposure monitoring, credit limit check, credit release workflow

**Standard Process Flows:**
- Order-to-Cash (O2C): Sales order through billing and payment receipt, including delivery and goods issue
- Quote-to-Order: Quotation creation, follow-up, conversion to sales order, win/loss tracking
- Returns Management: Return order, goods receipt for returns, credit memo, quality inspection integration

**Configuration Patterns:**
- Sales organization structure: Sales organization, distribution channel, division hierarchy aligned to commercial reporting needs
- Pricing procedure design: Access sequences, condition types, pricing procedure determination. Keep condition types under 30 per pricing procedure to maintain manageability
- Output management: Adobe Forms or SAP Document Compliance for invoice output. BRF+ rules for output determination
- Credit management: SAP Credit Management (FIN-FSCM-CR) integrated with SD, credit segment design, automatic credit limit assignment rules

**Common Pitfalls:**
- Over-complex pricing with excessive condition types creating maintenance nightmares
- Condition record maintenance burden if pricing rules are too granular
- Partner function design that does not account for complex trading scenarios (ship-to, bill-to, payer, sold-to separation)
- Incomplete availability check configuration leading to delivery commitment issues

#### Production Planning (PP)

**Key Scope Items:**
- 1GP -- Production Planning (discrete): MRP, planned orders, production orders, confirmations
- 1GQ -- Production Planning (process): Process orders, batch management integration, yield management
- 2QO -- Quality in Production: In-process inspection, final inspection, quality certificates for finished goods

**Configuration Patterns:**
- BOM management: Engineering BOM vs. manufacturing BOM with BOM transfer logic. For complex manufacturing (aerospace, high tech), multi-level BOM with variant configuration
- MRP configuration: Planning strategies (MTS, MTO, ATO), lot sizing procedures, safety stock calculation
- Shop floor integration: PP-SFC for discrete, PP-PI for process industries, with OEE integration via MII or DMC

#### Quality Management (QM)

**Key Scope Items:**
- 2QN -- Quality in Procurement: Incoming inspection triggered at goods receipt, vendor quality scoring
- 2QO -- Quality in Production: In-process and final inspection, quality certificates for outbound
- 2QP -- Quality in Sales: Outbound quality checks, Certificate of Analysis generation, customer-specific quality requirements

**Configuration Patterns:**
- Inspection plan design: Sampling procedures, dynamic modification rules, skip lot logic for trusted vendors
- Catalog management: Characteristic catalogs (physical/chemical attributes), defect code catalogs, usage decision codes
- Quality certificates: Certificate profiles, content determination, output via Adobe Forms

**Common Pitfalls:**
- Over-engineering inspection plans with too many characteristics per inspection lot
- Catalog explosion from creating separate codes for every minor variation
- Not leveraging batch classification for quality attributes, leading to duplicate data entry

#### Warehouse Management (WM / EWM)

**Key Scope Items:**
- 1NN -- Basic Warehouse Management: Embedded warehouse management within MM, bin-level stock tracking
- 2V4 -- Extended Warehouse Management: Full EWM with wave management, labor management, slotting, yard management

**Decision Framework -- Embedded WM vs. EWM:**
- Use embedded WM (stock room management) for simple warehouse operations (fewer than 3 storage types, no wave management, no complex picking strategies)
- Use EWM for complex warehouses (multiple storage types, RF/barcode scanning, task interleaving, labor management, integration with MHE)
- S/4HANA embedded EWM is available from S/4HANA 1709 onward and is the recommended path for new implementations requiring advanced warehouse capabilities

#### Global Trade Services (GTS)

**Key Scope Items:**
- 1D8 -- Export Processing: Export declaration automation, customs document generation
- Trade Preference Management: Origin determination, preference calculation for FTA utilization
- Compliance Management: Sanctioned party list screening, embargo checks, license management

**Configuration Patterns:**
- Export documentation automation: Integration with customs authorities (AES in US, ATLAS in Germany, single-window systems in East Africa)
- Sanction list management: Automated download of OFAC SDN, EU Consolidated List, UN sanctions. Screening at sales order creation and delivery
- ITAR/EAR compliance: Classification of controlled items, license management, deemed export tracking for aerospace/defense

**Common Pitfalls:**
- Underestimating regulatory complexity across multiple export jurisdictions
- Maintaining current sanction and denied party lists requires automated update processes
- Not integrating GTS screening into SD order flow from Day 1, requiring costly retrofit

#### Business Technology Platform (BTP)

**Extension Patterns:**
- Side-by-side extensions: Standalone applications on BTP that communicate with S/4HANA via APIs. Used for new UI, integration orchestration, advanced analytics
- Embedded extensions: Key user extensibility within S/4HANA using custom fields, custom logic (BAdIs), custom CDS views
- Clean Core compliance: Side-by-side extensions are always Clean Core compliant. Embedded extensions are compliant if they use released APIs and extension points only

**Integration Patterns:**
- SAP Integration Suite: Cloud Integration (CPI) for A2A and B2B integration, API Management for API governance, Event Mesh for event-driven architectures
- Standard integration content packages: Pre-built iFlows for common integration scenarios (e.g., S/4HANA to SuccessFactors, S/4HANA to Ariba, S/4HANA to Concur)

---

### Tier 2: Industry-Specific Patterns (Deep Coverage for Benchmark Scenarios)

#### Consumer Products / Agribusiness

**Batch Management for Agricultural Commodities:**
- Lot traceability from farm gate through processing, warehousing, and export
- Batch classification characteristics: origin (farm, region, cooperative), quality grade (AAA/AA/A/B), moisture content, screen size, altitude, harvest date, processing date, certification status
- Split valuation by batch to track cost-per-lot from farmer payment through export
- Shelf life management for perishable agricultural products with FEFO (First Expired, First Out) picking strategies
- Batch determination in sales orders to match customer quality requirements to available inventory

**Commodity Trading and Pricing:**
- Floating price agreements: Purchase contracts with price-to-be-fixed (PTBF) linked to commodity exchange reference prices (ICE for coffee, CBOT for grains)
- Differential pricing: Base price plus quality differential, location differential, certification premium
- Multi-currency procurement: Local currency payment to farmers, USD-denominated export contracts, exchange rate management
- Mark-to-market valuation for open commodity positions

**Certification and Compliance Tracking:**
- Fair Trade, Organic, UTZ/Rainforest Alliance, 4C certification tracking via batch classification and segregation
- Mass balance vs. identity preserved vs. segregated supply chain models
- Certificate of Origin generation for preferential trade agreements (AGOA, EBA, EPAs)
- Traceability reporting for EU Deforestation Regulation (EUDR) compliance

**Seasonal Procurement and Crop Cycle Management:**
- Procurement planning aligned to crop cycles (harvest seasons, flowering patterns)
- Advance payment management for smallholder farmers (pre-financing against future delivery)
- Cooperative/washing station management as vendor hierarchy
- Mobile-enabled goods receipt for remote collection points (Fiori apps or BTP mobile extensions)

#### High Tech / Aerospace and Defense

**Complex BOM Management:**
- Engineering BOM (eBOM): As-designed structure maintained by engineering team
- Manufacturing BOM (mBOM): As-planned structure optimized for production execution
- As-Built BOM: Actual components used per serial number, maintained through production confirmations
- BOM transfer and synchronization between eBOM and mBOM with engineering change management (ECM)
- Variant configuration for configurable products (CTO - Configure to Order)

**Project System Integration:**
- WBS-based program management for large defense/space programs
- Earned Value Management (EVM) with CPI/SPI calculations
- Milestone billing tied to WBS elements
- Long-term project accounting with percentage-of-completion or cost-to-cost revenue recognition
- Multi-year budget management with commitment tracking (funds management integration)

**Export Control (ITAR/EAR):**
- ITAR (International Traffic in Arms Regulations): Classification of defense articles, technical data control, manufacturing license agreements
- EAR (Export Administration Regulations): Commerce Control List (CCL) classification, license exception determination
- Deemed export tracking: Controlling access to controlled technical data by foreign nationals within the organization
- GTS integration: Automated screening of all sales orders, deliveries, and shipments against control lists
- Technology Control Plan (TCP) management: Document-level access controls linked to classification

**Serial Number Management:**
- Unit-level traceability for every manufactured item
- Serial number profiles: Pre-assigned, automatic at goods receipt, or at production confirmation
- As-maintained BOM: Tracking component replacements and repairs throughout product lifecycle
- Integration with Plant Maintenance (PM) for field service and MRO operations

---

### Clean Core Guidance

**SAP Clean Core Maturity Model (4 Levels):**
- **Level A -- Fully Clean:** Only standard SAP functionality plus BTP extensions via released APIs. Ideal target state for public cloud deployments.
- **Level B -- Mostly Clean:** Standard functionality with limited embedded extensions using released extension points (custom fields, custom logic via BAdIs). Acceptable for private cloud.
- **Level C -- Partially Clean:** Some classic modifications exist but are isolated and documented. Requires remediation plan for future cloud migration.
- **Level D -- Legacy Extensions:** Heavy modification of SAP standard code. Blocks cloud migration and innovation adoption. Requires transformation program.

**Decision Framework: Standard vs. BTP Extension vs. Classic Modification:**
1. Can the requirement be met with standard SAP configuration? If yes, use standard. (Target: 80%+ of requirements)
2. Can it be met with key user extensibility (custom fields, custom logic)? If yes, use embedded extension. (Target: 10-15%)
3. Does it require new UI, external integration, or complex logic? If yes, use BTP side-by-side extension. (Target: 5-10%)
4. Does it absolutely require modifying SAP standard code? This should be a last resort requiring architectural review board approval. (Target: less than 1%)

**ABAP Cloud Development Model:**
- Tier 1 (released APIs): Only released SAP APIs are accessible. Required for public cloud.
- Tier 2 (ABAP for Cloud): Access to released APIs plus a defined set of non-released objects. For private cloud and on-premise.
- Tier 3 (classic ABAP): Full access to all ABAP objects. On-premise only. Not recommended for new development.
- Custom code migration: Use SAP Custom Code Migration app (transaction /UI2/CL_CCM) to analyze existing custom code for cloud readiness, identifying deprecated APIs and proposing replacements.

---

### SAP GROW vs. RISE Decision Framework

| Criterion | SAP GROW | SAP RISE |
|---|---|---|
| **Target audience** | New to SAP, cloud-native companies | Existing SAP customers transforming to S/4HANA |
| **Typical company size** | Small to midmarket (under 1500 employees) | Midmarket to large enterprise |
| **Deployment** | Public cloud only | Private cloud (managed by SAP/hyperscaler) or public cloud |
| **Customization** | Standard scope items only, key user extensibility, BTP extensions | Full configuration flexibility, custom ABAP (Tier 2), BTP extensions |
| **Implementation approach** | Activate best practices, configure, extend | Greenfield, brownfield (system conversion), or selective data transition (bluefield) |
| **Timeline** | 3-6 months typical | 9-24 months typical |
| **TCO** | Lower (subscription-based, no infrastructure management) | Higher (but offsets existing maintenance costs) |
| **Included services** | SAP Business Network starter, SAP BTP credits, learning hub | Business suite transformation tools, SAP BTP credits, CPEA credits, migration services |

**Decision Criteria:**
- Existing SAP footprint: If running ECC/R3, RISE provides migration tools. If greenfield, GROW is faster.
- Customization needs: Heavy customization requirements point to RISE (private cloud). Standard processes point to GROW.
- Deployment preference: GROW is public cloud only. RISE offers choice.
- Budget: GROW has lower entry point. RISE has higher TCO but absorbs existing SAP license value.
- Timeline urgency: GROW can deliver faster. RISE requires migration planning.

---

### Sizing and Licensing Guidance

**User-Based Licensing:**
- SAP S/4HANA Cloud Professional User: Full transactional access (create, change, display in all modules the user is authorized for)
- SAP S/4HANA Cloud Limited Professional User: Restricted to specific tasks (typically self-service scenarios -- time entry, expense reports, purchase requisitions)
- Developer User: Access to ABAP development tools and BTP development environment
- FUE (Full User Equivalent) model: Alternative metric-based licensing where different user types consume different FUE ratios (e.g., Professional User = 1 FUE, Limited Professional = 0.1-0.3 FUE depending on scenario)

**Sizing by Transaction Volume:**
- Small (under 500 users): Single application server, standard DB sizing, basic HA configuration
- Midmarket (500-2000 users): Clustered application servers, enhanced DB sizing, full HA and DR
- Large enterprise (2000+ users): Scaled-out application tier, HANA scale-out or scale-up, global deployment with system replication

**SAP Business One vs. S/4HANA Cloud Decision:**
- SAP Business One: Under 500 employees, single-entity or simple multi-entity, limited manufacturing complexity, lower TCO requirement
- S/4HANA Cloud Public Edition (GROW): 100-1500 employees, multi-entity capable, standard industry processes, cloud-first strategy
- S/4HANA Cloud Private Edition (RISE): 500+ employees, complex multi-entity, heavy customization needs, regulated industries

---

## Step-by-Step Behavior

1. **Query Parsing** -- Interpret the query_type and all provided parameters. Validate that the query_type is one of the 10 supported types. If module or industry is provided, validate against known SAP module codes and industry classifications.

2. **Knowledge Base Search** -- Retrieve relevant content from the curated knowledge base. For scope_items queries, match on module and industry. For industry_map queries, match on industry and specific_topic. For clean_core_guidance, match on deployment_model and specific_topic.

3. **Relevance Scoring** -- Rank results by relevance to the specific query context. Scoring factors: direct module match (0.3 weight), industry match (0.25 weight), deployment model match (0.2 weight), specific_topic keyword match (0.25 weight). Results below 0.5 relevance are excluded.

4. **Contextualization** -- Adapt generic best practices to the specific client scenario. If industry is "Consumer Products" and specific_topic mentions agricultural products, surface agribusiness-specific batch management patterns. If deployment_model is "public_cloud", filter out scope items not available in cloud edition.

5. **Prerequisite Chain Resolution** -- For scope_items queries, identify prerequisite scope items that must be activated before the requested items. For example, 2QN (Quality in Procurement) requires 1A2 (Purchasing) and 1NM (Inventory Management).

6. **Gap Identification** -- Flag areas where the curated knowledge base does not have sufficient detail. Recommend consulting SAP Help Portal, SAP Notes, or Joule for Consultants (J4C) for gaps. Common gaps: transaction-code-level configuration steps, specific OSS notes for bug fixes, real-time scope item availability by S/4HANA release.

7. **Output Assembly** -- Package results with source references, applicability notes, prerequisites, deployment availability flags, and the standard disclaimer about knowledge currency.

---

## Constraints and Failure Modes

| Constraint | Handling |
|---|---|
| **Knowledge currency** | This is a demonstration tool with a curated knowledge base. It does not have real-time access to SAP systems. All outputs include a disclaimer noting that recommendations should be validated against current SAP documentation and the latest S/4HANA release notes. |
| **Scope item accuracy** | Scope item IDs and descriptions are based on publicly available SAP Best Practice Explorer catalogs. IDs may not reflect the latest S/4HANA quarterly release. |
| **Industry coverage** | Deep coverage for Consumer Products/Agribusiness and High Tech/Aerospace and Defense. Foundational coverage for other industries. The tool explicitly flags when a query falls outside deep coverage areas. |
| **Licensing specifics** | Licensing models, pricing, and packaging change frequently. All licensing guidance is directional and must be validated with SAP or a certified partner. Pricing figures are never provided. |
| **Configuration detail** | This tool provides guidance-level content, not transaction-code-level configuration instructions. For step-by-step IMG configuration, consult SAP Help Portal or J4C. |
| **Regulatory compliance** | Regulatory requirements (tax, trade compliance, data privacy) vary by jurisdiction and change frequently. All regulatory guidance must be validated with qualified legal and compliance advisors. |
| **No live API connection** | The tool cannot validate scope item availability for a specific S/4HANA release version. It cannot check real-time license entitlements or BTP service availability. |

---

## Example Usage

### Example 1: Scope Items Query for Agribusiness MM

**Input:**
```json
{
  "query_type": "scope_items",
  "module": "MM",
  "industry": "Consumer Products",
  "specific_topic": "agricultural commodity procurement with batch management"
}
```

**Output:**
```json
{
  "results": [
    {
      "title": "Procurement of Commodities with Batch Management",
      "category": "Scope Item",
      "sap_reference_id": "1A2 (Purchasing) + 1NM (Inventory Management) + Batch Management",
      "content": "For agricultural commodity procurement, configure batch management with automatic batch creation at goods receipt. Key configuration: Material type with batch management flag, batch classification with characteristics for origin (farm/region), quality grade, moisture content, harvest date. Valuation: Consider split valuation by batch to track cost per lot from farmer through processing and export. Integration: QM inspection at goods receipt triggers quality results posting to batch. Pricing: Consider differential pricing by grade/quality, with floating price capability for commodity markets.",
      "relevance_score": 0.95,
      "source": "SAP Best Practice Scope Item 1A2, adapted for Agricultural Commodities",
      "applicability_notes": "Highly relevant for coffee/agricultural commodity exporters. Batch management is critical for lot traceability requirements. Consider combining with QM scope item 2QN for integrated quality-at-receipt inspection. For smallholder farmer procurement, consider using simplified purchasing (scope item 4H3) with mobile-enabled goods receipt.",
      "prerequisites": ["1NM (Inventory Management)", "Material Master with Batch Management flag"],
      "deployment_availability": ["public_cloud", "private_cloud", "on_premise"]
    },
    {
      "title": "Inventory Management with Batch Traceability",
      "category": "Scope Item",
      "sap_reference_id": "1NM (Inventory Management)",
      "content": "Standard inventory management with batch tracking enables full traceability from receipt through consumption or sales. Key features: Batch determination in sales order (SD integration), batch where-used reporting, shelf life management for perishable agricultural products. For coffee specifically: track processing stage (cherry to parchment to green to roasted) as batch status with stock transfers between processing stages.",
      "relevance_score": 0.92,
      "source": "SAP Best Practice Scope Item 1NM, adapted for Agricultural Commodities",
      "applicability_notes": "Essential scope item for any agricultural commodity with traceability requirements. Combine with WM/EWM if multi-bin warehouse tracking is needed. EUDR compliance may require additional traceability granularity beyond standard batch management.",
      "prerequisites": ["Material Master configuration"],
      "deployment_availability": ["public_cloud", "private_cloud", "on_premise"]
    }
  ],
  "metadata": {
    "query_type": "scope_items",
    "total_results": 2,
    "knowledge_currency": "Based on SAP S/4HANA 2024/2025 best practice catalog (publicly available scope items). Validate against current release notes for latest updates.",
    "confidence_level": "high",
    "gaps_identified": ["Specific EUDR compliance configuration not covered in curated knowledge base"],
    "disclaimer": "This is a demonstration knowledge retrieval tool. Scope item IDs and descriptions are based on publicly available SAP best practice documentation. For implementation-grade guidance, consult SAP Help Portal, SAP Notes, or Joule for Consultants (J4C)."
  }
}
```

### Example 2: Clean Core Guidance for Mobile Money Integration

**Input:**
```json
{
  "query_type": "clean_core_guidance",
  "specific_topic": "extending S/4HANA for mobile money payment integration without violating clean core"
}
```

**Output:**
```json
{
  "results": [
    {
      "title": "Clean Core Extension Pattern: Third-Party Payment Integration via BTP",
      "category": "Clean Core Guidance",
      "sap_reference_id": "Clean Core Extension Framework - Side-by-Side Extension Pattern",
      "content": "Mobile money payment integration (Pesapal, M-Pesa, Airtel Money) should be implemented as a BTP side-by-side extension, NOT as a classic SAP modification. Architecture pattern: (1) SAP S/4HANA maintains payment requests and clearing via standard FI-AP payment program (F110), (2) BTP Integration Suite connects to mobile money provider APIs via REST/JSON adapters, (3) Payment status callbacks update SAP clearing documents via standard APIs (Business Partner API, Journal Entry API, Bank Statement API). This maintains Clean Core Level A compliance while enabling the integration. Key APIs: SAP_COM_0009 (Business Partner), SAP_COM_0008 (Bank Statement), Payment Integration API on SAP API Business Hub.",
      "relevance_score": 0.98,
      "source": "SAP Clean Core Extension Framework + BTP Integration Patterns",
      "applicability_notes": "This is the recommended pattern for ANY third-party payment provider integration. Avoids modifying SAP standard payment program (RFZALI00/F110) while enabling full mobile money support. Requires BTP license and Integration Suite subscription. For East African markets, consider Pesapal aggregator which consolidates M-Pesa, Airtel Money, and bank transfers behind a single API.",
      "prerequisites": ["BTP subscription", "SAP Integration Suite license", "FI-AP payment program configuration (standard)"],
      "deployment_availability": ["public_cloud", "private_cloud", "hybrid"]
    }
  ],
  "metadata": {
    "query_type": "clean_core_guidance",
    "total_results": 1,
    "knowledge_currency": "Clean Core framework as of SAP TechEd 2025. A2A protocol support announced but not yet generally available for custom payment integrations.",
    "confidence_level": "high",
    "gaps_identified": ["Specific Pesapal/M-Pesa API integration iFlow not available in standard SAP Integration Suite content catalog -- custom development required"],
    "disclaimer": "Clean Core compliance should be validated with SAP Custom Code Migration analysis tool and confirmed with SAP or a certified implementation partner."
  }
}
```

### Example 3: Industry Map Query for Aerospace Manufacturing

**Input:**
```json
{
  "query_type": "industry_map",
  "industry": "High Tech",
  "specific_topic": "satellite manufacturing with complex BOM and export controls"
}
```

**Output:**
```json
{
  "results": [
    {
      "title": "SAP for High Tech: Satellite/Aerospace Manufacturing Reference Architecture",
      "category": "Industry Solution Map",
      "sap_reference_id": "SAP Industry Solution Map - High Tech / Aerospace and Defense",
      "content": "Core module scope for satellite manufacturing: (1) PP-PI/PP-DI with complex multi-level BOM management (engineering BOM, manufacturing BOM, as-built BOM), engineering change management integration, serial number tracking per unit. (2) PS (Project System) for program-level cost tracking, WBS-based milestone billing, earned value management. (3) QM with inspection plans per manufacturing stage, Certificate of Conformance generation, non-conformance tracking per serial number. (4) GTS for ITAR/EAR export control screening, deemed export tracking, technology control plans, license management. (5) MM with approved vendor management, long-lead procurement, consignment, subcontracting for specialized components. (6) FI/CO with project-based revenue recognition (IFRS 15/ASC 606), multi-entity consolidation, government contract accounting if applicable.",
      "relevance_score": 0.94,
      "source": "SAP Industry Solution Map - High Tech + Aerospace and Defense best practices",
      "applicability_notes": "Satellite manufacturing represents one of the most complex SAP implementation patterns. Key differentiators: ITAR compliance is non-negotiable and requires GTS from Day 1; BOM complexity drives PP implementation timeline; project accounting (PS) integration with FI is critical for program profitability tracking. Typical implementation: 18-24 months, 3-wave approach (Wave 1: FI/CO/MM/SD core, Wave 2: PP/QM/PS production, Wave 3: GTS/EWM/Advanced Analytics).",
      "prerequisites": ["All core modules (FI, CO, MM, SD)", "GTS license", "PS activation"],
      "deployment_availability": ["private_cloud", "on_premise"]
    }
  ],
  "metadata": {
    "query_type": "industry_map",
    "total_results": 1,
    "knowledge_currency": "SAP Industry Solution Maps as of 2025. High Tech and Aerospace/Defense is one of SAP's most mature industry solutions with dedicated industry cloud capabilities.",
    "confidence_level": "high",
    "gaps_identified": ["Specific government contract accounting (FAR/DFAR compliance) configuration not covered in depth", "SAP Industry Cloud for A&D add-on scope items not enumerated"],
    "disclaimer": "Industry-specific implementation patterns should be validated against current SAP Industry Cloud solutions and with implementation partners who have Aerospace and Defense domain expertise and ITAR compliance experience."
  }
}
```

---

## Integration Points with Other Skills

| Consuming Skill | How Best Practices Are Used | Typical Query Types |
|---|---|---|
| **01 Client Discovery Intake** | Industry classification from intake drives which industry-specific best practices to surface. Company size and current system information drive GROW vs. RISE and migration pattern guidance. | `industry_map`, `licensing_guidance`, `sizing_guidance` |
| **02 Module Fit Analyzer** | Scope items ground fit/gap scoring in SAP's actual capability catalog. Clean Core guidance informs gap resolution approach (standard config vs. BTP extension vs. accept the gap). | `scope_items`, `clean_core_guidance`, `process_flow` |
| **03 Implementation Roadmap** | Industry patterns calibrate timeline estimates. Wave structure recommendations use established implementation patterns. Migration patterns inform the brownfield vs. greenfield decision. | `migration_pattern`, `industry_map`, `reference_architecture` |
| **04 Executive Proposal Drafter** | Industry benchmarks and SAP value propositions enrich the business case narrative. GROW vs. RISE positioning frames the commercial recommendation. | `licensing_guidance`, `industry_map`, `sizing_guidance` |

---

## Prompt Engineering Notes

### Key Design Decisions

1. **MCP tool specification format** -- Designed as a full MCP tool with JSON Schema input/output contracts to demonstrate the integration pattern, even though the current implementation uses a curated knowledge base. This makes the skill pack architecturally ready for live API connections. The schema follows the MCP specification (protocol version 2025-03-26) with named tools, typed inputs, and structured outputs.

2. **Curated knowledge base vs. live retrieval** -- In a production deployment, this would connect to SAP's APIs via MCP server adapters. For the academic demonstration, a well-curated knowledge base covering the two benchmark scenarios (Agribusiness and High Tech) provides sufficient depth while being transparent about limitations. The knowledge base is structured to be replaceable without changing the tool interface.

3. **Ten structured query types** -- The query types map to the most common knowledge retrieval patterns observed during SAP implementation scoping engagements: scope items (what to implement), process flows (how it works in SAP standard), industry maps (what is special for this industry), reference architectures (how to deploy it), Clean Core guidance (how to stay compliant with SAP's extensibility framework), migration patterns (how to get from here to there), integration patterns (how to connect systems), sizing guidance (how big to build it), licensing guidance (how to buy it), and change management patterns (how to drive adoption).

4. **Relevance scoring** -- Results include a numeric relevance score (0.0 to 1.0) to help consuming skills prioritize information when multiple results are returned. This mimics how J4C ranks its knowledge retrieval responses and allows downstream skills to filter for only high-confidence recommendations.

5. **Prerequisite chain resolution** -- Scope item results include prerequisite scope items, enabling Skill 02 (Module Fit Analyzer) to build dependency-aware implementation scope rather than treating each module as independent. This catches common scoping errors like activating QM without the required MM foundation.

6. **Disclaimer and knowledge currency** -- Every response includes a knowledge_currency indicator and disclaimer, reinforcing that this is a demonstration tool and that all recommendations must be validated against current SAP documentation. This is critical for professional credibility in a consulting context and prevents overreliance on potentially outdated information.

7. **Gap identification** -- The output explicitly flags areas where the curated knowledge base lacks depth, directing users to authoritative sources (SAP Help Portal, SAP Notes, J4C). This honest signaling of limitations increases trust rather than diminishing it.

### Iteration History

**v1 (Initial Design):** Simple keyword search returning flat text results. Problem: no structure for programmatic consumption, no relevance scoring, consuming skills could not reliably parse the output for automated processing.

**v2 (Structured Output):** Added JSON Schema for input/output, typed query categories, and basic relevance scoring. Problem: insufficient industry depth, no prerequisite tracking, no deployment model filtering.

**v3 (Current):** Full MCP tool specification with 10 query types, prerequisite chain resolution, deployment availability flags, confidence levels, gap identification, and deep industry-specific knowledge modules for both benchmark scenarios. Added Clean Core guidance as a first-class query type reflecting its importance in modern SAP implementations. Added source_system input parameter for migration-specific queries.

**Planned v4 Improvements:**
- Live API connection to SAP API Business Hub for real-time scope item catalog retrieval
- Integration with SAP Signavio Process Explorer API for BPMN-level process model retrieval
- RAG (Retrieval-Augmented Generation) pipeline over SAP Help Portal content for detailed configuration guidance
- A2A protocol integration for bidirectional communication with SAP Joule
- Expanded industry coverage beyond Consumer Products and High Tech to cover all 25 SAP industry classifications
- Version-aware scope item filtering (filter results by specific S/4HANA release version)
- Multi-language support for non-English SAP implementations
