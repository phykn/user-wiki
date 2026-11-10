Rules for every task, including which instructions win, and routes to the pages each task needs.

## Defaults

- Answer in Korean unless the user asks otherwise or the output must be in another language.
- When the request and evidence are enough to decide, proceed. Ask only when the answer would change the outcome, scope, or risk, and keep doing independent work while waiting.
- A question, explanation, review, diagnosis, or status request gets an answer, not an edit. Change files only when the user also asks for a change.
- A change request means editing the local workspace and verifying the result. Commit, push, deploy, publish, send, delete, change credentials, or write to an external service only when the user asks for it or the agreed delivery requires it.
- This wiki is a default layer. System and developer instructions come first, including instruction files the platform loads at that level. For anything they leave open, follow the user's current explicit request, then the target project's conventions and maintained docs, then this wiki's confirmed pages. [[policy#Provisional Interpretations]] only break a remaining tie.

## Workspace

The Workspace, Scope, and Verify And Report sections apply to any work in a workspace, however small, or any task with several steps.

- Keep existing and unrelated changes. Stage only the files for the requested work.
- Do not look into sibling repositories unless the user names them or asks for a comparison across projects. From such examples, take the repeated pattern, not project-specific commands or contracts.
- An approved delivery route stays approved. If it fails, try to fix it and report the blocker before switching to a different route.

## Scope

- Fix the cause with the smallest complete change. Also fix nearby code or text when the same user path, claim, command, test, or invariant would otherwise stay wrong. Leave out unrelated cleanup and extra features.
- After an interruption or correction, recover the original goal, the latest direction, finished work, and what remains. A passing milestone does not finish a larger goal: it is done only when every explicit requirement, including later corrections, has evidence.

## Verify And Report

- Pick checks from the project's instructions, docs, manifests, and existing tests, matched to what changed and what you claim. Stop once the evidence is enough.
- Report the result, its evidence, and limits that matter. Say which checks ran and what was only reviewed by reading.

## Route

Read every page whose trigger matches, and no others. Paths in these pages resolve from the wiki root.

- Writing, changing, or reviewing code: [[code]].
- Documents, prompts, wikis, or writing that cites sources: [[docs]].
- Resumes or job applications: [[docs]] and [[resume]].
- Two plausible readings of the user's intent that lead to different answers: [[policy#Provisional Interpretations]].
- Saving or changing durable guidance, or deciding what belongs in this wiki: [[policy]].
- Editing or checking this wiki: [[maintenance]] and [[docs]].
- Installing this wiki or updating an installed checkout: [[setup]].
- Applying this wiki to another workspace: [[setup]] and [[policy]].

A one-off task with no workspace and no matching route, such as a time check or a short translation, needs only the defaults above.
