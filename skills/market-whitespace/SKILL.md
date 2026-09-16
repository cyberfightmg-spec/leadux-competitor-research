# Skill: Market Whitespace

## Mission

Identify potentially valuable gaps in competitor coverage, then test whether those gaps reflect real demand and realistic entry conditions.

Whitespace is not “something competitors do not mention.” A gap is strategically useful only when there is evidence that a relevant customer segment/job exists and current alternatives cover it poorly.

Read first:

- `frameworks/whitespace-framework.md`
- `frameworks/evidence-protocol.md`
- `frameworks/output-contract.md`

## Input

```json
{
  "competitor_profiles": [],
  "customer_research": {},
  "voc": {},
  "pricing": {},
  "gtm": {},
  "product_intelligence": {},
  "target_customer": "",
  "geography": []
}
```

## Whitespace dimensions

Look for gaps across:

- audience / segment;
- JTBD / workflow;
- price / packaging;
- business model;
- product capability;
- implementation simplicity;
- integration;
- geography;
- language/localization;
- distribution/channel;
- positioning/message;
- trust/compliance;
- service level.

## Three-part opportunity test

Every candidate whitespace must pass three independent questions.

### 1. Demand exists?

Evidence may include:

- repeated customer pain;
- explicit search/alternative behavior;
- buying/switching discussions;
- public procurement where relevant;
- repeated workaround usage;
- segment-specific demand signals;
- existing spend on imperfect substitutes.

Online discussion alone is not sufficient for strong buying-demand claims.

### 2. Coverage is weak?

Evidence may include:

- few relevant competitors serving the segment/job;
- repeated complaints tied to the same uncovered need;
- pricing/packaging mismatch;
- missing workflow coverage;
- poor localization/geographic access;
- weak distribution where audience presence is evidenced.

“Feature not found on homepage” is not evidence of weak coverage.

### 3. Entry is plausible?

Consider observable constraints:

- technical complexity;
- integration requirements;
- regulation/compliance;
- implementation/service burden;
- incumbent distribution;
- switching costs;
- trust/brand barrier;
- capital or data requirements.

Do not invent CAC, margins or implementation costs. Mark unknown economics as assumptions/data gaps.

## False-whitespace test

Before promoting a gap, ask:

- Could competitors ignore it because customers do not care?
- Could the segment be too small/unprofitable?
- Could regulation/implementation make it unattractive?
- Could customers prefer a substitute for structural reasons?
- Are we seeing a search/data visibility gap instead of a market gap?
- Is the “gap” already covered under different language?

Run targeted searches against these alternative explanations.

## Opportunity confidence

Do not score opportunity only by LLM intuition.

Track dimensions separately:

- demand evidence;
- coverage evidence;
- entry plausibility;
- source diversity;
- recency;
- contradictory evidence.

Use `high|medium|low` unless a transparent scoring rubric is explicitly defined.

## Required output

Use the shared envelope plus:

```json
{
  "artifacts": {
    "opportunities": [
      {
        "opportunity_id": "opp_001",
        "title": "",
        "type": "audience|workflow|pricing|business_model|product|channel|geography|positioning|other",
        "target_segment": "",
        "demand_claim_ids": [],
        "coverage_claim_ids": [],
        "entry_claim_ids": [],
        "contradicting_claim_ids": [],
        "risks": [],
        "unknowns": [],
        "confidence": "high|medium|low",
        "validation_test": ""
      }
    ],
    "rejected_whitespace": [],
    "false_whitespace_checks": []
  }
}
```

## Recommendation rule

Do not call whitespace “best opportunity” until contradiction-check, evidence-verification and red-team are complete.

The output of this skill is a set of evidence-backed **opportunity hypotheses**, not final truth.
