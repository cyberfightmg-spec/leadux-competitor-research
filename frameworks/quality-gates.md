# Research Quality Gates

These gates are mandatory before a final strategic conclusion is published.

## Gate 1 — Scope integrity

Confirm:

- market/category is explicit;
- geography is explicit;
- target customer/JTBD is explicit or marked unknown;
- research date is recorded;
- research depth is known;
- unavailable tools/sources are disclosed.

## Gate 2 — Competitor-set integrity

Check that the research considered more than obvious brand competitors where relevant:

- direct;
- indirect;
- substitutes;
- DIY/manual alternatives;
- adjacent solutions.

If one category is not applicable, say why.

## Gate 3 — Regional coverage integrity

Run this gate when sub-national competition is material.

Confirm:

- national discovery was not used as a substitute for regional/local discovery;
- the chosen geographic level is explicit;
- Tier-A regions/cities have independent local discovery;
- local/regional competitors are represented where found;
- national, multi-regional, regional and local players are distinguished;
- registration geography is not treated as service coverage;
- branch duplication is controlled;
- regional price summaries disclose sample size and comparability limitations;
- regional VOC claims disclose sample quality;
- regional whitespace is backed by demand + weak-coverage + feasibility evidence;
- unresearched/materially under-covered regions are listed as data gaps.

For a `deep` country-level study in a region-sensitive market, failure of this gate prevents `VERIFIED` status.

Use `VERIFIED_WITH_GAPS` or `DEGRADED` depending on how strongly missing regional coverage can change the decision.

## Gate 4 — Evidence integrity

For every high-impact claim:

- evidence class exists;
- at least one traceable source exists unless it is an explicit assumption;
- observation/publication date is captured where possible;
- scope/time/unit match the claim;
- geographic scope matches the claim;
- source independence is not double-counted.

## Gate 5 — Number integrity

Every material number must be one of:

- directly observed fact with source;
- reproducible calculation with sourced inputs;
- explicitly labeled estimate with method;
- explicitly labeled assumption.

For regional numeric summaries also verify:

- sample size;
- comparability;
- geographic scope;
- date range;
- whether the number is an observed sample statistic or a true population statistic.

If a number cannot pass this gate, remove it from the factual narrative.

## Gate 6 — Contradiction check

Run `skills/contradiction-check/SKILL.md` before synthesis.

Unresolved contradictions must remain visible in the report.

## Gate 7 — Evidence verification

Run `skills/evidence-verification/SKILL.md` for claims that materially change:

- competitor classification;
- geographic coverage/classification;
- pricing conclusions;
- regional pricing conclusions;
- market opportunity;
- regional whitespace;
- recommendation;
- risk assessment.

## Gate 8 — Red team

Run `skills/red-team/SKILL.md` against the main thesis.

At minimum test:

- alternative explanations;
- sample bias;
- survivorship/visibility bias;
- capital-city/national-search bias;
- weak buying-intent inference;
- false whitespace;
- false regional whitespace;
- stale evidence;
- economics/entry constraints.

## Gate 9 — Data gaps

List unresolved high-impact questions explicitly.

Never hide gaps behind generic confidence language.

Regional gaps should identify the affected territory and why coverage is incomplete.

## Gate 10 — Recommendation traceability

Every recommendation must contain:

- action;
- why;
- supporting claim IDs;
- contradictory evidence if any;
- confidence;
- risk;
- next validation step.

If the recommendation is geography-specific, its supporting evidence must also be geography-specific.

## Gate 11 — Final report status

A report may be:

- `verified`;
- `verified_with_gaps`;
- `degraded`;
- `insufficient_evidence`.

Do not publish an authoritative recommendation when status is `insufficient_evidence`.

Do not award `verified` to a deep country-level study where material regional competition was not researched.
