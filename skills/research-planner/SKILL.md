---
name: research-planner
description: Converts a competitor-research request into a scoped, evidence-aware research plan.
---

# Research Planner

## Use when
At the start of any non-trivial competitor or market research task.

## Inputs
- user objective;
- market/category/product description;
- geography;
- target customer if known;
- known competitors if any;
- available tools/capabilities;
- requested depth.

## Workflow
1. Rewrite the user's request into a precise decision question.
2. Define customer JTBD and purchasing context.
3. Expand the category to include substitutes/DIY alternatives.
4. Identify key unknowns that could change the decision.
5. Create research questions by dimension: discovery, positioning, product, pricing, customer/VOC, GTM, signals, whitespace.
6. Choose source classes needed for each question.
7. Mark tasks that can run in parallel.
8. Set stop conditions based on evidence saturation, not arbitrary page counts.
9. Record capability limitations and expected data gaps.

## Output
Return a structured plan with `scope`, `research_questions`, `required_skills`, `source_plan`, `priority`, `parallel_groups`, `stop_conditions`, and `known_limitations`.

## Anti-patterns
Do not begin with a fixed list of competitors. Do not use the same source mix for SaaS, local services, ecommerce and B2B services.
