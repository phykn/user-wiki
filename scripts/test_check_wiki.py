#!/usr/bin/env python3
import contextlib
import importlib.util
import io
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().with_name("check-wiki.py")
SPEC = importlib.util.spec_from_file_location("check_wiki", SCRIPT)
wiki = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(wiki)

FIXTURE = {
    "README.md": "# README\n\nA small wiki.\n",
    "graph/index.md": "Entry page.\n\n## Route\n\n- Maintenance: [[maintenance]].\n",
    "graph/maintenance.md": "How the wiki is checked.\n\n## Check\n\nRun the checker.\n",
}


def write(root, path, text):
    target = root / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")


def make_wiki(root, files, remove=()):
    for path, text in {**FIXTURE, **files}.items():
        write(root, path, text)
    for path in remove:
        (root / path).unlink()


class CheckTests(unittest.TestCase):
    def assert_problems(self, files, expected, remove=()):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "wiki"
            make_wiki(root, files, remove)
            write(Path(tmp), "outside.md", "Outside the wiki.\n")
            self.assertEqual(wiki.check(root), expected)

    def test_valid_fixture(self):
        self.assert_problems({}, [])

    def test_missing_docs(self):
        self.assert_problems(
            {},
            ["MISSING_DOC README.md", "MISSING_DOC graph/index.md"],
            remove=["README.md", "graph/index.md"],
        )

    def test_root_holds_only_readme(self):
        self.assert_problems(
            {"index.md": "Wrong entry.\n", "CLAUDE.md": "Second entry.\n"},
            ["UNEXPECTED_DOC CLAUDE.md", "UNEXPECTED_DOC index.md"],
        )

    def test_nested_graph_doc(self):
        self.assert_problems({"graph/old/page.md": "Old page.\n"}, ["NESTED_GRAPH_DOC graph/old/page.md"])

    def test_empty_doc(self):
        for text in ("# Empty\n", "# Empty\n\n```\n[[missing]]\n```\n"):
            with self.subTest(text=text):
                self.assert_problems({"README.md": text}, ["EMPTY_DOC README.md"])

    def test_hashtag_line_is_body(self):
        self.assert_problems({"README.md": "#todo\n"}, [])

    def test_page_must_open_with_a_sentence(self):
        self.assert_problems(
            {"graph/maintenance.md": "# Maintenance\n\nRun the checker.\n\n## Check\n"},
            ["MISSING_SUMMARY graph/maintenance.md"],
        )

    def test_unsupported_syntax(self):
        self.assert_problems(
            {"README.md": "# README\n\n[Setup](graph/maintenance.md)\n\n[g]: graph/maintenance.md\n\n<!-- note -->\n"},
            [
                "UNSUPPORTED_SYNTAX README.md -> [Setup](graph/maintenance.md)",
                "UNSUPPORTED_SYNTAX README.md -> [g]: graph/maintenance.md",
                "UNSUPPORTED_SYNTAX README.md -> <!--",
            ],
        )

    def test_external_links_are_allowed(self):
        self.assert_problems(
            {"README.md": "See [the site](https://example.com \"Site\") or [mail](mailto:a@example.com).\n"}, []
        )

    def test_code_is_not_read_for_links_or_syntax(self):
        for text in (
            "Example: `[[missing]]`, `<!--`, and `[x](y.md)`.\n",
            "Example: ``a ` [[missing]] b``.\n",
            "```text\n[[missing]]\n```python\n[x](y.md)\n```\n",
            "~~~text`info\n[[missing]]\n~~~\n",
            "- Nested:\n\n  ```\n  [[missing]]\n  ```\n",
        ):
            with self.subTest(text=text):
                self.assert_problems({"README.md": "Examples.\n\n" + text}, [])

    def test_fences_inside_lists_and_quotes(self):
        self.assert_problems(
            {
                "README.md": "Examples.\n\n- ```text\n  [[missing]]\n  ```\n\n> ```\n> [[missing]]\n> ```\n\n"
                "1. ~~~\n   [[missing]]\n   ~~~\n\nSee [[gone]].\n"
            },
            ["BROKEN_LINK README.md -> gone"],
        )

    def test_unmatched_backticks_do_not_hide_links(self):
        for text in ("Literal ` and [[missing]].\n", "```inline``` and [[missing]].\n"):
            with self.subTest(text=text):
                self.assert_problems({"README.md": text}, ["BROKEN_LINK README.md -> missing"])

    def test_broken_paths(self):
        self.assert_problems(
            {
                "graph/maintenance.md": FIXTURE["graph/maintenance.md"]
                + "Run `scripts/missing.py`, `python3 scripts/absent.py --strict`, and `graph/../../outside.md`.\n"
                + "Globs and folders such as `graph/*.md`, `graph/`, and bare `CLAUDE.md` are fine.\n"
            },
            [
                "BROKEN_PATH graph/maintenance.md -> scripts/missing.py",
                "BROKEN_PATH graph/maintenance.md -> scripts/absent.py",
                "BROKEN_PATH graph/maintenance.md -> graph/../../outside.md",
            ],
        )

    def test_wikilinks_and_anchors(self):
        self.assert_problems(
            {
                "README.md": "# README\n\n## Local\n\n"
                "[[missing]], [[maintenance#Missing]], [[#Nowhere]], "
                "[[maintenance|alias]], [[maintenance#check]], [[#local]].\n"
            },
            [
                "BROKEN_LINK README.md -> missing",
                "BROKEN_ANCHOR README.md -> maintenance#Missing",
                "BROKEN_ANCHOR README.md -> #Nowhere",
            ],
        )

    def test_heading_closing_marks_are_ignored(self):
        self.assert_problems(
            {"graph/maintenance.md": "How the wiki is checked.\n\n## Check ##\n\nRun the checker.\n"}, []
        )

    def test_index_needs_a_route_section(self):
        self.assert_problems(
            {"graph/index.md": "Entry page.\n\n## Routes\n\n- [[maintenance]]\n"},
            ["MISSING_ROUTE_SECTION graph/index.md"],
        )

    def test_only_route_bullets_register_pages(self):
        for route in (
            "- Maintenance: [[maintenance]].\nExtra: [[extra]].\n",
            "- Maintenance: [[maintenance]].\n- Extra: `[[extra]]`.\n",
            "- Maintenance: [[maintenance]].\n\n## Pages\n\n- [[extra]]\n",
        ):
            with self.subTest(route=route):
                self.assert_problems(
                    {"graph/extra.md": "Extra page.\n", "graph/index.md": "Entry page.\n\n## Route\n\n" + route},
                    ["UNROUTED_PAGE graph/extra.md"],
                )

    def test_route_bullets_accept_all_markers_and_anchors(self):
        for marker in ("-", "*", "+"):
            with self.subTest(marker=marker):
                self.assert_problems(
                    {"graph/index.md": f"Entry page.\n\n## Route\n\n{marker} Check: [[maintenance#Check]].\n"}, []
                )


class MainTests(unittest.TestCase):
    def run_main(self, files, remove=()):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "wiki"
            make_wiki(root, files, remove)
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                code = wiki.main(root)
            return code, out.getvalue()

    def test_success(self):
        self.assertEqual(self.run_main({}), (0, "WIKI_CHECK_OK\n"))

    def test_failure_lines_are_ordered_and_unique(self):
        code, out = self.run_main({"README.md": "See [[missing]] and [[missing]].\n"}, remove=["graph/index.md"])
        self.assertEqual(code, 1)
        self.assertEqual(out.splitlines(), ["MISSING_DOC graph/index.md", "BROKEN_LINK README.md -> missing"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
