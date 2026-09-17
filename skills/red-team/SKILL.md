# Skill: Red Team

## Mission

Attempt to falsify the main strategic conclusions after the evidence set has been collected, contradiction-checked and substantially verified.

The red team must not merely list generic risks. It must attack the actual thesis using the available evidence and targeted counter-searches where useful.

Read first:

- `frameworks/evidence-protocol.md`
- `frameworks/quality-gates.md`
- `frameworks/output-contract.md`
- `frameworks/regional-intelligence.md` when regional analysis is active.

## Input

```json
{
  "main_theses": [],
  "opportunities": [],
  "recommendations": [],
  "claims": [],
  "verification_results": [],
  "contradictions": [],
  "data_gaps": [],
  "regional_analysis": null
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

### Regional competition challenge

When geography is material, ask:

- Are federal/national search results hiding strong local competitors?
- Is Moscow/Saint Petersburg or capital-city evidence overrepresented?
- Did we actually search Tier-A regions independently?
- Are offline/map-directory players underrepresented because they have weak websites?
- Are branches of national chains being double-counted as independent competitors?
- Are similarly named local companies being merged incorrectly?
- Does a competitor registered in a region actually serve that region?
- Is an online competitor being treated as equally strong everywhere without evidence?
- Could a local specialist be more relevant than a nationally visible brand for the selected customer?

### Whitespace challenge

- Is the gap empty because nobody wants it?
- Is it technically/regulatorily expensive?
- Is the segment too small or difficult to reach?
- Is the gap already covered but described differently?

### Regional whitespace challenge

- Is the apparent regional gap only a search-coverage gap?
- Did we check maps/directories and local-language queries?
- Did we check nearby cities and regional chains?
- Does low discovered competition reflect weak demand instead of opportunity?
- Are national players serving the region remotely or through partners?
- Is the region economically attractive enough for the proposed model?
- Are delivery, trust, logistics, regulation or local acquisition costs unknown?

A low competitor count alone is never sufficient evidence of regional opportunity.

### Pricing/economics challenge

- Are we assuming willingness-to-pay from list prices?
- Are delivery/implementation costs unknown?
- Does apparent low-price whitespace require an unsustainable service model?
- Are pricing units incomparable?

For regional pricing also ask:

- Are offers actually comparable between regions?
- Is the sample too small?
- Are premium capital-city providers overrepresented?
- Are tax/service-scope differences driving the observed gap?

Do not invent economics; unknown economics are themselves a risk/data gap.

### Evidence challenge

- Are the strongest claims based on one source family?
- Are sources stale?
- Are multiple articles copies of one origin?
- Are official marketing claims being treated as outcomes?
- Did verification fail on any recommendation-critical claim?
- Does the evidence geography actually match the recommendation geography?

### Sampling challenge

- Is one geography/platform/competitor overrepresented?
- Are we hearing users but not buyers?
- Are only successful companies visible?
- Are only dissatisfied reviewers visible?
- Is regional VOC based on too few entities or one platform?

### Execution challenge

- What capability, distribution, trust, integration, regulation or data barrier could prevent entry?
- What must be true operationally for the recommendation to work?
- If the recommendation is regional, what local capability or distribution must exist?

## Counter-searches

When a thesis is high-impact and evidence is weak, run targeted searches designed to find disconfirming evidence.

Examples:

```text
{segment} does not need {solution}
{competitor} alternative complaints
{problem} spreadsheet works
{category} failed implementation
{segment} budget {solution}
{category} {region}
{category synonym} {city}
{JTBD} {region}
{competitor} {city}
{service} {city} reviews
```

For regional whitespace, explicitly search alternative terms, maps/directories, branches, nearby markets and substitutes.

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
        "affected_geography": [],
        "unresolved_unknowns": [],
        "effect_on_recommendation": "invalidate|narrow|lower_confidence|none",
        "validation_step": ""
      }
    ],
    "regional_bias_findings": [],
    "false_regional_whitespace_findings": [],
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
- narrow a national thesis to specific regions when evidence supports only those regions;
- explicitly test capital-city and national-search bias;
- preserve the strongest surviving version of a thesis after narrowing;
- final synthesis must explicitly incorporate material red-team findings.
