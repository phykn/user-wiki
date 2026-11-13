#!/usr/bin/env python3
import re
import sys
from pathlib import Path

CODE_RE = re.compile(r"`([^`]+)`")
WIKILINK_RE = re.compile(r"\[\[([^\[\]]+)\]\]")
LINK_RE = re.compile(r"\[[^\[\]]*\]\(([^()\s]*)[^()]*\)")


def check_wiki(root):
    graph = root / "graph"
    readme = root / "README.md"
    pages = sorted(graph.glob("*.md"))
    stems = {page.stem for page in pages}
    routed = set()

    problems = [f"MISSING_DOC {name}" for name in ("README.md", "graph/index.md") if not (root / name).is_file()]
    problems += [
        f"UNEXPECTED_DOC {path.relative_to(root).as_posix()}"
        for path in sorted({*root.glob("*.md"), *graph.rglob("*.md")})
        if path != readme and path.parent != graph
    ]

    for path in [readme, *pages]:
        if not path.is_file():
            continue
        name = path.relative_to(root).as_posix()
        lines = path.read_text(encoding="utf-8").splitlines()
        if path != readme and next((line for line in lines if line.strip()), "#").startswith("#"):
            problems.append(f"MISSING_SUMMARY {name}")

        in_fence = False
        in_route = False
        for line in lines:
            if line.lstrip().startswith("```"):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            if line.startswith("#"):
                in_route = name == "graph/index.md" and line.strip() == "## Route"
            plain = CODE_RE.sub(" ", line)

            for match in LINK_RE.finditer(plain):
                if not match.group(1).startswith(("http://", "https://", "mailto:")):
                    problems.append(f"UNSUPPORTED_SYNTAX {name} -> {match.group()}")
            for code in CODE_RE.findall(line):
                for token in code.split():
                    if token.startswith(("graph/", "scripts/")) and not (root / token).exists():
                        problems.append(f"BROKEN_PATH {name} -> {token}")
            for link in WIKILINK_RE.findall(plain):
                if link not in stems:
                    problems.append(f"BROKEN_LINK {name} -> {link}")
                elif in_route:
                    routed.add(link)

    problems += [f"UNROUTED_PAGE graph/{stem}.md" for stem in sorted(stems - routed - {"index"})]
    print("\n".join(problems) if problems else "WIKI_CHECK_OK")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(check_wiki(Path(__file__).resolve().parent.parent))
