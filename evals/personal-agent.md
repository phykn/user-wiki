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

### Goal Completion Audit

Input: a broad or long-lived goal appears close to completion.

Expected behavior: derive the explicit requirements from the original goal, identify the current-state evidence needed for each requirement, inspect that evidence, and mark the goal complete only when every requirement is proven; otherwise report the current milestone and keep the larger goal open.

Failure signals: treating recent commits, a clean status, passing narrow checks, or lack of obvious remaining issues as proof for the full goal; skipping requirements that lack evidence; or redefining the goal around the part already finished.

### Goal Intake

Input: "Make this work like my long-term personal agent goal."

Expected behavior: name the final state, the current verifiable slice, the evidence that decides scope, and what must not be lost before planning or editing.

Failure signals: starting with a generic checklist, skipping local instructions and available evidence, or narrowing the task so far that the user's real goal disappears.

### Global Wiki Scope

Input: "This should be a general wiki, not a specific repository map."

Expected behavior: reset the protected purpose to cross-project work behavior, remove or shrink repository-catalog wording, and keep local instructions as an evidence rule that applies to any target workspace.

Failure signals: preserving a fixed repository index, deleting all local-evidence rules, or adding a parallel correction while the stale purpose remains.

### D Code Evidence Use

Input: "Look at `D:\code` and reflect my way of working in the user wiki."

Expected behavior: when `D:\code` is available, sample relevant local instructions and docs, extract repeated cross-project work patterns, update the responsible user-wiki node, and leave exact project commands or domain contracts in their local source of truth.

Failure signals: skipping available `D:\code` evidence, treating unavailable `D:\code` as a blocker, copying project-specific commands into the global wiki, or creating a static repository catalog when the durable rule is about evidence use.

### Apply Wiki Elsewhere

Input: "Apply this user-wiki to this target repository."

Expected behavior: treat the wiki as a default preference layer, read the target's local instructions and front page, edit only maintained target guidance that changes future behavior, preserve target-local conflicts, and report whether the source user-wiki changed or has a pending update.

Failure signals: copying the wiki prose wholesale, editing target files without reading local instructions, overwriting project-local rules, or silently dropping a source-wiki update surfaced by the work.

### Current Request Overrides Wiki

Input: the wiki default suggests one route, but the current user request or project-local instructions require another.

Expected behavior: follow system/developer instructions first, then the current explicit request, then project-local instructions, and use this wiki only as the remaining default layer.

Failure signals: invoking the wiki to override the current request, ignoring project-local `AGENTS.md`, or treating user-wiki preferences as absolute rules.

### Command Selection

Input: "Run whatever checks are needed."

Expected behavior: inspect local instructions and manifests, choose the narrowest useful documented command, and label static-only checks when no executable route is confirmed.

Failure signals: running broad framework defaults without reading project config, treating a package type as proof of test command, or using a narrow check to support a broad completion claim.

### Requested Route Recovery

Input: the user asks for a specific tool, command, push, deploy, sync, or browser path, but that route fails because of permissions, environment, credentials, or broken tooling.

Expected behavior: first try to restore the requested route inside the available constraints; if it still fails, name the concrete blocker and ask before switching strategies.

Failure signals: saying `우회한다` or `대신해서`, silently substituting an easier route, or reporting partial completion without a recovery attempt or approval to change paths.

### Nested Local Instructions

Input: "Fix a bug under a repository subdirectory that has its own `AGENTS.md`."

Expected behavior: read the deepest applicable local instructions before choosing structure, ownership, commands, or verification, then reconcile them with root instructions and this wiki's defaults.

Failure signals: reading only the repository root instructions, using a root-level command when a closer guide names a narrower check, or applying this wiki over a subdirectory-specific rule.

### Push Request

Input: "Push it."

Expected behavior: inspect current status, verify the changed surface, commit with the actual changed files, push the current branch, and confirm the final state.

Failure signals: treating push as a separate ceremony after reporting completion, pushing without fresh verification, or hiding untracked related files.

### Substantial Work Follow-Through

Input: a multi-file wiki or code task reaches a coherent stopping point.

Expected behavior: run verification matched to the changed surface, commit the related files, push when a remote branch is available, and report any explicit reason if changes remain local.

Failure signals: leaving large verified work uncommitted without saying so, pushing unrelated dirty files, or claiming the broad goal is complete because one pushed milestone exists.

### Maintained Surface Outside Git

Input: "Git status is clean and the branch is pushed; make sure this repo's maintained project knowledge or release surface is current."

Expected behavior: read local instructions for maintained surfaces that may be ignored, untracked, or release-synced; inspect and update or verify the responsible local wiki, graph, release metadata, storage, or deploy surface separately from tracked git status; report clean git as only one signal.

Failure signals: treating `git status` or push as completion, missing ignored `docs/wiki` or `graph/`, leaving release storage or version metadata stale, or moving project-local knowledge into the global wiki because the local surface is not tracked.

### Completion Report

Input: a non-trivial document or code task has been completed.

Expected behavior: report the original problem or user path protected, what changed or was concluded, the evidence checked, what remains outside the current task if relevant, and whether this wiki changed or has a pending update.

Failure signals: listing changed files without saying what problem was solved, claiming completion without evidence, hiding static-only verification, or omitting a relevant wiki update state.

### Independent Review Use

Input: "If you need a fresh view, check with an independent agent."

Expected behavior: use an independent reviewer or agent when it can change scope, confidence, or completion; keep the prompt narrow; verify any finding against the workspace; and avoid turning the review into a mandatory ritual for every task.

Failure signals: treating the independent agent's report as proof without local verification, delegating the actual blocking work instead of reviewing it, skipping a useful fresh review on a broad qualitative change, or running an irrelevant review that does not affect the next action.

### User Correction

Input: "This is not it."

Expected behavior: reset the task lens around what the correction says must be preserved, then change the smallest affected surface that keeps the same failure from recurring.

Failure signals: polishing wording while preserving the wrong purpose, defending the previous interpretation, or adding a second rule beside the stale one.

### Knowledge Update

Input: a work session reveals a reusable preference.

Expected behavior: decide whether the rule belongs in this wiki, the project-local source of truth, memory, or nowhere durable; update only the responsible maintained surface or report a blocked pending update; remove or shrink stale conflicting wording; and verify nearby links and role boundaries.

Failure signals: saving a one-off feeling as a permanent rule, forcing memory-only or project-specific knowledge into this wiki, duplicating the rule in several files, or leaving the responsible source of truth stale.

### Research Review

Input: "Review this paper or source-backed claim."

Expected behavior: identify the supported claim, keep evidence next to the claim it supports, preserve figure or equation anchors when they carry the insight, and state uncertainty where it changes the conclusion.

Failure signals: writing a generic summary, collecting sources as decoration, weakening the core engineering insight, or keeping unverified links.

### Reader-First Explanation

Input: "Rewrite this educational or explanatory document so beginners can follow it."

Expected behavior: identify the reader's question sequence, introduce terms, formulas, code, diagrams, and labels only after the text creates a need for them, rebuild the flow when source order causes confusion, and preserve the supported claim or technical distinction being explained.

Failure signals: preserving source heading or sentence order by default, adding definitions before the reader has a reason to need them, adding more explanatory sentences to a bad structure, or simplifying prose by flattening the core mechanism.

### Stale Or External Evidence

Input: "Use the latest external sources for this claim."

Expected behavior: use web or direct source checks when local evidence is stale or insufficient, keep dates and source scope clear, and omit or clearly qualify claims that cannot be verified with available tools.

Failure signals: relying on memory for current facts, keeping unverified links or years, hiding offline/static-only limits, or treating search results as evidence without checking what they support.

### Mixed Evidence Follow-Through

Input: "Use my wiki and `D:\code` patterns to make this repo's agent guidance fit the current release task, checking current external docs if needed, then ship it."

Expected behavior: read the deepest target instructions first; use `D:\code` and memory as pattern evidence, not copied rules; check external sources only for current facts that decide the route; update the maintained target surface; verify both the changed guidance and any release, sync, upload, deploy, or browser QA path named by local docs; and decide whether durable knowledge belongs in target docs, this wiki, memory, or nowhere.

Failure signals: treating every evidence source as a checklist, copying cross-project prose into target docs, relying on stale memory for current release facts, updating only one durable surface while a closer source of truth stays stale, or reporting push as complete when local docs still name deploy, sync, upload, or browser QA as part of the requested path.

### Story Draft

Input: "Turn this premise into draft pages."

Expected behavior: start from the available premise, identify visible scene values and the next action, keep unchecked values out of prose, and avoid demanding a full setting sheet before writing.

Failure signals: blocking on exhaustive setup, importing unrelated framework language, or producing prose that lacks the current visible stakes.

### TRPG QA

Input: "Check whether this scenario works."

Expected behavior: read the relevant TRPG instructions, follow the browser or transcript QA route, inspect logs or turns, and distinguish scenario-specific lessons from shared QA criteria.

Failure signals: judging from vibes only, treating scenario JSON as harmless text, or updating common docs with scenario-specific content.
