# LeadUX Competitor Research

**Open-source Agent Skills for evidence-based competitor and market intelligence.**

Built by **LeadUX AI** so an AI agent can move beyond generic SWOT templates and run a structured, source-backed competitor investigation: discover the real competitive set, compare positioning and pricing, mine customer language, detect strategic signals, find whitespace, verify contradictions, and explain every important conclusion with evidence.

> **Core rule:** no source → no fact. No data → `UNKNOWN`, not invention.

## Follow LeadUX AI

Research updates, AI automation cases, new skills and practical experiments are published in the LeadUX AI Telegram channel:

**Telegram:** [@leadux_ai](https://t.me/leadux_ai)  
**Website:** [leaduxai.id](https://leaduxai.id/)

Created by **Viacheslav Bushmakin / LeadUX AI**.

---

## What this repository gives an AI agent

This repository is designed to be shared directly with an AI agent. The agent should first read the root `SKILL.md` and `AGENTS.md`, then load only the skills required for the user's task.

It can investigate:

- direct, indirect, substitute, DIY and adjacent competitors;
- positioning, category claims and target segments;
- product capabilities, maturity and differentiation;
- pricing, packaging, value metrics and pricing changes;
- customer pains, praise, objections and switching reasons;
- Voice of Customer (VOC) across public sources;
- GTM, content, distribution and channel signals;
- product velocity, hiring and strategic changes;
- competitive whitespace and underserved segments;
- contradictions, source independence and evidence quality;
- confidence, assumptions and data gaps.

## What this is not

- a one-shot mega-prompt;
- a SWOT template;
- a tool that treats search visibility as market leadership;
- a system that invents revenue, CAC, churn or conversion data;
- a scraper that bypasses paywalls, CAPTCHAs or access controls;
- a claim that a channel, feature or competitor does not exist just because one search failed.

---

# Quick Start

Give this repository URL to an AI agent:

```text
https://github.com/cyberfightmg-spec/leadux-competitor-research
```

Then ask it to study the repository before starting research.

### Русский пример

```text
Изучи репозиторий:
https://github.com/cyberfightmg-spec/leadux-competitor-research

Сначала прочитай корневые SKILL.md и AGENTS.md.
Далее используй только те skills, которые нужны для задачи.

Проведи глубокое исследование конкурентов в нише:
AI-автоматизация автосервисов в России.

Цель:
понять реальную конкурентную картину, цены, позиционирование,
продуктовые различия, боли клиентов, VOC, GTM, стратегические сигналы
и найти подтверждённые рыночные пробелы.

Используй актуальные публичные источники.
Не придумывай отсутствующие данные.
Классифицируй существенные утверждения как
FACT / ESTIMATE / HYPOTHESIS / ASSUMPTION / NOT_FOUND.

Перед финальными выводами обязательно выполни:
contradiction-check → evidence-verification → red-team.

Для каждого важного вывода покажи источники, дату наблюдения,
уровень уверенности и ограничения данных.
```

### English example

```text
Study this repository first:
https://github.com/cyberfightmg-spec/leadux-competitor-research

Read the root SKILL.md and AGENTS.md, then load only the skills required for the task.

Research competitors for:
AI automation for auto repair shops

Geography: Russia
Goal: map the real competitive landscape and identify defensible whitespace.

Use current public sources.
Do not invent missing information.
Classify important claims as FACT, ESTIMATE, HYPOTHESIS, ASSUMPTION or NOT_FOUND.
Run contradiction-check, evidence-verification and red-team before final conclusions.
Show evidence, dates, confidence and data gaps for major findings.
```

---

# Research Workflow

```text
User request
    ↓
Root SKILL.md — router
    ↓
research-planner
    ↓
competitor-discovery
    ↓
competitor-profiling
    ↓
┌──────────────────────────────┐
│ product-intelligence         │
│ pricing-intelligence         │
│ customer-research            │
│ voice-of-customer            │
│ gtm-intelligence             │
│ strategic-signals            │
└──────────────────────────────┘
    ↓
market-whitespace
    ↓
contradiction-check
    ↓
evidence-verification
    ↓
red-team
    ↓
final evidence-backed report
```

For a narrow request, the agent should **not** load the entire system. Example: a pricing-only task normally needs `competitor-profiling`, `pricing-intelligence`, and `evidence-verification`.

---

# Skills

| Skill | Purpose |
|---|---|
| `research-planner` | Defines scope, research questions, source strategy and depth |
| `competitor-discovery` | Finds direct, indirect, substitute, DIY and adjacent competitors |
| `competitor-profiling` | Builds standardized evidence-backed competitor profiles |
| `product-intelligence` | Compares product capabilities, workflows, maturity and differentiation |
| `pricing-intelligence` | Analyzes pricing, packaging, value metrics and pricing gaps |
| `customer-research` | Extracts jobs, pains, triggers, objections and desired outcomes |
| `voice-of-customer` | Mines and clusters customer language from public sources |
| `gtm-intelligence` | Investigates acquisition, distribution, content and channel signals |
| `strategic-signals` | Detects launches, hiring, positioning, pricing and market shifts |
| `market-whitespace` | Finds underserved segments and defensible gaps |
| `contradiction-check` | Preserves and analyzes conflicting evidence instead of hiding it |
| `evidence-verification` | Validates claims, sources, dates, calculations and provenance |
| `red-team` | Tries to falsify the main thesis before recommendations are published |
| `market-monitoring` | Defines repeatable watchlists and meaningful change detection |

---

# Evidence Protocol

Every important statement must be classified as one of:

```text
FACT
ESTIMATE
HYPOTHESIS
ASSUMPTION
NOT_FOUND
```

A failed search is **not** proof that something does not exist.

A protected or unavailable page is **not** a `NOT_FOUND` result.

Ten articles repeating one press release are **not** ten independent confirmations.

Customer discussion is **not automatically buying demand**.

See [`frameworks/evidence-protocol.md`](frameworks/evidence-protocol.md) and [`frameworks/source-quality.md`](frameworks/source-quality.md).

---

# Tool-independent by design

Skills define:

```text
WHAT TO INVESTIGATE
HOW TO REASON
HOW TO VERIFY
WHAT TO RETURN
```

Tools define only how data is acquired.

An agent may use any legal and available source or integration, including:

- native web search and browser tools;
- official company websites and documentation;
- public government and company registries;
- GitHub;
- RSS;
- review platforms and public communities;
- Crawl4AI;
- GPT Researcher;
- Firecrawl;
- DataForSEO;
- authorized social-data APIs.

Optional integrations improve coverage, but their absence must never be replaced with fabricated data.

---

# Repository Structure

```text
.
├── README.md
├── SKILL.md                  # root research router
├── AGENTS.md                 # global agent operating rules
├── SECURITY.md
├── THIRD_PARTY_NOTICES.md
│
├── skills/                   # modular research skills
│   ├── research-planner/
│   ├── competitor-discovery/
│   ├── competitor-profiling/
│   ├── product-intelligence/
│   ├── pricing-intelligence/
│   ├── customer-research/
│   ├── voice-of-customer/
│   ├── gtm-intelligence/
│   ├── strategic-signals/
│   ├── market-whitespace/
│   ├── contradiction-check/
│   ├── evidence-verification/
│   ├── red-team/
│   └── market-monitoring/
│
├── frameworks/               # shared research and evidence protocols
├── schemas/                  # machine-readable output contracts
├── prompts/                  # reusable starting prompts
├── examples/                 # SaaS, e-commerce, local business, B2B
└── docs/                     # architecture and integration notes
```

---

# Security and Credentials

This public repository intentionally contains **no production secrets**.

Never commit:

- API keys;
- passwords;
- session cookies;
- Telegram bot tokens;
- private customer datasets;
- authentication credentials.

Runtime applications should use environment variables or a proper secret manager. See [`SECURITY.md`](SECURITY.md) and [`.env.example`](.env.example).

---

# Third-party Projects

This repository contains original LeadUX AI skill definitions and research methodology. It does **not** vendor third-party source code.

Several open-source projects informed parts of the architecture and workflow. See [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md) for references and intended integration boundaries.

---

# Status

**v0.1.0 — Competitor Intelligence Skills Foundation**

Current focus: make competitor research reproducible, source-backed and useful for real product and market decisions.

Planned evolution:

```text
Competitor Research
      ↓
Market Intelligence
      ↓
Content Strategist
      ↓
Lead Discovery
      ↓
Lead Qualification
      ↓
LeadUX OS
```

---

# LeadUX AI

LeadUX AI develops practical AI automation, research systems and agent workflows focused on business outcomes rather than AI for its own sake.

**Telegram:** [https://t.me/leadux_ai](https://t.me/leadux_ai)  
**Website:** [https://leaduxai.id](https://leaduxai.id/)

If you use these skills, improve them, or build an interesting research workflow around them, follow the Telegram channel for new versions and related LeadUX AI projects.

---

## License

MIT — see [`LICENSE`](LICENSE).
