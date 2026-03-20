#!/usr/bin/env python3
"""Package one or more .feature files into a zip archive for Xray Gherkin import workflows."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


def collect_feature_files(inputs: list[Path]) -> list[Path]:
    feature_files: list[Path] = []
    for item in inputs:
        if item.is_dir():
            feature_files.extend(sorted(item.rglob("*.feature")))
        elif item.suffix == ".feature" and item.is_file():
            feature_files.append(item)
    return feature_files


def main() -> int:
    parser = argparse.ArgumentParser(description="Package .feature files into an Xray-friendly zip archive.")
    parser.add_argument("inputs", nargs="+", help="Feature file(s) or directories to include")
    parser.add_argument("--output", required=True, help="Output zip file path")
    args = parser.parse_args()

    inputs = [Path(value) for value in args.inputs]
    output = Path(args.output)

    feature_files = collect_feature_files(inputs)
    if not feature_files:
        print("No .feature files found in the provided inputs.")
        return 1

    output.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(output, "w", compression=ZIP_DEFLATED) as archive:
        for feature_file in feature_files:
            archive.write(feature_file, arcname=feature_file.name)

    print(f"Packaged {len(feature_files)} feature file(s) into {output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
