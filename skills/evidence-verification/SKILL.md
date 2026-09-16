# Skill: Evidence Verification

## Mission

Audit material claims before strategic synthesis. Verify provenance, source quality, freshness, scope match, calculation trace and independence.

This skill is a quality-control layer, not a rewriting step.

Read first:

- `frameworks/evidence-protocol.md`
- `frameworks/source-quality.md`
- `frameworks/output-contract.md`
- `frameworks/quality-gates.md`

## Input

```json
{
  "claims": [],
  "sources": [],
  "insights": [],
  "high_impact_claim_ids": [],
  "contradictions": []
}
```

## Verification priority

Verify strongest first:

1. claims that directly change the recommendation;
2. current pricing/product availability;
3. competitor classification;
4. market-gap claims;
5. material numbers/calculations;
6. claims repeated prominently in the report;
7. lower-impact descriptive facts.

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

### Numbers

For direct numbers:

- source contains the number;
- units match;
- period matches;
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
- observation date;
- relevant access limitations.

One failed search does not pass verification.

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
    "source_independence_issues": [],
    "required_report_corrections": []
  }
}
```

## Publication rules

A high-impact claim that is `UNVERIFIED`, `CONTRADICTED` or `INSUFFICIENT_SOURCE` must not be presented as settled fact.

Options:

- remove it;
- downgrade it to hypothesis/assumption;
- show the contradiction/gap;
- run targeted validation.

## Quality rules

- do not “verify” a claim by finding another article that copied the same source;
- do not accept search snippets alone for high-impact facts when direct source verification is possible;
- do not validate arithmetic without checking input definitions;
- do not let polished prose override weak evidence;
- preserve failed verification in the audit trail.
