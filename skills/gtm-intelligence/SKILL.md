# Skill: GTM Intelligence

## Mission

Map how competitors appear to reach, educate, convert and retain customers using observable public evidence.

Do not confuse channel presence with channel effectiveness.

Read first:

- `frameworks/evidence-protocol.md`
- `frameworks/search-strategy.md`
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

## Observable GTM dimensions

Investigate where relevant:

- SEO / organic search;
- paid search / paid social;
- content marketing;
- YouTube/video;
- social channels;
- communities;
- partnerships;
- affiliates/referrals;
- marketplaces/directories;
- events/webinars;
- outbound signals;
- product-led growth;
- sales-led motion;
- free tools/templates;
- lead magnets;
- trials/demos;
- case-study/social proof strategy;
- local distribution/maps;
- channel/reseller strategy.

## Evidence levels

### Presence evidence

The competitor demonstrably uses a channel.

### Activity evidence

The competitor publishes/runs observable activity with some cadence.

### Traction proxy

Observable third-party or platform signals suggest attention/visibility.

### Performance evidence

Direct evidence ties the channel to outcomes.

Do not collapse these levels.

Example:

> Competitor publishes weekly YouTube videos — FACT.

> YouTube is their main acquisition channel — HYPOTHESIS unless direct evidence exists.

## Content footprint

Capture:

- topic clusters;
- content formats;
- target funnel stage;
- cadence;
- recurring CTAs;
- case-study density;
- comparison/alternative pages;
- programmatic/SEO patterns;
- language/geographic localization.

Do not use raw post volume as proof of effectiveness.

## SEO intelligence

If SEO data tools are available, capture separately:

- ranking keyword overlap;
- branded vs non-branded visibility;
- top landing-page categories;
- backlink/referring-domain signals;
- category/search-intent coverage.

If SEO tools are unavailable, use public/search observations only and mark coverage limitations.

Do not fabricate traffic estimates.

## Paid advertising

Use official/public ad libraries or observable ad evidence when available.

Do not infer budget/spend unless a reliable source directly provides it.

## Sales motion

Observable clues may include:

- demo CTA;
- contact-sales gating;
- self-serve signup;
- trial;
- enterprise pages;
- SDR/AE vacancies;
- partner/reseller pages.

These are signals. “Sales-led” or “PLG” classifications should include evidence and confidence.

## Channel whitespace

A channel gap requires both:

1. evidence the target audience is present/active there;
2. evidence competitor coverage is comparatively weak.

Absence of competitor visibility alone is not an opportunity.

## Required output

Use the shared envelope plus:

```json
{
  "artifacts": {
    "channel_matrix": [],
    "content_footprint": [],
    "sales_motion": [],
    "seo_signals": [],
    "paid_signals": [],
    "partnership_signals": [],
    "channel_whitespace_hypotheses": [],
    "performance_unknowns": []
  }
}
```

## Quality rules

- presence ≠ performance;
- follower/subscriber count ≠ customer count;
- search visibility ≠ market share;
- vacancy count ≠ sales success;
- content volume ≠ demand;
- label proxy metrics explicitly;
- keep paid/API-derived metrics separate from directly observed facts;
- use evidence verification for any GTM conclusion that materially drives a recommendation.
