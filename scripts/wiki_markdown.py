import re
from typing import Dict, List, NamedTuple, Optional, Set, Tuple
from urllib.parse import unquote


ROOT_FILE_REF = r"(?:[A-Za-z0-9_.-]+\.md|\.gitignore)"
MAINTAINED_DIR_REF = r"(?:graph|evals|scripts)[/\\]"
OPTIONAL_MAINTAINED_DIR_REF = rf"(?:{MAINTAINED_DIR_REF})?"
RELATIVE_PREFIX = r"(?:\.\.?[/\\])+"
PATH_TARGET = rf"(?:{RELATIVE_PREFIX})?(?:{OPTIONAL_MAINTAINED_DIR_REF}{ROOT_FILE_REF}|{MAINTAINED_DIR_REF}[^`\s)#]+)"
PATH_REF_RE = re.compile(PATH_TARGET)
LINK_TITLE = r"(?:\"[^\"]*\"|'[^']*'|\([^)]*\))"
MARKDOWN_LINK_RE = re.compile(
    rf"\]\(\s*(?:<([^>]+)>|([^\s)]+))(?:\s+{LINK_TITLE})?\s*\)"
)
REFERENCE_DEF_RE = re.compile(
    r"^ {0,3}\[(?!\^)[^\]]+\]:[ \t]*(?:<([^>]+)>|(\S+))"
    rf"(?:[ \t]+{LINK_TITLE})?[ \t]*$",
    re.MULTILINE,
)
WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
INLINE_CODE_RE = re.compile(
    r"(?<!`)(`+)(?!`)((?:(?!\n[ \t]*\n).)*?)(?<!`)\1(?!`)", re.DOTALL
)
INLINE_TOKEN_RE = re.compile(r"<!--|`+")
HEADING_RE = re.compile(r"^#{1,6}[ \t]+(.+?)(?:[ \t]+#+)?[ \t]*$", re.MULTILINE)
HEADING_MARKER_RE = re.compile(r"#{1,6}(?:[ \t]|$)")
EMPHASIS_RE = re.compile(r"[*~`]+|(?<![^\W_])_+|_+(?![^\W_])")
BULLET = r"[ \t]*[-+*][ \t]+"
PAGE_ENTRY_RE = re.compile(rf"^{BULLET}\[\[([^\]]+)\]\][ \t]*:", re.MULTILINE)
EXTERNAL_LINK_RE = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")
QUOTE_RE = re.compile(r"^ {0,3}> ?")
LIST_RE = re.compile(r"^ {0,3}(?:[-+*]|\d{1,9}[.)]) +")


class PathReference(NamedTuple):
    path: str
    fragment: Optional[str]
    display: str
    is_link: bool


def semantic_text(text: str) -> str:
    output: List[str] = []
    containers: List[Tuple[str, int]] = []
    fence_char: Optional[str] = None
    fence_length = 0
    offset = 0
    comment_end = 0
    code_end = 0
    for line in text.splitlines(keepends=True):
        start = offset
        offset += len(line)
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
            if start < comment_end or marker is None or (
                marker.group(1)[0] == "`" and "`" in stripped[marker.end() :]
            ):
                pos = start
                while pos < offset:
                    if pos < comment_end:
                        end = min(offset, comment_end)
                        output.append(re.sub(r"[^\r\n]", " ", text[pos:end]))
                    elif pos < code_end:
                        end = min(offset, code_end)
                        output.append(text[pos:end])
                    else:
                        token = INLINE_TOKEN_RE.search(text, pos, offset)
                        if token is None:
                            output.append(text[pos:offset])
                            break
                        output.append(text[pos:token.start()])
                        pos = token.start()
                        if token.group() == "<!--":
                            close = text.find("-->", token.end())
                            if close >= 0:
                                comment_end = close + 3
                                continue
                        else:
                            code = INLINE_CODE_RE.match(text, pos)
                            if code is not None:
                                code_end = code.end()
                                continue
                        end = token.end()
                        output.append(text[pos:end])
                    pos = end
                continue
            fence_char = marker.group(1)[0]
            fence_length = len(marker.group(1))
            code_end = 0
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


def link_text(text: str) -> str:
    return strip_inline_code(semantic_text(text))


def strip_inline_code(text: str) -> str:
    return INLINE_CODE_RE.sub(lambda match: "\n" * match.group(0).count("\n"), text)


def has_body(text: str) -> bool:
    return any(
        line.strip() and not HEADING_MARKER_RE.match(line.lstrip())
        for line in semantic_text(text).splitlines()
    )


def path_refs(text: str) -> List[PathReference]:
    semantic = semantic_text(text)
    refs = [
        PathReference(token, None, token, False)
        for match in INLINE_CODE_RE.finditer(semantic)
        for token in match.group(2).split()
        if PATH_REF_RE.fullmatch(token)
    ]
    markdown = strip_inline_code(semantic)
    links = [*MARKDOWN_LINK_RE.finditer(markdown), *REFERENCE_DEF_RE.finditer(markdown)]
    for match in links:
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
                is_link=True,
            )
        )
    return refs


def heading_keys(text: str) -> Set[str]:
    keys: Set[str] = set()
    counts: Dict[str, int] = {}
    for match in HEADING_RE.finditer(semantic_text(text)):
        label = heading_label(match.group(1)).casefold()
        slug = re.sub(r"[^\w\- ]", "", label).replace(" ", "-")
        key = slug
        while key in counts:
            counts[slug] += 1
            key = f"{slug}-{counts[slug]}"
        counts[key] = 0
        keys.update((label, key))
    return keys


def heading_label(heading: str) -> str:
    heading = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", heading)
    parts: List[str] = []
    pos = 0
    for code in INLINE_CODE_RE.finditer(heading):
        parts.append(EMPHASIS_RE.sub("", heading[pos : code.start()]))
        parts.append(code.group(2))
        pos = code.end()
    parts.append(EMPHASIS_RE.sub("", heading[pos:]))
    return "".join(parts).strip()


def section_text(text: str, heading: str) -> Optional[str]:
    match = re.search(
        rf"^##[ \t]+{re.escape(heading)}(?:[ \t]+#+)?[ \t]*$\n?"
        r"(.*?)(?=^##[ \t]+|\Z)",
        link_text(text),
        flags=re.MULTILINE | re.DOTALL,
    )
    return match.group(1) if match else None


def split_wikilink(target: str) -> Tuple[str, Optional[str], str]:
    display = target.split("|", 1)[0].strip()
    node, has_fragment, fragment = display.partition("#")
    return node.strip(), fragment.strip() if has_fragment else None, display


def wikilink_parts(text: str) -> List[Tuple[str, Optional[str], str]]:
    return [
        split_wikilink(match.group(1))
        for match in WIKILINK_RE.finditer(link_text(text))
    ]


def route_nodes(section: str) -> Set[str]:
    nodes = {
        split_wikilink(target)[0]
        for line in section.splitlines()
        if re.match(BULLET, line)
        for target in WIKILINK_RE.findall(line)
    }
    return nodes - {""}


def page_entry_nodes(section: str) -> List[str]:
    nodes = [split_wikilink(target)[0] for target in PAGE_ENTRY_RE.findall(section)]
    return [node for node in nodes if node]
