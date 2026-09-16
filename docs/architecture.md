# Architecture

The repository intentionally separates **skills** from **tools**.

```text
User intent
  → Root router
  → Research plan
  → Discovery
  → Specialist skills
  → Evidence ledger
  → Contradiction check
  → Verification
  → Red team
  → Report
```

A production application may persist sources, claims, insights and opportunities using the JSON schemas under `/schemas`. Search/crawling providers should be implemented through adapters outside the skill definitions.
