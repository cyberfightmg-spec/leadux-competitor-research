from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_SKILLS = [
    "research-planner",
    "competitor-discovery",
    "regional-intelligence",
    "competitor-profiling",
    "product-intelligence",
    "pricing-intelligence",
    "customer-research",
    "voice-of-customer",
    "gtm-intelligence",
    "content-performance-intelligence",
    "strategic-signals",
    "market-whitespace",
    "contradiction-check",
    "evidence-verification",
    "red-team",
    "strategy-handoff",
]

REQUIRED_SCHEMAS = [
    "source.schema.json",
    "claim.schema.json",
    "insight.schema.json",
    "competitor.schema.json",
    "opportunity.schema.json",
    "research.schema.json",
    "content-performance-pattern.schema.json",
    "strategy-handoff.schema.json",
]


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    if not version:
        fail("VERSION is empty")

    for name in REQUIRED_SKILLS:
        path = ROOT / "skills" / name / "SKILL.md"
        if not path.exists():
            fail(f"missing skill: {path.relative_to(ROOT)}")
        text = path.read_text(encoding="utf-8")
        if name in {"strategy-handoff", "content-performance-intelligence"} and not text.startswith("---\n"):
            fail(f"new integration skill lacks YAML frontmatter: {path.relative_to(ROOT)}")

    loaded = {}
    for name in REQUIRED_SCHEMAS:
        path = ROOT / "schemas" / name
        if not path.exists():
            fail(f"missing schema: {path.relative_to(ROOT)}")
        try:
            loaded[name] = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            fail(f"invalid JSON in {path.relative_to(ROOT)}: {exc}")

    handoff = loaded["strategy-handoff.schema.json"]
    props = handoff.get("properties", {})
    if "content_performance_patterns" not in props:
        fail("strategy handoff schema does not expose content_performance_patterns")

    perf = loaded["content-performance-pattern.schema.json"]
    evidence_enum = perf.get("properties", {}).get("evidence_level", {}).get("enum", [])
    required_levels = {"CONTENT_SIGNAL", "AUDIENCE_RESPONSE", "LEAD_SIGNAL", "BUSINESS_OUTCOME"}
    if set(evidence_enum) != required_levels:
        fail("content performance evidence levels are incomplete")

    root_skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    for term in ("content-performance-intelligence", "strategy-handoff"):
        if term not in root_skill:
            fail(f"root router does not reference {term}")

    print(f"OK: LeadUX Competitor Research {version} repository contracts validated")


if __name__ == "__main__":
    main()
