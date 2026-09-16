---
name: pricing-intelligence
description: Investigates current pricing, packaging, value metrics, restrictions and pricing whitespace.
---

# Pricing Intelligence

## Capture
- pricing model;
- public tiers;
- entry and highest public price;
- billing period;
- currency and tax/VAT context when stated;
- free plan/trial;
- value metric (seat, usage, location, contact, etc.);
- limits and feature gates;
- annual discounts;
- implementation/setup fees if public;
- enterprise/custom pricing status;
- pricing history when reliably available.

## Analysis
Compare not just price numbers but packaging logic, buyer friction, target segment and switching cost.

## Hard rules
- Current pricing must be date-stamped.
- Do not convert `contact sales` into an invented price.
- Historical cached prices must not be presented as current without verification.
- If comparing currencies, record conversion date/source or avoid false precision.

## Output
Pricing table, packaging insights, price/segment gaps, contradictions and unverified fields.
