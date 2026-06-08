Regression cases for the personal work agent goal.

These cases are not a command runner. Use them as review prompts before claiming that the agent behavior matches the wiki.

## Cases

### Entrypoint Repair

Input: "This project entrypoint feels wrong. Fix it."

Expected behavior: read the local instructions, identify the entrypoint's reader and role, remove stale route or duplicated explanation, verify changed links or references, and report the evidence checked.

Failure signals: rewriting the entrypoint as generic marketing copy, copying user-wiki prose into the target surface, or ignoring local instructions.

### Bug Fix

Input: "Fix this bug."

Expected behavior: reproduce or locate the failing path, preserve the local invariant, make the smallest coherent fix, run focused verification, then broaden checks only when the touched boundary requires it.

Failure signals: adding defensive abstractions without proving the failure path, skipping reproduction when it is feasible, or claiming completion from static confidence alone.

### Planning A Large Goal

Input: "Build my personal work agent."

Expected behavior: keep the full end state visible, split the work into independent verifiable milestones, state what the current milestone proves, and avoid redefining the goal around the first implemented file.

Failure signals: producing only a first-step checklist, claiming the lifetime goal is complete after wiki edits, or expanding into dashboards and voice before the work loop is reliable.

### Global Wiki Scope

Input: "This should be a general wiki, not a specific repository map."

Expected behavior: reset the protected purpose to cross-project work behavior, remove or shrink repository-catalog wording, and keep local instructions as an evidence rule that applies to any target workspace.

Failure signals: preserving a fixed repository index, deleting all local-evidence rules, or adding a parallel correction while the stale purpose remains.

### D Code Evidence Use

Input: "Look at `D:\code` and reflect my way of working in the user wiki."

Expected behavior: sample relevant local instructions and docs, extract repeated cross-project work patterns, update the responsible user-wiki node, and leave exact project commands or domain contracts in their local source of truth.

Failure signals: not inspecting `D:\code`, copying project-specific commands into the global wiki, or creating a static repository catalog when the durable rule is about evidence use.

### Command Selection

Input: "Run whatever checks are needed."

Expected behavior: inspect local instructions and manifests, choose the narrowest useful documented command, and label static-only checks when no executable route is confirmed.

Failure signals: running broad framework defaults without reading project config, treating a package type as proof of test command, or using a narrow check to support a broad completion claim.

### Push Request

Input: "Push it."

Expected behavior: inspect current status, verify the changed surface, commit with the actual changed files, push the current branch, and confirm the final state.

Failure signals: treating push as a separate ceremony after reporting completion, pushing without fresh verification, or hiding untracked related files.

### Substantial Work Follow-Through

Input: a multi-file wiki or code task reaches a coherent stopping point.

Expected behavior: run verification matched to the changed surface, commit the related files, push when a remote branch is available, and report any explicit reason if changes remain local.

Failure signals: leaving large verified work uncommitted without saying so, pushing unrelated dirty files, or claiming the broad goal is complete because one pushed milestone exists.

### Main Branch Cleanup

Input: "Use only main. Delete other branches."

Expected behavior: preserve committed work by integrating the extra branch into `main`, push `main`, delete the extra local and remote branches, and verify that the working tree is clean on `main`.

Failure signals: deleting an unmerged branch, leaving the remote branch behind, or creating another branch for ordinary work without being asked.

### User Correction

Input: "This is not it."

Expected behavior: reset the task lens around what the correction says must be preserved, then change the smallest affected surface that keeps the same failure from recurring.

Failure signals: polishing wording while preserving the wrong purpose, defending the previous interpretation, or adding a second rule beside the stale one.

### Knowledge Update

Input: a work session reveals a reusable preference.

Expected behavior: decide whether the rule is global or project-specific, update the responsible maintained document, remove or shrink stale conflicting wording, and verify nearby links and role boundaries.

Failure signals: saving a one-off feeling as a permanent rule, duplicating the rule in several files, or leaving the project-local source of truth stale.

### Research Review

Input: "Review this paper or source-backed claim."

Expected behavior: identify the supported claim, keep evidence next to the claim it supports, preserve figure or equation anchors when they carry the insight, and state uncertainty where it changes the conclusion.

Failure signals: writing a generic summary, collecting sources as decoration, weakening the core engineering insight, or keeping unverified links.

### Story Draft

Input: "Turn this premise into draft pages."

Expected behavior: start from the available premise, identify visible scene values and the next action, keep unchecked values out of prose, and avoid demanding a full setting sheet before writing.

Failure signals: blocking on exhaustive setup, importing unrelated framework language, or producing prose that lacks the current visible stakes.

### TRPG QA

Input: "Check whether this scenario works."

Expected behavior: read the relevant TRPG instructions, follow the browser or transcript QA route, inspect logs or turns, and distinguish scenario-specific lessons from shared QA criteria.

Failure signals: judging from vibes only, treating scenario JSON as harmless text, or updating common docs with scenario-specific content.
