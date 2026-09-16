# Skill: Market Monitoring

## Mission

Turn a completed competitor study into a repeatable watchlist that detects meaningful market changes without flooding the user with noise.

This skill defines what to monitor, how to compare snapshots, how to classify changes and when a change is important enough to surface.

Read first:

- `frameworks/evidence-protocol.md`
- `frameworks/fallback-policy.md`
- `frameworks/output-contract.md`

## Input

```json
{
  "research_id": "",
  "tier_a_competitors": [],
  "tier_b_competitors": [],
  "important_claims": [],
  "watch_dimensions": [],
  "baseline_snapshots": []
}
```

## Default watch dimensions

For Tier A competitors, monitor where relevant:

- homepage positioning;
- pricing/packaging;
- product/feature pages;
- changelog/release notes;
- integrations;
- jobs/careers;
- case studies/customer pages;
- official announcements;
- public regulatory/company events;
- review/VOC theme shifts.

For Tier B, use lighter monitoring unless a signal increases relevance.

## Snapshot rule

Preserve dated snapshots or structured observations.

Do not compare only final summaries. Monitoring should be able to answer:

```text
What changed?
From what?
To what?
When observed?
Which source proves it?
Why might it matter?
```

## Raw change vs meaningful event

A DOM/text diff is not automatically a market event.

Ignore or de-prioritize:

- cosmetic design changes;
- tracking code;
- rotating testimonials;
- timestamps/session content;
- minor wording with no semantic change.

Promote changes such as:

- price/tier change;
- category/positioning shift;
- new target segment;
- major product launch;
- new integration cluster;
- market/geography expansion signal;
- material partnership;
- major hiring pattern;
- shutdown/deprecation;
- repeated customer-theme shift.

## Event schema

```json
{
  "event_id": "evt_001",
  "entity_id": "",
  "type": "pricing|positioning|product|integration|hiring|partnership|regulation|voc|other",
  "old_value": null,
  "new_value": null,
  "detected_at": "",
  "source_ids": [],
  "claim_ids": [],
  "importance": "high|medium|low",
  "confidence": "high|medium|low",
  "interpretation": "",
  "interpretation_class": "FACT|HYPOTHESIS",
  "alternative_explanations": []
}
```

## Importance test

A change is more important when it materially affects:

- target segment overlap;
- price/value positioning;
- product differentiation;
- distribution advantage;
- entry barriers;
- regulatory feasibility;
- a current strategic recommendation.

Do not use social engagement alone as an importance score.

## Alert policy

Surface only events that are either:

- objectively material to the research thesis; or
- specifically requested in the watchlist.

Group related small changes into one event where appropriate.

Example:

```text
Observed:
- Enterprise page added
- SSO launched
- 3 enterprise sales roles advertised

Interpretation:
Possible increased enterprise focus.

Class: HYPOTHESIS
Confidence: Medium
```

## Re-baselining

When an event is verified:

1. preserve the old snapshot;
2. create the new snapshot;
3. update affected claims;
4. identify affected insights/recommendations;
5. re-run contradiction/evidence checks if the change can alter the strategic thesis.

## Required output

Use the shared envelope plus:

```json
{
  "artifacts": {
    "watchlist": [],
    "events": [],
    "ignored_noise": [],
    "claims_to_reverify": [],
    "recommendations_potentially_affected": []
  }
}
```

## Quality rules

- monitoring failure must not be reported as “no changes”;
- a source becoming inaccessible is a monitoring/data-quality event, not a market event;
- never infer motive from a change without evidence;
- current pricing changes require primary-source verification when possible;
- preserve historical values instead of overwriting them.
