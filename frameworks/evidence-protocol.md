# Evidence Protocol

Every material statement must be classifiable.

## Evidence types

### FACT
Directly supported by a source appropriate to the claim.

Required: source URL, observed/retrieved date, scope, and exact value/text where material.

### ESTIMATE
Calculated or reported approximate value.

Required: method, formula or originating estimator, inputs, assumptions and uncertainty.

### HYPOTHESIS
Interpretation supported by evidence but not directly proven.

Required: supporting claim IDs, contradictory evidence if any, and validation path.

### ASSUMPTION
A working premise necessary to proceed.

Required: why it is needed and how it could be tested.

### NOT_FOUND
Research was performed but evidence was not located in the checked search space.

Required: where/how searched, date, and limitations. `NOT_FOUND` must never be rewritten as "does not exist".

## Evidence chain

```text
Source → Claim → Insight → Strategic conclusion
```

Claims must not cite other unsourced model prose as evidence.

## Mutable facts

Pricing, features, positioning, employee counts, plans, availability and policies can change. Always add an observed date and prefer current primary sources.

## Numerical claims

Every important number must have either:

- a primary/secondary source; or
- a reproducible calculation linked to sourced inputs and labeled assumptions.
