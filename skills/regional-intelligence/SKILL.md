# Skill: Regional Intelligence

## Mission

Build an evidence-backed regional competitive map instead of treating a country as one homogeneous market.

Use this skill when geography spans a country, multiple regions, states/provinces, federal subjects, cities, or other meaningful sub-national markets — especially for local services, healthcare, education, real estate, automotive, retail, hospitality, agencies, construction, professional services and other location-sensitive categories.

The goal is not to enumerate every location mechanically. The goal is to determine where competition, pricing, positioning, customer language, channel structure and market whitespace materially differ by region.

Read first:

- `frameworks/regional-intelligence.md`
- `frameworks/evidence-protocol.md`
- `frameworks/source-quality.md`
- `frameworks/search-strategy.md`
- `frameworks/output-contract.md`
- the relevant `source-packs/*` file when available.

## Core principles

1. Registration region ≠ operating region ≠ service region.
2. National visibility ≠ regional strength.
3. Search-result count ≠ market size.
4. Number of discovered competitors ≠ total number of competitors.
5. One office address does not prove regional market coverage.
6. Online availability does not automatically make a business a strong national competitor.
7. Regional averages must disclose sample size, source coverage and observation period.
8. Do not compare regional price levels without preserving currency, tax context, unit, service scope and observation date.
9. Do not declare a regional gap unless both demand evidence and weak-coverage evidence exist.
10. Deep country-level research is incomplete when material regional competition is ignored.

---

# When to activate

Activate this skill when at least one applies:

- geography contains a whole country and the market has meaningful local/regional delivery;
- the user explicitly asks for regions, cities, territories or local competitors;
- maps/directories/local reviews are important source families;
- pricing, demand or positioning plausibly differs by geography;
- competitor discovery is dominated by national SEO-heavy brands and may hide regional players;
- the research decision concerns expansion into specific territories.

For purely global digital products with no meaningful geographic differentiation, regional analysis may be reduced or marked `not_material`, but this decision must be explained.

---

# Input

```json
{
  "market_definition": "",
  "customer_job": "",
  "target_customer": "",
  "country": "",
  "requested_regions": [],
  "requested_cities": [],
  "market_archetype": "",
  "known_competitors": [],
  "research_depth": "quick|standard|deep",
  "available_capabilities": []
}
```

---

# Step 1 — Build the geographic model

Determine the smallest geographic unit that materially changes competition.

Possible levels:

```text
COUNTRY
MACRO_REGION / FEDERAL_DISTRICT
REGION / STATE / PROVINCE / FEDERAL_SUBJECT
CITY
LOCAL_AREA
```

Do not force every market to city level.

Examples:

- SaaS sold nationally: country + selected regional validation may be enough.
- Dental clinics: city-level competition is usually material.
- Real-estate agencies: city/metro market is usually material.
- Industrial equipment: federal subject or industrial cluster may matter more than city.

Record the selected level and why.

---

# Step 2 — Separate geographic concepts

For every serious competitor distinguish:

```text
registered_region
headquarters
physical_locations
service_regions
verified_regions
national_coverage
```

Also classify geographic role:

```text
NATIONAL
MULTI_REGIONAL
REGIONAL
LOCAL
ONLINE_ONLY
UNKNOWN
```

This classification is independent of competitor type (`DIRECT`, `INDIRECT`, etc.).

A competitor can be:

```text
DIRECT + REGIONAL
INDIRECT + NATIONAL
SUBSTITUTE + LOCAL
```

Do not infer operating coverage from legal registration alone.

---

# Step 3 — Prioritize regions

Do not automatically research every administrative region with equal depth.

Create regional tiers based on evidence relevant to the market.

Possible prioritization signals:

- target-customer population;
- number of relevant businesses/entities;
- category density;
- observed demand/search/community signal;
- economic activity relevant to the niche;
- purchasing-power proxy where justified;
- procurement activity where relevant;
- known competitor concentration;
- strategic relevance to the user's decision.

Never invent weights or values silently. If reliable regional prioritization data is unavailable, use a transparent practical sampling strategy and label it.

Suggested depth:

```text
Region Tier A — deep regional research
Region Tier B — standard regional research
Region Tier C — discovery / coverage scan
```

Region tier is not a ranking of region quality. It controls research depth.

---

# Step 4 — Run national discovery first

Identify:

- national brands;
- multi-regional chains;
- digital/online competitors with broad coverage;
- obvious category leaders;
- substitutes and adjacent solutions.

This creates the baseline but must not be treated as the whole market.

---

# Step 5 — Run independent regional discovery waves

For selected regions/cities repeat discovery using local modifiers and local source families.

For each region combine:

```text
category + region
category + city
problem/JTBD + region
service + city
alternatives + city
buyer-language query + region
```

Also use appropriate local directories, maps, business catalogs, marketplaces, regional communities, public registries and official sources.

Regional discovery must be capable of finding competitors absent from national search results.

For Russia, follow `source-packs/russia.md` and include relevant city/subject variants where permitted and useful.

---

# Step 6 — Resolve entities across regions

Prevent double counting.

One brand with branches in five cities is one competitor entity with multiple verified geographic presences, unless separate franchise/legal entities materially operate as independent competitors.

Store region-level presence evidence separately.

Do not merge similarly named local businesses without evidence.

---

# Step 7 — Build the regional competitor map

For every selected region capture when supported:

```json
{
  "region_id": "",
  "competitors_discovered": 0,
  "direct_discovered": 0,
  "indirect_discovered": 0,
  "substitute_discovered": 0,
  "tier_a_competitors": [],
  "dominant_positioning_patterns": [],
  "observed_price_summary": {},
  "customer_themes": [],
  "channel_patterns": [],
  "whitespace_hypotheses": [],
  "coverage_confidence": "HIGH|MEDIUM|LOW"
}
```

Counts must be described as **discovered in checked sources**, never as the total market population unless an authoritative source establishes the total.

---

# Step 8 — Regional pricing

Where comparable public prices exist, preserve every observation before aggregation.

For a regional summary show:

- comparable offer/service definition;
- sample size `n`;
- observed min/max;
- median where sample and comparability justify it;
- currency;
- tax/VAT context when known and material;
- observation dates;
- source coverage;
- excluded non-comparable observations.

Prefer language such as:

> Median among 23 comparable public price observations collected from the checked sources.

Never write:

> Average price in the region is X

when the dataset is only a small convenience sample.

If `n` is too small or offers are not comparable, report raw observations or a range and mark the limitation.

---

# Step 9 — Regional positioning and product patterns

Compare whether competitors in different regions emphasize different:

- audiences;
- pains;
- promises;
- specialties;
- service bundles;
- proof mechanisms;
- price/value framing;
- local trust signals;
- online vs offline delivery.

Only call a pattern regional if it recurs across multiple independent entities/sources in that region.

---

# Step 10 — Regional VOC

Attach location to customer evidence only when the location is actually known or can be responsibly inferred from the source context.

For regional themes track:

- sample size;
- entity diversity;
- source diversity;
- recency;
- intensity;
- possible platform/sample bias.

If the sample is insufficient, use:

```text
INSUFFICIENT_REGIONAL_SAMPLE
```

Do not manufacture regional percentages from tiny samples.

---

# Step 11 — Regional GTM and distribution

Observe regional differences in:

- map/directory presence;
- local SEO;
- regional social/community presence;
- marketplace presence;
- local partnerships;
- events;
- branch/store footprint;
- local media/content;
- public procurement where relevant.

Presence is not effectiveness. Separate:

```text
PRESENCE
ACTIVITY
TRACTION_PROXY
PERFORMANCE_EVIDENCE
```

---

# Step 12 — Regional whitespace

A regional opportunity hypothesis requires three independent questions:

```text
1. Is there evidence of demand in this region?
2. Is relevant competitor coverage genuinely weaker/different?
3. Is entry/service delivery feasible for this region?
```

A low discovered competitor count alone is not whitespace.

Possible regional whitespace types:

- underserved customer segment;
- missing price tier;
- missing specialty/service bundle;
- weak local language/positioning;
- weak channel coverage;
- poor online/offline accessibility;
- business-model gap;
- workflow gap.

Run a false-whitespace counter-search before publishing a strong opportunity conclusion.

---

# Step 13 — Coverage and saturation

Regional coverage approaches saturation when repeated local discovery waves yield few new high-relevance entities and source families are reasonably diverse.

For every researched region assign:

```text
HIGH_COVERAGE
MEDIUM_COVERAGE
LOW_COVERAGE
NOT_RESEARCHED
```

Explain why.

A Deep country-level study cannot receive `VERIFIED` if regional competition is material but regional coverage is materially missing.

Use `VERIFIED_WITH_GAPS` or `DEGRADED` depending on severity.

---

# Required output

Use the shared skill envelope plus:

```json
{
  "artifacts": {
    "regional_analysis_material": true,
    "geographic_level": "REGION|CITY|MIXED",
    "national_players": [],
    "regions": [],
    "regional_comparison": [],
    "regional_whitespace": [],
    "coverage": {
      "regions_planned": 0,
      "regions_researched": 0,
      "tier_a_regions_completed": 0,
      "material_gaps": []
    }
  }
}
```

Use `schemas/region.schema.json` for machine-readable region artifacts.

---

# Quality checks

Before returning, confirm:

- national and regional competitors are not conflated;
- registration and service geography are separated;
- national search results did not substitute for local discovery;
- regional competitors are deduplicated across cities/branches;
- regional price summaries disclose sample size;
- VOC regional claims disclose sample quality;
- discovered counts are not presented as total market counts;
- regional whitespace has demand + weak coverage + feasibility evidence;
- missing material regions are explicitly reported.

The objective is not to create a decorative map. The objective is to expose competitive structures that disappear when an entire country is treated as one market.
