# LeadUX Competitor Research

**Open-source Agent Skills for evidence-based competitor and market intelligence.**

Give this repository to an AI agent, ask it to study `SKILL.md` and `AGENTS.md`, and use the modular skills to run a structured competitor investigation instead of a generic SWOT summary.

> **Core rule:** no source → no fact. Missing data → `UNKNOWN`, not invention.

Built by **Viacheslav Bushmakin / LeadUX AI**.

**Telegram:** [@leadux_ai](https://t.me/leadux_ai)  
**Website:** [leaduxai.id](https://leaduxai.id/)

---

## v0.3.0 — Regional Intelligence

Version 0.3 adds a dedicated regional competitive-intelligence layer.

The system no longer treats a country as one homogeneous market when location is material. It can separate national, multi-regional, regional and local competitors; run independent discovery by region/city; compare observed pricing, positioning, VOC and GTM patterns; and test regional whitespace with explicit coverage controls.

Key additions:

- new [`regional-intelligence`](skills/regional-intelligence/SKILL.md) skill;
- new [`frameworks/regional-intelligence.md`](frameworks/regional-intelligence.md);
- new [`schemas/region.schema.json`](schemas/region.schema.json);
- national vs regional/local discovery waves;
- `NATIONAL / MULTI_REGIONAL / REGIONAL / LOCAL / ONLINE_ONLY` geographic roles;
- separate registration, headquarters, physical presence and service coverage;
- regional Tier A/B/C research prioritization;
- regional pricing with sample-size/comparability rules;
- regional VOC and GTM analysis;
- regional whitespace + false-whitespace checks;
- mandatory Regional Coverage Gate for deep country-level research when geography is material;
- stronger Russia-specific regional research workflow.

See [`CHANGELOG.md`](CHANGELOG.md).

---

# What this repository is

This is a modular research methodology for AI agents.

It helps an agent investigate:

- direct competitors;
- indirect competitors;
- substitutes;
- DIY/manual alternatives;
- adjacent solutions;
- national, multi-regional, regional and local competitors;
- positioning;
- target segments and JTBD;
- product/workflow differences;
- pricing and packaging;
- regional price differences when evidence supports them;
- customer pains and objections;
- Voice of Customer;
- GTM and distribution;
- regional channel patterns;
- strategic signals;
- market whitespace;
- regional whitespace;
- contradictions;
- evidence quality;
- risks and counter-arguments.

The intended reasoning chain is:

```text
SOURCE
  ↓
CLAIM
  ↓
INSIGHT
  ↓
STRATEGIC CONCLUSION
  ↓
RECOMMENDATION
```

The agent should be able to show why it reached an important conclusion.

---

# What this repository is NOT

It is not:

- a one-shot mega-prompt;
- a generic SWOT generator;
- a tool that treats search ranking as market share;
- a workflow that assumes Moscow/federal search results represent all of Russia;
- a system that invents revenue, CAC, churn or customer counts;
- a crawler designed to bypass CAPTCHA/paywalls/authentication;
- a workflow that treats one bad review as a market-wide pain;
- a workflow that declares a competitor/feature/channel absent after one failed search.

---

# Quick Start

Give your AI agent this repository:

```text
https://github.com/cyberfightmg-spec/leadux-competitor-research
```

Then ask:

```text
Изучи репозиторий:
https://github.com/cyberfightmg-spec/leadux-competitor-research

Сначала прочитай SKILL.md и AGENTS.md.
Далее используй только нужные skills.

Проведи глубокое исследование конкурентов в нише:
[НИША]

География:
[СТРАНА]

Если рынок зависит от региона/города, обязательно используй regional-intelligence:
отдельно найди федеральных, региональных и локальных игроков,
сравни цены, позиционирование, VOC и каналы по регионам,
а также покажи покрытие и ограничения выборки.

Не придумывай отсутствующие данные.
Все существенные выводы подтверждай источниками.
Классифицируй важные утверждения как
FACT / ESTIMATE / HYPOTHESIS / ASSUMPTION / NOT_FOUND.

Перед финальным выводом обязательно выполни:
contradiction-check → evidence-verification → red-team.
```

For Russia-focused research, use the ready prompt:

[`prompts/deep-russia-research.md`](prompts/deep-russia-research.md)

---

# How the agent should work

```text
User request
    ↓
Root SKILL.md
    ↓
Capability detection
    ↓
Geographic Source Pack
    ↓
research-planner
    ↓
competitor-discovery
    ↓
regional-intelligence (when material)
    ↓
competitor-profiling
    ↓
┌───────────────────────────────┐
│ product-intelligence          │
│ pricing-intelligence          │
│ customer-research             │
│ voice-of-customer             │
│ gtm-intelligence              │
│ strategic-signals             │
└───────────────────────────────┘
    ↓
market-whitespace
    ↓
contradiction-check
    ↓
evidence-verification
    ↓
red-team
    ↓
Final evidence-backed report
```

The system uses **progressive skill loading**. A narrow pricing task should not automatically run the full pipeline.

---

# Regional Intelligence

Regional analysis is a separate research dimension, not just an address field.

For every serious competitor the system can distinguish:

```text
registered_region
headquarters
physical_locations
service_regions
verified_regions
national_coverage
```

It also assigns a geographic role independently from competitor type:

```text
DIRECT + NATIONAL
DIRECT + REGIONAL
INDIRECT + LOCAL
SUBSTITUTE + ONLINE_ONLY
```

A deep country-level study in a location-sensitive market must not receive `VERIFIED` status when material regional competition was ignored.

Regional comparisons may include, when supported by evidence:

```text
region
research tier
competitors discovered in checked sources
Tier-A competitors
observed price range / median + sample size
positioning patterns
customer themes
channel patterns
regional whitespace hypotheses
coverage status
material caveats
```

Important: `competitors discovered` is not the same as the total competitor population.

---

# Skills

| Skill | What it does |
|---|---|
| [`research-planner`](skills/research-planner/SKILL.md) | Converts the request into questions, sources, geographic scope, skills, research waves and stop conditions |
| [`competitor-discovery`](skills/competitor-discovery/SKILL.md) | Finds direct, indirect, substitute, DIY and adjacent competitors using national and regional discovery where material |
| [`regional-intelligence`](skills/regional-intelligence/SKILL.md) | Maps national/regional/local competition, regional pricing, positioning, VOC, GTM and whitespace |
| [`competitor-profiling`](skills/competitor-profiling/SKILL.md) | Builds standardized evidence-backed competitor profiles |
| [`product-intelligence`](skills/product-intelligence/SKILL.md) | Compares workflows, capabilities, maturity and differentiation |
| [`pricing-intelligence`](skills/pricing-intelligence/SKILL.md) | Captures current prices, packaging, value metrics and pricing gaps |
| [`customer-research`](skills/customer-research/SKILL.md) | Extracts JTBD, pains, triggers, objections, outcomes and alternatives |
| [`voice-of-customer`](skills/voice-of-customer/SKILL.md) | Mines real customer language, complaints, praise and switching reasons |
| [`gtm-intelligence`](skills/gtm-intelligence/SKILL.md) | Maps observable acquisition, distribution, content and sales signals |
| [`strategic-signals`](skills/strategic-signals/SKILL.md) | Detects pricing, product, hiring, positioning and market changes |
| [`market-whitespace`](skills/market-whitespace/SKILL.md) | Tests underserved segments and gaps against demand and entry evidence |
| [`contradiction-check`](skills/contradiction-check/SKILL.md) | Reconciles or preserves conflicting evidence |
| [`evidence-verification`](skills/evidence-verification/SKILL.md) | Audits provenance, geography, scope, freshness, calculations and independence |
| [`red-team`](skills/red-team/SKILL.md) | Tries to falsify the main thesis, including regional-bias and false-whitespace risks |
| [`market-monitoring`](skills/market-monitoring/SKILL.md) | Defines watchlists, snapshot diffing and meaningful market events |

---

# Shared Research Frameworks

Start with:

- [`frameworks/evidence-protocol.md`](frameworks/evidence-protocol.md)
- [`frameworks/search-strategy.md`](frameworks/search-strategy.md)
- [`frameworks/fallback-policy.md`](frameworks/fallback-policy.md)
- [`frameworks/output-contract.md`](frameworks/output-contract.md)
- [`frameworks/source-quality.md`](frameworks/source-quality.md)
- [`frameworks/confidence-model.md`](frameworks/confidence-model.md)
- [`frameworks/research-depth.md`](frameworks/research-depth.md)
- [`frameworks/regional-intelligence.md`](frameworks/regional-intelligence.md)
- [`frameworks/quality-gates.md`](frameworks/quality-gates.md)
- [`frameworks/report-framework.md`](frameworks/report-framework.md)

---

# Evidence classes

Every material research statement should be distinguishable as:

```text
FACT
ESTIMATE
HYPOTHESIS
ASSUMPTION
NOT_FOUND
```

A hypothesis must never silently become a fact in the final report.

---

# Research in waves

Production research normally uses multiple waves:

```text
WAVE 1 — broad national/category/JTBD discovery
WAVE 2 — entity verification + classification
WAVE 3 — regional/local discovery where material
WAVE 4 — deep competitor analysis
WAVE 5 — targeted gap closure + counter-searches
```

The agent stops based on **evidence saturation**, not because it reached an arbitrary source count.

---

# Research depth

### Quick

Reconnaissance or narrow comparison.

### Standard

Normal evidence-backed competitor analysis.

### Deep

For market entry, product strategy, positioning, pricing, expansion and serious opportunity validation.

Deep mode requires:

```text
contradiction-check
→ evidence-verification
→ red-team
→ final synthesis
```

When geography is material, it also requires the **Regional Coverage Gate**.

---

# Russia Source Pack 🇷🇺

For research in Russia, the root router loads:

[`source-packs/russia.md`](source-packs/russia.md)

It covers national and regional source families, including official statistics/registries, official competitor sources, Yandex Maps / 2GIS, hh.ru, relevant marketplaces, public communities and domain-specific sources.

For region-sensitive markets, Russia research uses:

```text
NATIONAL DISCOVERY
+
REGIONAL / CITY DISCOVERY
+
REGIONAL COVERAGE CHECK
```

Registration region must never be treated as proof that a company serves that region, and a Moscow/federal result set must never substitute for regional discovery.

---

# Graceful fallback

Optional integrations are accelerators, not requirements.

The methodology can work with native web/search/browser capabilities. If available, external tools may improve coverage:

- Crawl4AI;
- GPT Researcher;
- Firecrawl;
- DataForSEO;
- authorized social-data APIs.

If a tool is unavailable:

```text
SKIP TOOL
→ USE LEGAL FALLBACK SOURCE
→ RECORD COVERAGE GAP IF MATERIAL
→ CONTINUE RESEARCH
```

A tool failure must never be reported as “no market activity”.

---

# Machine-readable schemas

The repo includes:

- [`source.schema.json`](schemas/source.schema.json)
- [`claim.schema.json`](schemas/claim.schema.json)
- [`insight.schema.json`](schemas/insight.schema.json)
- [`competitor.schema.json`](schemas/competitor.schema.json)
- [`region.schema.json`](schemas/region.schema.json)
- [`opportunity.schema.json`](schemas/opportunity.schema.json)
- [`research.schema.json`](schemas/research.schema.json)
- [`report.schema.json`](schemas/report.schema.json)
- [`skill-output.schema.json`](schemas/skill-output.schema.json)

---

# Final quality gates

Before a deep report is published, the system checks:

- scope integrity;
- competitor-set coverage;
- regional coverage when material;
- evidence provenance;
- material numbers;
- geographic scope match;
- contradictions;
- source independence;
- verification results;
- red-team findings;
- unresolved data gaps;
- recommendation traceability.

Final report status must be one of:

```text
VERIFIED
VERIFIED_WITH_GAPS
DEGRADED
INSUFFICIENT_EVIDENCE
```

---

# Security

This public repository intentionally contains **no production secrets**.

Never commit API keys, passwords, Telegram bot tokens, cookies/session tokens, customer credentials or private customer datasets.

See [`SECURITY.md`](SECURITY.md).

---

# Project direction

```text
Competitor Intelligence
        ↓
Market Intelligence
        ↓
AI Content Strategist
        ↓
Lead Discovery Agent
        ↓
Lead Intake / Qualification
        ↓
LeadUX OS
```

The same evidence graph can later feed content, lead discovery and qualification instead of forcing each agent to start research from zero.

---

# LeadUX AI

LeadUX AI builds practical AI automation and agent systems focused on business outcomes rather than AI for its own sake.

Follow development, experiments and new agent skills:

**Telegram:** [https://t.me/leadux_ai](https://t.me/leadux_ai)  
**Website:** [https://leaduxai.id](https://leaduxai.id/)

Created by **Viacheslav Bushmakin / LeadUX AI**.

---

## License

MIT — see [`LICENSE`](LICENSE).
