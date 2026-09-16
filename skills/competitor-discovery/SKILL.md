# Skill: Competitor Discovery

## Mission

Discover the real competitive set for the customer's job-to-be-done, not just the most visible brands in the category.

This skill must find and classify:

- direct competitors;
- indirect competitors;
- substitutes;
- DIY/manual alternatives;
- adjacent solutions.

Read first:

- `frameworks/competitor-taxonomy.md`
- `frameworks/search-strategy.md`
- `frameworks/fallback-policy.md`
- `frameworks/output-contract.md`

Load the relevant geographic source pack when available.

## Input

```json
{
  "market_definition": "",
  "customer_job": "",
  "target_customer": "",
  "geography": [],
  "search_vocabulary": [],
  "known_competitors": [],
  "research_depth": "quick|standard|deep"
}
```

## Core rule

Do not answer “who are the competitors?” by searching only the formal category name.

The same customer budget may go to:

- specialist software;
- general software;
- agencies/services;
- spreadsheets;
- messengers;
- manual labor;
- internal development;
- marketplace/platform tools;
- adjacent products that absorb the same workflow.

## Discovery process

### 1. Seed expansion

Build candidate terms from:

- category names;
- buyer/problem language;
- JTBD;
- known brands;
- alternatives language;
- local-language variants;
- product-review vocabulary;
- marketplace/directory categories.

### 2. Run independent discovery families

Use as many as are relevant and available:

#### Category search

Find products explicitly describing themselves as part of the category.

#### Problem/JTBD search

Find products/services customers use to solve the underlying job without using the category term.

#### Alternative search

Use known competitors to discover “alternatives”, “analogs”, comparison pages and switching discussions.

#### Customer-language search

Look for “what do you use for…”, “how do you handle…”, “recommend…”, “instead of…”, reviews and community discussions.

#### Directory / marketplace / app discovery

Use relevant public directories, app stores, maps, marketplaces or industry catalogs when applicable.

#### SEO/content neighborhood

Where available, identify entities repeatedly appearing around the same problem/category queries. Treat visibility as discovery evidence only, not market-share evidence.

#### Registry/domain discovery

For markets/geographies where official/public company sources help, use them to verify entity identity or uncover relevant operators.

### 3. Verify entity identity

For every serious candidate, verify when possible:

- canonical brand name;
- official domain;
- geography;
- actual product/service;
- target segment;
- whether the company/product is active as of the research date.

Do not merge entities solely by similar names.

### 4. Classify competitor type

Use the taxonomy:

```text
DIRECT
INDIRECT
SUBSTITUTE
DIY
ADJACENT
```

Classification should be based on overlap in customer, JTBD and budget, not marketing category alone.

### 5. Score relevance

Use an explainable overlap model. Suggested dimensions:

```text
JTBD overlap          25
Target-customer       25
Geography             15
Product/workflow      15
Price/budget overlap  10
Distribution context   5
Market relevance       5
```

The exact weights may be adapted to the market, but changes must be explicit.

Do not confuse relevance score with company quality or market strength.

### 6. Assign depth tier

```text
Tier A — highest decision relevance; deep profile
Tier B — meaningful competitor; medium profile
Tier C — map-level context
```

Tiering should be relative to the research question, not brand fame.

### 7. Run gap searches

Before stopping, ask:

- Did we discover at least one non-obvious substitute where one plausibly exists?
- Are local/regional players missing?
- Did English-only or Russian-only search hide competitors?
- Are service/manual alternatives missing?
- Are category comparison pages over-weighting SEO-heavy vendors?

### 8. Saturation

Discovery approaches saturation when two consecutive waves produce few new high-relevance entities and no new competitor type.

If the market appears unusually sparse, run a deliberate “false whitespace” search before concluding that competition is low.

## Negative evidence

Never say:

> There are no competitors.

unless the claim has an extraordinarily strong, explicitly bounded basis.

Prefer:

> No additional direct competitors were found in the source/query families checked as of DATE; indirect and substitute solutions remain listed separately.

## Required output

Use the shared envelope plus:

```json
{
  "artifacts": {
    "candidate_count": 0,
    "competitors": [
      {
        "entity_id": "cmp_001",
        "name": "",
        "official_url": "",
        "type": "DIRECT|INDIRECT|SUBSTITUTE|DIY|ADJACENT",
        "relevance_score": 0,
        "classification_confidence": "high|medium|low",
        "reason": "",
        "tier": "A|B|C",
        "source_ids": []
      }
    ],
    "search_families_used": [],
    "saturation_notes": "",
    "missing_competitor_types": []
  }
}
```

## Quality checks

Before returning:

- remove duplicate entities;
- separate brands from legal entities where relevant;
- verify official domains for Tier A;
- explain every Tier A classification;
- flag uncertain/inactive candidates;
- keep weak candidates out of the deep-analysis queue.
