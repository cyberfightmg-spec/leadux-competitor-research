# Skill: Voice of Customer

## Mission

Mine, normalize and cluster real customer language so the research captures how customers describe problems, alternatives, outcomes, objections and switching decisions in their own words.

This skill is not sentiment decoration. Its purpose is to create usable evidence for positioning, product strategy, content, sales and market-gap analysis.

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
  "source_candidates": [],
  "research_depth": "quick|standard|deep"
}
```

## Source families

Use relevant public/authorized sources such as:

- product/service reviews;
- app-store reviews;
- marketplace reviews;
- Reddit / forums / professional communities;
- YouTube comments;
- public social discussions;
- support/community threads;
- comparison/switching discussions;
- user-provided interview/support/sales data.

For Russia, consider the guidance in `source-packs/russia.md`.

## Unit of analysis

A VOC record should preserve enough context to avoid quote mining.

```json
{
  "voc_id": "voc_001",
  "source_id": "src_001",
  "competitor": "",
  "segment": "",
  "date": "",
  "language": "ru",
  "type": "pain|praise|request|objection|switch|outcome|workaround",
  "theme": "",
  "text_or_paraphrase": "",
  "intensity": "high|medium|low|unknown",
  "context": "",
  "claim_ids": []
}
```

## Extraction rules

Extract only what the text reasonably supports.

Example:

Customer says:

> “Настраивали два дня, но потом работает нормально.”

Supported records may include:

- implementation/setup friction;
- eventual satisfaction/reliability perception.

Unsupported:

- company has poor support;
- all users need two days;
- product is hard for SMB generally.

## Theme clustering

Cluster semantically similar statements, but preserve original records.

Potential themes:

- setup complexity;
- price/value;
- missing integration;
- reliability;
- support;
- speed;
- UX;
- reporting;
- customization;
- mobile experience;
- migration;
- automation limits;
- trust/security.

Do not force every market into this list.

## Theme scoring

For each theme track separately:

- frequency;
- source diversity;
- recency;
- segment fit;
- intensity;
- competitor distribution.

Do not collapse these into one opaque “sentiment score.”

Example:

```json
{
  "theme": "setup complexity",
  "mentions": 27,
  "independent_source_groups": 4,
  "segment_fit": "high",
  "recency": "high",
  "intensity": "medium",
  "confidence": "high"
}
```

## Switching analysis

Pay special attention to explicit switching evidence:

- “moved from X to Y because…”;
- “looking for an alternative because…”;
- “we stayed with X because…”;
- “we went back to spreadsheets because…”.

Switching evidence is often more decision-useful than generic ratings.

## Praise vs purchase drivers

A praised feature is not automatically a purchase driver.

Label separately:

- liked after purchase;
- reason for choosing;
- reason for staying;
- reason for switching;
- reason for rejecting.

Only claim a buying criterion when evidence directly supports it.

## Source independence and spam

Check for:

- duplicate/cross-posted reviews;
- suspicious identical wording;
- one campaign/platform dominating;
- vendor testimonials masquerading as independent reviews;
- affiliate content.

Lower confidence where independence is weak.

## Required output

Use the shared envelope plus:

```json
{
  "artifacts": {
    "voc_records": [],
    "themes": [],
    "switching_reasons": [],
    "objections": [],
    "desired_outcomes": [],
    "workarounds": [],
    "exact_language_patterns": [],
    "source_bias_notes": []
  }
}
```

## Quality rules

- never fabricate quotes;
- keep quote length minimal and context-preserving;
- do not infer demographic details not present;
- do not equate rating with market demand;
- do not treat one platform as representative of the whole market;
- expose sample size and source diversity;
- send contested themes to `contradiction-check` when they materially affect strategy.
