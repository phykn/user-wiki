#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Dict, List, NamedTuple, Optional, Set, Tuple

ROOT_DOCS = ("AGENTS.md", "README.md")
INDEX = "graph/index.md"
ENTRY_LIMIT = 600
PATH_PREFIXES = ("graph/", "evals/", "scripts/")
EXTERNAL_PREFIXES = ("http://", "https://", "mailto:")

FENCE_RE = re.compile(r"`{3,}|~{3,}")
CONTAINER_RE = re.compile(r"[ \t]*(?:>[ \t]*)*(?:(?:[-*+]|\d+[.)])[ \t]+)?")  # quote and list markers
CODE_RE = re.compile(r"(?<!`)(`+)(?!`)(.+?)(?<!`)\1(?!`)")
HEADING_RE = re.compile(r" {0,3}(#{1,6})(?:[ \t]+(.*?))?(?:[ \t]+#+)?[ \t]*$")
WIKILINK_RE = re.compile(r"\[\[([^\[\]\n]+)\]\]")
LINK_RE = re.compile(r"!?\[[^\[\]\n]*\]\(([^()\s]*)[^()\n]*\)")
REF_DEF_RE = re.compile(r" {0,3}\[[^\[\]\n]+\]:")
BULLET_RE = re.compile(r"[ \t]*[-*+][ \t]")


class Line(NamedTuple):
    raw: str
    plain: str  # the line with inline code blanked out
    codes: List[str]
    level: int  # heading level, 0 for other lines
    title: str


class Doc(NamedTuple):
    name: str
    path: Path
    text: str
    lines: List[Line]  # lines outside fenced code blocks


def main(root: Path) -> int:
    problems = check(root)
    print("\n".join(problems) if problems else "WIKI_CHECK_OK")
    return 1 if problems else 0


def check(root: Path) -> List[str]:
    root = root.resolve()
    graph = root / "graph"
    problems = [f"MISSING_DOC {name}" for name in (*ROOT_DOCS, INDEX) if not (root / name).is_file()]
    problems += [f"UNEXPECTED_DOC {p.name}" for p in sorted(root.glob("*.md")) if p.name not in ROOT_DOCS]
    problems += [
        f"NESTED_GRAPH_DOC {p.relative_to(root).as_posix()}"
        for p in sorted(graph.rglob("*.md"))
        if p.parent != graph
    ]

    paths = [root / name for name in ROOT_DOCS]
    paths += sorted(graph.glob("*.md")) + sorted((root / "evals").rglob("*.md"))
    docs = [read_doc(root, path) for path in paths if path.is_file()]
    pages = {doc.path.stem: doc for doc in docs if doc.name.startswith("graph/")}
    referenced: Set[Path] = set()
    for doc in docs:
        doc_problems, refs = check_doc(root, doc, pages)
        problems += doc_problems
        if not doc.name.startswith("evals/"):
            referenced |= refs

    by_name = {doc.name: doc for doc in docs}
    agents, index = by_name.get("AGENTS.md"), by_name.get(INDEX)
    if agents and not any(INDEX in line_tokens(line) for line in agents.lines):
        problems.append(f"MISSING_ENTRY_REF AGENTS.md -> {INDEX}")
    if index:
        route = route_lines(index)
        if route is None:
            problems.append(f"MISSING_ROUTE_SECTION {INDEX}")
        else:
            routed = {
                split_link(match.group(1))[0]
                for line in route
                if BULLET_RE.match(line.raw)
                for match in WIKILINK_RE.finditer(line.plain)
            }
            problems += [
                f"UNROUTED_PAGE {doc.name}"
                for stem, doc in sorted(pages.items())
                if stem != "index" and stem not in routed
            ]
    problems += [
        f"UNROUTED_EVAL {doc.name}"
        for doc in docs
        if doc.name.startswith("evals/") and doc.path.resolve() not in referenced
    ]
    words = sum(len(doc.text.split()) for doc in (agents, index) if doc)
    if words > ENTRY_LIMIT:
        problems.append(f"ENTRY_OVER_BUDGET AGENTS.md + {INDEX} -> {words} words (limit {ENTRY_LIMIT})")
    return list(dict.fromkeys(problems))


def read_doc(root: Path, path: Path) -> Doc:
    text = path.read_text(encoding="utf-8-sig")
    lines: List[Line] = []
    fence = ""
    for raw in text.splitlines():
        stripped = raw[CONTAINER_RE.match(raw).end():]
        marker = FENCE_RE.match(stripped)
        rest = stripped[marker.end():] if marker else ""
        if fence:
            if marker and marker.group()[0] == fence[0] and len(marker.group()) >= len(fence) and not rest.strip():
                fence = ""
            continue
        if marker and not (marker.group()[0] == "`" and "`" in rest):
            fence = marker.group()
            continue
        heading = HEADING_RE.match(raw)
        lines.append(Line(
            raw=raw,
            plain=CODE_RE.sub(" ", raw),
            codes=[match.group(2) for match in CODE_RE.finditer(raw)],
            level=len(heading.group(1)) if heading else 0,
            title=(heading.group(2) or "") if heading else "",
        ))
    return Doc(path.relative_to(root).as_posix(), path, text, lines)


def check_doc(root: Path, doc: Doc, pages: Dict[str, Doc]) -> Tuple[List[str], Set[Path]]:
    problems: List[str] = []
    unsupported: List[str] = []
    broken: List[str] = []
    links: List[str] = []
    refs: Set[Path] = set()
    body = [line for line in doc.lines if line.raw.strip()]
    if all(line.level for line in body):
        problems.append(f"EMPTY_DOC {doc.name}")
    elif doc.name.startswith("graph/") and body[0].level:
        problems.append(f"MISSING_SUMMARY {doc.name}")

    for line in doc.lines:
        found = [m.group() for m in LINK_RE.finditer(line.plain) if not m.group(1).startswith(EXTERNAL_PREFIXES)]
        if REF_DEF_RE.match(line.plain):
            found.append(line.plain.strip())
        if "<!--" in line.plain:
            found.append("<!--")
        unsupported += [f"UNSUPPORTED_SYNTAX {doc.name} -> {item}" for item in found]

        for token in line_tokens(line):
            if not token.startswith(PATH_PREFIXES) or any(char in token for char in "*?["):
                continue
            target = (root / token).resolve()
            if root in target.parents and target.exists():
                refs.add(target)
            else:
                broken.append(f"BROKEN_PATH {doc.name} -> {token}")

        for match in WIKILINK_RE.finditer(line.plain):
            page, title = split_link(match.group(1))
            target_doc = pages.get(page) if page else doc
            if target_doc is None:
                links.append(f"BROKEN_LINK {doc.name} -> {page}")
            elif title is not None and title.casefold() not in {
                other.title.casefold() for other in target_doc.lines if other.level
            }:
                links.append(f"BROKEN_ANCHOR {doc.name} -> {page}#{title}")

    cases = case_problems(doc) if doc.name.startswith("evals/") else []
    return problems + unsupported + broken + links + cases, refs


def case_problems(doc: Doc) -> List[str]:
    problems: List[str] = []
    case: Optional[str] = None
    linked = False
    for line in doc.lines + [Line("", "", [], 1, "")]:
        if 0 < line.level <= 3:
            if case is not None and not linked:
                problems.append(f"CASE_WITHOUT_RULE {doc.name} -> {case}")
            case, linked = (line.title if line.level == 3 else None), False
        elif case is not None and line.plain.startswith("Rule:"):
            linked = linked or any(split_link(m.group(1))[1] for m in WIKILINK_RE.finditer(line.plain))
    return problems


def route_lines(doc: Doc) -> Optional[List[Line]]:
    section: Optional[List[Line]] = None
    for line in doc.lines:
        if 0 < line.level <= 2:
            if section is not None:
                return section
            if line.level == 2 and line.title.casefold() == "route":
                section = []
        elif section is not None:
            section.append(line)
    return section


def split_link(inner: str) -> Tuple[str, Optional[str]]:
    page, sep, title = inner.split("|", 1)[0].partition("#")
    return page.strip(), (title.strip() if sep else None)


def line_tokens(line: Line) -> List[str]:
    return [token for code in line.codes for token in code.split()]


if __name__ == "__main__":
    sys.exit(main(Path(__file__).resolve().parents[1]))
