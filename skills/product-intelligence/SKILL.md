# Skill: Product Intelligence

## Mission

Compare how competitors solve the customer's job, not just whether a feature checkbox exists.

The output should reveal workflow differences, product maturity, implementation friction, integration depth and defensible differentiation.

Read first:

- `frameworks/evidence-protocol.md`
- `frameworks/output-contract.md`
- `frameworks/fallback-policy.md`

## Input

```json
{
  "competitors": [],
  "customer_job": "",
  "target_customer": "",
  "research_depth": "quick|standard|deep"
}
```

## Product research dimensions

Investigate only dimensions relevant to the market:

- core workflows;
- primary use cases;
- feature groups;
- AI/automation depth;
- integrations;
- API/webhooks;
- customization;
- onboarding/setup;
- implementation requirements;
- collaboration/roles;
- mobile/desktop/web support;
- reporting/analytics;
- security/compliance claims;
- enterprise controls;
- support/training;
- localization/languages.

## Workflow-first analysis

Start with the customer job.

For each competitor answer:

1. What triggers the workflow?
2. What steps does the user perform?
3. What does the product automate?
4. Where is human input required?
5. What is the output/outcome?
6. What systems must be integrated?
7. What obvious friction or dependency exists?

Feature presence alone is insufficient.

## Evidence hierarchy

Prefer:

1. current official documentation;
2. current product/feature pages;
3. public demos/help centers;
4. changelog/release notes;
5. official app/integration listings;
6. customer reviews for observed usability/reliability;
7. secondary reviews only when primary evidence is unavailable.

## Feature status vocabulary

Use:

```text
VERIFIED_AVAILABLE
VERIFIED_LIMITED
VERIFIED_NOT_AVAILABLE
CLAIMED
UNCLEAR
NOT_CHECKED
```

Never use `VERIFIED_NOT_AVAILABLE` merely because a feature was not found on the homepage.

## Product maturity

Do not create a magical maturity score without evidence.

Assess dimensions separately, such as:

- workflow completeness;
- integration breadth/depth;
- configuration depth;
- enterprise controls;
- release velocity;
- reliability evidence;
- implementation complexity.

Each assessment requires claim IDs and confidence.

## Differentiation test

A feature is not automatically differentiation.

For a candidate differentiator ask:

- Is it uncommon among relevant competitors?
- Is it relevant to the target customer's job?
- Is there evidence customers value it?
- Is it difficult/expensive to copy?
- Is it part of the competitor's positioning or just a hidden capability?

Classify as:

```text
TABLE_STAKES
MINOR_DIFFERENTIATOR
MEANINGFUL_DIFFERENTIATOR
UNCLEAR
```

## Required output

Use the shared envelope plus:

```json
{
  "artifacts": {
    "workflow_comparison": [],
    "capability_matrix": [],
    "integration_comparison": [],
    "implementation_notes": [],
    "differentiators": [],
    "table_stakes": [],
    "product_gaps": [],
    "uncertain_features": []
  }
}
```

## Quality rules

- compare the same product tier/version where possible;
- state when a feature requires enterprise/custom plans;
- preserve date/version context;
- do not infer quality from feature count;
- do not call a capability absent after a shallow search;
- separate official claims from customer-reported experience;
- route material conflicts to `contradiction-check`.
