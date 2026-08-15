# Skill 05 Output: SAP Best Practices Fetcher — HHE Queries

> **Fictional scenario.** This company and every figure below are invented for benchmarking purposes. No resemblance to any real business is intended.

## Query 1: Scope Items for Agricultural Commodity Procurement with Batch Management

### Input
```json
{
  "query_type": "scope_items",
  "module": "MM",
  "industry": "Consumer Products",
  "company_size": "midmarket",
  "specific_topic": "raw cashew procurement from smallholder farmers with batch management and mobile money payment"
}
```

### Output
```json
{
  "results": [
    {
      "title": "Procurement of Agricultural Commodities with Batch Management",
      "category": "Scope Item",
      "sap_reference_id": "1A2 (Purchasing) + 1NM (Inventory Management) + Batch Management Configuration",
      "content": "For raw cashew procurement from smallholder farmers, configure batch management with automatic batch creation at goods receipt. Key configuration: (1) Material type ZCSH (cashew) with batch management flag enabled, split valuation active; (2) Batch classification with characteristics: origin_region (char), moisture_pct_intake (num), kernel_grade (char), outturn_ratio (num), harvest_date, defect_rate_pct (num), screen_size (num); (3) Split valuation by batch enables cost tracking per lot from farmer delivery through all 4 processing stages; (4) Stock transfer postings (movement type 309) to track processing stage transitions: raw intake → drying → shelling → grading/export-ready; (5) Batch determination in SD at sales order to enable lot allocation to specific buyer contracts based on grade.",
      "relevance_score": 0.97,
      "source": "SAP Best Practice Scope Item 1A2 + 1NM, adapted for Agricultural Commodities — Raw Cashew",
      "applicability_notes": "Critical for HHE. The batch classification schema should be designed during Explore phase with input from HHE's quality team — kernel grade and outturn ratio are the primary value drivers for premium raw cashew. Consider simplified purchasing (scope item 4H3) for the farmer procurement scenario, as full strategic purchasing is over-engineered for smallholder deliveries. For the 1,800-3,200+ farmer master data, use vendor classification with group 'FARM' and maintain geo-coordinates for export traceability."
    },
    {
      "title": "Mobile-Enabled Goods Receipt for Agricultural Collection Points",
      "category": "Scope Item + BTP Extension",
      "sap_reference_id": "BTP Mobile Extension — SAP Mobile Start / Custom Fiori App",
      "content": "For raw cashew collection at remote field locations, implement a mobile-enabled goods receipt process via BTP. Architecture: (1) Fiori app running on SAP Mobile Start with offline capability (critical for rural locations with intermittent connectivity); (2) Capture farmer ID, cashew weight, visual quality grade at point of collection; (3) Auto-create purchase order + goods receipt + batch record when connectivity restores; (4) Trigger mobile money payment via BTP Integration Suite → provider API. This pattern maintains Clean Core Level A compliance as all custom logic resides on BTP.",
      "relevance_score": 0.93,
      "source": "SAP BTP Extension Pattern — Mobile Field Operations for Agriculture",
      "applicability_notes": "High value for HHE's field operations but adds BTP licensing cost. Evaluate whether the volume of farmer transactions (1,800-3,200+ farmers × multiple deliveries per season) justifies the investment vs. a simpler tablet-based data entry at the collection station with daily batch upload."
    }
  ],
  "metadata": {
    "query_type": "scope_items",
    "total_results": 2,
    "knowledge_currency": "Based on SAP S/4HANA 2024/2025 best practice catalog. Raw cashew / agribusiness is not a standard SAP industry solution — recommendations adapted from Consumer Products and Agricultural Commodities patterns.",
    "disclaimer": "Scope item IDs are based on publicly available SAP best practice documentation. For implementation-grade configuration guidance, consult SAP Help Portal, SAP Notes, or Joule for Consultants (J4C)."
  }
}
```

---

## Query 2: EU Food-Safety Traceability with SAP GTS

### Input
```json
{
  "query_type": "clean_core_guidance",
  "module": "GTS",
  "industry": "Consumer Products",
  "specific_topic": "EU food-safety import traceability for raw cashew exports — geo-location traceability, documentation requirements"
}
```

### Output
```json
{
  "results": [
    {
      "title": "Export Traceability Architecture for Agricultural Commodity Exporters",
      "category": "Compliance Architecture + Clean Core Guidance",
      "sap_reference_id": "SAP GTS + SAP Sustainability Control Tower + BTP Extension",
      "content": "EU food-safety import rules increasingly expect exporters placing agricultural commodities on the EU market to be able to provide: (1) Geo-location coordinates of production regions; (2) Time of production (harvest period); (3) Supporting documentation confirming sourcing practices. For HHE's architecture: Option A (Full GTS): Implement SAP GTS with trade preference management and compliance screening; embed traceability data in export documentation. Requires GTS license — may be cost-prohibitive for mid-market. Option B (BTP Extension — Recommended for HHE): Build traceability compliance as a BTP side-by-side extension: (a) Farmer master data extended with geo-coordinates (latitude/longitude/region) stored as custom fields via BTP; (b) Batch record linked to farmer → geo-location → harvest date; (c) Traceability documentation generated as a PDF from batch + farmer + geo data at export; (d) Integration with EU import systems via API when available. This maintains Clean Core Level A while meeting documentation expectations at lower cost than full GTS. Key APIs: Business Partner API (SAP_COM_0009), Batch API, SD Delivery API.",
      "relevance_score": 0.96,
      "source": "SAP Sustainability Solutions + Agricultural Export Traceability Patterns (2025)",
      "applicability_notes": "Traceability documentation matters for HHE's EU market. The BTP extension approach is recommended over full GTS for cost reasons. However, if HHE's EU export volume grows significantly, upgrading to GTS provides more robust compliance management. HHE should capture geo-data for ALL farmers regardless of current buyer destination to future-proof compliance."
    }
  ],
  "metadata": {
    "query_type": "clean_core_guidance",
    "total_results": 1,
    "knowledge_currency": "SAP's traceability-specific solutions continue to expand; full GA status varies by module. BTP extension approach is production-ready.",
    "disclaimer": "Export documentation requirements should be validated with legal counsel and the specific requirements of HHE's EU importing partners. Regulatory landscape is evolving."
  }
}
```

---

## Query 3: Quality Management for Raw Cashew (Kernel Grading Protocol)

### Input
```json
{
  "query_type": "process_flow",
  "module": "QM",
  "industry": "Consumer Products",
  "specific_topic": "quality inspection for raw cashew using industry grading protocol — kernel outturn ratio, moisture analysis, defect counting, Certificate of Quality"
}
```

### Output
```json
{
  "results": [
    {
      "title": "Quality Inspection Process for Raw Cashew — Kernel Grading Protocol Integration",
      "category": "Process Flow",
      "sap_reference_id": "2QN (Quality in Procurement) + 2QP (Quality in Sales) + Certificate Management",
      "content": "Configure QM inspection plans aligned to industry raw-cashew grading standards. Process flow: (1) INSPECTION AT GOODS RECEIPT (raw cashew delivery): Visual inspection — nut color, defect screening. Characteristics: nut_color_score (1-5), foreign_matter (Y/N), insect_damage_pct. Usage decision: Accept/Reject/Downgrade. (2) INSPECTION AT PROCESSING STAGE (post-shelling): Physical analysis — moisture content (target 6-8%), kernel outturn ratio (KOR, target 45-50 lbs kernel per 80kg raw), whole/broken kernel ratio, defect count per grading standard. Characteristics: moisture_pct (num), outturn_ratio (num), whole_kernel_pct (num), defect_score (calculated). (3) GRADING EVALUATION (pre-export): Industry grading form — kernel count per lb, color grade, breakage assessment, scorched/spotted defect classification. Grading_total_score (num, target premium tier for HHE's positioning). (4) CERTIFICATE OF QUALITY: Auto-generate Certificate of Quality (CoQ) from inspection results; attach to SD delivery as output document for buyer. Includes: lot number, origin region, moisture, outturn ratio, kernel grade, defect rate, inspector name/date.",
      "relevance_score": 0.95,
      "source": "SAP QM Best Practice adapted for Raw Cashew Grading Protocol",
      "applicability_notes": "QM is a revenue-critical module for HHE — premium-grade raw cashew commands higher pricing than commodity grade, and the quality documentation (CoQ) is what buyers pay the premium for. The grading evaluation inspection plan should be configured with HHE's quality lead during Explore phase. Consider maintaining outturn ratio and grade as batch characteristics (not just inspection results) so they are visible in SD for batch determination — this enables allocating highest-grade lots to highest-paying buyers. Integration: QM results post to batch classification → SD batch determination uses kernel_grade as selection criterion."
    }
  ],
  "metadata": {
    "query_type": "process_flow",
    "total_results": 1,
    "knowledge_currency": "Raw cashew grading standards as of 2025. QM configuration patterns are stable across S/4HANA releases.",
    "disclaimer": "Inspection plan configuration is highly client-specific. The grading protocol mapping to SAP QM characteristics should be validated with HHE's quality team during Explore phase Fit-to-Standard workshops."
  }
}
```

---

## Query 4: SAP GROW vs. RISE vs. Business One Decision for Mid-Market Agribusiness

### Input
```json
{
  "query_type": "sizing_guidance",
  "company_size": "midmarket",
  "deployment_model": "public_cloud",
  "specific_topic": "SAP Business One vs. S/4HANA Cloud Public Edition (GROW) for agricultural commodity exporter, ~65 employees, $900K-$3.1M revenue, 6 currencies, batch management required"
}
```

### Output
```json
{
  "results": [
    {
      "title": "SAP Product Selection: Business One vs. S/4HANA Cloud (GROW) for Mid-Market Agribusiness",
      "category": "Sizing Guidance",
      "sap_reference_id": "SAP GROW Program + SAP Business One Evaluation Criteria",
      "content": "Decision framework for HHE: OPTION A — SAP Business One (Cloud): Strengths: Purpose-built for SMBs with <500 employees and <$500M revenue. Lower TCO ($1,500-$3,500/user/year cloud subscription). Faster implementation (3-5 months). Includes core FI, purchasing, sales, inventory, basic production. Batch management available. Multi-currency supported. Weaknesses for HHE: Limited QM functionality (no industry grading-protocol-level inspection plans); no GTS module (traceability documentation would require third-party add-on); limited batch classification depth; no native BTP integration for mobile money; growth ceiling if HHE scales beyond mid-market. OPTION B — SAP S/4HANA Cloud Public Edition via GROW: Strengths: Full QM with inspection plans (critical for kernel grading); batch management with deep classification; path to GTS for traceability documentation; BTP integration for mobile money; no growth ceiling; SAP best practice scope items pre-configured. Weaknesses for HHE: Higher TCO ($3,000-$6,000/user/year GROW pricing, typically with minimum commitment); longer implementation (6-9 months); more complex for a 65-employee company; requires more change management investment. RECOMMENDATION: If HHE's growth plan materializes (7,000 farmers, increased container volume, enhanced traceability documentation required) — S/4HANA Cloud via GROW is the better long-term investment. If HHE wants lowest risk and fastest time-to-value — Business One with a plan to migrate when they outgrow it. KEY DECISION FACTOR: QM depth. If kernel grading and outturn-ratio documentation is truly a revenue differentiator (and selling premium raw cashew to specialty importers, it clearly is), then S/4HANA's QM module justifies the premium over Business One.",
      "relevance_score": 0.94,
      "source": "SAP GROW Program Criteria + SAP Business One Product Capabilities + Mid-Market Sizing Guidance",
      "applicability_notes": "This is a genuine edge case — HHE sits right at the boundary between Business One and S/4HANA. The QM requirement is the tiebreaker. Most 65-employee companies would go Business One. But HHE's premium cashew positioning makes quality management a core business capability, not an afterthought. Recommend presenting both options to Amina Cheyo and the investor with clear TCO comparison."
    }
  ],
  "metadata": {
    "query_type": "sizing_guidance",
    "total_results": 1,
    "knowledge_currency": "SAP GROW pricing and Business One capabilities as of early 2026. Pricing varies by region and partner — East Africa pricing may differ from published global rates.",
    "disclaimer": "Licensing and pricing must be validated with SAP or a certified partner. GROW program eligibility criteria and pricing are subject to change."
  }
}
```

---

## Query 5: Multi-Currency Configuration for 6 Currencies in East Africa

### Input
```json
{
  "query_type": "scope_items",
  "module": "FI",
  "specific_topic": "multi-currency configuration for East African exporter with 6 currencies (TZS local, USD primary export, EUR, CAD, KRW, INR)"
}
```

### Output
```json
{
  "results": [
    {
      "title": "Multi-Currency Financial Accounting for Agricultural Commodity Exporter",
      "category": "Scope Item + Configuration Pattern",
      "sap_reference_id": "1FC (General Ledger) + J58 (Foreign Currency Valuation) + 1YR (AR) + 1YS (AP)",
      "content": "Configure multi-currency for HHE: (1) COMPANY CODE CURRENCY: TZS (Tanzanian Shillings) — local reporting currency, tax currency. (2) PARALLEL CURRENCIES: Configure 2 parallel ledgers — Currency Type 10: TZS (local), Currency Type 30: USD (group reporting / primary export currency). This enables dual-currency financial statements without separate ledger maintenance. (3) EXCHANGE RATE TYPES: Maintain daily rates for all 6 currencies. Source: Bank of Tanzania (BOT) published rates for TZS pairs. Configure automatic exchange rate download from BOT or use SAP standard ECB rates for EUR-based crosses. (4) FOREIGN CURRENCY VALUATION (J58): Month-end FX revaluation of open items in AR (buyer receivables in USD/EUR/CAD/KRW/INR) and AP (farmer payables in TZS, supplier payables if any in foreign currency). (5) AR CONFIGURATION: Customer master data for each buyer with their invoice currency (Baltic Nut Traders=EUR, Meridian Food Import=KRW, Casa do Caju=EUR, Northgate Commodities=CAD, Sunrise Ingredients=INR, others=USD). (6) AP CONFIGURATION: Farmer vendor master data with payment currency TZS; mobile money payment method for disbursement. (7) CO-PA INTEGRATION: Profitability analysis in USD to enable cross-market margin comparison — margins calculated with consistent FX translation regardless of buyer invoice currency.",
      "relevance_score": 0.93,
      "source": "SAP Best Practice Scope Items 1FC + J58, adapted for Multi-Currency East African Exporter",
      "applicability_notes": "6 currencies is unusual for a 65-employee company and adds configuration complexity to FI. The parallel currency approach (TZS local + USD group) is the standard pattern. For the less common currencies (KRW, INR), consider whether HHE actually invoices in these currencies or if buyers pay in EUR/USD. If some buyers pay in EUR regardless of country, the active currency count may be lower than 6. Clarify during Explore phase."
    }
  ],
  "metadata": {
    "query_type": "scope_items",
    "total_results": 1,
    "knowledge_currency": "Multi-currency configuration is stable across S/4HANA releases. Bank of Tanzania exchange rate integration may require custom BTP integration if no standard connector exists.",
    "disclaimer": "Currency configuration and exchange rate management should be validated with HHE's accounting team and auditors during Explore phase."
  }
}
```

---

## Summary: Key Best Practices Applied to HHE

| Topic | Key Recommendation | SAP Reference |
|---|---|---|
| Batch Management | Auto-create batches at raw-cashew receipt with classification schema for origin, moisture, grade, outturn ratio | 1A2 + 1NM + Batch Config |
| Export Traceability | BTP side-by-side extension for geo-location capture + documentation generation (cheaper than full GTS) | BTP Extension Pattern |
| Quality Management | Map kernel grading protocol to QM inspection plans; outturn ratio as batch characteristic for SD batch determination | 2QN + 2QP + Certificate Mgmt |
| Product Sizing | S/4HANA Cloud GROW recommended over Business One — QM depth is the tiebreaker for premium raw cashew | GROW Program Criteria |
| Multi-Currency | TZS local + USD parallel currency; 6 currency pairs with BOT exchange rates; CO-PA in USD for cross-market margin analysis | 1FC + J58 |
| Mobile Money | BTP Integration Suite → provider API; Clean Core Level A compliant; trigger from FI-AP payment run | BTP Integration Pattern |
