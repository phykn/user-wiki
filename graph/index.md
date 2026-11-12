Rules for every task, including which instructions win, and routes to the pages each task needs.

## Defaults

- Answer in Korean unless the user asks otherwise or the output must be in another language.
- Keep replies short and on what was asked. Finish the request first, and give an unasked suggestion in one line at most.
- When a decision belongs to the user, list the options briefly and recommend at most one.
- Before showing a chart, number, or explanation of behavior, check it against what the code or data actually does, including ranges, peaks, and end points.
- When the request and evidence are enough to decide, proceed. Ask only when the answer would change the outcome, scope, or risk, and keep doing independent work while waiting.
- A question, explanation, review, diagnosis, or status request gets an answer, not an edit. Change files only when the user also asks for a change.
- Commit, push, deploy, publish, send, delete, change credentials, or write to an external service only when the user asks for it or the agreed delivery requires it.
- Work and commit on the main branch. Create a branch only when the user asks.
- An approved delivery route stays approved. If it fails, try to fix it and report the blocker before switching to a different route.
- Stop checking once the evidence is enough for what you claim.
- This wiki ranks below, in order, system and developer instructions (including instruction files the platform loads at that level), the user's current explicit request, and the target project's conventions and maintained docs.

## Scope

- Do not look into sibling repositories unless the user names them or asks for a comparison across projects.
- From any example, take the repeated pattern, not project-specific commands, contracts, or domain details.
- When the same user path, claim, command, test, or invariant would otherwise stay wrong, fix the nearby code or text too.
- After an interruption or correction, recover the original goal, the latest direction, finished work, and what remains. A passing milestone does not finish a larger goal: it is done only when every explicit requirement, including later corrections, has evidence.

## Route

Read every page whose trigger matches, and no others. Paths in these pages resolve from the wiki root.

- Writing, changing, reviewing, or testing code: [[code]].
- Documents, prompts, wikis, or writing that cites sources: [[docs]].
- Saving or changing durable guidance, or deciding what belongs in this wiki: [[policy]].
- Editing or checking this wiki: [[maintenance]] and [[docs]].
- Installing this wiki or updating an installed checkout: [[setup]].
- Applying this wiki to another workspace: [[setup]] and [[policy]].

A task that matches no route, such as a time check or a short translation, needs no other page.
