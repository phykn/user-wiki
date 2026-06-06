Record only major user-wiki structural changes. Detailed rule text belongs in the responsible document.

## 2026-06-06

- Lightened the wiki runtime route: size the task before expanding reading, keep one-off work direct, and read related pages only when they change the current decision.
- Added small examples for applying `intuition.md`, tightened duplication ownership, and reduced `theory.md` into a temporary tie-breaker with stale-interpretation guards.
- Replaced the fixed `user-wiki update:` reporting ritual with natural update reporting only when the wiki changed or a pending wiki update remains.
- Converted shallow examples into bad/good pairs and added autonomy failure guards so the wiki is less self-referential and easier to execute.
- Clarified canonical route and cross-repository application: `AGENTS.md` -> `graph/index.md`, no root `index.md`, target-repo entrypoints first, required `workflow.md`, and explicit source-wiki update reporting.
- Added the autonomous-work target: the wiki should make AI work in the user's way, not merely match tone or report that pages were read.
- Strengthened response and evidence standards: problem-first completion reports, concrete verification evidence, explicit static reasoning when verification cannot run, and reader-fit explanations.
- Refined question, proposal, and autonomy rules: ask only when the answer changes the next action, choose AI-judgable alternatives directly, revise contradicted plans, and incorporate in-scope counterexamples immediately.
- Refined structural cleanup boundaries: fix in-scope structural problems, clean affected neighborhoods and broader whole structures when local fixes preserve the wrong shape, and separate large counterexamples into current work versus new work.

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
