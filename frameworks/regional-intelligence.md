# Regional Intelligence Framework

Use this framework whenever competition, customer behavior, pricing, availability or distribution may vary materially inside the selected country or geography.

## Why this exists

Country-level research is often distorted by:

- national brands dominating search results;
- Moscow/Saint Petersburg or capital-city bias;
- SEO-heavy companies hiding strong local players;
- legal-registration geography being confused with operating geography;
- national averages hiding regional price and demand differences;
- map/directory competitors being omitted from ordinary web search;
- online competitors being treated as equally strong in every region.

Regional intelligence is therefore a separate analytical dimension, not one address field.

---

## Geographic hierarchy

Represent geography at the level material to the business:

```text
COUNTRY
→ MACRO_REGION / FEDERAL_DISTRICT
→ REGION / STATE / PROVINCE / FEDERAL_SUBJECT
→ CITY
→ LOCAL_AREA
```

Do not always go to the smallest administrative level. Choose the level at which competition or buying behavior can plausibly change.

---

## Presence taxonomy

Each competitor may have two independent classifications:

### Competitive relationship

```text
DIRECT
INDIRECT
SUBSTITUTE
DIY
ADJACENT
```

### Geographic role

```text
NATIONAL
MULTI_REGIONAL
REGIONAL
LOCAL
ONLINE_ONLY
UNKNOWN
```

Do not infer one from the other.

### Geographic fields

Keep separate:

```text
registered_region
headquarters
physical_locations
service_regions
verified_regions
national_coverage
```

`registered_region` is legal/administrative identity evidence only. It does not prove where the competitor actively sells or serves customers.

---

## Regional prioritization

Deep country research should not spend equal effort on every region automatically.

Prioritize regions using the best available evidence relevant to the market. Potential signals include:

- target-customer count;
- category/business density;
- demand proxies;
- economic or industry activity;
- public procurement where relevant;
- competitor concentration;
- strategic importance to the research question;
- population or purchasing-power proxies when justified.

Store the reason behind every Tier-A region.

Recommended tiers:

```text
A — deep regional analysis
B — standard regional analysis
C — discovery/coverage scan
```

These tiers control research depth only. They do not mean “best” or “worst” region.

---

## Discovery architecture

Use two distinct discovery layers:

```text
NATIONAL DISCOVERY
+
REGIONAL / LOCAL DISCOVERY
```

National discovery is not a substitute for regional discovery.

### National discovery finds

- national and multi-regional competitors;
- broad category leaders;
- substitutes available across the country;
- major digital/online alternatives.

### Regional discovery finds

- regional brands;
- city-level competitors;
- branches/chains with uneven coverage;
- local service businesses;
- local price and positioning variants;
- region-specific substitutes and customer language.

Use local modifiers and source families appropriate to the country.

---

## Entity resolution

One brand operating in multiple regions is normally one competitor entity with multiple presence records.

Do not count every branch as a separate competitor unless the franchise/legal/operating model makes it strategically independent.

Do not merge similarly named local firms without identity evidence.

Useful identifiers include:

- canonical brand name;
- official domain;
- legal entity name;
- official registration identifiers;
- branch/location addresses;
- phone or official contact data where publicly available and lawful.

---

## Regional competitor density

`competitors_discovered` means exactly:

> number of relevant competitor entities discovered in the checked source/query families.

It must never silently mean:

> total number of competitors in the region.

Every density statement should carry:

- source families checked;
- date;
- geographic scope;
- coverage confidence;
- duplicate/branch handling method.

---

## Regional pricing

Preserve raw observations first.

Only aggregate offers that are meaningfully comparable.

A regional price summary should include:

```text
sample size (n)
min/max observed
median when justified
currency
unit/service definition
tax/VAT context if material
observation date range
source coverage
excluded observations
```

Avoid claiming a universal regional average from a convenience sample.

When comparability is weak, report raw observations or segmented ranges instead.

---

## Regional positioning

A regional positioning pattern requires repetition across multiple independent competitors/sources.

Potential dimensions:

- audience;
- specialty;
- core promise;
- price/value framing;
- proof/trust mechanism;
- local identity;
- online/offline delivery;
- service bundle.

A single company is not a regional pattern.

---

## Regional VOC

Attach location only when the source provides enough evidence.

Track:

```text
n observations
number of competitor entities
number of source families
recency
intensity
bias notes
```

Use `INSUFFICIENT_REGIONAL_SAMPLE` if the evidence cannot support a regional comparison.

Do not create percentage comparisons from tiny samples.

---

## Regional GTM

Regional distribution may differ by:

- maps/directories;
- local SEO;
- regional social communities;
- branch footprint;
- local partnerships;
- local marketplaces;
- local events;
- public procurement;
- regional media.

Separate:

```text
PRESENCE
ACTIVITY
TRACTION_PROXY
PERFORMANCE_EVIDENCE
```

A visible channel is not automatically an effective channel.

---

## Regional whitespace

A regional whitespace hypothesis must have evidence for all three:

```text
DEMAND
+
WEAK / DIFFERENT COMPETITOR COVERAGE
+
ENTRY FEASIBILITY
```

Low competitor discovery alone is not sufficient.

Always run a false-whitespace check:

- alternative category terms;
- nearby cities/regions;
- maps/directories;
- service/manual substitutes;
- local-language queries;
- branches of national brands;
- offline operators with weak websites.

---

## Coverage model

For each researched region use:

```text
HIGH_COVERAGE
MEDIUM_COVERAGE
LOW_COVERAGE
NOT_RESEARCHED
```

Suggested interpretation:

### HIGH_COVERAGE
Multiple relevant source families checked, regional/local discovery performed, key Tier-A entities verified, and repeated gap searches produce few new high-relevance entities.

### MEDIUM_COVERAGE
Useful evidence exists but one or more important source families or local query families remain incomplete.

### LOW_COVERAGE
Only limited sources/query families were checked; conclusions must remain tentative.

### NOT_RESEARCHED
Region intentionally or accidentally outside the analyzed sample.

---

## Country-level integrity rule

If regional dynamics are material to the market, a `deep` country-level study cannot be `VERIFIED` unless regional research was performed to a decision-useful level.

Missing material regional coverage must result in:

```text
VERIFIED_WITH_GAPS
```

or, when the gap materially undermines the study:

```text
DEGRADED
```

---

## Required regional comparison fields

A final comparison may include, when supported:

```text
region
research tier
competitors discovered
Tier-A competitors
observed public price range/median + n
positioning patterns
customer themes
channel patterns
whitespace hypotheses
coverage status
material caveats
```

Never fill a field with invented data just to make the table look complete.
