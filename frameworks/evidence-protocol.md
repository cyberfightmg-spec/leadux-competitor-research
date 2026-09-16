# Evidence Protocol v0.2

This protocol defines how research claims are represented and how uncertainty is preserved.

## Evidence classes

### FACT

A directly supported statement about an observable/verifiable state or event.

Requirements:

- traceable source;
- source actually supports the claim;
- date/period when time-sensitive;
- correct unit/scope/entity.

Example:

```text
[FACT] Competitor X lists the Pro plan at 4,990 RUB/month on its official pricing page, observed 2026-09-16.
```

A company's self-description may be a fact about **what the company claims**, not independent proof of the underlying outcome.

Example:

```text
[FACT] Company X describes the product as “AI-first”.
```

Not:

```text
[FACT] Company X is AI-first.
```

unless the term is operationally defined and independently supported.

---

### ESTIMATE

A derived quantity or externally estimated quantity where the true value is not directly observed.

Requirements:

- method;
- formula where applicable;
- input claim IDs/sources;
- assumptions;
- range/sensitivity when useful.

Example:

```text
[ESTIMATE] Bottom-up serviceable market = 12,000 target companies × 48,000 RUB annual spend = 576M RUB/year.
```

Inputs must themselves be sourced or explicitly assumed.

---

### HYPOTHESIS

An interpretation that explains a pattern but is not directly proven.

Requirements:

- supporting claims;
- plausible alternative explanations;
- confidence;
- validation path where decision-relevant.

Example:

```text
[HYPOTHESIS] Competitor X may be moving upmarket because it added SSO, launched an enterprise page and is advertising enterprise sales roles.
```

---

### ASSUMPTION

A value/proposition temporarily accepted to proceed despite missing evidence.

Requirements:

- explicit label;
- why it is needed;
- sensitivity/impact;
- how it can be validated.

High-sensitivity assumptions must appear in the final report.

---

### NOT_FOUND

A bounded negative research result.

Requirements:

- what was searched;
- source/query families checked;
- observation date;
- access/tool limitations.

Correct:

```text
[NOT_FOUND] No public price was found on the official pricing/product pages, public offer documents and targeted searches checked on 2026-09-16.
```

Incorrect:

```text
Competitor has no pricing.
```

`NOT_FOUND` means “not found in the documented search space”, not universal non-existence.

---

# Claim provenance

Every material claim should be traceable through:

```text
claim_id
→ source_id(s)
→ URL / artifact
→ observed/published date
→ evidence class
→ verification status
```

Calculated claims additionally need:

```text
formula
→ input claim IDs
→ unit conversions
→ assumptions
```

# Observation vs interpretation

Keep separate objects for:

```text
OBSERVATION
INTERPRETATION
STRATEGIC IMPLICATION
```

Example:

```text
Observation [FACT]: price changed from 990 to 1,490 RUB.
Interpretation [HYPOTHESIS]: vendor may be testing higher willingness to pay.
Implication [HYPOTHESIS]: low-price positioning may become less crowded.
```

Do not merge them into one factual sentence.

# Source independence

A source count is not corroboration count.

Record an `independence_group` or origin family when several sources derive from the same:

- press release;
- government dataset;
- analyst report;
- company announcement;
- syndicated article.

# Time and scope

Claims that change over time should record observation/source period.

Claims should be scoped by relevant dimensions such as:

- geography;
- customer population;
- product tier/version;
- currency;
- tax context;
- time period;
- legal entity/brand.

# Confidence

Confidence is evidence quality, not how strongly the researcher believes the thesis.

Consider:

- source directness;
- reliability;
- recency;
- corroboration;
- independence;
- scope match;
- contradiction status.

Prefer transparent `high|medium|low` unless a deterministic numeric rubric is defined.

# Numbers lint

Before publication scan every material number.

It must be:

1. sourced FACT;
2. reproducible ESTIMATE;
3. explicit ASSUMPTION;
4. or removed from factual prose.

# Research integrity

Negative results are valid research outcomes.

Conflicting evidence is valid research data.

Unknowns are valid outputs.

The system is optimized for decision usefulness under uncertainty, not for producing complete-looking reports.
