#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
GRAPH_DIR = ROOT / "graph"
EVALS_DIR = ROOT / "evals"
ROOT_DOCS = [ROOT / "AGENTS.md", ROOT / "README.md"]
REQUIRED_DOCS = [ROOT / "AGENTS.md", ROOT / "README.md", GRAPH_DIR / "index.md"]
ROOT_FILE_REF = r"(?:[A-Za-z0-9_.-]+\.md|\.gitignore)"
MAINTAINED_DIR_REF = r"(?:graph|evals|scripts)[/\\]"
OPTIONAL_MAINTAINED_DIR_REF = rf"(?:{MAINTAINED_DIR_REF})?"
PATH_REF_RE = re.compile(rf"`({OPTIONAL_MAINTAINED_DIR_REF}{ROOT_FILE_REF}|{MAINTAINED_DIR_REF}[^`]+)`")
MARKDOWN_PATH_REF_RE = re.compile(
    rf"\]\(\s*({OPTIONAL_MAINTAINED_DIR_REF}{ROOT_FILE_REF}|{MAINTAINED_DIR_REF}[^\s)#]+)"
    r"(?:#[^\s)]*)?(?:\s+\"[^\"]*\")?\s*\)"
)
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)")
GLOB_CHARS = "*?[]"
INTENTIONAL_ABSENT_ROOT_REFS = {"index.md"}


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

    path_ref_files = [*ROOT_DOCS, *[p for p in graph_files if p.name != "changelog.md"], *eval_files]
    for path in path_ref_files:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        path_refs = [*PATH_REF_RE.findall(text), *MARKDOWN_PATH_REF_RE.findall(text)]
        for target in path_refs:
            if any(char in target for char in GLOB_CHARS):
                continue
            normalized_target = target.replace("\\", "/")
            candidate_paths = (
                [ROOT / normalized_target]
                if "/" in normalized_target
                else [path.parent / normalized_target, ROOT / normalized_target]
            )
            if normalized_target in INTENTIONAL_ABSENT_ROOT_REFS and not any(
                candidate.exists() for candidate in candidate_paths
            ):
                continue
            if not any(candidate.exists() for candidate in candidate_paths):
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
