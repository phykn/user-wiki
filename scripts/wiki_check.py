"""Validate a wiki checkout and return ordered, unique diagnostics."""

from collections import Counter
from pathlib import Path
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


ROOT_DOCS = ("AGENTS.md", "README.md")
REQUIRED_DOCS = (*ROOT_DOCS, "graph/index.md")
GLOB_CHARS = "*?[]"


def check_wiki(root: Path) -> List[str]:
    root = root.resolve()
    graph_files = sorted((root / "graph").glob("*.md"))
    eval_files = sorted((root / "evals").rglob("*.md"))
    sources = [*(root / name for name in ROOT_DOCS), *graph_files]
    texts = {
        path: path.read_text(encoding="utf-8")
        for path in [*sources, *eval_files]
        if path.is_file()
    }
    refs = {path: path_refs(text) for path, text in texts.items()}

    problems = check_layout(root, texts)
    problems.extend(check_path_refs(root, texts, refs))
    problems.extend(check_graph(root, graph_files, texts))

    referenced_paths: Set[Path] = set()
    for source in sources:
        for ref in refs.get(source, []):
            target = existing_repo_path(root, source, ref.path)
            if target is not None:
                referenced_paths.add(target)
    for path in eval_files:
        if path not in referenced_paths:
            problems.append(f"UNROUTED_EVAL_DOC {path.relative_to(root).as_posix()}")

    return list(dict.fromkeys(problems))


def check_layout(root: Path, texts: Dict[Path, str]) -> List[str]:
    problems: List[str] = []
    graph_dir = root / "graph"
    for path in sorted(graph_dir.rglob("*.md")):
        if path.parent != graph_dir:
            problems.append(
                f"UNSUPPORTED_NESTED_GRAPH_DOC {path.relative_to(root).as_posix()}"
            )
    if (root / "index.md").exists():
        problems.append("UNEXPECTED_DOC index.md")
    for name in REQUIRED_DOCS:
        if not (root / name).is_file():
            problems.append(f"MISSING_DOC {name}")
    for path, text in texts.items():
        if not has_body(text):
            problems.append(f"EMPTY_DOC {path.relative_to(root).as_posix()}")
    return problems


def check_path_refs(
    root: Path,
    texts: Dict[Path, str],
    refs: Dict[Path, List[PathReference]],
) -> List[str]:
    problems: List[str] = []
    for source, entries in refs.items():
        name = source.relative_to(root).as_posix()
        for ref in entries:
            if ref.allow_glob and any(char in ref.path for char in GLOB_CHARS):
                continue
            target = existing_repo_path(root, source, ref.path)
            if target is None:
                problems.append(f"BROKEN_PATH_REF {name} -> {ref.display}")
            elif ref.fragment is not None and not anchor_exists(
                target, ref.fragment, texts
            ):
                problems.append(f"BROKEN_ANCHOR {name} -> {ref.display}")

    agents_doc = root / "AGENTS.md"
    index_doc = (root / "graph/index.md").resolve()
    if not any(
        existing_repo_path(root, agents_doc, ref.path) == index_doc
        for ref in refs.get(agents_doc, [])
    ):
        problems.append("MISSING_ENTRYPOINT_REF AGENTS.md -> graph/index.md")
    return problems


def existing_repo_path(root: Path, source: Path, target: str) -> Optional[Path]:
    for candidate in candidate_paths(root, source, target):
        resolved = candidate.resolve()
        try:
            resolved.relative_to(root)
        except ValueError:
            continue
        if resolved.is_file():
            return resolved
    return None


def candidate_paths(root: Path, source: Path, target: str) -> List[Path]:
    if not target:
        return [source]
    normalized = target.replace("\\", "/")
    if normalized.startswith(("./", "../")):
        return [source.parent / normalized]
    if normalized.startswith("/"):
        return []
    if "/" in normalized:
        return [root / normalized]
    return [source.parent / normalized, root / normalized]


def anchor_exists(path: Path, fragment: str, texts: Dict[Path, str]) -> bool:
    if path.suffix.casefold() != ".md":
        return True
    text = texts.get(path)
    if text is None:
        text = path.read_text(encoding="utf-8")
    return unquote(fragment).strip().casefold() in heading_keys(text)


def check_graph(
    root: Path, graph_files: List[Path], texts: Dict[Path, str]
) -> List[str]:
    problems: List[str] = []
    nodes: Dict[str, Path] = {}
    folded_names: Dict[str, str] = {}
    for path in graph_files:
        name = path.stem
        folded = name.casefold()
        if folded in folded_names and folded_names[folded] != name:
            problems.append(f"DUPLICATE_GRAPH_NODE {folded_names[folded]} -> {name}")
        folded_names[folded] = name
        nodes[name] = path

    for source, text in texts.items():
        name = source.relative_to(root).as_posix()
        for node, fragment, display in wikilink_parts(text):
            target = source if not node else nodes.get(node)
            if target is None:
                problems.append(f"BROKEN_WIKILINK {name} -> {node}")
            elif fragment is not None and not anchor_exists(target, fragment, texts):
                problems.append(f"BROKEN_WIKILINK_ANCHOR {name} -> {display}")

    index_text = texts.get(root / "graph/index.md")
    if index_text is not None:
        route = section_text(index_text, "Route")
        pages = section_text(index_text, "Pages")
        if route is None:
            problems.append("MISSING_INDEX_SECTION graph/index.md -> Route")
        if pages is None:
            problems.append("MISSING_INDEX_SECTION graph/index.md -> Pages")

        expected = set(nodes) - {"index"}
        routed = wikilink_nodes(bullet_text(route or ""))
        entries = Counter(page_entry_nodes(pages or ""))
        for node in sorted(expected - routed):
            problems.append(f"UNROUTED_GRAPH_DOC graph/{node}.md")
        for node in sorted(expected - entries.keys()):
            problems.append(f"UNLISTED_GRAPH_DOC graph/{node}.md")
        for node in sorted(entries):
            if entries[node] > 1:
                problems.append(f"DUPLICATE_PAGE_ENTRY graph/index.md -> {node}")
    return problems
