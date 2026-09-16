---
name: contradiction-check
description: Detects conflicting values, source disagreements, stale evidence and mismatched scope before synthesis.
---

# Contradiction Check

Search the claim set for:
- different current prices for the same plan;
- conflicting feature availability;
- company claims vs customer reports;
- date/version mismatch;
- geography mismatch;
- different entities with similar names;
- estimates derived from the same upstream source;
- claims that changed over time.

## Resolution
Do not silently choose or average. Prefer current primary evidence where appropriate, document unresolved contradictions, and lower confidence when needed.

## Output
`conflict_id`, affected claim IDs, likely cause, resolution status, preferred claim if justified, and confidence impact.
