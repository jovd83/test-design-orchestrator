#!/usr/bin/env python3
"""Lightweight validators for bundled test artifact formats."""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path


BDD_PATTERNS = {
    "Feature": re.compile(r"^Feature:\s+\S+", re.MULTILINE),
    "Scenario": re.compile(r"^\s*Scenario(?: Outline)?:\s+\S+", re.MULTILINE),
    "Given": re.compile(r"^\s*Given\s+\S+", re.MULTILINE),
    "When": re.compile(r"^\s*When\s+\S+", re.MULTILINE),
    "Then": re.compile(r"^\s*Then\s+\S+", re.MULTILINE),
}

MARKDOWN_TEST_CASE_PATTERNS = {
    "Title": re.compile(r"^\*\*Title:\*\*\s+\S+", re.MULTILINE),
    "Steps": re.compile(r"^\| Step \| Action \| Expected Result \|$", re.MULTILINE),
    "Execution Type": re.compile(r"^- Execution Type:\s+\S+", re.MULTILINE),
    "Design Status": re.compile(r"^- Design Status:\s+\S+", re.MULTILINE),
}

ZEPHYR_REQUIRED_HEADERS = [
    "Folder",
    "Name",
    "Objective",
    "Status",
    "Precondition",
    "Labels",
    "Step",
    "Expected Result",
    "Execution Type",
    "Priority",
    "Estimated Time",
    "Is Open",
]


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def validate_bdd(text: str) -> list[str]:
    errors = [f"Missing {label}" for label, pattern in BDD_PATTERNS.items() if not pattern.search(text)]
    return errors


def validate_markdown_test_case(text: str) -> list[str]:
    errors = [
        f"Missing markdown test case section: {label}"
        for label, pattern in MARKDOWN_TEST_CASE_PATTERNS.items()
        if not pattern.search(text)
    ]
    return errors


def validate_zephyr_csv(text: str) -> list[str]:
    rows = list(csv.reader(text.splitlines()))
    if not rows:
        return ["CSV content is empty"]

    header = rows[0]
    if header != ZEPHYR_REQUIRED_HEADERS:
        return ["CSV header does not match the bundled Zephyr Scale template"]

    if len(rows) < 2:
        return ["CSV must contain at least one data row"]

    return []


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a formatted test artifact.")
    parser.add_argument("format", choices=["bdd", "markdown", "xray", "zephyr"])
    parser.add_argument("path", help="Path to the file to validate")
    args = parser.parse_args()

    path = Path(args.path)
    if not path.exists():
        print(f"Error: file not found: {path}")
        return 1

    text = _read_text(path)

    if args.format in {"bdd", "xray"}:
        errors = validate_bdd(text)
    elif args.format == "markdown":
        errors = validate_markdown_test_case(text)
    else:
        errors = validate_zephyr_csv(text)

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
