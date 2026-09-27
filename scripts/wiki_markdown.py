"""Extract maintained references and routes from wiki Markdown."""

import re
from typing import Dict, List, NamedTuple, Optional, Set, Tuple
from urllib.parse import unquote


ROOT_FILE_REF = r"(?:[A-Za-z0-9_.-]+\.md|\.gitignore)"
MAINTAINED_DIR_REF = r"(?:graph|evals|scripts)[/\\]"
OPTIONAL_MAINTAINED_DIR_REF = rf"(?:{MAINTAINED_DIR_REF})?"
RELATIVE_PREFIX = r"(?:\.\.?[/\\])+"
PATH_TARGET = rf"(?:{RELATIVE_PREFIX})?(?:{OPTIONAL_MAINTAINED_DIR_REF}{ROOT_FILE_REF}|{MAINTAINED_DIR_REF}[^`\s)#]+)"
PATH_REF_RE = re.compile(PATH_TARGET)
MARKDOWN_LINK_RE = re.compile(
    r"\]\(\s*(?:<([^>]+)>|([^\s)]+))"
    r"(?:\s+(?:\"[^\"]*\"|'[^']*'|\([^)]*\)))?\s*\)"
)
WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
INLINE_CODE_RE = re.compile(
    r"(?<!`)(`+)(?!`)((?:(?!\n[ \t]*\n).)*?)(?<!`)\1(?!`)", re.DOTALL
)
HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
HEADING_RE = re.compile(r"^#{1,6}[ \t]+(.+?)[ \t]*#*[ \t]*$", re.MULTILINE)
BULLET = r"[ \t]*[-+*][ \t]+"
PAGE_ENTRY_RE = re.compile(rf"^{BULLET}\[\[([^\]]+)\]\][ \t]*:", re.MULTILINE)
EXTERNAL_LINK_RE = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")
QUOTE_RE = re.compile(r"^ {0,3}> ?")
LIST_RE = re.compile(r"^ {0,3}(?:[-+*]|\d{1,9}[.)]) +")


class PathReference(NamedTuple):
    path: str
    fragment: Optional[str]
    display: str
    allow_glob: bool


def strip_fenced_code(text: str) -> str:
    output: List[str] = []
    containers: List[Tuple[str, int]] = []
    fence_char: Optional[str] = None
    fence_length = 0
    for line in text.splitlines(keepends=True):
        rest = line.expandtabs(4)
        depth = 0
        for kind, width in containers:
            if kind == "quote":
                quote = QUOTE_RE.match(rest)
                if quote is None:
                    break
                rest = rest[quote.end() :]
            elif rest.startswith(" " * width):
                rest = rest[width:]
            elif not rest.strip():
                rest = "\n"
            else:
                break
            depth += 1
        if depth < len(containers):
            containers = containers[:depth]
            fence_char = None

        if fence_char is None:
            while True:
                quote = QUOTE_RE.match(rest)
                item = LIST_RE.match(rest)
                if quote is not None:
                    containers.append(("quote", 0))
                    rest = rest[quote.end() :]
                elif item is not None:
                    containers.append(("list", item.end()))
                    rest = rest[item.end() :]
                else:
                    break

        stripped = rest.lstrip(" ")
        indent = len(rest) - len(stripped)
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
    return strip_inline_code(semantic_text(text))


def strip_inline_code(text: str) -> str:
    return INLINE_CODE_RE.sub(lambda match: "\n" * match.group(0).count("\n"), text)


def has_body(text: str) -> bool:
    return any(
        line.strip() and not line.lstrip().startswith("#")
        for line in semantic_text(text).splitlines()
    )


def path_refs(text: str) -> List[PathReference]:
    semantic = semantic_text(text)
    refs = [
        PathReference(match.group(2), None, match.group(2), True)
        for match in INLINE_CODE_RE.finditer(semantic)
        if PATH_REF_RE.fullmatch(match.group(2))
    ]
    markdown = strip_inline_code(semantic)
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
        line for line in link_text(text).splitlines() if re.match(rf"^{BULLET}", line)
    )


def page_entry_nodes(text: str) -> List[str]:
    nodes: List[str] = []
    for match in PAGE_ENTRY_RE.finditer(link_text(text)):
        display = match.group(1).split("|", 1)[0].strip()
        node, _separator, _fragment = display.partition("#")
        if node.strip():
            nodes.append(node.strip())
    return nodes
