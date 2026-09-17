# Skill: Competitor Discovery

## Mission

Discover the real competitive set for the customer's job-to-be-done, not just the most visible brands in the category.

This skill must find and classify:

- direct competitors;
- indirect competitors;
- substitutes;
- DIY/manual alternatives;
- adjacent solutions.

It must also avoid national-search bias when regional/local competition is material.

Read first:

- `frameworks/competitor-taxonomy.md`
- `frameworks/search-strategy.md`
- `frameworks/fallback-policy.md`
- `frameworks/output-contract.md`
- `frameworks/regional-intelligence.md` when regional analysis is active.

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
  "regional_analysis": {
    "material": false,
    "geographic_level": "",
    "regional_tiers": []
  },
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

Likewise, do not answer a country-level question by looking only at national search results. Strong regional players may have weak national visibility.

---

# Discovery process

## 1. Seed expansion

Build candidate terms from:

- category names;
- buyer/problem language;
- JTBD;
- known brands;
- alternatives language;
- local-language variants;
- product-review vocabulary;
- marketplace/directory categories;
- region/city modifiers when regional analysis is active.

## 2. National discovery wave

Run independent discovery families as relevant:

### Category search

Find products explicitly describing themselves as part of the category.

### Problem/JTBD search

Find products/services customers use to solve the underlying job without using the category term.

### Alternative search

Use known competitors to discover alternatives, analogs, comparison pages and switching discussions.

### Customer-language search

Look for “what do you use for…”, “how do you handle…”, “recommend…”, “instead of…”, reviews and community discussions.

### Directory / marketplace / app discovery

Use relevant public directories, app stores, maps, marketplaces or industry catalogs when applicable.

### SEO/content neighborhood

Where available, identify entities repeatedly appearing around the same problem/category queries. Treat visibility as discovery evidence only, not market-share evidence.

### Registry/domain discovery

For markets/geographies where official/public company sources help, use them to verify entity identity or uncover relevant operators.

The national wave should identify:

- national players;
- multi-regional players;
- major category brands;
- digital/online alternatives;
- broad substitutes.

It is a baseline, not the complete competitor set when location is material.

---

## 3. Regional/local discovery wave

If `regional_analysis.material = true`, run independent discovery for selected regions/cities.

For each Tier-A region, combine category/problem vocabulary with local geography:

```text
{category} + {region}
{category} + {city}
{JTBD/problem} + {region}
{service} + {city}
{alternative wording} + {city}
{buyer-language query} + {region}
```

Use local source families where relevant:

- maps;
- directories;
- local business catalogs;
- local marketplace listings;
- regional communities;
- local review platforms;
- region-specific public registries/statistics;
- regional search results;
- official location/service-area pages.

For Tier-B regions use a narrower but still independent discovery wave.

Tier-C regions may receive a coverage scan rather than deep profiling.

Regional discovery must be capable of finding competitors that do not appear in national results.

---

## 4. Verify entity identity

For every serious candidate verify when possible:

- canonical brand name;
- official domain;
- actual product/service;
- target segment;
- active/inactive status;
- legal identity where relevant;
- registration region if available;
- operating/service regions;
- branch/location evidence.

Do not merge entities solely by similar names.

Do not treat registration region as proof of service coverage.

---

## 5. Classify competitor type

Use:

```text
DIRECT
INDIRECT
SUBSTITUTE
DIY
ADJACENT
```

Classification is based on overlap in customer, JTBD and budget, not marketing category alone.

If regional analysis is active, also classify geographic role:

```text
NATIONAL
MULTI_REGIONAL
REGIONAL
LOCAL
ONLINE_ONLY
UNKNOWN
```

These are independent dimensions.

---

## 6. Score relevance

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

The exact weights may be adapted, but changes must be explicit.

Do not confuse relevance score with company quality, market share or strength.

For regional research, `Geography` should reflect verified relevance to the researched territory, not registration address alone.

---

## 7. Assign depth tier

```text
Tier A — highest decision relevance; deep profile
Tier B — meaningful competitor; medium profile
Tier C — map-level context
```

Tiering is relative to the research question, not brand fame.

A strong local player can be Tier A even if it is unknown nationally.

---

## 8. Entity deduplication across regions

Do not count the same chain/brand separately for every branch unless local units operate strategically independently.

Represent one competitor with multiple verified geographic presences.

Preserve local branch/location evidence separately.

---

## 9. Gap searches

Before stopping, ask:

- Did we discover at least one non-obvious substitute where one plausibly exists?
- Are local/regional players missing?
- Did national SEO visibility hide regional leaders?
- Did English-only or Russian-only search hide competitors?
- Are service/manual alternatives missing?
- Are category comparison pages over-weighting SEO-heavy vendors?
- Did we search maps/directories where the business is location-sensitive?
- Did we verify branches/service regions of national players?

If the market appears unusually sparse, run a deliberate false-whitespace search.

---

## 10. Saturation

National discovery approaches saturation when two consecutive waves produce few new high-relevance entities and no new competitor type.

Regional discovery approaches saturation independently for each Tier-A region when repeated local waves produce few new relevant entities across multiple source/query families.

Do not claim regional saturation if only one source family was checked.

---

# Negative evidence

Never say:

> There are no competitors in Region X.

unless there is an extraordinarily strong and explicitly bounded basis.

Prefer:

> No additional direct competitors were found in the regional source/query families checked as of DATE; coverage status is MEDIUM and indirect/substitute solutions remain listed separately.

---

# Required output

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
        "geographic_role": "NATIONAL|MULTI_REGIONAL|REGIONAL|LOCAL|ONLINE_ONLY|UNKNOWN",
        "relevance_score": 0,
        "classification_confidence": "high|medium|low",
        "reason": "",
        "tier": "A|B|C",
        "verified_regions": [],
        "source_ids": []
      }
    ],
    "national_search_families_used": [],
    "regional_search_families_used": {},
    "regional_coverage": [],
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
- keep weak candidates out of the deep-analysis queue;
- do not replace regional discovery with national search;
- do not present discovered competitor counts as total market counts;
- preserve coverage limitations by region.
