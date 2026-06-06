## Purpose

Accumulate only project-common work preferences and user understanding. Do not exaggerate a feeling from one conversation into a permanent rule.

`intuition.md` is the higher-level judgment sense. This document is the operating contract for that sense: updates, document boundaries, and priority.

## Scope

Documents, code, reviews, design, operating rules, and repeated work count as non-trivial work.

One-off results such as checking the time, short translations, or single command output may be excluded.

## Update Criteria

Update the relevant documents even if the user does not explicitly say "save this" in the following cases:

- The user explicitly says something like "reflect this in the global wiki," "do it this way going forward," or "save this as my preference."
- The user clearly states a project-common preference or work method.
- The user says existing wiki content is wrong or stale.
- The user directly asks to create or edit a specific document.
- A confirmed work method changes, so the related document also needs to be aligned.

Automatic updates should directly reflect only clear project-common preferences surfaced in the current conversation. Do not create a background log or candidate extraction system outside the conversation.

Project-specific content belongs in that project's `AGENTS.md` or project wiki.

These update rules still apply when this wiki is being used from another project. If a target-repository task surfaces a new or corrected project-common preference, update this source user-wiki when it is available and writable. If the source wiki is not writable or not checked out, state the pending user-wiki update in the final answer instead of silently treating the target-repository edit as enough.

## Update Loop

At the end of non-trivial work, check:

1. Does the center, tension, purpose, constraints, and direction of dissatisfaction from the original problem remain after the answer or edit?
2. Is any newly surfaced preference or correction valid outside the current repo?
3. Would it reduce the chance of repeating the same mistake in future work?
4. Is it clear enough to add as a confirmed rule in the responsible document?
5. Does it conflict with existing confirmed documents, or make any existing content stale?

If the wiki was edited, check for empty documents, duplication, stale wording, and broken links where relevant. `commands.md` may list repeated commands, but this document owns the requirement to check.

Record major structural changes or changes spanning multiple documents in `changelog.md`. Do not repeat detailed rule text there.

End the final answer with one visible line: `user-wiki update: <updated files, pending update, or none>`.
For target-repository work, this line is still required even when the target repository also changed.

## Placement

Reflect confirmed preferences in the responsible document.

Reflect current interpretations that help understand the user in `theory.md`.

## Document Structure Principles

Write documents in a MECE way.

- Each document has an independent purpose.
- Do not repeat the same content across multiple documents.
- Do not mix content that belongs to another document's purpose.
- Summary documents should contain only entrypoints and links; detailed rules belong in the responsible document.

Create a new document only when one of the following is true:

- The confirmed content is worth keeping as a node.
- Adding it to an existing document would mix purposes.

Filenames follow these rules:

- `index.md` and `policy.md` are fixed operating anchors.
- Other documents default to short English noun forms, while user-specified names or tool names remain as-is.
- Separate words with hyphens.
- Do not put particles or explanatory sentences in filenames.

## Priority

If instructions conflict, follow this order:

1. System and developer instructions.
2. The current explicit user request.
3. Project `AGENTS.md` and project-local instructions.
4. Confirmed documents in this wiki.
