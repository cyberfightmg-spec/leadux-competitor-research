# Changelog

## 0.3.0 — 2026-09-17

### Regional Intelligence

- Added new `skills/regional-intelligence/SKILL.md`.
- Added `frameworks/regional-intelligence.md`.
- Added machine-readable `schemas/region.schema.json`.
- Updated root `SKILL.md` so deep country-level research activates regional intelligence when sub-national competition is material.
- Added national vs regional/local discovery waves.
- Added independent geographic-role classification:
  - NATIONAL
  - MULTI_REGIONAL
  - REGIONAL
  - LOCAL
  - ONLINE_ONLY
  - UNKNOWN
- Expanded competitor geography model to separate:
  - registered region
  - headquarters
  - physical locations
  - service regions
  - verified regions
  - national coverage
- Added Tier A/B/C regional prioritization and transparent sampling fallback.
- Added regional pricing rules with explicit sample size, comparability, observation dates and coverage limitations.
- Added regional VOC safeguards including `INSUFFICIENT_REGIONAL_SAMPLE`.
- Added regional GTM/channel-pattern analysis.
- Added regional whitespace methodology requiring demand + weak/different coverage + entry feasibility.
- Added false-regional-whitespace counter-search requirements.
- Added Regional Coverage Gate to `frameworks/quality-gates.md`.
- A deep country-level study in a region-sensitive market can no longer receive `VERIFIED` status when material regional research is missing.
- Updated `skills/research-planner` with regional-materiality detection, geographic level selection and region prioritization.
- Updated `skills/competitor-discovery` to avoid national-search bias and run independent regional discovery waves.
- Updated `skills/evidence-verification` to audit geographic scope, service coverage, regional counts, pricing samples, VOC samples and regional whitespace.
- Updated `skills/red-team` to attack capital-city bias, national-search bias, branch duplication and false regional whitespace.
- Expanded `source-packs/russia.md` with a Russia-specific regional research workflow.
- Updated `prompts/deep-russia-research.md` so deep Russia research automatically includes the regional layer when material.
- Updated `frameworks/report-framework.md` with a dedicated Regional Competitive Landscape, regional pricing/VOC/GTM and regional coverage gaps.
- Updated README to expose Regional Intelligence as a first-class project capability.

## 0.2.0 — 2026-09-16

### Production research layer

- Upgraded root `SKILL.md` into a full research router.
- Added capability detection and geography-aware source-pack selection.
- Added production multi-wave search strategy and saturation rules.
- Added graceful fallback policy for unavailable/protected sources and optional APIs.
- Added shared structured skill output contract.
- Added explicit research quality gates.
- Added Russia Source Pack with official/public source guidance and Russia-specific integrity rules.
- Productionized:
  - research-planner
  - competitor-discovery
  - competitor-profiling
  - product-intelligence
  - pricing-intelligence
  - customer-research
  - voice-of-customer
  - gtm-intelligence
  - strategic-signals
  - market-whitespace
  - contradiction-check
  - evidence-verification
  - red-team
  - market-monitoring
- Strengthened Evidence Protocol, Source Quality, Confidence, Research Depth and Report frameworks.
- Expanded machine-readable source, claim, insight, competitor, opportunity, research and report schemas.
- Added shared `skill-output.schema.json`.
- Added ready-to-use `prompts/deep-russia-research.md`.
- Updated README with v0.2 workflow, Russia instructions and LeadUX AI links.

## 0.1.0 — 2026-09-16

- Initial public skill repository.
- Root research router.
- Modular competitor intelligence skills.
- Evidence, VOC, whitespace and reporting foundations.
- Initial schemas, examples and prompts.
- Security and third-party notices.
