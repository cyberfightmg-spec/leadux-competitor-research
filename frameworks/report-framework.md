# Final Research Report Framework v0.3

The final report must be decision-useful, evidence-backed and explicit about uncertainty.

Do not dump raw research in the order it was collected.

## 1. Research header

Include:

- research objective;
- market/category;
- geography;
- whether regional analysis is material;
- geographic level used;
- target customer/JTBD;
- research date;
- depth: quick/standard/deep;
- tools/source families used;
- important unavailable sources/tools;
- integrity status.

Integrity status:

```text
VERIFIED
VERIFIED_WITH_GAPS
DEGRADED
INSUFFICIENT_EVIDENCE
```

## 2. Executive findings

Lead with the most decision-relevant findings, not background.

For each major finding show:

- finding;
- evidence class where relevant;
- confidence;
- supporting claim IDs/sources;
- geographic scope;
- material caveat.

Do not present a national conclusion when evidence is concentrated in one or two cities without saying so.

Avoid an unsupported single-number market score. If a scoring rubric is used, expose dimensions and evidence behind each score.

## 3. Market definition

Explain:

- what market/JTBD was studied;
- what is inside/outside scope;
- what substitute/manual alternatives were considered;
- important terminology differences;
- why the chosen geographic level is appropriate.

## 4. Competitive landscape

Show:

- direct;
- indirect;
- substitutes;
- DIY/manual;
- adjacent.

When regional analysis is material, also show geographic role:

```text
NATIONAL
MULTI_REGIONAL
REGIONAL
LOCAL
ONLINE_ONLY
```

Distinguish Tier A/B/C research depth.

Do not present discovery relevance as market share.

## 5. Regional Competitive Landscape

Include this section whenever sub-national competition is material.

Show:

- regional prioritization method;
- Tier A/B/C regions or sampling strategy;
- national vs regional/local competitor structure;
- regions researched vs not researched;
- coverage status by region;
- meaningful regional differences.

A regional comparison table may include, when supported:

| Region | Research tier | Competitors discovered in checked sources | Tier-A competitors | Observed price summary + n | Positioning patterns | VOC patterns | Channel patterns | Whitespace | Coverage | Caveats |
|---|---|---:|---|---|---|---|---|---|---|---|

Rules:

- discovered count ≠ total market population;
- registration region ≠ service coverage;
- national search visibility ≠ regional leadership;
- blank/unknown data must stay blank/unknown rather than being invented;
- regional differences require region-specific evidence.

## 6. Tier-A competitor comparison

Compare only decision-relevant dimensions:

- target segment;
- JTBD;
- competitor type;
- geographic role;
- verified operating/service geography;
- positioning;
- product/workflow;
- pricing/packaging;
- customer evidence;
- GTM/distribution;
- strategic signals;
- threat/overlap.

Avoid giant feature matrices in the executive layer. Put detailed matrices in appendices/drilldown.

## 7. Customer / VOC

Include:

- jobs;
- pains;
- triggers;
- desired outcomes;
- objections;
- alternatives;
- switching reasons;
- repeated language patterns;
- sample-bias limitations.

Separate high-frequency themes from intense but rare complaints.

For regional VOC comparisons show:

- sample size;
- entity diversity;
- source diversity;
- recency;
- bias caveats.

If evidence is insufficient, state `INSUFFICIENT_REGIONAL_SAMPLE` instead of forcing a comparison.

## 8. Pricing

Include:

- original price observations;
- comparable normalized scenarios where valid;
- value metrics;
- packaging differences;
- public pricing gaps;
- observation dates;
- custom/unknown pricing as unknown, not zero.

For regional pricing comparisons, preserve:

```text
comparable offer definition
sample size (n)
observed min/max
median when justified
currency
unit
VAT/tax context where material
observation date range
source coverage
excluded observations
```

Do not call a small convenience sample a universal regional average.

## 9. GTM / distribution

Separate:

- channel presence;
- activity;
- traction proxies;
- actual performance evidence.

When regional analysis is material, compare local SEO/maps/directories, branches, partnerships, communities, marketplaces, events and other local distribution signals where relevant.

Do not present presence as channel effectiveness.

## 10. Strategic signals

Show observed change separately from interpretation.

Example:

```text
FACT: Enterprise page added on DATE.
HYPOTHESIS: This may indicate increased enterprise focus.
```

For geographic expansion distinguish an observed branch/service-area change from a hypothesis about regional strategy.

## 11. Whitespace / opportunity hypotheses

Every opportunity should show:

- target segment/job;
- geography when relevant;
- demand evidence;
- weak-coverage evidence;
- entry feasibility evidence;
- contradictory evidence;
- confidence;
- risks;
- validation step.

For regional whitespace require:

```text
REGIONAL DEMAND
+
WEAK / DIFFERENT REGIONAL COMPETITOR COVERAGE
+
REGIONAL ENTRY FEASIBILITY
```

Low discovered competitor count alone is not an opportunity.

## 12. Contradictions

List unresolved material conflicts explicitly.

Show:

- claims in conflict;
- geographic scope of each claim;
- likely reason;
- resolution status;
- effect on confidence/recommendation.

A national claim and a regional claim may both be true if scopes differ; do not treat them as contradictory before checking geography.

## 13. Red-team findings

Show the strongest arguments against the main thesis.

Include regional-bias challenges where material:

- capital-city bias;
- federal-search bias;
- missing local/offline competitors;
- regional sample imbalance;
- false regional whitespace;
- branch/service-area confusion.

For each finding show severity, evidence, effect on recommendation and validation path.

## 14. Recommendations

Every recommendation follows:

```text
ACTION
WHY
EVIDENCE
CONTRADICTORY EVIDENCE
CONFIDENCE
RISK
WHAT TO TEST NEXT
```

For geography-specific recommendations, supporting evidence must match the same geography.

Avoid generic advice that could apply to any business.

## 15. Where NOT to compete

When evidence permits, explicitly identify segments, positioning battles or regions where entering would likely mean fighting an incumbent advantage with weak differentiation.

This section must be evidence-based, not rhetorical.

## 16. Regional coverage and data gaps

List unresolved high-impact unknowns.

For regional research also show:

```text
regions planned
regions researched
Tier-A regions completed
material regions not researched
source families missing by region
regional coverage status
```

Examples:

- Competitor X has no verifiable public enterprise pricing.
- No reliable public CAC benchmark was found for this niche.
- Customer evidence is overrepresented by Moscow.
- Regional map coverage for two Tier-A cities was unavailable.
- Service-area evidence for Competitor Y remains ambiguous.

Include how each gap could be validated.

## 17. Sources / evidence appendix

Provide traceable source references grouped logically by claim/entity and geography where relevant.

For machine-readable workflows, preserve IDs matching the JSON schemas.

## Report style

- concise executive layer;
- detailed drilldown below;
- tables where comparison helps;
- geography, dates and units visible;
- sample sizes visible for regional numeric summaries;
- facts and hypotheses visibly distinct;
- no decorative certainty;
- no generic SWOT filler unless explicitly requested.

## Regional integrity rule

If regional dynamics are material, a deep country-level study cannot be published as `VERIFIED` when regional research is materially incomplete.

Use:

```text
VERIFIED_WITH_GAPS
```

or:

```text
DEGRADED
```

depending on whether missing regional evidence could materially change the decision.
