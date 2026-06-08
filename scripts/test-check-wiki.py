#!/usr/bin/env python3
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


SOURCE_SCRIPT = Path(__file__).resolve().with_name("check-wiki.py")


def write_file(root: Path, path: str, text: str) -> None:
    target = root / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")


def make_fixture(root: Path) -> None:
    write_file(root, "AGENTS.md", "# Agents\n")
    write_file(root, "README.md", "# README\n")
    write_file(root, "graph/index.md", "# Index\n[[commands]]\n")
    write_file(root, "graph/commands.md", "# Commands\n")
    write_file(root, "evals/personal-agent.md", "# Personal Agent\n")
    (root / "scripts").mkdir(exist_ok=True)
    shutil.copy2(SOURCE_SCRIPT, root / "scripts/check-wiki.py")


def run_check(root: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "scripts/check-wiki.py"],
        cwd=root,
        text=True,
        capture_output=True,
    )


def assert_result(
    name: str,
    mutate,
    expected_code: int,
    expected_output: str,
) -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        make_fixture(root)
        mutate(root)
        result = run_check(root)
        output = result.stdout + result.stderr
        if result.returncode != expected_code or expected_output not in output:
            print(f"FAIL {name}")
            print(f"expected code {expected_code}, output containing {expected_output!r}")
            print(f"actual code {result.returncode}")
            print(output)
            raise SystemExit(1)


def main() -> int:
    assert_result(
        "valid fixture",
        lambda root: None,
        0,
        "WIKI_CHECK_OK",
    )
    assert_result(
        "missing required entrypoint",
        lambda root: (root / "graph/index.md").unlink(),
        1,
        "MISSING_DOC graph/index.md",
    )
    assert_result(
        "missing backtick path reference",
        lambda root: write_file(root, "graph/commands.md", "# Commands\n`scripts/missing.py`\n"),
        1,
        "BROKEN_PATH_REF graph/commands.md -> scripts/missing.py",
    )
    assert_result(
        "glob path reference is not a stale file reference",
        lambda root: write_file(root, "graph/commands.md", "# Commands\n`graph/*.md`\n"),
        0,
        "WIKI_CHECK_OK",
    )
    assert_result(
        "missing markdown path reference",
        lambda root: write_file(root, "README.md", "# README\n[missing](graph/missing.md)\n"),
        1,
        "BROKEN_PATH_REF README.md -> graph/missing.md",
    )
    print("CHECK_WIKI_TESTS_OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
