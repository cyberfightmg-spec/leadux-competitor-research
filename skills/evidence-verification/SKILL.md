# Skill: Evidence Verification

## Mission

Audit material claims before strategic synthesis. Verify provenance, source quality, freshness, scope match, geographic match, calculation trace and independence.

This skill is a quality-control layer, not a rewriting step.

Read first:

- `frameworks/evidence-protocol.md`
- `frameworks/source-quality.md`
- `frameworks/output-contract.md`
- `frameworks/quality-gates.md`
- `frameworks/regional-intelligence.md` when regional analysis is active.

## Input

```json
{
  "claims": [],
  "sources": [],
  "insights": [],
  "high_impact_claim_ids": [],
  "contradictions": [],
  "regional_analysis": null
}
```

## Verification priority

Verify strongest first:

1. claims that directly change the recommendation;
2. current pricing/product availability;
3. competitor classification;
4. geographic role / service-coverage claims;
5. market-gap and regional-whitespace claims;
6. material numbers/calculations;
7. claims repeated prominently in the report;
8. lower-impact descriptive facts.

## Verification checklist

### Provenance

- Does the claim point to a traceable source?
- Can the source actually be opened/identified?
- Does the cited source contain evidence for the claim?

### Evidence class

- Is it correctly labeled `FACT`, `ESTIMATE`, `HYPOTHESIS`, `ASSUMPTION` or `NOT_FOUND`?
- Has an estimate been presented as a fact?
- Has a marketing claim been presented as independently verified?

### Scope

Check:

- entity;
- product/tier;
- geography;
- time period;
- customer segment;
- unit/currency;
- metric definition.

Do not allow evidence from one city/region to silently support a national claim.

### Geographic verification

When regional analysis is active, explicitly verify:

```text
registered_region
headquarters
physical_locations
service_regions
verified_regions
geographic_role
```

Rules:

- registration address is not service coverage;
- one branch does not prove region-wide strength;
- online availability does not automatically prove national market relevance;
- national visibility does not prove local leadership;
- a geographic role must be supported by presence/service evidence.

### Regional counts

If the report says a region has `N` competitors, verify what `N` actually means.

Valid wording may be:

> N relevant competitors discovered in checked source/query families.

Do not validate it as a total-market count unless an authoritative population source supports that interpretation.

### Regional pricing

Verify:

- offers are genuinely comparable;
- sample size is stated;
- raw observations exist;
- min/max/median calculations are reproducible;
- currency/unit/tax context match;
- date range is explicit;
- convenience sample is not presented as a population average.

### Regional VOC

Verify:

- location attribution is supported;
- sample size is visible;
- source/entity diversity is known;
- tiny samples are not converted to percentages or region-wide claims;
- `INSUFFICIENT_REGIONAL_SAMPLE` is used when appropriate.

### Regional whitespace

A geography-specific opportunity must have evidence for:

```text
regional demand
+
weak/different competitor coverage
+
entry feasibility
```

Low discovered competitor count alone does not pass verification.

### Freshness

For time-sensitive claims, verify the evidence is current enough for the decision. A stale but accurate historical claim should be labeled historical, not current.

### Source quality

Evaluate separately:

- reliability/directness;
- relevance to the claim;
- freshness;
- independence.

A high-authority source can still be irrelevant to a specific claim.

### Independence

Check whether apparent corroboration comes from the same original press release/report/data source.

Regional sources also require diversity: ten map listings from one platform do not equal ten independent source families.

### Numbers

For direct numbers:

- source contains the number;
- units match;
- period matches;
- geography matches;
- currency/tax context is understood when material.

For calculations:

- formula is explicit;
- input claim IDs exist;
- arithmetic is reproducible;
- assumptions are labeled;
- no hidden multiplier or unit conversion exists.

### NOT_FOUND

Require a documented search space:

- queries/source families checked;
- geography checked;
- observation date;
- relevant access limitations.

One failed national or regional search does not pass verification.

## Verification statuses

Use:

```text
VERIFIED
VERIFIED_WITH_LIMITATIONS
UNVERIFIED
CONTRADICTED
STALE
MISCLASSIFIED
INSUFFICIENT_SOURCE
```

## Required output

Use the shared envelope plus:

```json
{
  "artifacts": {
    "verification_results": [
      {
        "claim_id": "",
        "status": "VERIFIED|VERIFIED_WITH_LIMITATIONS|UNVERIFIED|CONTRADICTED|STALE|MISCLASSIFIED|INSUFFICIENT_SOURCE",
        "checks": [],
        "problems": [],
        "corrected_class": null,
        "replacement_claim": null,
        "confidence": "high|medium|low",
        "notes": ""
      }
    ],
    "verified_high_impact_claims": [],
    "failed_high_impact_claims": [],
    "unsupported_numbers": [],
    "geographic_scope_mismatches": [],
    "regional_sample_issues": [],
    "source_independence_issues": [],
    "required_report_corrections": []
  }
}
```

## Publication rules

A high-impact claim that is `UNVERIFIED`, `CONTRADICTED` or `INSUFFICIENT_SOURCE` must not be presented as settled fact.

A geography-specific recommendation must not be published as high-confidence when its supporting evidence comes mainly from another geography.

Options:

- remove it;
- downgrade it to hypothesis/assumption;
- narrow its geographic scope;
- show the contradiction/gap;
- run targeted validation.

## Quality rules

- do not verify a claim by finding another article that copied the same source;
- do not accept search snippets alone for high-impact facts when direct source verification is possible;
- do not validate arithmetic without checking input definitions;
- do not let polished prose override weak evidence;
- do not generalize capital-city evidence to the whole country silently;
- do not confuse legal registration with operational/service geography;
- preserve failed verification in the audit trail.
