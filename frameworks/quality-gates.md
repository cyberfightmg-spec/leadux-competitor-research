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

## Gate 3 — Evidence integrity

For every high-impact claim:

- evidence class exists;
- at least one traceable source exists unless it is an explicit assumption;
- observation/publication date is captured where possible;
- scope/time/unit match the claim;
- source independence is not double-counted.

## Gate 4 — Number integrity

Every material number must be one of:

- directly observed fact with source;
- reproducible calculation with sourced inputs;
- explicitly labeled estimate with method;
- explicitly labeled assumption.

If a number cannot pass this gate, remove it from the factual narrative.

## Gate 5 — Contradiction check

Run `skills/contradiction-check/SKILL.md` before synthesis.

Unresolved contradictions must remain visible in the report.

## Gate 6 — Evidence verification

Run `skills/evidence-verification/SKILL.md` for claims that materially change:

- competitor classification;
- pricing conclusions;
- market opportunity;
- whitespace;
- recommendation;
- risk assessment.

## Gate 7 — Red team

Run `skills/red-team/SKILL.md` against the main thesis.

At minimum test:

- alternative explanations;
- sample bias;
- survivorship/visibility bias;
- weak buying-intent inference;
- false whitespace;
- stale evidence;
- economics/entry constraints.

## Gate 8 — Data gaps

List unresolved high-impact questions explicitly.

Never hide gaps behind generic confidence language.

## Gate 9 — Recommendation traceability

Every recommendation must contain:

- action;
- why;
- supporting claim IDs;
- contradictory evidence if any;
- confidence;
- risk;
- next validation step.

## Gate 10 — Final report status

A report may be:

- `verified`;
- `verified_with_gaps`;
- `degraded`;
- `insufficient_evidence`.

Do not publish an authoritative recommendation when status is `insufficient_evidence`.
