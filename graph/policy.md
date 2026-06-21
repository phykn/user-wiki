## Purpose

Accumulate only project-common work preferences and user understanding. Do not turn one conversation's feeling into a permanent rule.

This document owns update rules, document boundaries, and priority. Use [[docs]] for wording, filenames, and graph-shape standards.

## Scope

This policy applies to durable preferences and repeated work: documents, code, reviews, design, operating rules, and corrections meant to affect future answers.

It usually does not apply to one-off results such as checking the time, short translations, or single command output.

## Update Criteria

Update the responsible document even if the user does not explicitly say "save this" when:

- the user explicitly asks to save, reflect, or use something going forward;
- the user clearly states a project-common preference or work method;
- the user says existing wiki content is wrong or stale;
- the user directly asks to create or edit a specific document;
- a confirmed work method changes, so the related document also needs to change.

Automatic updates should directly reflect only clear project-common preferences surfaced in the current conversation. Do not create a background log or candidate extraction system outside the conversation.

Project-specific content belongs in that project's `AGENTS.md` or project wiki.

When this wiki is used from another project, the same rule applies: update this source wiki when a new project-common preference is confirmed and the source wiki is writable. If it is not writable or not checked out, report the pending user-wiki update instead of silently dropping it.

## Update Loop

At the end of non-trivial work, check:

1. Does the original purpose still survive the answer or edit?
2. Is any newly surfaced preference valid outside the current workspace?
3. Would saving it reduce a repeated failure?
4. Is there one responsible document for it?
5. Would it conflict with or make existing content stale?

If these checks do not identify a reusable failure or confirmed preference, do not update the wiki.

If the wiki was edited, check for empty documents, duplication, stale wording, broken links, and role overlap where relevant. `commands.md` may list repeated commands, but this document owns the requirement to check.

Record major structural changes or changes spanning multiple documents in `changelog.md`. Do not repeat detailed rule text there.

## Placement

- Put each rule in the one document future readers will use.
- Put current interpretations that help understand the user in [[theory]].
- Keep summary documents to entrypoints and links; detailed rules belong in the responsible document.
- Create a new document only when an existing document would mix purposes or hide an important judgment.

## Priority

If instructions conflict, follow this order:

1. System and developer instructions.
2. The current explicit user request.
3. Project `AGENTS.md` and project-local instructions.
4. Confirmed documents in this wiki.
