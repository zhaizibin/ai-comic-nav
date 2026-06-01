from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "deep-analysis"
SKILL_MD = SKILL / "SKILL.md"


def fail(message: str) -> None:
    raise SystemExit(f"validation failed: {message}")


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end == -1:
        fail("SKILL.md frontmatter must close with ---")
    raw = text[4:end].strip().splitlines()
    data: dict[str, str] = {}
    for line in raw:
        if ":" not in line:
            fail(f"invalid frontmatter line: {line}")
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()
    return data


def main() -> None:
    if not SKILL_MD.exists():
        fail("missing skills/deep-analysis/SKILL.md")

    text = SKILL_MD.read_text(encoding="utf-8")
    metadata = parse_frontmatter(text)

    if metadata.get("name") != "deep-analysis":
        fail("frontmatter name must be deep-analysis")
    if "description" not in metadata or len(metadata["description"]) < 80:
        fail("frontmatter description must be specific enough to trigger the skill")
    if set(metadata) != {"name", "description"}:
        fail("frontmatter should contain only name and description")

    links = sorted(set(re.findall(r"`(methods/[^`]+\.md)`", text)))
    if len(links) != 9:
        fail(f"expected 9 method links, found {len(links)}")

    for rel in links:
        path = SKILL / rel
        if not path.exists():
            fail(f"missing linked method file: {rel}")
        body = path.read_text(encoding="utf-8")
        if len(body.strip()) < 500:
            fail(f"method file is too thin: {rel}")

    agent_yaml = SKILL / "agents" / "openai.yaml"
    if not agent_yaml.exists():
        fail("missing agents/openai.yaml")

    print("Deep Analysis skill validation passed.")


if __name__ == "__main__":
    main()
