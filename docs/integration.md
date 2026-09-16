# Runtime integration guidance

A wrapper application can combine these skills with search/crawling/data tools. Recommended behavior:

1. detect available providers at runtime;
2. use cheap/public sources first;
3. preserve raw source snapshots and retrieval dates;
4. normalize sources into claim records;
5. call LLMs for semantic extraction, clustering, interpretation and synthesis — not for facts that can be parsed deterministically;
6. keep paid providers optional;
7. never fail the research solely because one optional provider is unavailable.

For a Telegram/WebApp product, keep authentication, billing, databases, queues and API keys in a separate private/product repository.
