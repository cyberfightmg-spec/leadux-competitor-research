---
name: content-performance-intelligence
description: >-
  Identify and normalize observable high-performing competitor and adjacent-creator content so downstream strategy can learn from repeated performance patterns without confusing visibility with business results.
metadata:
  version: 0.4.0
  category: competitor-content-intelligence
  evidence_mode: required
license: MIT
---

# Skill: Content Performance Intelligence

## Mission
Find content that materially overperforms each account's own normal baseline, decompose the reusable mechanism, and distinguish observable content performance from actual business outcomes.

This skill answers:

> What content appears to work unusually well for relevant competitors/adjacent experts, how repeatable is that pattern across accounts, and what exactly is observable versus assumed?

## Hard rule
Never treat raw views, likes, followers, or virality as proof of leads, sales, revenue, authority, or customer acquisition unless those business outcomes are independently evidenced.

## Candidate universe
Include when relevant:
- direct competitors;
- indirect competitors;
- category educators;
- founder-led experts serving the same buyer;
- adjacent creators with comparable audience/problem structure;
- substitutes with strong content-led distribution.

Do not only select the largest accounts.

## Baseline method
When enough comparable public posts exist for an account:

1. collect a defined recent sample;
2. preserve platform, format, date and observable metrics;
3. compute/estimate an account-local baseline using comparable posts;
4. calculate an outlier ratio only when numerator and baseline use comparable metrics;
5. record sample size and coverage limitations.

Preferred simple measure:

```text
outlier_multiplier = post_metric / account_baseline_metric
```

Use medians rather than means when a small number of viral posts would distort the baseline.

If baseline cannot be established, do not invent one. Mark `BASELINE_UNAVAILABLE`.

## Comparable-metric rule
Do not compare:
- Instagram views directly to LinkedIn reactions;
- YouTube long-form views directly to Shorts without qualification;
- old lifetime metrics to recent-window metrics without qualification;
- posts with hidden/private metrics as if zero;
- follower count as a substitute for reach.

## Decomposition
For meaningful outliers extract, when observable:
- topic;
- audience/problem;
- hook/opening pattern;
- angle / promise;
- format;
- duration/length;
- content structure;
- proof/evidence used;
- CTA type;
- visual pattern;
- emotional/tension mechanism;
- freshness/news dependency;
- comments/reaction themes when available;
- publication date;
- platform-native context.

## Pattern confidence
A reusable pattern becomes stronger when:
- it appears across multiple high-performing posts from one account;
- it repeats across multiple independent accounts;
- it persists across time rather than one viral event;
- it aligns with VOC/market evidence;
- first-party results later show a similar mechanism working for the target brand.

Classify:

```text
SINGLE_OUTLIER
REPEATED_ACCOUNT_PATTERN
CROSS_ACCOUNT_PATTERN
FIRST_PARTY_CONFIRMED_PATTERN
```

## Outcome evidence ladder
Keep these separate:

1. `CONTENT_SIGNAL` — views/reactions/comments/shares/saves etc.
2. `AUDIENCE_RESPONSE` — meaningful comment/request/switching/intent signals.
3. `LEAD_SIGNAL` — public or supplied evidence of inquiries/leads.
4. `BUSINESS_OUTCOME` — public or supplied evidence of revenue/customer/business result.

Never upgrade one level to another by inference alone.

## Anti-survivorship checks
- inspect ordinary and bottom performers, not only winners;
- note account size and posting frequency;
- look for paid/boosted disclosure when observable;
- account for news/event spikes;
- note collaborations/giveaways/celebrity effects;
- avoid claiming a hook caused performance when many variables changed.

## Output
Produce records conforming to:

`schemas/content-performance-pattern.schema.json`

Also report:
- sample definition;
- accounts analyzed;
- platform/metric limitations;
- repeated pattern candidates;
- contradictions;
- confidence;
- what downstream Strategist may test versus what it should not copy.

## Strategy handoff
When downstream strategy is requested, include content performance patterns in the `strategy-handoff` package.

The downstream Strategist must still test founder fit, brand fit, audience fit and transfer assumptions before using any pattern.
