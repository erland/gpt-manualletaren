#!/usr/bin/env python3
"""Backward-compatible entrypoint for the canonical GPT Byggaren 1.6.14 engine.

The old custom ZIP assembler has been removed. All six distributions are now
created by scripts/build_distributions.py and checked by its validator.
"""
import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", required=True)
    args = parser.parse_args()
    for command in (
        [sys.executable, str(ROOT / "scripts/validate_project.py")],
        [sys.executable, str(ROOT / "scripts/lint_gpt_project.py"), "--project-root", str(ROOT)],
        [sys.executable, str(ROOT / "scripts/build_distributions.py"), "--project-root", str(ROOT), "--version", args.version],
        [sys.executable, str(ROOT / "scripts/validate_distributions.py"), "--project-root", str(ROOT)],
    ):
        subprocess.run(command, check=True, cwd=ROOT)


if __name__ == "__main__":
    main()
