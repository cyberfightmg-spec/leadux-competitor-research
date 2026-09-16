# LeadUX Competitor Research

**Open-source Agent Skills for evidence-based competitor and market intelligence.**

Give this repository to an AI agent, ask it to study `SKILL.md` and `AGENTS.md`, and use the modular skills to run a structured competitor investigation instead of a generic SWOT summary.

> **Core rule:** no source → no fact. Missing data → `UNKNOWN`, not invention.

Built by **Viacheslav Bushmakin / LeadUX AI**.

**Telegram:** [@leadux_ai](https://t.me/leadux_ai)  
**Website:** [leaduxai.id](https://leaduxai.id/)

---

## v0.2.0 — Production Research Layer

Version 0.2 adds the operational layer required for deeper real-world research:

- multi-wave search strategy;
- capability detection and graceful fallbacks;
- shared structured output contract;
- stronger Evidence Protocol;
- source independence and contradiction handling;
- explicit quality gates;
- production-level planner/discovery/profiling skills;
- stronger product, pricing, customer, VOC, GTM and strategic-signal skills;
- false-whitespace testing;
- mandatory evidence verification and red team for deep research;
- machine-readable research schemas;
- **Russia Source Pack** for Russia-focused research;
- ready-to-use Deep Russia prompt.

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
- positioning;
- target segments and JTBD;
- product/workflow differences;
- pricing and packaging;
- customer pains and objections;
- Voice of Customer;
- GTM and distribution;
- strategic signals;
- market whitespace;
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

# Skills

| Skill | What it does |
|---|---|
| [`research-planner`](skills/research-planner/SKILL.md) | Converts the request into questions, sources, skills, research waves and stop conditions |
| [`competitor-discovery`](skills/competitor-discovery/SKILL.md) | Finds direct, indirect, substitute, DIY and adjacent competitors |
| [`competitor-profiling`](skills/competitor-profiling/SKILL.md) | Builds standardized evidence-backed competitor profiles |
| [`product-intelligence`](skills/product-intelligence/SKILL.md) | Compares workflows, capabilities, maturity and differentiation |
| [`pricing-intelligence`](skills/pricing-intelligence/SKILL.md) | Captures current prices, packaging, value metrics and pricing gaps |
| [`customer-research`](skills/customer-research/SKILL.md) | Extracts JTBD, pains, triggers, objections, outcomes and alternatives |
| [`voice-of-customer`](skills/voice-of-customer/SKILL.md) | Mines real customer language, complaints, praise and switching reasons |
| [`gtm-intelligence`](skills/gtm-intelligence/SKILL.md) | Maps observable acquisition, distribution, content and sales signals |
| [`strategic-signals`](skills/strategic-signals/SKILL.md) | Detects pricing, product, hiring, positioning and market changes |
| [`market-whitespace`](skills/market-whitespace/SKILL.md) | Tests underserved segments and gaps against demand and entry evidence |
| [`contradiction-check`](skills/contradiction-check/SKILL.md) | Reconciles or preserves conflicting evidence |
| [`evidence-verification`](skills/evidence-verification/SKILL.md) | Audits provenance, scope, freshness, calculations and independence |
| [`red-team`](skills/red-team/SKILL.md) | Tries to falsify the main strategic thesis |
| [`market-monitoring`](skills/market-monitoring/SKILL.md) | Defines watchlists, snapshot diffing and meaningful market events |

---

# Shared Research Frameworks

The individual skills share one operating discipline.

Start with:

- [`frameworks/evidence-protocol.md`](frameworks/evidence-protocol.md)
- [`frameworks/search-strategy.md`](frameworks/search-strategy.md)
- [`frameworks/fallback-policy.md`](frameworks/fallback-policy.md)
- [`frameworks/output-contract.md`](frameworks/output-contract.md)
- [`frameworks/source-quality.md`](frameworks/source-quality.md)
- [`frameworks/confidence-model.md`](frameworks/confidence-model.md)
- [`frameworks/research-depth.md`](frameworks/research-depth.md)
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

Examples:

```text
[FACT]
Competitor X lists its Pro plan at 4,990 RUB/month on the official pricing page.
Observed: 2026-09-16.
```

```text
[HYPOTHESIS]
Competitor X may be moving toward enterprise customers.

Evidence:
- enterprise page launched;
- SSO added;
- enterprise sales roles advertised.
```

A hypothesis must never silently become a fact in the final report.

---

# Research in waves

Production research should normally use multiple waves:

```text
WAVE 1
Broad category/JTBD discovery

WAVE 2
Entity verification + classification

WAVE 3
Deep competitor analysis

WAVE 4
Targeted gap closure + counter-searches
```

The agent should stop based on **evidence saturation**, not because it reached an arbitrary source count.

---

# Research depth

### Quick

Reconnaissance or narrow comparison.

### Standard

Normal evidence-backed competitor analysis.

### Deep

For market entry, product strategy, positioning, pricing and serious opportunity validation.

Deep mode requires:

```text
contradiction-check
→ evidence-verification
→ red-team
→ final synthesis
```

See [`frameworks/research-depth.md`](frameworks/research-depth.md).

---

# Russia Source Pack 🇷🇺

For research in Russia, the root router loads:

[`source-packs/russia.md`](source-packs/russia.md)

It prioritizes relevant source families such as:

- official FNS/company information;
- Rosstat and official statistics;
- public procurement data when relevant;
- Fedresurs/public company events when relevant;
- official competitor websites and documents;
- Yandex Maps / 2GIS for local discovery and customer signals;
- hh.ru as a hiring signal;
- relevant marketplaces, reviews and public communities;
- domain-specific official regulators and registries.

Important distinctions are built into the pack:

```text
Tender value ≠ competitor revenue
Vacancy count ≠ company growth
Telegram subscribers ≠ customers
Map rating ≠ universal business quality
OKVED ≠ proof of primary revenue activity
```

The source pack is guidance, not permission to bypass platform restrictions.

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

The repo includes schemas intended for agent pipelines and future applications:

- [`source.schema.json`](schemas/source.schema.json)
- [`claim.schema.json`](schemas/claim.schema.json)
- [`insight.schema.json`](schemas/insight.schema.json)
- [`competitor.schema.json`](schemas/competitor.schema.json)
- [`opportunity.schema.json`](schemas/opportunity.schema.json)
- [`research.schema.json`](schemas/research.schema.json)
- [`report.schema.json`](schemas/report.schema.json)
- [`skill-output.schema.json`](schemas/skill-output.schema.json)

This lets a product store structured research instead of treating the whole analysis as one text blob.

---

# Final quality gates

Before a deep report is published, the system checks:

- scope integrity;
- competitor-set coverage;
- evidence provenance;
- material numbers;
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

Never commit:

- API keys;
- passwords;
- Telegram bot tokens;
- cookies/session tokens;
- customer credentials;
- private customer datasets.

See [`SECURITY.md`](SECURITY.md).

---

# Project direction

This repository is the first research layer of the broader LeadUX agent architecture:

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
