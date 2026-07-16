#!/usr/bin/env python3
from pathlib import Path
import re
import sys
from typing import Dict, List, NamedTuple, Optional, Set, Tuple
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
GRAPH_DIR = ROOT / "graph"
EVALS_DIR = ROOT / "evals"
INDEX_DOC = GRAPH_DIR / "index.md"
ROOT_DOCS = [ROOT / "AGENTS.md", ROOT / "README.md"]
REQUIRED_DOCS = [*ROOT_DOCS, INDEX_DOC]
ROOT_FILE_REF = r"(?:[A-Za-z0-9_.-]+\.md|\.gitignore)"
MAINTAINED_DIR_REF = r"(?:graph|evals|scripts)[/\\]"
OPTIONAL_MAINTAINED_DIR_REF = rf"(?:{MAINTAINED_DIR_REF})?"
RELATIVE_PREFIX = r"(?:\.\.?[/\\])+"
PATH_TARGET = rf"(?:{RELATIVE_PREFIX})?(?:{OPTIONAL_MAINTAINED_DIR_REF}{ROOT_FILE_REF}|{MAINTAINED_DIR_REF}[^`\s)#]+)"
PATH_REF_RE = re.compile(rf"`({PATH_TARGET})`")
MARKDOWN_LINK_RE = re.compile(
    r"\]\(\s*(?:<([^>]+)>|([^\s)]+))"
    r"(?:\s+(?:\"[^\"]*\"|'[^']*'|\([^)]*\)))?\s*\)"
)
WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
INLINE_CODE_RE = re.compile(r"`+[^`\n]*`+")
HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
HEADING_RE = re.compile(r"^#{1,6}[ \t]+(.+?)[ \t]*#*[ \t]*$", re.MULTILINE)
PAGE_ENTRY_RE = re.compile(r"^[ \t]*-[ \t]+\[\[([^\]]+)\]\][ \t]*:", re.MULTILINE)
EXTERNAL_LINK_RE = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")
GLOB_CHARS = "*?[]"


class PathReference(NamedTuple):
    path: str
    fragment: Optional[str]
    display: str
    allow_glob: bool


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def strip_fenced_code(text: str) -> str:
    output: List[str] = []
    fence_char: Optional[str] = None
    fence_length = 0
    for line in text.splitlines(keepends=True):
        stripped = line.lstrip(" \t")
        indent = len(line) - len(stripped)
        marker = re.match(r"(`{3,}|~{3,})", stripped) if indent <= 3 else None
        if fence_char is None:
            if marker is None:
                output.append(line)
                continue
            fence_char = marker.group(1)[0]
            fence_length = len(marker.group(1))
        elif (
            marker is not None
            and marker.group(1)[0] == fence_char
            and len(marker.group(1)) >= fence_length
            and not stripped[len(marker.group(1)) :].strip()
        ):
            fence_char = None
            fence_length = 0
        if line.endswith(("\n", "\r")):
            output.append("\n")
    return "".join(output)


def semantic_text(text: str) -> str:
    without_fences = strip_fenced_code(text)
    return HTML_COMMENT_RE.sub(
        lambda match: "\n" * match.group(0).count("\n"),
        without_fences,
    )


def link_text(text: str) -> str:
    return INLINE_CODE_RE.sub("", semantic_text(text))


def has_body(text: str) -> bool:
    return any(
        line.strip() and not line.lstrip().startswith("#")
        for line in semantic_text(text).splitlines()
    )


def path_refs(text: str) -> List[PathReference]:
    semantic = semantic_text(text)
    refs = [
        PathReference(match.group(1), None, match.group(1), True)
        for match in PATH_REF_RE.finditer(semantic)
    ]
    markdown = INLINE_CODE_RE.sub("", semantic)
    for match in MARKDOWN_LINK_RE.finditer(markdown):
        raw = (match.group(1) or match.group(2)).strip()
        if raw.startswith("//") or EXTERNAL_LINK_RE.match(raw):
            continue
        path_and_query, has_fragment, fragment = raw.partition("#")
        path, _, _query = path_and_query.partition("?")
        refs.append(
            PathReference(
                path=unquote(path),
                fragment=unquote(fragment) if has_fragment else None,
                display=raw,
                allow_glob=False,
            )
        )
    return refs


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


def heading_keys(text: str) -> Set[str]:
    keys: Set[str] = set()
    slug_counts: Dict[str, int] = {}
    for match in HEADING_RE.finditer(semantic_text(text)):
        heading = match.group(1).strip()
        heading = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", heading)
        heading = re.sub(r"[*_~`]", "", heading).strip()
        keys.add(heading.casefold())
        slug = re.sub(r"[^\w\s-]", "", heading.casefold())
        slug = re.sub(r"[\s-]+", "-", slug).strip("-")
        if slug:
            count = slug_counts.get(slug, 0)
            keys.add(slug if count == 0 else f"{slug}-{count}")
            slug_counts[slug] = count + 1
    return keys


def anchor_exists(path: Path, fragment: str, texts: Dict[Path, str]) -> bool:
    if path.suffix.casefold() != ".md":
        return True
    text = texts.get(path)
    if text is None:
        text = path.read_text(encoding="utf-8")
    return unquote(fragment).strip().casefold() in heading_keys(text)


def section_text(text: str, heading: str) -> Optional[str]:
    match = re.search(
        rf"^##[ \t]+{re.escape(heading)}[ \t]*$\n?(.*?)(?=^##[ \t]+|\Z)",
        semantic_text(text),
        flags=re.MULTILINE | re.DOTALL,
    )
    return match.group(1) if match else None


def wikilink_parts(text: str) -> List[Tuple[str, Optional[str], str]]:
    parts: List[Tuple[str, Optional[str], str]] = []
    for match in WIKILINK_RE.finditer(link_text(text)):
        display = match.group(1).split("|", 1)[0].strip()
        node, has_fragment, fragment = display.partition("#")
        parts.append((node.strip(), fragment.strip() if has_fragment else None, display))
    return parts


def wikilink_nodes(text: str) -> Set[str]:
    return {node for node, _fragment, _display in wikilink_parts(text) if node}


def bullet_text(text: str) -> str:
    return "\n".join(
        line for line in text.splitlines() if re.match(r"^[ \t]*-[ \t]+", line)
    )


def page_entry_nodes(text: str) -> List[str]:
    nodes: List[str] = []
    for match in PAGE_ENTRY_RE.finditer(link_text(text)):
        display = match.group(1).split("|", 1)[0].strip()
        node, _separator, _fragment = display.partition("#")
        if node.strip():
            nodes.append(node.strip())
    return nodes


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
