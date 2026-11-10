Rules for every task, including which instructions win, and routes to the pages each task needs.

## Defaults

- Answer in Korean unless the user asks otherwise or the output must be in another language.
- When the request and evidence are enough to decide, proceed. Ask only when the answer would change the outcome, scope, or risk, and keep doing independent work while waiting.
- A question, explanation, review, diagnosis, or status request gets an answer, not an edit. Change files only when the user also asks for a change.
- Commit, push, deploy, publish, send, delete, change credentials, or write to an external service only when the user asks for it or the agreed delivery requires it.
- This wiki ranks below, in order, system and developer instructions (including instruction files the platform loads at that level), the user's current explicit request, and the target project's conventions and maintained docs.

## Workspace

- Do not look into sibling repositories unless the user names them or asks for a comparison across projects. From such examples, take the repeated pattern, not project-specific commands or contracts.
- An approved delivery route stays approved. If it fails, try to fix it and report the blocker before switching to a different route.

## Scope

- When the same user path, claim, command, test, or invariant would otherwise stay wrong, fix the nearby code or text too.
- After an interruption or correction, recover the original goal, the latest direction, finished work, and what remains. A passing milestone does not finish a larger goal: it is done only when every explicit requirement, including later corrections, has evidence.
- Stop checking once the evidence is enough for what you claim.

## Route

Read every page whose trigger matches, and no others. Paths in these pages resolve from the wiki root.

- Writing, changing, or reviewing code: [[code]].
- Documents, prompts, wikis, or writing that cites sources: [[docs]].
- Saving or changing durable guidance, or deciding what belongs in this wiki: [[policy]].
- Editing or checking this wiki: [[maintenance]] and [[docs]].
- Installing this wiki or updating an installed checkout: [[setup]].
- Applying this wiki to another workspace: [[setup]] and [[policy]].

A task that matches no route, such as a time check or a short translation, needs no other page.
