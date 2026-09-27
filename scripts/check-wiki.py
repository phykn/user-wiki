#!/usr/bin/env python3
from pathlib import Path
import sys
from typing import Dict, List, Optional, Set
from urllib.parse import unquote

from wiki_markdown import (
    PathReference,
    bullet_text,
    has_body,
    heading_keys,
    page_entry_nodes,
    path_refs,
    section_text,
    wikilink_nodes,
    wikilink_parts,
)


ROOT = Path(__file__).resolve().parents[1]
GRAPH_DIR = ROOT / "graph"
EVALS_DIR = ROOT / "evals"
INDEX_DOC = GRAPH_DIR / "index.md"
ROOT_DOCS = [ROOT / "AGENTS.md", ROOT / "README.md"]
REQUIRED_DOCS = [*ROOT_DOCS, INDEX_DOC]
GLOB_CHARS = "*?[]"


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def candidate_paths(source: Path, target: str) -> List[Path]:
    if not target:
        return [source]
    normalized = target.replace("\\", "/")
    if normalized.startswith(("./", "../")):
        return [source.parent / normalized]
    if normalized.startswith("/"):
        return []
    if "/" in normalized:
        return [ROOT / normalized]
    return [source.parent / normalized, ROOT / normalized]


def existing_repo_path(source: Path, target: str) -> Optional[Path]:
    root = ROOT.resolve()
    for candidate in candidate_paths(source, target):
        resolved = candidate.resolve()
        try:
            resolved.relative_to(root)
        except ValueError:
            continue
        if resolved.is_file():
            return resolved
    return None


def anchor_exists(path: Path, fragment: str, texts: Dict[Path, str]) -> bool:
    if path.suffix.casefold() != ".md":
        return True
    text = texts.get(path)
    if text is None:
        text = path.read_text(encoding="utf-8")
    return unquote(fragment).strip().casefold() in heading_keys(text)


def main() -> int:
    problems: List[str] = []
    seen_problems: Set[str] = set()

    def add_problem(problem: str) -> None:
        if problem not in seen_problems:
            seen_problems.add(problem)
            problems.append(problem)

    graph_files = sorted(GRAPH_DIR.glob("*.md"))
    nested_graph_files = sorted(
        path for path in GRAPH_DIR.rglob("*.md") if path.parent != GRAPH_DIR
    )
    eval_files = sorted(EVALS_DIR.rglob("*.md")) if EVALS_DIR.exists() else []

    for path in nested_graph_files:
        add_problem(f"UNSUPPORTED_NESTED_GRAPH_DOC {rel(path)}")

    root_index = ROOT / "index.md"
    if root_index.exists():
        add_problem("UNEXPECTED_DOC index.md")

    for path in REQUIRED_DOCS:
        if not path.is_file():
            add_problem(f"MISSING_DOC {rel(path)}")

    maintained_files = [*ROOT_DOCS, *graph_files, *eval_files]
    texts: Dict[Path, str] = {}
    for path in maintained_files:
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        texts[path] = text
        if not has_body(text):
            add_problem(f"EMPTY_DOC {rel(path)}")

    refs_by_file: Dict[Path, List[PathReference]] = {}
    for path, text in texts.items():
        refs = path_refs(text)
        refs_by_file[path] = refs
        for ref in refs:
            if ref.allow_glob and any(char in ref.path for char in GLOB_CHARS):
                continue
            existing = existing_repo_path(path, ref.path)
            if existing is None:
                add_problem(f"BROKEN_PATH_REF {rel(path)} -> {ref.display}")
                continue
            if ref.fragment is not None and not anchor_exists(
                existing, ref.fragment, texts
            ):
                add_problem(f"BROKEN_ANCHOR {rel(path)} -> {ref.display}")

    agents_refs = refs_by_file.get(ROOT / "AGENTS.md", [])
    index_resolved = INDEX_DOC.resolve()
    if not any(
        existing_repo_path(ROOT / "AGENTS.md", ref.path) == index_resolved
        for ref in agents_refs
    ):
        add_problem("MISSING_ENTRYPOINT_REF AGENTS.md -> graph/index.md")

    graph_names: Dict[str, Path] = {}
    casefold_names: Dict[str, str] = {}
    for path in graph_files:
        folded = path.stem.casefold()
        if folded in casefold_names and casefold_names[folded] != path.stem:
            add_problem(
                f"DUPLICATE_GRAPH_NODE {casefold_names[folded]} -> {path.stem}"
            )
        casefold_names[folded] = path.stem
        graph_names[path.stem] = path

    for path, text in texts.items():
        for node, fragment, display in wikilink_parts(text):
            target_path = path if not node else graph_names.get(node)
            if target_path is None:
                add_problem(f"BROKEN_WIKILINK {rel(path)} -> {node}")
                continue
            if fragment is not None and not anchor_exists(
                target_path, fragment, texts
            ):
                add_problem(f"BROKEN_WIKILINK_ANCHOR {rel(path)} -> {display}")

    index_text = texts.get(INDEX_DOC)
    if index_text is not None:
        route = section_text(index_text, "Route")
        pages = section_text(index_text, "Pages")
        if route is None:
            add_problem("MISSING_INDEX_SECTION graph/index.md -> Route")
        if pages is None:
            add_problem("MISSING_INDEX_SECTION graph/index.md -> Pages")

        expected_nodes = set(graph_names) - {"index"}
        route_nodes = wikilink_nodes(bullet_text(route or ""))
        page_entries = page_entry_nodes(pages or "")
        page_nodes = set(page_entries)
        for node in sorted(expected_nodes - route_nodes):
            add_problem(f"UNROUTED_GRAPH_DOC graph/{node}.md")
        for node in sorted(expected_nodes - page_nodes):
            add_problem(f"UNLISTED_GRAPH_DOC graph/{node}.md")
        for node in sorted(page_nodes):
            if page_entries.count(node) > 1:
                add_problem(f"DUPLICATE_PAGE_ENTRY graph/index.md -> {node}")

    referenced_repo_paths: Set[str] = set()
    for source in [*ROOT_DOCS, *graph_files]:
        for ref in refs_by_file.get(source, []):
            existing = existing_repo_path(source, ref.path)
            if existing is not None:
                referenced_repo_paths.add(rel(existing))
    for path in eval_files:
        if rel(path) not in referenced_repo_paths:
            add_problem(f"UNROUTED_EVAL_DOC {rel(path)}")

    if problems:
        print("\n".join(problems))
        return 1

    print("WIKI_CHECK_OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
