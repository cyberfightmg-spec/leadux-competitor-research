---
name: strategy-handoff
description: >-
  Export a verified LeadUX Competitor Research run into the normalized evidence package consumed by LeadUX Content Strategist without changing upstream evidence semantics.
metadata:
  version: 0.4.0
  category: research-integration
  evidence_mode: required
license: MIT
---

# Skill: Strategy Handoff

## Mission
Export a strategy-ready evidence package from a completed LeadUX Competitor Research run without reinterpreting, upgrading, simplifying, or cleaning away inconvenient evidence.

This skill is the formal boundary:

```text
RESEARCHER → STRATEGIST
```

The researcher packages evidence. It does not decide content pillars, channels, formats, cadence, hooks, creator angles, or publishing tactics.

## Required preconditions
For `deep` / full research, run:

```text
contradiction-check
→ evidence-verification
→ red-team
→ synthesis
→ strategy-handoff
```

If `integrity_status = INSUFFICIENT_EVIDENCE`, export may still occur for diagnosis, but preserve that status exactly.

## Required inputs
Preserve stable upstream IDs and include the decision-relevant subset of:

- research run metadata;
- verified and limited claims;
- insights;
- market opportunities;
- VOC records/themes;
- strategic signals;
- GTM/content-footprint artifacts;
- **content-performance patterns and normalized outliers**;
- contradictions;
- material data gaps;
- observation/freshness dates.

## Evidence preservation rules
1. Do not flatten stable IDs into prose.
2. Do not rewrite `HYPOTHESIS` or `ASSUMPTION` as `FACT`.
3. Do not use `CONTRADICTED`, `STALE`, `MISCLASSIFIED`, or `INSUFFICIENT_SOURCE` claims as clean evidence.
4. Do not remove contradicting claims because they complicate downstream strategy.
5. Preserve geography, time period, target segment and population qualifiers.
6. Preserve `UNKNOWN` / data gaps.
7. Do not add recommendations that were not research outputs.
8. Preserve content-performance evidence level exactly: `CONTENT_SIGNAL`, `AUDIENCE_RESPONSE`, `LEAD_SIGNAL`, or `BUSINESS_OUTCOME`.
9. Preserve account-local baseline/sample limitations for performance patterns.

## Selection policy
A handoff need not include every artifact, but it must include every artifact that could materially change downstream strategy.

If an artifact type is omitted, record it in `handoff.omitted_artifact_types` and explain selection logic.

## Output
Produce one JSON object conforming to:

`schemas/strategy-handoff.schema.json`

Populate at minimum:
- `research_package_id`;
- `research_run`;
- `claims`;
- `insights`;
- `integrity_status`;
- `handoff.generated_at`;
- `handoff.producer_version`;
- `handoff.target_system = leadux-content-strategist`;
- `handoff.selection_notes`;
- `handoff.omitted_artifact_types`.

## Quality checks
Before export verify:
- included insight references resolve to included claims or are explicitly omitted;
- market opportunities preserve original support/contradiction IDs;
- content-performance patterns preserve baseline/sample/evidence-level limitations;
- stable IDs are unchanged;
- freshness dates are preserved;
- integrity status matches the research run;
- contradictions/high-impact gaps remain visible;
- no content-strategy recommendation was invented during packaging.

## Handoff readiness
- `VERIFIED` → normal strategy work may proceed.
- `VERIFIED_WITH_GAPS` → proceed with gap-sensitive decisions labeled/tested.
- `DEGRADED` → limited strategy/experiments only unless risk is explicitly accepted.
- `INSUFFICIENT_EVIDENCE` → route missing questions back to research before core strategy decisions.

## Boundary
The output of this skill is evidence, not strategy.

The next system owns:

```text
Founder/Brand Context
+ research package
+ validated strategy patterns
+ first-party performance
→ strategic choices
```
