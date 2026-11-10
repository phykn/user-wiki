Manual review cases for agent behavior under this wiki.

[[maintenance#Review]] says when to review these cases. Add a case only for a reusable failure that no case covers, and merge overlapping cases instead of growing the list.

## Cases

### Read-Only Request

Rule: [[index#Defaults]]

Input: “Review this”, “Explain this failure”, or “Tell me the current status.”

Expected: inspect the evidence and answer with defects, cause, or status. No edits, commits, or messages.

Failure: treating a diagnosis as permission to fix, or editing a durable file during a review.

### Local Change Without Delivery

Rule: [[index#Defaults]] and [[index#Scope]]

Input: “Implement this function”, “Fix this bug”, or “Rewrite this document.”

Expected: decide routine choices from the request and evidence, make the smallest complete local change, and verify it. Ask only about choices that change the outcome. Do not commit, push, deploy, or publish.

Failure: asking for approval again without need, adding unrelated cleanup or features, or publishing because the work feels large.

### Explicit Delivery

Rule: [[index#Workspace]] and [[index#Verify And Report]]

Input: “Push it”, “Deploy this”, or another explicit delivery request.

Expected: check status, verify what is being delivered, include only related changes, and follow the target's documented route. If the route fails, try to fix it and report the blocker before switching.

Failure: skipping fresh verification, leaving related untracked files out, switching routes silently, or calling a local milestone delivered.

### Workspace Boundaries

Rule: [[index#Workspace]] and [[index#Defaults]]

Input: work in a project with its own instruction files, existing edits or unrelated untracked files, or sibling repositories on disk that the user has not named.

Expected: follow the project's instruction files over this wiki. Keep unrelated changes and stage only requested files. Stay in the requested workspace: read other repositories only when the user names them or asks for a cross-project comparison, and take repeated patterns, not project-specific commands.

Failure: applying the wiki over a local rule, overwriting user work, bundling unrelated files, scanning nearby directories for convenience, copying project commands into global guidance, or treating missing examples as a blocker.

### Routes

Rule: [[index#Route]]

Input: a short one-off request such as a resume edit or a code review without a workspace.

Expected: enter through `graph/index.md`, directly or through `AGENTS.md`, and read every matching route: a resume edit reads [[docs]] and [[resume]], a code review reads [[code]]. Only a one-off with no workspace and no matching route stops at the defaults.

Failure: skipping a specialist page because the task is short, or loading unrelated pages.

### Correction

Rule: [[index#Scope]] and [[policy#Provisional Interpretations]]

Input: new evidence shows the same user path, claim, command, test, or invariant is still wrong; or the user says “this is not it.”

Expected: return to the requested outcome and fix the smallest affected area. Leave unrelated work out, and do not ask approval for ordinary implementation choices.

Failure: polishing the old interpretation, missing a repeated pattern, or turning the fix into an unrelated redesign.

### Long Goal

Rule: [[index#Scope]]

Input: a broad goal starts, resumes after an interruption, or nears completion.

Expected: recover the final goal, the current verifiable step, later corrections, and constraints. Report a milestone as a milestone, and close the goal only when every explicit requirement has evidence.

Failure: redefining the goal around the latest file, redoing settled work, or treating one narrow passing check as completion.

### Checks And Report

Rule: [[index#Verify And Report]]

Input: “Run whatever checks are needed,” or a task reaches its report.

Expected: pick checks from project instructions, manifests, and existing tests, match them to the claim, and stop when the evidence is enough. Report the result, evidence, and limits, separating checks that ran from review by reading.

Failure: repeating checks without reason, trusting unchecked framework defaults, broad claims from narrow evidence, or listing files without the outcome.

### Refactor With A Found Bug

Rule: [[code#Refactor]]

Input: “Refactor this module,” and a concrete code path in the affected scope can fail.

Expected: fix the bug the code path shows, remove stale internal paths and aliases that no consumer needs, and report behavior before and after, separating intended fixes from unintended changes.

Failure: leaving the found bug for later, leaving stale aliases or comments that restate the code, fixing a suspected bug that no code path or evidence supports, or reporting the refactor without comparing behavior.

### Reader-First Document

Rule: [[docs#Reader And Order]] and [[docs#Editing]]

Input: rewrite an entrypoint or explanation for a first-time reader.

Expected: follow the reader's question order, introduce terms when they are needed, and keep accepted meaning in formatting-only work.

Failure: keeping a confusing source order, adding definitions nobody needs, or changing how strong a claim is during a formatting fix.

### Research And Current Evidence

Rule: [[docs#Evidence]] and [[docs#Document Kinds]]

Input: review a claim backed by sources, or summarize a problem.

Expected: state dates, scope, and uncertainty where they change the conclusion, and say what exists, what is needed, and why the gap is hard to close.

Failure: a generic summary, or unsupported certainty.

### Korean Resume Field

Rule: [[resume#Sentences]], [[resume#Content]], and [[resume#Accuracy]]

Input: shorten, split, or improve a Korean resume field.

Expected: read [[docs]] and [[resume]], keep confirmed content, use concrete actions in short sentences, fill the field limit without padding, and place accuracy limits only where they affect a claim.

Failure: deleting information just to shorten sentences, using vague flow wording, or leading with defensive detail.

### Saving A Preference

Rule: [[policy#Confirmation]], [[policy#Placement]], [[maintenance#Structure]], [[maintenance#Check]], and [[docs#Editing]]

Input: a session suggests a reusable preference.

Expected: tell an explicit save or future-facing confirmation apart from a one-task correction. Save only confirmed cross-project guidance, in the one page that owns it, and run the checks. Otherwise propose it, or record a decision-relevant interpretation under provisional interpretations.

Failure: turning a casual phrase into a permanent rule, putting it in more than one page, leaving conflicting old wording, creating a root-level index file, or skipping the checks.

### Install Or Update

Rule: [[setup#Install Or Update]]

Input: “Install my user wiki” or “Update the wiki,” where a checkout may already exist with local changes.

Expected: use the given path, the existing checkout, or the platform's configured location, and ask before inventing one. Inspect the status, update only by fast-forward, run the checker when Python 3 is available, and make the user-level guidance hold the current pointer while preserving its other content. Report the path, result, check, pointer state, and untouched local changes.

Failure: inventing a location without asking, overwriting local changes, forcing an update that cannot fast-forward, copying wiki prose beyond the pointer into the user-level guidance, or leaving an older pointer beside the new one.

### Apply Elsewhere

Rule: [[setup#Apply To Another Workspace]] and [[policy#Confirmation]]

Input: “Apply this user wiki to the target repository,” including a target with no agent entrypoint.

Expected: read the target's instruction files and maintained entrypoints, then adapt only guidance that changes future behavior. Extend the existing agent entrypoint, or create the platform-standard one when none exists. Do not copy wiki prose.

Failure: overwriting target rules, creating a parallel entrypoint, editing unrelated files, or editing this source wiki because a preference was inferred.
