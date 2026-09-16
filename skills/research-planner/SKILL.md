# Skill: Research Planner

## Mission

Convert an ambiguous market/competitor request into an executable research plan with explicit questions, scope, source strategy, skill routing, budgets, stop conditions and verification requirements.

Do not research the market deeply in this skill. Plan the research so downstream skills know exactly what must be established.

Read first:

- `frameworks/search-strategy.md`
- `frameworks/fallback-policy.md`
- `frameworks/output-contract.md`
- `frameworks/research-depth.md`

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
- validate an underserved segment;
- understand why customers switch;
- monitor strategic changes.

If the user asks for “market research” with no explicit decision, default to producing a competitive landscape + demand/customer evidence + whitespace hypotheses, not a generic encyclopedia.

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

Classify the research context because source strategy should change by market type.

Possible archetypes:

- SaaS / software;
- B2B services;
- local business;
- e-commerce / marketplace;
- consumer app;
- industrial / manufacturing;
- regulated / financial / healthcare;
- mixed / unknown.

Use this classification only to prioritize sources, not to force conclusions.

## Step 4 — Build research questions

Questions must be falsifiable/actionable.

Bad:

> Is competitor X good?

Better:

> Which customer segment does competitor X explicitly target, what evidence supports that classification, and how does it overlap with our target ICP?

A deep competitor study should normally cover, when relevant:

- competitive set;
- target segments / JTBD;
- positioning;
- product/workflow;
- pricing/packaging;
- customer pains/praise/switching;
- GTM/distribution;
- strategic signals;
- whitespace;
- risks/contradictions.

## Step 5 — Mark high-impact questions

Some claims can materially change the recommendation. Mark them `high_impact`.

Examples:

- current price;
- whether a competitor truly serves the target segment;
- market gap existence;
- whether repeated customer pain is segment-wide;
- regulatory barrier;
- a calculated market size input.

High-impact questions require stronger evidence verification later.

## Step 6 — Choose skills

Return only required skills.

Example full run:

```json
[
  "competitor-discovery",
  "competitor-profiling",
  "product-intelligence",
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

Do not include unrelated skills simply because they exist.

## Step 7 — Source plan

For every research question define preferred source families and fallback families.

Example:

```json
{
  "question": "What is the current public price?",
  "preferred_sources": ["official_pricing", "official_docs"],
  "fallback_sources": ["official_offer_terms", "authorized_app_listing", "reputable_secondary_source"],
  "verification": "direct source preferred",
  "high_impact": true
}
```

## Step 8 — Parallelization

Identify tasks that can be researched independently.

Typical parallel blocks:

- competitor deep dives;
- pricing collection;
- VOC/community mining;
- GTM/content footprint;
- strategic signals.

Do not parallelize steps that depend on unresolved scope or entity identity.

## Step 9 — Research budget

Translate depth into an effort plan.

The numbers below are guidance, not hard quotas.

### Quick

- reconnaissance;
- 3–5 high-relevance competitors;
- minimal source triangulation;
- narrow question set.

### Standard

- broader discovery;
- roughly 5–10 deeply relevant competitors where the market supports it;
- multiple source families;
- contradiction check for important findings.

### Deep

- multiple search waves;
- Tier A + selected Tier B competitors;
- deeper VOC/GTM/signals;
- targeted gap-closure searches;
- mandatory contradiction-check, evidence-verification and red-team.

Do not fabricate competitor counts when the market is smaller.

## Step 10 — Stop conditions

Define completion by evidence saturation, not arbitrary source count.

Examples:

- two discovery waves yield almost no new high-relevance competitors;
- all high-impact research questions are evidenced or explicitly unresolved;
- remaining missing data is unlikely to change the main decision;
- additional sources are duplicates or low-value copies.

## Required output

Use the shared output envelope plus:

```json
{
  "artifacts": {
    "scope": {},
    "market_archetype": "",
    "research_questions": [
      {
        "id": "rq_001",
        "question": "",
        "priority": "high|medium|low",
        "high_impact": true,
        "preferred_sources": [],
        "fallback_sources": [],
        "assigned_skills": []
      }
    ],
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

Do ask/stop only when ambiguity changes the identity of the market so much that research would likely answer the wrong question.
