Record only major user-wiki structural changes. Detailed rule text belongs in the responsible document.

## 2026-06-06

- Added reader-fit rules for documents: write for what the reader can see, judge, and do next instead of displaying everything the AI knows.
- Extended that reader-fit rule into general workflow, coding, and proposals: ask or propose only where it changes the next action.
- Added a completion-reporting rule that explains the original problem, why the change was made, how it resolves the problem, and what verified it.
- Clarified that concrete verification evidence is preferred over purely logical assurance in completion reports.
- Clarified that when verification cannot be run, the report should say so and explain the strongest available static reasoning plus remaining risk.
- Clarified that in-scope structural problems should be fixed as part of the work, while unrelated cleanup stays out of scope.
- Broadened structural cleanup guidance so adjacent files, sections, entrypoints, and role boundaries are cleaned when they share the same structural cause.
- Clarified how the required `user-wiki update:` line works when higher-priority system citations or machine-readable blocks must follow it, and strengthened repeated verification commands.
- Clarified that `AGENTS.md` -> `graph/index.md` is the canonical route and that missing root `index.md` / `CORE.md` files should not be narrated as a problem.
- Added a workflow rule that wiki guidance should affect the actual working hypothesis, edit choice, review standard, or answer shape rather than only being reported as read.
- Reflected the user's preferred evidence-driven explanation pattern across the judgment anchor and document-writing rules without copying domain-specific example content.
- Added guidance for applying this wiki to another Git repository through target-repo entrypoints rather than copying wiki content wholesale, and made `workflow.md` required for that path.
- Clarified that project-common preferences surfaced during target-repository work should update the source user-wiki when writable, or be reported as pending when not writable, with an explicit `user-wiki update:` final line.

## 2026-06-03

- Made the root `AGENTS.md` the user-wiki bootstrap entrypoint, and moved the actual wiki document nodes under the `graph/` folder.
- Updated `index.md` and `tools.md` so reading and check locations use the new `graph/` structure.
- Added root `README.md` as the repository-facing entrypoint.
- Refined English wording after the graph translation pass.
- Split autonomous AI guidance so `intuition.md` owns judgment criteria and `workflow.md` owns progress habits.
- Replaced `tools.md` with `commands.md` so repeated commands stay separate from wiki policy.
- Rewrote `intuition.md` in natural English while preserving its judgment role.

## 2026-06-02

- Reorganized the wiki around general defaults.
- Organized the current core flow into `intuition.md`, `policy.md`, `workflow.md`, `code.md`, `docs.md`, `theory.md`, and `tools.md`.
- Deleted `candidate-preferences.md` and removed the operating path for separately storing unconfirmed candidates.

## 2026-05-30

- Created the initial user-wiki structure and update loop.
- Strengthened the connection for finding and checking the user-wiki from Desktop/CLI.
