# Skill: Red Team

## Mission

Attempt to falsify the main strategic conclusions after the evidence set has been collected, contradiction-checked and substantially verified.

The red team must not merely list generic risks. It must attack the actual thesis using the available evidence and targeted counter-searches where useful.

Read first:

- `frameworks/evidence-protocol.md`
- `frameworks/quality-gates.md`
- `frameworks/output-contract.md`

## Input

```json
{
  "main_theses": [],
  "opportunities": [],
  "recommendations": [],
  "claims": [],
  "verification_results": [],
  "contradictions": [],
  "data_gaps": []
}
```

## Preconditions

Do not run red-team as the first research step.

Preferred order:

```text
research
→ contradiction-check
→ evidence-verification
→ red-team
→ final synthesis
```

## Attack dimensions

For each important thesis ask:

### Demand challenge

- Are we confusing discussion/search interest with buying intent?
- Is the pain frequent enough to matter?
- Is evidence concentrated in a small unhappy subgroup?
- Do customers tolerate the current workaround because the problem is not valuable enough to solve?

### Competition challenge

- Are important competitors hidden by different category language?
- Are substitutes stronger than direct competitors?
- Does a large incumbent already bundle the capability?
- Are we underestimating distribution/brand/switching costs?

### Whitespace challenge

- Is the gap empty because nobody wants it?
- Is it technically/regulatorily expensive?
- Is the segment too small or difficult to reach?
- Is the gap already covered but described differently?

### Pricing/economics challenge

- Are we assuming willingness-to-pay from list prices?
- Are delivery/implementation costs unknown?
- Does apparent low-price whitespace require an unsustainable service model?
- Are pricing units incomparable?

Do not invent economics; unknown economics are themselves a risk/data gap.

### Evidence challenge

- Are the strongest claims based on one source family?
- Are sources stale?
- Are multiple articles copies of one origin?
- Are official marketing claims being treated as outcomes?
- Did verification fail on any recommendation-critical claim?

### Sampling challenge

- Is one geography/platform/competitor overrepresented?
- Are we hearing users but not buyers?
- Are only successful companies visible?
- Are only dissatisfied reviewers visible?

### Execution challenge

- What capability, distribution, trust, integration, regulation or data barrier could prevent entry?
- What must be true operationally for the recommendation to work?

## Counter-searches

When a thesis is high-impact and evidence is weak, run targeted searches designed to find disconfirming evidence.

Examples:

```text
{segment} does not need {solution}
{competitor} alternative complaints
{problem} spreadsheet works
{category} failed implementation
{segment} budget {solution}
```

Adapt queries to local language and market context.

Do not manufacture opposition if no credible counter-evidence exists.

## Severity

Classify red-team findings:

```text
FATAL
MATERIAL
MANAGEABLE
WEAK_COUNTERARGUMENT
```

A `FATAL` finding means the current recommendation cannot responsibly stand without new evidence or a changed strategy.

## Required output

Use the shared envelope plus:

```json
{
  "artifacts": {
    "challenges": [
      {
        "thesis_id": "",
        "challenge": "",
        "severity": "FATAL|MATERIAL|MANAGEABLE|WEAK_COUNTERARGUMENT",
        "supporting_claim_ids": [],
        "counter_evidence": [],
        "unresolved_unknowns": [],
        "effect_on_recommendation": "invalidate|narrow|lower_confidence|none",
        "validation_step": ""
      }
    ],
    "surviving_theses": [],
    "invalidated_theses": [],
    "narrowed_theses": [],
    "highest_sensitivity_assumptions": []
  }
}
```

## Quality rules

- attack the thesis, not the writing style;
- use real counter-evidence when available;
- do not create fake balance against overwhelmingly strong evidence;
- distinguish unknowns from evidence against;
- preserve the strongest surviving version of a thesis after narrowing;
- final synthesis must explicitly incorporate material red-team findings.
