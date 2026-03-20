#!/usr/bin/env python3
"""Validate the structure and basic contracts of this skill repository."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]
REQUIRED_DIRS = [
    "agents",
    "assets/templates",
    "references",
    "examples",
    "evals",
    "scripts",
]
SUBSKILLS = [
    "acceptance-criteria-to-test-cases",
    "boundary-value-analysis",
    "classification-tree-nwise",
    "decision-table",
    "equivalence-partitioning",
    "state-transition",
    "technique-selector",
    "test-case-formatter",
    "use-case-testing",
]
NAME_PATTERN = re.compile(r"^[a-z0-9-]+$")
FRONTMATTER_PATTERN = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
LOCAL_REF_PATTERN = re.compile(r"\./[A-Za-z0-9._/\-]+")
EXPECTED_AUTHOR = "jovd83"
EXPECTED_VERSION = "v2.0.0"


def parse_frontmatter(path: Path) -> tuple[dict, str] | tuple[None, str]:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_PATTERN.match(text)
    if not match:
        return None, f"{path}: missing or invalid YAML frontmatter"

    try:
        fields = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        return None, f"{path}: invalid YAML frontmatter: {exc}"

    if not isinstance(fields, dict):
        return None, f"{path}: frontmatter must be a YAML object"

    return fields, text


def validate_skill_file(path: Path, errors: list[str]) -> None:
    parsed, text_or_error = parse_frontmatter(path)
    if parsed is None:
        errors.append(text_or_error)
        return

    fields = parsed
    text = text_or_error
    required_keys = {"name", "description"}
    optional_keys = {"metadata"}
    if not required_keys.issubset(fields):
        errors.append(f"{path}: frontmatter must include {sorted(required_keys)}")
    unexpected_keys = set(fields) - (required_keys | optional_keys)
    if unexpected_keys:
        errors.append(f"{path}: unexpected frontmatter keys {sorted(unexpected_keys)}")

    name = fields.get("name", "")
    description = fields.get("description", "")
    if not NAME_PATTERN.fullmatch(name):
        errors.append(f"{path}: invalid skill name {name!r}")
    if len(description) == 0 or len(description) > 1024:
        errors.append(f"{path}: description must be between 1 and 1024 characters")

    metadata = fields.get("metadata")
    if metadata is None:
        errors.append(f"{path}: metadata block is required")
    elif not isinstance(metadata, dict):
        errors.append(f"{path}: metadata must be an object")
    else:
        if metadata.get("author") != EXPECTED_AUTHOR:
            errors.append(f"{path}: metadata.author must be {EXPECTED_AUTHOR!r}")
        if metadata.get("version") != EXPECTED_VERSION:
            errors.append(f"{path}: metadata.version must be {EXPECTED_VERSION!r}")

    for raw_ref in LOCAL_REF_PATTERN.findall(text):
        ref = raw_ref.rstrip("`.,)")
        target = REPO_ROOT / ref[2:]
        if not target.exists():
            errors.append(f"{path}: missing referenced path {ref}")


def validate_openai_yaml(errors: list[str]) -> None:
    path = REPO_ROOT / "agents" / "openai.yaml"
    if not path.exists():
        errors.append(f"{path}: missing")
        return

    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        errors.append(f"{path}: invalid YAML: {exc}")
        return

    if not isinstance(data, dict) or not isinstance(data.get("interface"), dict):
        errors.append(f"{path}: interface block is required")
        return

    interface = data["interface"]
    for required in ["display_name", "short_description", "default_prompt", "icon_small", "icon_large", "brand_color"]:
        if required not in interface:
            errors.append(f"{path}: missing interface.{required}")

    for icon_key in ["icon_small", "icon_large"]:
        icon_path = interface.get(icon_key)
        if isinstance(icon_path, str) and icon_path.startswith("./"):
            if not (REPO_ROOT / icon_path[2:]).exists():
                errors.append(f"{path}: missing referenced icon {icon_path}")


def validate_json_fixture(path: Path, required_keys: set[str], errors: list[str]) -> None:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"{path}: invalid JSON: {exc}")
        return

    if not isinstance(data, list) or not data:
        errors.append(f"{path}: fixture must be a non-empty JSON list")
        return

    for index, item in enumerate(data, start=1):
        if not isinstance(item, dict):
            errors.append(f"{path}: item {index} must be an object")
            continue
        missing = required_keys - set(item)
        if missing:
            errors.append(f"{path}: item {index} missing keys {sorted(missing)}")


def main() -> int:
    errors: list[str] = []

    for relative_dir in REQUIRED_DIRS:
        path = REPO_ROOT / relative_dir
        if not path.exists():
            errors.append(f"{path}: required directory is missing")

    validate_skill_file(REPO_ROOT / "SKILL.md", errors)
    for subskill in SUBSKILLS:
        validate_skill_file(REPO_ROOT / subskill / "SKILL.md", errors)

    validate_openai_yaml(errors)
    validate_json_fixture(REPO_ROOT / "evals" / "trigger-queries.json", {"query", "should_trigger"}, errors)
    validate_json_fixture(
        REPO_ROOT / "evals" / "technique-selection-cases.json",
        {"id", "scenario", "expected_primary"},
        errors,
    )

    if not any((REPO_ROOT / "examples").iterdir()):
        errors.append(f"{REPO_ROOT / 'examples'}: at least one example file is required")

    if errors:
        print("Repository validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Repository validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
