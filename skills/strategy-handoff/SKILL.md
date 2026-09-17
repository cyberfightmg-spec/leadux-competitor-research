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

This skill is the formal boundary between:

```text
RESEARCHER → STRATEGIST
```

The researcher packages evidence. It does not decide content pillars, channels, formats, cadence, hooks, creator angles, or publishing tactics.

## Required preconditions

For `deep` / full research, run the normal final gates first:

```text
contradiction-check
→ evidence-verification
→ red-team
→ synthesis
→ strategy-handoff
```

If `integrity_status = INSUFFICIENT_EVIDENCE`, export may still occur for diagnosis, but the handoff must preserve that status and must not imply strategy readiness.

## Required inputs

Preserve stable upstream IDs and include the decision-relevant subset of:

- research run metadata;
- verified and limited claims;
- insights;
- market opportunities;
- VOC records and themes;
- strategic signals;
- GTM/content-footprint artifacts;
- contradictions;
- material data gaps;
- observation/freshness dates where available.

## Evidence preservation rules

1. Do not flatten stable IDs into prose.
2. Do not rewrite `HYPOTHESIS` or `ASSUMPTION` as `FACT`.
3. Do not use a `CONTRADICTED`, `STALE`, `MISCLASSIFIED`, or `INSUFFICIENT_SOURCE` claim as if it were clean verified evidence.
4. Do not remove contradicting claims merely because they complicate downstream strategy.
5. Preserve geography, time period, target segment and population qualifiers where available.
6. Preserve `UNKNOWN` / data gaps instead of filling them with plausible values.
7. Do not add recommendations that were not already research outputs.

## Selection policy

A strategy handoff is not required to include every artifact produced during research. It must include every artifact that could materially change the downstream content or positioning decision.

If an artifact type is omitted, record the omission in `handoff.omitted_artifact_types` and explain selection logic in `handoff.selection_notes`.

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
- `handoff.selection_notes`;
- `handoff.omitted_artifact_types`.

## Quality checks

Before export, verify:

- every included insight reference resolves to an included claim or is explicitly documented as omitted;
- every included market opportunity keeps its original supporting/contradicting claim IDs;
- stable IDs are unchanged;
- freshness dates are preserved where available;
- package integrity status matches the research run;
- contradictions and high-impact gaps remain visible;
- no content-strategy recommendation was invented during packaging.

## Handoff readiness

Use these downstream meanings:

- `VERIFIED` → normal strategy work may proceed;
- `VERIFIED_WITH_GAPS` → strategy may proceed, but gap-sensitive decisions must be labeled or tested;
- `DEGRADED` → only limited strategy / experiments should proceed unless the user explicitly accepts the risk;
- `INSUFFICIENT_EVIDENCE` → route missing questions back to research before making core strategy decisions.

## Boundary

The output of this skill is **evidence**, not a content strategy.

The next system owns:

```text
brand/business context
+ research package
+ first-party performance
+ proven strategy patterns
→ strategic choices
```
