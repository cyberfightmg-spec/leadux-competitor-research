# LeadUX Competitor Research

**Open-source Agent Skills for evidence-based competitor, market, customer and content-performance intelligence.**

Give this repository to an AI agent, ask it to study `SKILL.md` and `AGENTS.md`, and use only the skills needed for the research objective.

> **Core rule:** no source → no fact. Missing data → `UNKNOWN`, not invention.

Built by **Viacheslav Bushmakin / LeadUX AI**.

---

## v0.4.0 — Strategy Handoff + Content Performance Intelligence

Version 0.4 turns the repository into the upstream evidence layer for LeadUX Content Strategist.

New capabilities:

- `strategy-handoff` — exports a verified evidence package without changing research semantics;
- `content-performance-intelligence` — identifies observable content outliers relative to each account's own baseline;
- content performance pattern schema;
- explicit separation between `CONTENT_SIGNAL`, `AUDIENCE_RESPONSE`, `LEAD_SIGNAL`, and `BUSINESS_OUTCOME`;
- normalized outlier patterns can be handed downstream to the strategist;
- Founder/Brand Context is deliberately **not** invented here — it is a separate Strategist input.

The system now supports:

```text
MARKET / COMPETITOR / CUSTOMER RESEARCH
        ↓
CONTENT PERFORMANCE INTELLIGENCE
        ↓
contradiction-check
→ evidence-verification
→ red-team
→ synthesis
        ↓
strategy-handoff
        ↓
LeadUX Content Strategist
```

---

# What this repository investigates

Depending on the request:

- direct and indirect competitors;
- substitutes and DIY/manual alternatives;
- national, regional and local competition;
- positioning;
- target segments and JTBD;
- product/workflow differences;
- pricing and packaging;
- customer pains, objections and desired outcomes;
- Voice of Customer;
- GTM and distribution;
- competitor content footprint;
- **observable competitor/adjacent-creator content performance**;
- strategic signals;
- market/regional whitespace;
- contradictions;
- evidence quality;
- risks and counter-arguments.

Preferred reasoning chain:

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

---

# Content Performance Intelligence

`skills/content-performance-intelligence/SKILL.md` answers a different question from ordinary GTM analysis.

GTM/content footprint asks:

> What does this competitor publish and where?

Content Performance Intelligence asks:

> Which pieces materially outperform that account's own normal level, does the mechanism repeat, and how strong is the evidence?

Where comparable public data exists, the skill uses an account-local baseline rather than absolute vanity numbers.

Example:

```text
Account A
normal median = 1,500 views
outlier = 18,000 views
→ 12× baseline

Account B
normal median = 180,000 views
post = 220,000 views
→ 1.22× baseline
```

The first post may be a stronger performance signal despite having fewer absolute views.

The skill distinguishes:

```text
SINGLE_OUTLIER
REPEATED_ACCOUNT_PATTERN
CROSS_ACCOUNT_PATTERN
FIRST_PARTY_CONFIRMED_PATTERN
```

And never silently converts platform engagement into business impact:

```text
CONTENT_SIGNAL
AUDIENCE_RESPONSE
LEAD_SIGNAL
BUSINESS_OUTCOME
```

Views are not leads. Comments are not revenue. Business outcomes require separate evidence.

---

# Strategy Handoff

When research is intended for downstream content strategy, run:

```text
contradiction-check
→ evidence-verification
→ red-team
→ synthesis
→ strategy-handoff
```

The handoff can preserve:

- claims and source lineage;
- insights;
- market opportunities;
- VOC;
- GTM/content footprints;
- content-performance patterns;
- strategic signals;
- contradictions;
- data gaps;
- geography / segment / time qualifiers;
- research integrity status.

It does **not** decide:

- founder positioning;
- priority offers;
- content pillars;
- channel mix;
- hooks;
- cadence;
- Creator briefs.

Those belong to LeadUX Content Strategist, which combines this evidence with Founder/Brand Context and first-party performance.

---

# Regional Intelligence

Regional analysis remains a first-class dimension when geography matters.

The system can distinguish:

```text
registered_region
headquarters
physical_locations
service_regions
verified_regions
national_coverage
```

and classify:

```text
NATIONAL
MULTI_REGIONAL
REGIONAL
LOCAL
ONLINE_ONLY
UNKNOWN
```

A deep country-level study in a location-sensitive market should not receive `VERIFIED` status when material regional competition was ignored.

---

# Quick Start

Repository:

```text
https://github.com/cyberfightmg-spec/leadux-competitor-research
```

Example strategy-input request:

```text
Изучи SKILL.md и AGENTS.md.

Проведи глубокое исследование рынка и конкурентов в нише:
[НИША]

География:
[ГЕОГРАФИЯ]

Цель исследования:
подготовить доказательную базу для LeadUX Content Strategist.

Помимо обычного competitor/VOC/GTM исследования,
если публичные контент-метрики доступны и сопоставимы:
- используй content-performance-intelligence;
- найди публикации, которые являются аутлайерами относительно собственного baseline каждого аккаунта;
- ищи повторяемые паттерны между несколькими аккаунтами;
- отдельно классифицируй CONTENT_SIGNAL / AUDIENCE_RESPONSE / LEAD_SIGNAL / BUSINESS_OUTCOME;
- не считай просмотры доказательством продаж.

Не придумывай отсутствующие данные.
Классифицируй утверждения как FACT / ESTIMATE / HYPOTHESIS / ASSUMPTION / NOT_FOUND.

Перед передачей стратегу выполни:
contradiction-check → evidence-verification → red-team → synthesis → strategy-handoff.
```

---

# What this repository is NOT

It is not:

- a generic SWOT generator;
- a one-shot mega-prompt;
- a system that equates search visibility with market share;
- a workflow that equates viral content with commercial success;
- a workflow that invents revenue, CAC, churn, reach or conversion;
- a system that copies competitor tactics into strategy;
- a crawler designed to bypass access controls;
- the Founder/Brand Context store;
- the final Content Strategist or Creator.

---

# Integrity statuses

Full research ends with one of:

```text
VERIFIED
VERIFIED_WITH_GAPS
DEGRADED
INSUFFICIENT_EVIDENCE
```

That status is preserved exactly in strategy handoff.

The goal is not to sound certain. The goal is to preserve exactly what is known, observed, estimated, hypothesized and still unknown.
