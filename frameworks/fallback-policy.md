# Source & Tool Fallback Policy

Research should degrade gracefully when a source or integration is unavailable.

## Default acquisition order

Prefer the cheapest, most direct and most auditable method first:

1. official/public page or registry;
2. normal HTTP fetch / text extraction;
3. search engine discovery + direct source open;
4. browser rendering for JS-heavy pages;
5. optional crawler/API integration;
6. alternative independent source;
7. record a data gap.

Do not jump to expensive or opaque tooling if a primary public source is available.

## Protected pages

If a page is behind authentication, CAPTCHA, paywall or explicit access protection:

- do not bypass it;
- set `access_status = protected`;
- search for an authorized/public alternative;
- do not mark the underlying fact as absent.

## Optional integrations

Firecrawl, DataForSEO, UnifAPI, commercial social APIs and similar tools are optional accelerators.

If unavailable:

- skip the integration;
- preserve the research question;
- attempt another legal source family;
- lower coverage/confidence only where the missing source materially matters.

## Browser fallback

Use a browser only when static fetching cannot retrieve materially important content. Do not use stealth or anti-detection features to evade access controls.

## Conflicting sources

Do not silently select the value that best fits the thesis.

When sources conflict:

1. prefer the more direct/primary source for the same period and scope;
2. check whether dates, units, population or product tiers differ;
3. preserve both claims if the conflict remains;
4. pass the issue to `contradiction-check`;
5. lower confidence until reconciled.

## Stale sources

A source can be valid but stale. Mark freshness separately from reliability.

Suggested review windows, adjustable by market:

- pricing: prefer observations within 30 days;
- product/features: prefer within 90 days;
- jobs/hiring: prefer within 30 days;
- customer language: weight the last 12 months, with recent evidence favored;
- official annual statistics: use the latest released period and state the period explicitly.

## Failure semantics

`tool failed` != `market is quiet`.

`page protected` != `feature absent`.

`no result in one source` != `NOT_FOUND`.

Every failure that affects coverage must be visible in `data_gaps` or run status.
