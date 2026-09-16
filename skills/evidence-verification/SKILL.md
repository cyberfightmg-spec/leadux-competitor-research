---
name: evidence-verification
description: Performs a verification pass over high-impact claims, numbers, sources, classifications and conclusions.
---

# Evidence Verification

## Verify high-impact claims first
Prioritize claims that affect:
- strongest/most dangerous competitor;
- pricing conclusions;
- customer pain prevalence;
- whitespace recommendations;
- strategic direction;
- final recommendations.

## Checks
1. Source URL exists and supports the exact claim.
2. Source date/freshness is appropriate.
3. Claim scope matches geography/segment/product version.
4. Numeric claims have provenance/calculation trace.
5. Corroborating sources are independent.
6. Hypotheses are not phrased as facts.
7. `NOT_FOUND` is not converted to absence.
8. Quotes are faithful and minimal.
9. Contradictions are surfaced.

## Output
Verification status per major claim: `VERIFIED`, `PARTIALLY_VERIFIED`, `UNVERIFIED`, `CONTRADICTED`, with notes and required follow-up.
