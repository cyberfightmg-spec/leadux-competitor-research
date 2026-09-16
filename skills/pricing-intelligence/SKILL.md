# Skill: Pricing Intelligence

## Mission

Build a current, comparable view of competitor pricing and packaging, then identify evidence-backed pricing gaps without inventing unit economics or willingness-to-pay.

Read first:

- `frameworks/evidence-protocol.md`
- `frameworks/fallback-policy.md`
- `frameworks/output-contract.md`

## Input

```json
{
  "competitors": [],
  "target_customer": "",
  "geography": [],
  "research_depth": "quick|standard|deep"
}
```

## Research dimensions

For each relevant competitor capture when publicly available:

- pricing model;
- plan/tier names;
- entry price;
- recurring period;
- currency;
- tax/VAT context when material and known;
- usage/seat/account/location limits;
- value metric;
- included features;
- feature gating;
- free plan;
- trial;
- annual discount;
- onboarding/setup fees;
- implementation/services fees;
- overages;
- custom/enterprise pricing;
- cancellation/commitment terms when clearly public.

## Preferred evidence order

1. official pricing page;
2. official public offer / terms / billing docs;
3. official sales/product documentation;
4. official marketplace/app listing;
5. archived/historical snapshots when explicitly analyzing change;
6. reputable secondary source only as fallback.

Do not use an old review/blog as the current price without verification.

## Observation contract

Every price observation should include:

```json
{
  "competitor": "",
  "plan": "",
  "amount": null,
  "currency": "",
  "period": "month|year|one_time|usage|custom|unknown",
  "unit": "seat|account|location|usage|other|unknown",
  "tax_context": "",
  "observed_at": "YYYY-MM-DD",
  "source_id": "",
  "status": "verified|partial|historical|unknown"
}
```

## Normalization

Normalize only when mathematically legitimate.

Examples:

- annual price → monthly equivalent, while preserving the annual commitment;
- per-seat price → do not compare directly with per-location price without a scenario;
- usage pricing → compare at explicit usage scenarios, not one arbitrary number.

Keep original observations alongside normalized scenarios.

## Pricing model classification

Possible models:

- flat subscription;
- per seat;
- per account/workspace;
- per location;
- usage/consumption;
- transaction/revenue share;
- freemium;
- one-time/license;
- implementation/project;
- custom/enterprise;
- hybrid.

## Packaging analysis

Analyze:

- entry friction;
- value metric;
- feature gates;
- tier jumps;
- limits;
- enterprise gates;
- annual incentives;
- bundling;
- obvious decoy/anchoring structure when evidenced.

Do not claim pricing psychology as fact; treat interpretation as hypothesis.

## Price-gap analysis

A gap is not simply “nobody has a $49 plan.”

Test whether:

1. the target segment exists;
2. the segment has a different usage/value profile;
3. current competitors poorly cover the segment;
4. there is some evidence of willingness to pay or budget;
5. lower pricing would not obviously destroy the delivery model.

If economics are unknown, keep the gap as a hypothesis.

## Historical pricing

When snapshots exist, record:

```text
old plan → new plan
old price → new price
packaging changes
observed dates
```

Do not infer why the company changed pricing unless supported.

## Required output

Use the shared envelope plus:

```json
{
  "artifacts": {
    "price_observations": [],
    "normalized_scenarios": [],
    "packaging_comparison": [],
    "value_metrics": [],
    "public_pricing_missing": [],
    "historical_changes": [],
    "pricing_gap_hypotheses": []
  }
}
```

## Quality rules

- current public price claims should preferably be observed within 30 days;
- preserve currency and billing period;
- do not compare incomparable units without explicit scenarios;
- custom pricing means `custom/unknown`, not zero;
- “contact sales” is not evidence of high price;
- do not infer margins, CAC or willingness-to-pay from list price alone;
- verify material price conclusions before final synthesis.
