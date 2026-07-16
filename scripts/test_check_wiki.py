#!/usr/bin/env python3
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from typing import List
import unittest


SOURCE_SCRIPT = Path(__file__).resolve().with_name("check-wiki.py")


def write_file(root: Path, path: str, text: str) -> None:
    target = root / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")


def make_fixture(root: Path) -> None:
    write_file(root, "AGENTS.md", "# Agents\nCanonical: `graph/index.md`.\n")
    write_file(root, "README.md", "# README\nSee `AGENTS.md`.\n")
    write_file(
        root,
        "graph/index.md",
        "# Index\n\n## Route\n\n- Maintenance: [[commands]].\n\n"
        "## Pages\n\n- [[commands]]: maintenance commands.\n",
    )
    write_file(
        root,
        "graph/commands.md",
        "# Commands\n\nReview `evals/personal-agent.md`.\n",
    )
    write_file(
        root,
        "evals/personal-agent.md",
        "# Personal Agent\n\nReview behavior changes.\n",
    )
    (root / "scripts").mkdir(exist_ok=True)
    shutil.copy2(SOURCE_SCRIPT, root / "scripts/check-wiki.py")


def run_check(root: Path) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, "scripts/check-wiki.py"],
        cwd=root,
        text=True,
        capture_output=True,
    )


class WikiCheckTests(unittest.TestCase):
    def assert_check(self, mutate, expected: List[str]) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            make_fixture(root)
            mutate(root)
            result = run_check(root)
            expected_code = 0 if expected == ["WIKI_CHECK_OK"] else 1
            self.assertEqual(result.returncode, expected_code, result.stderr)
            self.assertEqual(result.stdout.splitlines(), expected)
            self.assertEqual(result.stderr, "")

    def test_valid_fixture(self) -> None:
        self.assert_check(lambda root: None, ["WIKI_CHECK_OK"])

    def test_missing_required_entrypoint(self) -> None:
        self.assert_check(
            lambda root: (root / "graph/index.md").unlink(),
            [
                "MISSING_DOC graph/index.md",
                "BROKEN_PATH_REF AGENTS.md -> graph/index.md",
                "MISSING_ENTRYPOINT_REF AGENTS.md -> graph/index.md",
            ],
        )

    def test_missing_canonical_route_reference(self) -> None:
        self.assert_check(
            lambda root: write_file(root, "AGENTS.md", "# Agents\n\nNo route.\n"),
            ["MISSING_ENTRYPOINT_REF AGENTS.md -> graph/index.md"],
        )

    def test_canonical_route_requires_an_exact_path_reference(self) -> None:
        self.assert_check(
            lambda root: write_file(
                root,
                "AGENTS.md",
                "# Agents\n\nThe unrelated name badgraph/index.md.bak appears here.\n",
            ),
            ["MISSING_ENTRYPOINT_REF AGENTS.md -> graph/index.md"],
        )

    def test_unexpected_root_index(self) -> None:
        self.assert_check(
            lambda root: write_file(root, "index.md", "# Wrong\n\nWrong route.\n"),
            ["UNEXPECTED_DOC index.md"],
        )

    def test_heading_only_document_is_empty(self) -> None:
        self.assert_check(
            lambda root: write_file(root, "evals/personal-agent.md", "# Empty\n"),
            ["EMPTY_DOC evals/personal-agent.md"],
        )

    def test_comment_only_document_is_empty(self) -> None:
        self.assert_check(
            lambda root: write_file(
                root,
                "evals/personal-agent.md",
                "# Empty\n\n<!-- This is not guidance. -->\n",
            ),
            ["EMPTY_DOC evals/personal-agent.md"],
        )

    def test_missing_backtick_path_reference(self) -> None:
        self.assert_check(
            lambda root: write_file(
                root,
                "graph/commands.md",
                "# Commands\n\nReview `evals/personal-agent.md`.\n"
                "Run `scripts/missing.py`.\n",
            ),
            ["BROKEN_PATH_REF graph/commands.md -> scripts/missing.py"],
        )

    def test_glob_path_reference_is_allowed(self) -> None:
        self.assert_check(
            lambda root: write_file(
                root,
                "graph/commands.md",
                "# Commands\n\nReview `evals/personal-agent.md` and `graph/*.md`.\n",
            ),
            ["WIKI_CHECK_OK"],
        )

    def test_missing_markdown_path_reference(self) -> None:
        self.assert_check(
            lambda root: write_file(
                root,
                "README.md",
                "# README\n\n[Missing](graph/missing.md)\n",
            ),
            ["BROKEN_PATH_REF README.md -> graph/missing.md"],
        )

    def test_missing_relative_markdown_path_reference(self) -> None:
        self.assert_check(
            lambda root: write_file(
                root,
                "graph/commands.md",
                "# Commands\n\nReview `evals/personal-agent.md`.\n"
                "See [missing](../missing.md).\n",
            ),
            ["BROKEN_PATH_REF graph/commands.md -> ../missing.md"],
        )

    def test_markdown_query_does_not_bypass_path_check(self) -> None:
        self.assert_check(
            lambda root: write_file(
                root,
                "README.md",
                "# README\n\n[Missing](graph/missing.md?raw=1)\n",
            ),
            ["BROKEN_PATH_REF README.md -> graph/missing.md?raw=1"],
        )

    def test_missing_markdown_anchor(self) -> None:
        self.assert_check(
            lambda root: write_file(
                root,
                "README.md",
                "# README\n\n[Bad](graph/commands.md#does-not-exist)\n",
            ),
            ["BROKEN_ANCHOR README.md -> graph/commands.md#does-not-exist"],
        )

    def test_existing_markdown_anchor(self) -> None:
        self.assert_check(
            lambda root: write_file(
                root,
                "README.md",
                "# README\n\n[Commands](graph/commands.md#commands)\n",
            ),
            ["WIKI_CHECK_OK"],
        )

    def test_missing_root_path_reference(self) -> None:
        self.assert_check(
            lambda root: write_file(root, "README.md", "# README\n\n`MISSING.md`\n"),
            ["BROKEN_PATH_REF README.md -> MISSING.md"],
        )

    def test_missing_root_dotfile_reference(self) -> None:
        self.assert_check(
            lambda root: write_file(root, "README.md", "# README\n\n`.gitignore`\n"),
            ["BROKEN_PATH_REF README.md -> .gitignore"],
        )

    def test_intentional_missing_root_index_mention(self) -> None:
        self.assert_check(
            lambda root: write_file(
                root,
                "README.md",
                "# README\n\nThere is no root-level index entrypoint.\n",
            ),
            ["WIKI_CHECK_OK"],
        )

    def test_explicit_root_relative_index_reference_is_checked(self) -> None:
        self.assert_check(
            lambda root: write_file(
                root,
                "graph/commands.md",
                "# Commands\n\nReview `evals/personal-agent.md` and `../index.md`.\n",
            ),
            ["BROKEN_PATH_REF graph/commands.md -> ../index.md"],
        )

    def test_broken_wikilink(self) -> None:
        self.assert_check(
            lambda root: write_file(
                root,
                "graph/index.md",
                "# Index\n\n## Route\n\n- [[commands]] and [[missing]].\n\n"
                "## Pages\n\n- [[commands]]: commands.\n- [[missing]]: missing.\n",
            ),
            ["BROKEN_WIKILINK graph/index.md -> missing"],
        )

    def test_missing_wikilink_anchor(self) -> None:
        self.assert_check(
            lambda root: write_file(
                root,
                "graph/index.md",
                "# Index\n\n## Route\n\n- [[commands#missing]].\n\n"
                "## Pages\n\n- [[commands]]: commands.\n",
            ),
            ["BROKEN_WIKILINK_ANCHOR graph/index.md -> commands#missing"],
        )

    def test_wikilinks_are_checked_outside_graph(self) -> None:
        self.assert_check(
            lambda root: write_file(
                root,
                "README.md",
                "# README\n\nSee [[missing]].\n",
            ),
            ["BROKEN_WIKILINK README.md -> missing"],
        )

    def test_fenced_examples_are_not_links(self) -> None:
        self.assert_check(
            lambda root: write_file(
                root,
                "README.md",
                "# README\n\nExamples only.\n\n```markdown\n"
                "[[missing]]\n[Bad](graph/missing.md)\n```\n",
            ),
            ["WIKI_CHECK_OK"],
        )

    def test_fence_with_info_text_does_not_close_an_outer_fence(self) -> None:
        self.assert_check(
            lambda root: write_file(
                root,
                "README.md",
                "# README\n\nExamples only.\n\n```text\n```python\n"
                "[[missing-inside-code]]\n```\n```\n",
            ),
            ["WIKI_CHECK_OK"],
        )

    def test_unrouted_graph_document(self) -> None:
        def mutate(root: Path) -> None:
            write_file(root, "graph/orphan.md", "# Orphan\n\nOrphan guidance.\n")
            write_file(
                root,
                "graph/index.md",
                "# Index\n\n## Route\n\n- [[commands]].\n\n"
                "## Pages\n\n- [[commands]]: commands.\n"
                "- [[orphan]]: orphan.\n",
            )

        self.assert_check(mutate, ["UNROUTED_GRAPH_DOC graph/orphan.md"])

    def test_unlisted_graph_document(self) -> None:
        def mutate(root: Path) -> None:
            write_file(root, "graph/orphan.md", "# Orphan\n\nOrphan guidance.\n")
            write_file(
                root,
                "graph/index.md",
                "# Index\n\n## Route\n\n- [[commands]].\n- [[orphan]].\n\n"
                "## Pages\n\n- [[commands]]: commands.\n",
            )

        self.assert_check(mutate, ["UNLISTED_GRAPH_DOC graph/orphan.md"])

    def test_comment_only_route_registration_is_ignored(self) -> None:
        def mutate(root: Path) -> None:
            write_file(root, "graph/orphan.md", "# Orphan\n\nOrphan guidance.\n")
            write_file(
                root,
                "graph/index.md",
                "# Index\n\n## Route\n\n- [[commands]].\n"
                "<!-- - [[orphan]]. -->\n\n## Pages\n\n"
                "- [[commands]]: commands.\n- [[orphan]]: orphan.\n",
            )

        self.assert_check(mutate, ["UNROUTED_GRAPH_DOC graph/orphan.md"])

    def test_comment_only_page_registration_is_ignored(self) -> None:
        def mutate(root: Path) -> None:
            write_file(root, "graph/orphan.md", "# Orphan\n\nOrphan guidance.\n")
            write_file(
                root,
                "graph/index.md",
                "# Index\n\n## Route\n\n- [[commands]].\n- [[orphan]].\n\n"
                "## Pages\n\n- [[commands]]: commands.\n"
                "<!-- - [[orphan]]: orphan. -->\n",
            )

        self.assert_check(mutate, ["UNLISTED_GRAPH_DOC graph/orphan.md"])

    def test_duplicate_page_entry(self) -> None:
        self.assert_check(
            lambda root: write_file(
                root,
                "graph/index.md",
                "# Index\n\n## Route\n\n- [[commands]].\n\n"
                "## Pages\n\n- [[commands]]: first.\n- [[commands]]: second.\n",
            ),
            ["DUPLICATE_PAGE_ENTRY graph/index.md -> commands"],
        )

    def test_nested_graph_document_is_rejected(self) -> None:
        self.assert_check(
            lambda root: write_file(
                root,
                "graph/nested/page.md",
                "# Nested\n\nUnsupported nested node.\n",
            ),
            ["UNSUPPORTED_NESTED_GRAPH_DOC graph/nested/page.md"],
        )

    def test_unrouted_eval_document(self) -> None:
        self.assert_check(
            lambda root: write_file(
                root,
                "evals/other.md",
                "# Other\n\nUnrouted review prompts.\n",
            ),
            ["UNROUTED_EVAL_DOC evals/other.md"],
        )

    def test_comment_only_eval_reference_is_ignored(self) -> None:
        self.assert_check(
            lambda root: write_file(
                root,
                "graph/commands.md",
                "# Commands\n\nNo active eval route.\n"
                "<!-- `evals/personal-agent.md` -->\n",
            ),
            ["UNROUTED_EVAL_DOC evals/personal-agent.md"],
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
