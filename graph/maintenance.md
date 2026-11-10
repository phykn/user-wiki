How this wiki is laid out, written, and checked.

## Structure

- The root holds two Markdown files: `AGENTS.md`, the entry for agents working here and for older pointers, and `README.md`. There is intentionally no root-level index or second entry file.
- Pages sit directly in `graph/`, with no subfolders. The `Route` section of `graph/index.md` links every page from a bullet.
- Each page opens with one sentence that states its responsibility. Read those opening lines to decide which page owns a rule.
- `graph/index.md` is read on every task, and `AGENTS.md` too by agents that start here or follow an older pointer, so together they stay within 600 words. Make room before adding to them.
- Review cases live in `evals/`. The page that says when to review an eval file links it. Each case has a `Rule:` line that links the section that owns its rule.

## Syntax

The checker understands only this subset of Markdown, so keep links and paths within it.

- Write each paragraph and list item on one line. The checker reads one line at a time, so it misses a wrapped link, path, or route.
- Write headings as plain text, without emphasis or links.
- Link a page with `[[page]]`, a section with `[[page#Heading]]`, and a section of the same page with `[[#Heading]]`. The heading text must match, ignoring case.
- Name a wiki file in inline code by its path from the wiki root, such as `graph/setup.md`. A path that starts with `graph/`, `evals/`, or `scripts/` must exist inside the wiki; globs are not checked.
- Use Markdown links only for external `http`, `https`, or `mailto` addresses. Do not use relative Markdown links, reference definitions, or HTML comments; the checker reports them.
- Put examples that contain links or paths in fenced code blocks, which the checker skips.

## Check

After every edit to this wiki, run these from the wiki root and fix what they report, then inspect the status:

- `python3 scripts/check-wiki.py`: checks the layout, empty pages, pages that open with a heading, the syntax subset, paths, links, anchors, routes, eval links and `Rule:` lines, and the entry budget. It prints `WIKI_CHECK_OK`, or one problem per line and exits with status 1.
- `python3 -m unittest discover -s scripts -p 'test_*.py' -v`: runs the checker's regression tests against small fixture wikis.
- `git diff --check`: checks whitespace in pending changes. It skips untracked files, so run `git add -N` on new files first.
- `git status --short --branch`: shows added, modified, and deleted files and branch sync before finishing.

If the commands cannot run, report that the review was static only.

## Review

- `git ls-files --cached --others --exclude-standard` and `git grep -n --untracked '<term>'`: list maintained files, including new ones, and find duplicate rules, stale wording, and filename references.
- `evals/behavior.md` holds review prompts, not automatic tests. After an edit that changes behavior, review only the cases whose `Rule:` line links a changed section.
