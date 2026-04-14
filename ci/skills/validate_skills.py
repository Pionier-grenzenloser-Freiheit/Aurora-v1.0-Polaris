import re
import sys
from pathlib import Path

import yaml
from jsonschema import Draft7Validator


ROOT = Path(__file__).resolve().parents[2]
SKILLS_DIR = ROOT / ".github" / "skills"
SCHEMA_PATH = ROOT / "schemas" / "skill_frontmatter.schema.yaml"
TOOL_REGISTRY_PATH = ROOT / "ops" / "tool_registry.yaml"


def parse_frontmatter(md_text: str) -> dict:
    if not md_text.startswith("---\n"):
        raise ValueError("SKILL.md must start with YAML frontmatter delimited by ---")
    parts = md_text.split("\n---\n", 1)
    if len(parts) != 2:
        raise ValueError("Frontmatter must be terminated by a line with ---")
    front = parts[0].strip("-\n")
    data = yaml.safe_load(front) or {}
    if not isinstance(data, dict):
        raise ValueError("Frontmatter must be a YAML mapping/object")
    return data


def load_schema() -> Draft7Validator:
    schema = yaml.safe_load(SCHEMA_PATH.read_text(encoding="utf-8"))
    return Draft7Validator(schema)


def load_tool_registry() -> set[str]:
    data = yaml.safe_load(TOOL_REGISTRY_PATH.read_text(encoding="utf-8")) or {}
    tools = data.get("tools", [])
    if not isinstance(tools, list):
        raise ValueError("ops/tool_registry.yaml must contain a top-level 'tools' list")
    return set(str(t) for t in tools)


def main() -> int:
    if not SKILLS_DIR.exists():
        print(f"SKILLS_DIR missing: {SKILLS_DIR}", file=sys.stderr)
        return 2

    validator = load_schema()
    allowed_tools = load_tool_registry()

    name_pattern = re.compile(r"^[a-z0-9-]+$")
    errors = []

    for skill_dir in sorted([p for p in SKILLS_DIR.iterdir() if p.is_dir()], key=lambda p: p.name):
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            errors.append(f"{skill_dir}: missing SKILL.md")
            continue

        try:
            fm = parse_frontmatter(skill_md.read_text(encoding="utf-8"))
        except Exception as e:
            errors.append(f"{skill_md}: frontmatter parse error: {e}")
            continue

        schema_errors = sorted(validator.iter_errors(fm), key=lambda e: e.path)
        for e in schema_errors:
            loc = "/".join([str(x) for x in e.path]) or "(root)"
            errors.append(f"{skill_md}: schema error at {loc}: {e.message}")

        skill_name = str(fm.get("name", ""))
        if skill_name and not name_pattern.match(skill_name):
            errors.append(f"{skill_md}: name must match ^[a-z0-9-]+$")

        if skill_name and skill_dir.name != skill_name:
            errors.append(
                f"{skill_md}: directory name '{skill_dir.name}' must match frontmatter name '{skill_name}'"
            )

        tools = fm.get("allowed_tools", [])
        if isinstance(tools, list):
            for t in tools:
                if str(t) not in allowed_tools:
                    errors.append(
                        f"{skill_md}: allowed_tools contains unknown tool '{t}' (not in ops/tool_registry.yaml)"
                    )

    if errors:
        print("Skill validation failed:", file=sys.stderr)
        for e in errors:
            print(f"- {e}", file=sys.stderr)
        return 1

    print("Skill validation OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
