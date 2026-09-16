# Skill: Strategic Signals

## Mission

Detect meaningful competitor and market changes from public evidence without turning every announcement, vacancy or content post into a strategic conclusion.

Read first:

- `frameworks/evidence-protocol.md`
- `frameworks/fallback-policy.md`
- `frameworks/output-contract.md`

## Input

```json
{
  "competitors": [],
  "market": "",
  "geography": [],
  "baseline_snapshots": [],
  "research_depth": "quick|standard|deep"
}
```

## Signal categories

Track where relevant:

- pricing changes;
- packaging changes;
- positioning changes;
- new product/features;
- integrations;
- new vertical pages;
- new geography/language;
- partnerships;
- acquisitions/funding;
- leadership changes;
- hiring patterns;
- product/release velocity;
- customer/logo/case-study changes;
- regulatory events;
- shutdown/deprecation;
- major complaint/theme shifts.

## Evidence hierarchy

Prefer:

1. official changelog/release notes/pricing/docs;
2. official company announcements;
3. official registries/filings where relevant;
4. public job listings;
5. reliable media reporting;
6. community/review signals for customer-side changes.

## Signal vs interpretation

Always separate:

```text
OBSERVED SIGNAL
↓
POSSIBLE INTERPRETATION
↓
CONFIDENCE
↓
ALTERNATIVE EXPLANATIONS
```

Example:

Observed:

- three enterprise sales roles advertised;
- SSO launched;
- enterprise page added.

Possible interpretation:

> The company may be increasing focus on enterprise customers.

Classification: `HYPOTHESIS`, not FACT.

## Hiring analysis

Classify public roles when relevant:

- engineering;
- AI/data;
- sales;
- enterprise;
- marketing/content;
- customer success/support;
- partnerships;
- international/local expansion.

A job posting proves only that the role is/was advertised. It does not prove growth, headcount, hiring completion or profitability.

## Product velocity

Use public dated release evidence.

Track:

- release cadence;
- major vs minor changes;
- recurring strategic themes;
- integration velocity;
- AI/automation emphasis;
- enterprise/control additions;
- deprecated functionality.

Do not compare velocity across competitors when changelog visibility differs without stating that limitation.

## Change detection

When baseline snapshots exist:

1. detect raw changes;
2. remove cosmetic/noise changes;
3. classify meaningful change type;
4. verify using current primary source;
5. assess strategic implication;
6. record alternative explanations.

## Signal importance

Score dimensions separately rather than using arbitrary “high impact” language:

- relevance to target segment;
- magnitude of change;
- evidence directness;
- persistence (one-off vs repeated);
- strategic consequence;
- confidence.

## Required output

Use the shared envelope plus:

```json
{
  "artifacts": {
    "signals": [
      {
        "type": "pricing|product|positioning|hiring|partnership|funding|regulation|other",
        "entity_id": "",
        "observed_change": "",
        "observed_at": "",
        "supporting_claim_ids": [],
        "interpretation": "",
        "interpretation_class": "FACT|HYPOTHESIS",
        "alternative_explanations": [],
        "confidence": "high|medium|low"
      }
    ],
    "strategic_patterns": [],
    "unverified_signals": []
  }
}
```

## Quality rules

- do not equate activity with success;
- do not infer funding amount from vague announcements;
- do not infer expansion success from localization/landing pages;
- do not infer customer growth from logo additions alone;
- do not treat a single vacancy as a hiring trend;
- use dates aggressively because strategic signals decay quickly;
- route conflicting signals through `contradiction-check`.
