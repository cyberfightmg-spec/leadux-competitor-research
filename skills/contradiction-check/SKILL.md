# Skill: Contradiction Check

## Mission

Find, classify and preserve conflicts in the evidence before synthesis. The goal is not to force one answer; it is to determine whether claims actually disagree, refer to different scopes/periods, or can be reconciled.

Read first:

- `frameworks/evidence-protocol.md`
- `frameworks/source-quality.md`
- `frameworks/output-contract.md`

## Input

```json
{
  "claims": [],
  "sources": [],
  "high_impact_claim_ids": [],
  "research_scope": {}
}
```

## What counts as a contradiction candidate

Look for claims about the same or closely related:

- entity;
- attribute;
- product/plan;
- geography;
- time period;
- population/segment;
- metric/unit;

that differ materially.

Examples:

- current price differs across sources;
- company says target is SMB while case studies/pricing suggest enterprise focus;
- official feature docs conflict with old reviews;
- two market-size estimates use different market definitions;
- one source says product is available in Russia while current official docs exclude it.

## Reconciliation sequence

For each candidate:

### 1. Scope check

Do the claims refer to the same:

- date/period;
- geography;
- customer segment;
- product version/tier;
- tax/currency/unit;
- legal entity/brand?

If not, this may be a scope difference rather than contradiction.

### 2. Freshness check

A current official source may supersede an older source for a time-sensitive fact.

Do not delete the historical claim; mark it historical.

### 3. Source-directness check

Prefer the source that directly measures/states the relevant fact for the same scope.

Examples:

- current official pricing > old third-party pricing article;
- official registry identity > aggregator profile;
- direct customer quote > paraphrase by affiliate blog for that customer's statement.

### 4. Independence check

Two sources may repeat the same origin. Treat them as one evidence family.

### 5. Definition check

Market size, “customer”, “active user”, “revenue” and similar terms often differ by definition. Preserve definitions before deciding there is conflict.

### 6. Unresolved state

If conflict remains, do not choose the thesis-friendly value. Keep both claims and lower confidence.

## Contradiction types

Use:

```text
TEMPORAL
SCOPE
DEFINITION
SOURCE_CONFLICT
MARKETING_VS_CUSTOMER
PRIMARY_VS_SECONDARY
UNRESOLVED
```

## Required output

Use the shared envelope plus:

```json
{
  "artifacts": {
    "contradictions": [
      {
        "id": "con_001",
        "claim_ids": [],
        "type": "",
        "impact": "high|medium|low",
        "status": "resolved|partially_resolved|unresolved|not_a_true_contradiction",
        "resolution": "",
        "preferred_claim_id": null,
        "reason": "",
        "confidence_effect": "none|lower|major_lower",
        "next_validation": ""
      }
    ],
    "claims_reclassified": [],
    "high_impact_unresolved": []
  }
}
```

## Quality rules

- never average conflicting values just to create one number;
- never prefer a source because it supports the desired recommendation;
- preserve historical changes rather than calling them errors;
- distinguish company claim vs independent/customer evidence;
- unresolved high-impact contradictions must be shown in the final report and sent to evidence verification/red-team.
