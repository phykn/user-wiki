#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
GRAPH_DIR = ROOT / "graph"
EVALS_DIR = ROOT / "evals"
ROOT_DOCS = [ROOT / "AGENTS.md", ROOT / "README.md"]
REQUIRED_DOCS = [ROOT / "AGENTS.md", ROOT / "README.md", GRAPH_DIR / "index.md"]
PATH_REF_DOCS = [*ROOT_DOCS, GRAPH_DIR / "index.md"]
PATH_REF_RE = re.compile(r"`((?:graph|evals|scripts)[/\\][^`]+)`")
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)")


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def main() -> int:
    problems = []
    graph_files = sorted(GRAPH_DIR.glob("*.md"))
    eval_files = sorted(EVALS_DIR.glob("*.md")) if EVALS_DIR.exists() else []

    for path in REQUIRED_DOCS:
        if not path.exists():
            problems.append(f"MISSING_DOC {rel(path)}")

    for path in [*ROOT_DOCS, *graph_files, *eval_files]:
        if not path.exists():
            continue
        if not path.read_text(encoding="utf-8").strip():
            problems.append(f"EMPTY_DOC {rel(path)}")

    for path in PATH_REF_DOCS:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for target in PATH_REF_RE.findall(text):
            target_path = ROOT / target.replace("\\", "/")
            if not target_path.exists():
                problems.append(f"BROKEN_PATH_REF {rel(path)} -> {target}")

    graph_names = {path.stem for path in graph_files}
    for path in graph_files:
        text = path.read_text(encoding="utf-8")
        for target in WIKILINK_RE.findall(text):
            if target not in graph_names:
                problems.append(f"BROKEN_WIKILINK {rel(path)} -> {target}")

    if problems:
        print("\n".join(problems))
        return 1

    print("WIKI_CHECK_OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
