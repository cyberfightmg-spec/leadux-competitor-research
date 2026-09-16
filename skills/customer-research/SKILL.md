# Skill: Customer Research

## Mission

Build an evidence-based view of customer jobs, pains, triggers, desired outcomes, objections, buying criteria and alternatives.

Do not invent personas. Do not confuse competitor messaging with customer reality.

Read first:

- `frameworks/voc-framework.md`
- `frameworks/evidence-protocol.md`
- `frameworks/output-contract.md`

## Input

```json
{
  "market": "",
  "target_customer": "",
  "competitors": [],
  "geography": [],
  "research_depth": "quick|standard|deep"
}
```

## Research modes

Use one or more depending on available data:

### Existing evidence

User-provided interviews, notes, sales calls, support tickets, surveys or documents.

### Public signal mining

Reviews, forums, communities, comments, public case studies and buyer discussions.

### Primary research planning

When evidence is insufficient, propose interview/survey/experiment questions. Do not fabricate responses.

## What to extract

### Jobs-to-be-done

What progress is the customer trying to make?

Separate:

- functional job;
- emotional job;
- social job;

only where evidence supports it.

### Pains

Capture:

- problem statement;
- context;
- current workaround;
- consequence;
- frequency signal;
- intensity signal;
- segment.

### Trigger events

Look for events that make the customer actively seek change:

- growth;
- hiring;
- new regulation;
- failure of current tool;
- rising volume;
- price increase;
- workflow complexity;
- new channel/location/product.

Treat triggers as hypotheses until supported by customer evidence.

### Desired outcomes

Capture outcomes in customer language when possible.

### Objections

Examples:

- cost;
- implementation effort;
- migration risk;
- trust;
- security;
- missing integration;
- complexity;
- team adoption.

### Alternatives

What does the customer use today?

This may include direct competitors, spreadsheets, messaging apps, internal staff, agencies, manual processes or doing nothing.

### Buying criteria

Infer only from repeated evidence such as reviews, comparisons, interview data or public buyer discussions.

## Evidence confidence

Suggested qualitative confidence:

### High

Theme appears unprompted across 3+ reasonably independent source groups and matches the target segment.

### Medium

Theme appears across 2 independent source groups or repeatedly in one highly relevant segment-specific source.

### Low

Single source, weak segment match, prompted response, or ambiguous context.

Confidence is not frequency alone.

## Recency

For changing products/markets, weight recent evidence more strongly. Public customer evidence from the last 12 months is generally more relevant, while older evidence may still be useful for persistent jobs/pains if labeled by date.

## Sample-bias checks

Before promoting a theme ask:

- Are we seeing mostly unhappy reviewers?
- Are users unusually technical?
- Is one competitor overrepresented?
- Is one geography/platform dominating?
- Are we hearing users but not buyers?
- Are reviews incentivized or copied?

## Segmentation

Do not create demographic/persona details without evidence.

Segment by decision-relevant variables such as:

- company size;
- role;
- workflow maturity;
- use case;
- vertical;
- geography;
- current alternative;
- usage volume.

## Required output

Use the shared envelope plus:

```json
{
  "artifacts": {
    "segments": [],
    "jobs": [],
    "pains": [],
    "trigger_events": [],
    "desired_outcomes": [],
    "objections": [],
    "alternatives": [],
    "buying_criteria": [],
    "language_patterns": [],
    "sample_bias_notes": []
  }
}
```

Each material theme should include source/claim IDs and confidence.

## Quality rules

- personas must emerge from evidence;
- a competitor case study is first-party evidence, not independent VOC;
- a repeated phrase across copied reviews is not independent corroboration;
- one loud complaint must not become a market-wide pain;
- separate buyer from user when evidence indicates different roles;
- preserve exact short customer phrases when legally/ethically appropriate, otherwise paraphrase faithfully.
