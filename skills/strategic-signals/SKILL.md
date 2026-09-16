---
name: strategic-signals
description: Detects recent competitor changes and strategic direction signals with explicit confidence.
---

# Strategic Signals

Look for dated changes in:
- pricing/packaging;
- positioning;
- new products/features;
- integrations;
- geography/language;
- vertical focus;
- partnerships;
- hiring patterns;
- funding/acquisition;
- product shutdowns;
- review sentiment shifts;
- release velocity.

## Interpretation rule
One signal rarely proves strategy. Build hypotheses from multiple independent signals.

Example: enterprise page + SSO release + several enterprise sales roles may support a hypothesis of enterprise movement. Label it a hypothesis unless explicitly announced.

## Output
`event`, `date`, `observed facts`, `interpretation`, `supporting_claim_ids`, `contradicting_claim_ids`, `confidence`.
