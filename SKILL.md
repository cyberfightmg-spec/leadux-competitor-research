---
name: leadux-competitor-research
description: Routes evidence-first competitor and market intelligence tasks to modular LeadUX research skills.
license: MIT
metadata:
  version: 0.1.0
  author: LeadUX AI
---

# LeadUX Competitor Research — Root Router

Use this skill when the user asks for competitor research, competitive intelligence, market mapping, pricing comparison, customer complaint analysis, GTM analysis, market whitespace, or validation of a competitive thesis.

## Mission

Produce **decision-useful competitive intelligence**, not generic summaries. Every major conclusion must be traceable to evidence, and uncertainty must remain visible.

## Step 0 — Detect capabilities

Before research, inventory the tools actually available. Record capabilities such as:

```text
web_search: yes/no
browser_fetch: yes/no
javascript_browser: yes/no
github: yes/no
public_registries: yes/no
review_sources: yes/no
social_sources: yes/no
paid_seo_data: yes/no
```

Never claim a source was checked if the current environment cannot access it.

## Step 1 — Route the task

For a **full competitor study**, load in this order:

1. `skills/research-planner/SKILL.md`
2. `skills/competitor-discovery/SKILL.md`
3. `skills/competitor-profiling/SKILL.md`
4. specialist skills selected by the plan
5. `skills/market-whitespace/SKILL.md`
6. `skills/contradiction-check/SKILL.md`
7. `skills/evidence-verification/SKILL.md`
8. `skills/red-team/SKILL.md`

For narrow tasks, load only what is needed:

- pricing: profiling + pricing + verification;
- customer complaints: profiling + voice-of-customer + verification;
- positioning: profiling + GTM + verification;
- competitor discovery only: planner + discovery + verification;
- whitespace: requires discovery + customer/VOC + competitor coverage + verification + red-team.

## Step 2 — Establish scope

At minimum derive or ask only if truly necessary:

- research objective;
- geography;
- target customer / buyer;
- customer job-to-be-done;
- product/category definition;
- time sensitivity;
- known competitors;
- desired depth: quick / standard / deep.

Do not blindly accept the user's category definition. Expand to alternatives that compete for the same job or budget.

## Step 3 — Maintain an evidence ledger

Every important claim must be one of:

- `FACT`
- `ESTIMATE`
- `HYPOTHESIS`
- `ASSUMPTION`
- `NOT_FOUND`

Follow `frameworks/evidence-protocol.md`.

## Step 4 — Separate raw evidence from interpretation

Required chain:

```text
SOURCE → CLAIM → INSIGHT → STRATEGIC CONCLUSION
```

Do not allow a strategic conclusion to exist without supporting claim IDs or explicit assumptions.

## Step 5 — Use progressive depth

Research many candidates shallowly, then spend depth on the most relevant competitors.

Default pattern:

- Tier A: 5–8 competitors, deep research;
- Tier B: 10–20 competitors, medium research;
- Tier C: market-map only.

Adjust to market size and evidence saturation.

## Step 6 — Verify before synthesis

Before final output:

1. check duplicate-source independence;
2. check contradictory claims;
3. check freshness;
4. check numerical provenance;
5. check competitor classification;
6. check whether absence claims are actually `NOT_FOUND`;
7. run red-team against the leading thesis.

## Hard rules

Never:

- invent revenue, CAC, conversion, churn, market share, employee processes, CRM usage, or internal operations;
- treat company marketing copy as independent proof of performance;
- infer a missing feature solely because it was not visible on the homepage;
- infer a missing channel after checking only one platform;
- infer that a market gap is attractive without evidence of demand;
- count syndicated copies of one source as independent corroboration;
- bypass access controls, CAPTCHAs or paywalls.

## Final output contract

A full study should contain:

1. scope and research date;
2. capabilities and data gaps;
3. competitive landscape and taxonomy;
4. Tier A competitor profiles;
5. positioning / product / pricing / VOC / GTM comparison;
6. contradictions and uncertain claims;
7. validated whitespace opportunities;
8. where not to compete;
9. what to test next;
10. evidence appendix with source URLs and observed dates.
