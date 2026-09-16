# Deep Competitor Research — Russia

Copy this prompt into an AI agent together with the repository URL.

```text
Изучи репозиторий:
https://github.com/cyberfightmg-spec/leadux-competitor-research

ОБЯЗАТЕЛЬНО сначала прочитай:
- SKILL.md
- AGENTS.md
- frameworks/evidence-protocol.md
- frameworks/search-strategy.md
- frameworks/fallback-policy.md
- frameworks/quality-gates.md
- source-packs/russia.md

После этого загружай только нужные для задачи skills.

ЗАДАЧА

Проведи глубокое исследование конкурентов и рыночной ситуации.

Ниша / рынок:
[ВСТАВЬТЕ НИШУ]

География:
Россия

Целевая аудитория / клиент, если известна:
[ВСТАВЬТЕ ИЛИ ОСТАВЬТЕ UNKNOWN]

Цель исследования:
[например: найти рыночные пробелы / понять конкурентов / проверить идею / выбрать позиционирование / сравнить цены]

Режим:
DEEP

ПРАВИЛА

1. Не ограничивайся очевидными брендами.
2. Ищи DIRECT, INDIRECT, SUBSTITUTE, DIY и ADJACENT альтернативы.
3. Не принимай категорию из запроса за окончательное определение рынка — сначала определи JTBD и реальные альтернативы покупателя.
4. Используй русские и английские варианты терминов, синонимы, аббревиатуры и язык клиентов.
5. Для фактов по российским компаниям и рынку при необходимости приоритизируй официальные источники из source-packs/russia.md.
6. Маркетинговое заявление компании является фактом только о том, что компания это заявляет. Не превращай его в независимый факт об эффективности.
7. Не придумывай revenue, клиентов, CAC, churn, conversion, долю рынка, цены, штат, внутренние процессы или эффективность каналов.
8. Каждое существенное утверждение классифицируй:
   FACT / ESTIMATE / HYPOTHESIS / ASSUMPTION / NOT_FOUND.
9. Для FACT указывай источник и дату/период, когда это важно.
10. Для ESTIMATE показывай формулу, исходные данные и assumptions.
11. NOT_FOUND используй только после документированного поиска по нескольким разумным source/query families.
12. Не считай несколько перепечаток одной новости независимыми подтверждениями.
13. Search snippets используй для discovery, а не как предпочтительное финальное доказательство.
14. Если страница защищена/недоступна — отметь источник как protected/unavailable и используй fallback. Не делай вывод, что информация/функция отсутствует.
15. Не обходи CAPTCHA, paywall, authentication или другие ограничения доступа.

ПРОЦЕСС

Выполни исследование волнами:

WAVE 1 — определить рынок/JTBD, vocabulary и широко найти кандидатов.
WAVE 2 — проверить сущности и классифицировать конкурентов.
WAVE 3 — глубоко исследовать Tier A конкурентов:
- positioning
- product/workflows
- pricing/packaging
- customers/VOC
- GTM/distribution
- strategic signals
WAVE 4 — закрыть только важные пробелы и проверить альтернативные объяснения.

Для Tier A проведи глубокий анализ.
Tier B используй для контекста.
Tier C достаточно оставить на карте рынка.

ОБЯЗАТЕЛЬНЫЙ ФИНАЛЬНЫЙ QUALITY PIPELINE

Перед финальным ответом выполни строго по порядку:

1. contradiction-check
2. evidence-verification
3. red-team
4. final synthesis

ФИНАЛЬНЫЙ ОТЧЁТ

Сделай отчёт по frameworks/report-framework.md.

Обязательно включи:

- Scope + дата исследования
- Market/JTBD definition
- Competitive landscape
- Direct / indirect / substitutes / DIY / adjacent
- Tier A competitors
- Positioning comparison
- Product/workflow comparison
- Pricing/packaging
- Customer pains + VOC
- GTM/distribution
- Strategic signals
- Market whitespace hypotheses
- False-whitespace checks
- Contradictions
- Evidence verification failures/limitations
- Red-team findings
- Где имеет смысл конкурировать
- Где НЕ имеет смысла конкурировать
- Recommendations
- What to validate next
- Data gaps
- Sources

Для каждой стратегически важной рекомендации покажи:
ACTION
WHY
EVIDENCE
CONTRADICTORY EVIDENCE
CONFIDENCE
RISK
WHAT TO TEST NEXT

В конце укажи Research Integrity Status:
VERIFIED / VERIFIED_WITH_GAPS / DEGRADED / INSUFFICIENT_EVIDENCE.

Главная цель:
не написать красивый обзор, а максимально снизить неопределённость и показать, какие выводы действительно подтверждены данными.
```
