# Russia Source Pack

Use this source pack when the research geography includes the Russian Federation.

The goal is not to force every source into every project. Select source families according to the research questions, market type and geographic level.

For region-sensitive markets, country-level research must combine national and regional/local discovery. Federal search results are not a substitute for regional competitor research.

---

# Regional research rule for Russia

When regional dynamics are material, use:

```text
NATIONAL DISCOVERY
+
REGIONAL / CITY DISCOVERY
+
REGIONAL COVERAGE CHECK
```

Read:

- `skills/regional-intelligence/SKILL.md`
- `frameworks/regional-intelligence.md`
- `frameworks/quality-gates.md`

A deep Russia study in a location-sensitive market must not receive `VERIFIED` status if material regional competition was ignored.

Do not automatically research all federal subjects equally. Prioritize Tier A/B/C regions according to evidence relevant to the niche, or use a transparent sampling strategy when prioritization data is limited.

---

# Geographic model

Depending on the niche, research may use:

```text
RUSSIA
→ FEDERAL DISTRICT / MACRO-REGION
→ FEDERAL SUBJECT
→ CITY
→ LOCAL AREA
```

The research level should follow the actual competitive unit.

Examples:

- local services: city often matters;
- real estate: city/metro area often matters;
- clinics: city/local catchment often matters;
- industrial B2B: federal subject or industrial cluster may matter;
- national SaaS: regional analysis may be lighter unless geography changes demand, distribution or pricing.

---

# Source hierarchy

## Tier A — official / primary public data

Prefer for legal status, company identity, official statistics, public procurement and regulation.

### Federal Tax Service (ФНС)

- https://www.nalog.gov.ru/
- Open taxpayer/company services: https://www.nalog.gov.ru/donline/

Useful for publicly available company and entrepreneur information, status, extracts, OKVED and related official data exposed by FNS services.

Important:

```text
registration region ≠ headquarters ≠ branch footprint ≠ service region
```

Do not infer customer coverage or operational strength from registration data alone.

### Rosstat / official statistics

- https://rosstat.gov.ru/
- Statistics: https://rosstat.gov.ru/statistic
- Databases: https://rosstat.gov.ru/databases

Useful for market context and, where available, regional/municipal differences in population, industries, employment, prices, production and other relevant variables.

Always state statistical period, unit and geographic level.

Do not use national statistics as a direct measurement of a narrow regional niche unless the mapping is justified.

### Unified Information System in Procurement (ЕИС)

- https://zakupki.gov.ru/

Use public procurement records when relevant to B2G demand, supplier activity, contract categories and regional public-sector buying signals.

A procurement event is not total market demand and procurement volume is not competitor revenue.

### Fedresurs

- https://fedresurs.ru/

Use publicly accessible disclosures when relevant to company events and legally published notices.

Verify entity identity using INN/OGRN or other stable identifiers where possible.

### Other official sources by domain

Depending on the niche, consider relevant regulators and official registries, for example:

- Bank of Russia — https://cbr.ru/
- Rospatent / FIPS — https://rospatent.gov.ru/ and https://fips.ru/
- regional government/open-data portals where directly relevant;
- domain-specific regulators and registries.

Use only when they answer an actual research question.

---

# Tier B — competitor primary sources

Use official competitor sources for public facts about the offer and geography:

- official website;
- pricing pages;
- product/service pages;
- branch/location pages;
- service-area pages;
- public offer/terms;
- documentation;
- changelog/release notes;
- official Telegram/VK/YouTube channels;
- official app/store listings;
- official case studies/customer pages;
- official career/vacancy pages.

For geographic claims distinguish:

```text
REGISTERED
HEADQUARTERED
PHYSICAL_LOCATION
SERVICE_AVAILABLE
ONLINE_AVAILABLE
PARTNER_PRESENCE
```

One office or legal address does not prove broad regional coverage.

Marketing claims are evidence of what the company claims, not independent proof of results.

---

# Tier C — local discovery, demand, customer and distribution signals

## Yandex Maps

- https://yandex.ru/maps/

Useful for:

- city/region competitor discovery;
- local category density;
- branch/location verification;
- public rating/review signals;
- operating information;
- regional VOC/customer language.

Treat map results as platform observations, not complete census data.

A result count is not total competitor count.

## 2GIS

- https://2gis.ru/

Useful for local company discovery, locations, categories, branch presence and public review/business-card signals where available.

Respect platform access rules and do not circumvent restrictions.

## hh.ru

- https://hh.ru/

Public vacancies may provide geography-specific hiring signals.

A regional vacancy is evidence that a role is advertised for that geography; it is not proof of successful expansion, revenue growth or actual headcount.

## Marketplaces / app stores / directories

Depending on the niche, public listings may provide:

- regional seller/provider presence;
- public price observations;
- assortment/service availability;
- review language;
- location/category signals.

Always distinguish platform seller data from manufacturer/brand/company data.

---

# Tier D — regional community / public discussion

Potential sources include publicly accessible:

- Telegram channels/posts;
- VK communities;
- YouTube videos/comments;
- local/professional forums;
- review websites;
- industry communities;
- regional media/community sources where relevant.

Use mainly for:

- VOC;
- pains;
- objections;
- switching reasons;
- local alternatives;
- regional language;
- emerging demand or service gaps.

Do not convert a small discussion sample into a regional market-size or buying-demand claim.

When comparing VOC between regions, disclose sample size, entity diversity, source diversity and bias.

Use `INSUFFICIENT_REGIONAL_SAMPLE` when evidence is too weak for comparison.

---

# Tier E — media / analyst / secondary sources

Use reputable business/industry media and specialist publications for context, events and attributed estimates.

Whenever a secondary article cites an original report, filing, company statement or official statistic, prefer the original source.

Do not count multiple articles based on the same original release as independent corroboration.

---

# Russian-language search expansion

Generate variants across:

- singular/plural;
- common case forms;
- abbreviations;
- colloquial buyer language;
- English product/category names;
- transliterated brand names;
- region names;
- city names;
- local service terms.

Example national vocabulary:

```text
CRM автосервис
CRM для автосервиса
программа автосервиса
учёт в автосервисе
автоматизация СТО
система для СТО
запись клиентов автосервис
```

Example regional wave:

```text
CRM автосервис Казань
программа для СТО Казань
автоматизация автосервиса Татарстан
учёт автосервиса Екатеринбург
CRM СТО Краснодар
```

Do not rely only on the formal industry category; buyers and local providers may use different language.

---

# Recommended regional discovery sequence

For each selected Tier-A region/city:

```text
1. category + geography search
2. JTBD/problem + geography search
3. maps/directories
4. known competitor branch/service-area verification
5. local review/VOC sources
6. local price observations
7. alternative/substitute search
8. false-whitespace counter-search
```

Tier-B regions can use a narrower independent wave.

Tier-C regions may receive coverage scans.

---

# Russia-specific entity resolution

Prefer stable identifiers where publicly available:

```text
INN
OGRN / OGRNIP
official domain
legal entity name
brand name
registered region
verified branch/location
verified service region
```

Do not merge two businesses solely because names are similar.

Do not count every branch of one chain as a separate competitor unless strategically independent.

---

# Regional pricing integrity

If regional public prices are compared, preserve raw observations.

A regional summary should show:

```text
comparable service/product definition
sample size (n)
observed min/max
median where justified
currency
VAT/tax context when known and material
observation date range
source coverage
excluded non-comparable observations
```

Prefer:

> Median among 23 comparable public observations found in checked sources.

Do not write:

> Average price in Kazan is X

when only a small convenience sample was observed.

---

# Russia-specific research integrity

- Tender value ≠ competitor revenue.
- Vacancy count ≠ employee count or growth.
- Telegram subscribers ≠ customers.
- Map rating ≠ universal business quality.
- OKVED ≠ proof of primary revenue activity.
- Registered region ≠ service coverage.
- Discovered competitor count ≠ total competitor count.
- Federal search visibility ≠ strength in every region.
- Online availability ≠ regional market leadership.
- Regional whitespace requires demand + weak coverage + entry feasibility.

---

# Required Russia evidence coverage

For a deep study, include:

```text
Russia evidence coverage

National source families checked: ...
Regional analysis material: yes/no + reason
Geographic level used: ...
Tier-A regions/cities: ...
Tier-B regions/cities: ...
Tier-C coverage: ...
Regional source families checked: ...
Material regions not researched: ...
Coverage limitations: ...
```

If regional dynamics are material and coverage is materially incomplete, final status must be `VERIFIED_WITH_GAPS` or `DEGRADED`, not `VERIFIED`.
