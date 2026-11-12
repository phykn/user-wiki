#!/usr/bin/env python3
import re
import sys
from collections import namedtuple
from pathlib import Path

ROOT_DOCS = ("README.md",)
INDEX = "graph/index.md"
PATH_PREFIXES = ("graph/", "scripts/")
EXTERNAL_PREFIXES = ("http://", "https://", "mailto:")

FENCE_RE = re.compile(r"`{3,}|~{3,}")
CONTAINER_RE = re.compile(r"[ \t]*(?:>[ \t]*)*(?:(?:[-*+]|\d+[.)])[ \t]+)?")  # quote and list markers
CODE_RE = re.compile(r"(?<!`)(`+)(?!`)(.+?)(?<!`)\1(?!`)")
HEADING_RE = re.compile(r" {0,3}(#{1,6})(?:[ \t]+(.*?))?(?:[ \t]+#+)?[ \t]*$")
WIKILINK_RE = re.compile(r"\[\[([^\[\]\n]+)\]\]")
LINK_RE = re.compile(r"!?\[[^\[\]\n]*\]\(([^()\s]*)[^()\n]*\)")
REF_DEF_RE = re.compile(r" {0,3}\[[^\[\]\n]+\]:")
BULLET_RE = re.compile(r"[ \t]*[-*+][ \t]")


# plain is the line with inline code blanked out; level is 0 for a line that is not a heading
Line = namedtuple("Line", "raw plain codes level title")
# lines holds only the lines outside fenced code blocks
Doc = namedtuple("Doc", "name path lines")


def main(root):
    problems = check(root)
    print("\n".join(problems) if problems else "WIKI_CHECK_OK")
    return 1 if problems else 0


def check(root):
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
    paths += sorted(graph.glob("*.md"))
    docs = [read_doc(root, path) for path in paths if path.is_file()]
    pages = {doc.path.stem: doc for doc in docs if doc.name.startswith("graph/")}
    for doc in docs:
        problems += check_doc(root, doc, pages)

    index = pages.get("index")
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
    return list(dict.fromkeys(problems))


def read_doc(root, path):
    text = path.read_text(encoding="utf-8")
    lines = []
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
    return Doc(path.relative_to(root).as_posix(), path, lines)


def check_doc(root, doc, pages):
    problems = []
    unsupported = []
    broken = []
    links = []
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

        for token in (token for code in line.codes for token in code.split()):
            if not token.startswith(PATH_PREFIXES) or any(char in token for char in "*?["):
                continue
            target = (root / token).resolve()
            if root not in target.parents or not target.exists():
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

    return problems + unsupported + broken + links


def route_lines(doc):
    section = None
    for line in doc.lines:
        if 0 < line.level <= 2:
            if section is not None:
                return section
            if line.level == 2 and line.title.casefold() == "route":
                section = []
        elif section is not None:
            section.append(line)
    return section


def split_link(inner):
    page, sep, title = inner.split("|", 1)[0].partition("#")
    return page.strip(), (title.strip() if sep else None)


if __name__ == "__main__":
    sys.exit(main(Path(__file__).resolve().parents[1]))
