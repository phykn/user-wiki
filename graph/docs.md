Confirmed preferences for documents, research, wikis, prompts, and work instructions.

## Reader And Order

Write for the reader's next question or decision.

- A README or first screen explains what the project is, why it matters, and whether the reader needs it, before any internal structure.
- Use predictable headings. Introduce a term, diagram, or code block only after the reader needs it.
- When an explanation is confusing, fix its order before adding sentences. Write procedures in the order they run.
- Name concrete objects, actions, and outputs in easy words that do not depend on hidden context.
- Prefer removing content to adding it. Add only what the reader needs to understand, judge, or act, and keep necessary meaning.

## Names And Duplication

- Prefer short noun filenames without redundant type prefixes or names that look like duplicates.
- Do not repeat what a filename, heading, nearby sentence, or responsible page already says. Give each bullet a distinct role.

## Editing Boundaries

- A formatting-only edit keeps accepted claims, names, technical scope, and meaning.
- Do not bring in a technique from another document unless the task needs it.

## Evidence

- From an example, take the structure that transfers, not its domain details.
- Put evidence next to the claim it supports. Check time-sensitive facts against current direct sources.
- Keep facts apart from interpretation. State dates, scope, and uncertainty where they change the conclusion.
- A problem summary states what exists, what is needed, and why the gap is hard to close.

## Document Graph

- Entry pages decide which page to read for which task. Links in other pages only point to a dependency or the page that owns a rule.
- Keep graph pages flat. List every page in both `graph/index.md` sections: `Route` gives its reading trigger, and `Pages` gives its responsibility.
- Link each eval file from the page that tells agents when to review it.
- Keep a page separate only when its own responsibility and route make guidance easier to find.

## Files, Sources, And Records

- In a process that produces files, make the output file and the next input clear. Keep runtime work files apart from rules.
- Keep input names in summaries and filenames, and keep source lists apart from interpretation.
- When text copied from a browser or form lacks a value, mark it text-unverified unless the visible page shows it is empty.
- A reusable process record stores the order of questions, the criteria for judgment, and how the next action is chosen.
- Write a long-term goal as an operating contract with success criteria, non-goals, and signals that show progress.

## Check

Read the changed page starting from its entrypoint. Check that accepted meaning survived, that page responsibilities do not overlap, and that nothing is duplicated, stale, empty, or broken. Replace conflicting wording instead of adding a correction beside it. Run this wiki's checks from [[commands]].
