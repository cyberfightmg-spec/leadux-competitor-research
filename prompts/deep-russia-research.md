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
- frameworks/regional-intelligence.md
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
[например: найти рыночные пробелы / понять конкурентов / проверить идею / выбрать позиционирование / сравнить цены / найти региональные возможности]

Режим:
DEEP

ПРАВИЛА

1. Не ограничивайся очевидными федеральными брендами.
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

РЕГИОНАЛЬНАЯ ЛОГИКА

Сначала определи, материальна ли региональная конкуренция для этой ниши.

Если ниша зависит от города/региона, физического присутствия, локального доверия, локальных цен, карт/каталогов, регионального спроса или региональных каналов — ОБЯЗАТЕЛЬНО используй:

skills/regional-intelligence/SKILL.md

Для таких рынков нельзя считать федеральную выдачу полной картиной России.

Разделяй:

- NATIONAL
- MULTI_REGIONAL
- REGIONAL
- LOCAL
- ONLINE_ONLY

И отдельно:

- registered_region
- headquarters
- physical_locations
- service_regions
- verified_regions

Регион регистрации не является доказательством работы в регионе.

Не исследуй все регионы одинаково автоматически. Сначала сформируй Tier A / Tier B / Tier C регионы или прозрачную sampling strategy.

ПРОЦЕСС

WAVE 1 — определить рынок/JTBD, vocabulary и широко найти федеральных/национальных кандидатов.

WAVE 2 — проверить сущности и классифицировать конкурентов.

WAVE 3 — если региональность материальна, выполнить отдельный REGIONAL DISCOVERY:
- выбрать Tier A/B/C регионы/города;
- запускать category + region/city запросы;
- запускать JTBD/problem + region/city запросы;
- использовать Yandex Maps / 2GIS и другие релевантные локальные источники;
- искать локальных игроков, которых нет в федеральной выдаче;
- проверять филиалы и service regions национальных игроков;
- исключать дубли филиалов одной сети.

WAVE 4 — глубоко исследовать Tier A конкурентов:
- positioning
- product/workflows
- pricing/packaging
- customers/VOC
- GTM/distribution
- strategic signals
- geographic role / service coverage

WAVE 5 — сравнить регионы, если позволяют данные:
- discovered competitor landscape
- observed price differences
- positioning patterns
- VOC patterns
- GTM/channel patterns
- regional whitespace
- coverage confidence

WAVE 6 — закрыть важные пробелы и провести false-whitespace/counter-searches.

РЕГИОНАЛЬНЫЕ ЦЕНЫ

Если сравниваешь цены по регионам, обязательно показывай:
- что именно сравнивается;
- sample size (n);
- min/max observed;
- median только если выборка и сопоставимость это позволяют;
- валюту;
- дату/период;
- source coverage;
- ограничения выборки.

Не называй convenience sample «средней ценой региона».

РЕГИОНАЛЬНЫЙ VOC

Не делай региональные проценты и выводы на маленькой выборке.
Если данных недостаточно, используй:
INSUFFICIENT_REGIONAL_SAMPLE.

ОБЯЗАТЕЛЬНЫЙ ФИНАЛЬНЫЙ QUALITY PIPELINE

Перед финальным ответом выполни строго по порядку:

1. contradiction-check
2. evidence-verification
3. red-team
4. regional coverage gate, если региональность материальна
5. final synthesis

ФИНАЛЬНЫЙ ОТЧЁТ

Сделай отчёт по frameworks/report-framework.md.

Обязательно включи:

- Scope + дата исследования
- Market/JTBD definition
- Competitive landscape
- Direct / indirect / substitutes / DIY / adjacent
- National / multi-regional / regional / local structure
- Regional Competitive Landscape, если региональность материальна
- Tier A competitors
- Positioning comparison
- Product/workflow comparison
- Pricing/packaging
- Regional pricing comparison, если доказуемо
- Customer pains + VOC
- Regional VOC differences, только если sample достаточен
- GTM/distribution
- Regional GTM/channel differences, если доказуемо
- Strategic signals
- Market whitespace hypotheses
- Regional whitespace hypotheses
- False-whitespace checks
- Contradictions
- Evidence verification failures/limitations
- Red-team findings
- Где имеет смысл конкурировать
- Где НЕ имеет смысла конкурировать
- Recommendations
- What to validate next
- Data gaps
- Regional coverage gaps
- Sources

Для региональной таблицы, если она уместна, используй:

REGION
RESEARCH TIER
COMPETITORS DISCOVERED IN CHECKED SOURCES
TIER-A COMPETITORS
OBSERVED PRICE RANGE / MEDIAN + N
POSITIONING PATTERNS
VOC PATTERNS
CHANNEL PATTERNS
WHITESPACE
COVERAGE STATUS
CAVEATS

Не выдавай количество найденных конкурентов за общее количество компаний на рынке.

Для каждой стратегически важной рекомендации покажи:
ACTION
WHY
EVIDENCE
CONTRADICTORY EVIDENCE
CONFIDENCE
RISK
WHAT TO TEST NEXT

Если рекомендация относится к конкретному региону, evidence тоже должно относиться к этому региону.

В конце укажи Research Integrity Status:
VERIFIED / VERIFIED_WITH_GAPS / DEGRADED / INSUFFICIENT_EVIDENCE.

Deep-анализ регионально-зависимой ниши по России НЕ МОЖЕТ быть VERIFIED, если исследована только федеральная выдача и отсутствует достаточный regional coverage.

Главная цель:
не написать красивый обзор, а максимально снизить неопределённость и показать, как федеральная и региональная конкурентная среда реально отличаются.
```
