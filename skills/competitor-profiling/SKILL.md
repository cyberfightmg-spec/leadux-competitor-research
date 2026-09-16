# Skill: Competitor Profiling

## Mission

Build a standardized, evidence-backed profile for a verified competitor so later skills can compare entities without mixing fact, marketing language and interpretation.

Use this skill primarily for Tier A and selected Tier B competitors.

Read first:

- `frameworks/evidence-protocol.md`
- `frameworks/source-quality.md`
- `frameworks/fallback-policy.md`
- `frameworks/output-contract.md`

## Input

```json
{
  "entity_id": "cmp_001",
  "name": "",
  "official_url": "",
  "competitor_type": "DIRECT|INDIRECT|SUBSTITUTE|DIY|ADJACENT",
  "target_market": "",
  "geography": [],
  "research_depth": "quick|standard|deep"
}
```

## Principle

A competitor profile must separate:

1. what the company publicly claims;
2. what can be independently observed;
3. what customers report;
4. what the researcher infers.

Never merge these into one narrative voice.

## Research dimensions

### 1. Identity

When relevant and publicly verifiable:

- brand;
- canonical domain;
- legal entity / identifiers;
- operating geography;
- product/service names;
- company status;
- founding/funding/team only when sourced.

Do not force unavailable corporate data into the profile.

### 2. Positioning

Capture first-party wording:

- homepage headline;
- subheadline;
- CTA;
- target audience statements;
- category label;
- promised outcome;
- proof elements;
- differentiation claims.

Then create a separate interpreted positioning object.

Example:

```json
{
  "claimed_positioning": {
    "headline": "",
    "target": "",
    "promise": ""
  },
  "interpreted_positioning": {
    "category": "",
    "primary_segment": "",
    "positioning_angle": "simplicity|price|performance|vertical|enterprise|other",
    "claim_ids": []
  }
}
```

### 3. Target customer / JTBD

Look for direct evidence from:

- website copy;
- case studies;
- customer logos;
- pricing/packaging;
- documentation;
- industry pages;
- reviews/customer stories.

Do not classify the ICP only from one headline if other evidence conflicts.

### 4. Product surface

Capture high-level product/workflow areas and pass detailed comparison to `product-intelligence`.

### 5. Pricing surface

Record whether public pricing is found and route detailed work to `pricing-intelligence`.

### 6. Customer evidence

Record available review/community source families and route interpretation to `customer-research` / `voice-of-customer`.

### 7. GTM footprint

Record observable channels and route performance interpretation to `gtm-intelligence`.

### 8. Strategic signals

Capture changelog, jobs, launches, partnerships and major public changes for `strategic-signals`.

## Source order

Prefer:

1. official website/docs/pricing;
2. official company/public registry information;
3. first-party changelog/case studies;
4. reputable review platforms/community sources;
5. reputable secondary sources;
6. weak aggregators only as discovery clues.

## Profile freshness

For time-sensitive dimensions record `observed_at`.

Current pricing/product positioning should not silently rely on stale cached pages.

## Strengths and weaknesses

Do not generate generic strengths/weaknesses automatically.

A strength/weakness is an **insight** that needs evidence.

Good:

> Customers repeatedly praise fast setup across three independent review sources; official onboarding also emphasizes same-day deployment.

Bad:

> Strength: good UX.

## Required output

Use the shared envelope plus:

```json
{
  "artifacts": {
    "profile": {
      "entity_id": "",
      "identity": {},
      "competitor_type": "",
      "positioning": {},
      "target_segments": [],
      "jtbd": [],
      "product_summary": {},
      "pricing_status": "public|partial|custom|not_found|unknown",
      "customer_evidence_available": [],
      "gtm_footprint": [],
      "strategic_signal_sources": [],
      "evidence_backed_strengths": [],
      "evidence_backed_weaknesses": [],
      "open_questions": []
    }
  }
}
```

## Quality checks

Before returning:

- verify the official domain;
- separate company claims from independent evidence;
- include dates for current offer/pricing observations;
- do not state revenue, customer count, market share or growth unless directly supported;
- do not infer internal CRM/processes from external website behavior;
- route unresolved contradictions to `contradiction-check`.
