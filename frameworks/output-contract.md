# Shared Skill Output Contract

Every research skill MUST return structured output that can be consumed by another skill or agent.

## Required envelope

```json
{
  "skill": "competitor-discovery",
  "status": "complete|partial|degraded|blocked",
  "coverage": {
    "attempted": [],
    "completed": [],
    "missing": []
  },
  "sources": [],
  "claims": [],
  "artifacts": {},
  "data_gaps": [],
  "next_actions": []
}
```

## Status meanings

- `complete` — required dimensions were covered to the selected research depth.
- `partial` — useful result exists but one or more non-critical dimensions are missing.
- `degraded` — important sources/tools were unavailable; conclusions must explicitly reflect reduced confidence.
- `blocked` — the skill cannot responsibly produce its core output.

Never convert `partial` or `degraded` into an apparently complete narrative report.

## Source object

Minimum fields:

```json
{
  "source_id": "src_...",
  "url": "https://...",
  "title": "...",
  "source_type": "official|company|registry|review|community|media|dataset|other",
  "source_tier": "A|B|C|D|E|F",
  "published_at": null,
  "observed_at": "YYYY-MM-DD",
  "independence_group": "origin_...",
  "access_status": "ok|protected|unavailable|partial"
}
```

## Claim object

Every material claim must follow `schemas/claim.schema.json` and the evidence protocol.

Allowed evidence classes:

- `FACT`
- `ESTIMATE`
- `HYPOTHESIS`
- `ASSUMPTION`
- `NOT_FOUND`

## Data gaps

A data gap is not a failure. Record:

```json
{
  "question": "What could not be established?",
  "attempted_sources": [],
  "reason": "protected|no_public_data|tool_unavailable|conflicting_sources|other",
  "impact": "high|medium|low",
  "recommended_validation": "..."
}
```

## Composability rule

Skills should return evidence and structured findings, not only prose. A later synthesis step may create prose, but must preserve claim/source traceability.
