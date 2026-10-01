#!/usr/bin/env python3
"""Check the wiki containing this script, regardless of the working directory."""

from pathlib import Path
import sys

from wiki_check import check_wiki


def main() -> int:
    problems = check_wiki(Path(__file__).resolve().parents[1])
    print("\n".join(problems) if problems else "WIKI_CHECK_OK")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
