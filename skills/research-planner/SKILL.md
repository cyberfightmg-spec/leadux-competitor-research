# Skill: Research Planner

## Mission

Convert an ambiguous market/competitor request into an executable research plan with explicit questions, scope, geographic structure, source strategy, skill routing, budgets, stop conditions and verification requirements.

Do not research the market deeply in this skill. Plan the work so downstream skills know exactly what must be established.

Read first:

- `frameworks/search-strategy.md`
- `frameworks/fallback-policy.md`
- `frameworks/output-contract.md`
- `frameworks/research-depth.md`
- `frameworks/regional-intelligence.md` when geography may be material.

If geography includes Russia, also read `source-packs/russia.md`.

## Input

```json
{
  "research_goal": "",
  "market": "",
  "geography": [],
  "target_customer": "",
  "jtbd": "",
  "known_competitors": [],
  "focus": [],
  "research_depth": "quick|standard|deep",
  "available_capabilities": []
}
```

Unknown fields are allowed.

## Step 1 — Define the decision

Translate the request into the decision the research must support.

Examples:

- map competitors;
- decide whether to enter a category;
- choose positioning;
- compare prices;
- identify regional expansion opportunities;
- validate an underserved segment;
- understand why customers switch;
- monitor strategic changes.

If the user asks for “market research” with no explicit decision, default to competitive landscape + demand/customer evidence + whitespace hypotheses, not a generic encyclopedia.

## Step 2 — Challenge the category definition

Ask internally:

- What job is the customer actually trying to accomplish?
- What do they do today without this category?
- Is the user's category too narrow?
- Are there local terms/synonyms that buyers use instead?
- Is the buyer different from the end user?

Produce:

```json
{
  "market_definition": "",
  "customer_job": "",
  "buyer": "",
  "user": "",
  "adjacent_categories": [],
  "substitute_types": [],
  "search_vocabulary": []
}
```

## Step 3 — Determine market archetype

Possible archetypes:

- SaaS / software;
- B2B services;
- local business;
- e-commerce / marketplace;
- consumer app;
- industrial / manufacturing;
- regulated / financial / healthcare;
- mixed / unknown.

Use this only to prioritize sources and geographic depth, not to force conclusions.

## Step 4 — Determine whether regional intelligence is material

Do not assume country-level data is sufficient.

Set:

```json
{
  "regional_analysis": {
    "material": true,
    "reason": "",
    "geographic_level": "COUNTRY|MACRO_REGION|REGION|CITY|LOCAL_AREA|MIXED",
    "requested_regions": [],
    "requested_cities": [],
    "prioritization_method": ""
  }
}
```

Regional analysis is normally material when:

- service delivery is local/physical;
- location affects price, availability, competition or trust;
- maps/directories/local reviews matter;
- the user asks for a whole country and regional players may be hidden by national search;
- expansion into specific regions is part of the decision.

For `deep` country-level research in a location-sensitive market, include `regional-intelligence` automatically.

If regional analysis is not material, explain why.

## Step 5 — Prioritize regions

When regional intelligence is material, do not research every region equally by default.

Build regional research tiers using available evidence relevant to the niche, such as:

- target-customer population;
- category/business density;
- industry/economic activity;
- demand signals;
- competitor concentration;
- procurement activity where relevant;
- strategic relevance.

Use:

```text
Region Tier A — deep
Region Tier B — standard
Region Tier C — discovery/coverage scan
```

If reliable prioritization data is unavailable, define a transparent sampling strategy instead of fabricating regional scores.

## Step 6 — Build research questions

Questions must be falsifiable/actionable.

A deep study should normally cover, when relevant:

- competitive set;
- national vs regional/local competitor structure;
- target segments / JTBD;
- positioning;
- product/workflow;
- pricing/packaging;
- regional price variation;
- customer pains/praise/switching;
- regional VOC differences where sample supports them;
- GTM/distribution;
- regional channel patterns;
- strategic signals;
- whitespace and regional whitespace;
- risks/contradictions.

## Step 7 — Mark high-impact questions

Examples:

- current price;
- whether a competitor truly serves the target region;
- whether a discovered local player is active;
- market gap existence;
- regional gap existence;
- whether repeated customer pain is segment-wide;
- regulatory barrier;
- a calculated market-size input.

High-impact questions require stronger verification later.

## Step 8 — Choose skills

Return only required skills.

Example country-wide local-service run:

```json
[
  "competitor-discovery",
  "regional-intelligence",
  "competitor-profiling",
  "pricing-intelligence",
  "customer-research",
  "voice-of-customer",
  "gtm-intelligence",
  "strategic-signals",
  "market-whitespace",
  "contradiction-check",
  "evidence-verification",
  "red-team"
]
```

Do not include `regional-intelligence` when geography is demonstrably irrelevant.

## Step 9 — Source plan

For every research question define preferred and fallback source families.

For regional questions include local source families, for example:

```json
{
  "question": "Which competitors actively serve Kazan?",
  "preferred_sources": ["official_locations", "official_service_area", "maps_directories"],
  "fallback_sources": ["local_search", "regional_catalogs", "public_reviews"],
  "verification": "service presence must be evidenced; registration region alone is insufficient",
  "high_impact": true
}
```

## Step 10 — Parallelization

Typical parallel blocks:

- national competitor discovery;
- regional discovery by Tier-A region;
- competitor deep dives;
- pricing collection;
- VOC/community mining;
- GTM/content footprint;
- strategic signals.

Do not parallelize work that depends on unresolved entity identity or geography definitions.

## Step 11 — Research budget

### Quick

- reconnaissance;
- 3–5 high-relevance competitors;
- regional scan only if central to the question.

### Standard

- broader discovery;
- roughly 5–10 deeply relevant competitors where the market supports it;
- selected high-value regions when material;
- multiple source families;
- contradiction check for important findings.

### Deep

- multiple national discovery waves;
- independent regional discovery where material;
- Tier A + selected Tier B competitors;
- Tier-A regions deeply researched;
- deeper VOC/GTM/signals;
- targeted gap-closure searches;
- mandatory contradiction-check, evidence-verification and red-team.

Do not fabricate competitor or region counts when the market/data does not support them.

## Step 12 — Stop conditions

Completion is based on evidence saturation, not arbitrary source counts.

Examples:

- two discovery waves yield almost no new high-relevance competitors;
- Tier-A regional discovery reaches reasonable saturation;
- all high-impact questions are evidenced or explicitly unresolved;
- remaining missing data is unlikely to change the main decision;
- additional sources are duplicates or low-value copies.

## Required output

Use the shared output envelope plus:

```json
{
  "artifacts": {
    "scope": {},
    "market_archetype": "",
    "regional_analysis": {
      "material": true,
      "reason": "",
      "geographic_level": "",
      "regional_tiers": [],
      "coverage_target": ""
    },
    "research_questions": [],
    "skills": [],
    "parallel_groups": [],
    "stop_conditions": [],
    "research_depth": "",
    "known_limitations": []
  }
}
```

## Failure rules

Do not ask the user for extra detail if the task can proceed responsibly with explicit unknowns.

Do ask/stop only when ambiguity changes the identity of the market or geography so much that research would likely answer the wrong question.
