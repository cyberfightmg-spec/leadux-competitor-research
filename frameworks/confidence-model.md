# Confidence Model v0.2

Confidence represents the strength of evidence supporting a specific claim or insight. It is not an “AI certainty” score and not an opportunity score.

## Default output

Prefer qualitative levels:

```text
HIGH
MEDIUM
LOW
```

A numeric score may be used internally only when its components and thresholds are deterministic and visible.

## Confidence dimensions

Evaluate independently:

### Directness

Does the source directly establish the claim?

### Reliability

Is the source appropriate for this type of fact?

### Relevance / scope match

Does evidence match the same entity, geography, segment, product, period and unit?

### Freshness

Is it current enough for the research question?

### Corroboration

Is the finding supported by additional evidence?

### Independence

Are corroborating sources genuinely independent?

### Contradiction state

Does unresolved evidence conflict with the claim?

### Sample quality

For VOC/customer findings, is the sample diverse and relevant enough?

## Suggested interpretation

### HIGH

Typically:

- direct/relevant source;
- current for the claim;
- strong scope match;
- independently corroborated when warranted;
- no material unresolved contradiction.

### MEDIUM

Useful evidence exists but one or more dimensions are limited, for example:

- one strong source only;
- modest sample;
- indirect evidence;
- some staleness;
- incomplete corroboration;
- non-critical unresolved uncertainty.

### LOW

Typically:

- weak/indirect source;
- poor scope match;
- stale evidence;
- one anecdote;
- unclear independence;
- major unresolved contradiction;
- important missing inputs.

## Claim vs insight confidence

An insight derived from several claims should not automatically inherit the highest claim confidence.

Example:

```text
Claim A: HIGH
Claim B: HIGH
Interpretation connecting A+B: may still be MEDIUM
```

because the causal/strategic inference itself may be uncertain.

## Opportunity confidence

Keep evidence confidence separate from opportunity attractiveness.

Example:

```text
Demand evidence: HIGH
Competitor-coverage evidence: MEDIUM
Entry feasibility evidence: LOW

Opportunity confidence: LOW/MEDIUM
```

A potentially attractive opportunity with weak feasibility evidence should not become “85% confident.”

## Confidence downgrades

Lower confidence when:

- source is stale for a time-sensitive claim;
- independent corroboration collapses into one origin;
- entity identity is uncertain;
- important scope differs;
- contradiction remains unresolved;
- result depends on a high-sensitivity assumption;
- tool/source failure prevents meaningful verification.

## Confidence upgrades

Increase confidence only when new evidence directly resolves uncertainty, for example:

- official current pricing verifies a secondary price claim;
- independent VOC sources reproduce the same segment-specific theme;
- an official registry resolves entity ambiguity;
- targeted search resolves a contradiction.

More words or more search results do not increase confidence by themselves.
