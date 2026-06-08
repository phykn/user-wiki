How to proceed after the judgment in [[intuition]].

Default response language is Korean unless the user asks otherwise, or code, identifiers, source quotes, or an external format require another language.

Ask only when the answer changes the next action, implementation choice, claim, or risk. If the available evidence already decides the route, proceed.

Prefer concrete verification: commands run, reproduced behavior, rendered output, checked sources, or inspected diffs. If verification cannot run, say what static reasoning proves and what risk remains.

## Goal Intake

For broad or long-running requests, define the working goal before planning:

1. Name the final state the user is pointing at.
2. Name the current slice that can be changed or verified now.
3. Name the evidence that decides scope: current workspace, deepest applicable local instructions, this wiki, relevant `D:\code` examples when that path is available, memory, or web sources when local evidence is stale.
4. Name what must not be lost while narrowing the task.

Use `D:\code` examples when available to find repeated work patterns such as read-before-editing, local source-of-truth routing, public-surface alignment, and matched verification. Do not copy exact project commands, domain contracts, or route details into the global workflow.

## Agentic Work Loop

For non-trivial work, keep the whole goal visible while choosing the next verifiable step.

1. State the working goal and what must not be lost.
2. Read the deepest applicable local instructions and evidence.
3. Choose scope by whether the same user path, reader understanding, claim, command, or local invariant would still fail.
4. Execute the smallest coherent change that moves the real goal forward.
5. Verify with evidence matched to the changed surface.
6. Decide whether any durable knowledge update belongs in this wiki, the project-local source of truth, memory, or nowhere durable.

Do not ask when the answer would not change the next action. Do not stop at a first plausible pass when an important in-scope counterexample still changes the goal, scope, route, or verification.

## Request Routing

Classify the request by the next artifact or proof it needs:

- Question: answer from the smallest reliable source of truth.
- Plan: produce a decision-complete plan tied to files, checks, and assumptions.
- Document change: preserve the reader's next action and verify routes, links, and duplication.
- Code change: preserve behavior and local invariants, then verify with focused tests or builds.
- Review: lead with defects, risks, missing tests, and evidence.
- Research: keep evidence close to each claim and separate fact from interpretation.
- Deploy or push: treat verification, commit, push, sync, or deploy as part of the requested path.
- Knowledge update: decide this wiki, project-local source of truth, memory, or nowhere durable before editing.

For broad goals, show where the current step sits in the larger goal without redefining the goal around that step.

When memory storage has separate platform rules, follow those rules. If memory is the responsible durable surface but the current environment cannot update it directly, report the pending memory update instead of silently writing it elsewhere.

## Command Confidence

Prefer commands named in the deepest applicable `AGENTS.md`, README, release doc, or package manifest. If no command is confirmed, inspect local config and tests before using framework defaults.

When reporting verification, distinguish documented commands, focused inferred commands, and static-only checks. Do not use a narrow passing check as proof for a broad goal.

Do not infer deployment from workspace shape. Use only deploy, release, storage, or publish commands confirmed in current local docs, manifests, or prior verified workflow.

## Multi-Step Work

When a task needs more than one meaningful step, keep each step independently checkable:

- File or surface: what will be changed or inspected.
- Reason: why that step moves the original goal forward.
- Proof: the command, diff, rendered output, source, or reread that verifies it.
- Recovery: what to do if the requested route fails before changing strategy.

Do not claim a milestone is done until the evidence covers that milestone's actual scope.

For substantial work in a git workspace, finish the path with verification, commit, and push when a remote branch is available and the user has not asked to hold changes locally. If branch or remote setup blocks this, report the concrete state and leave the working tree explicit.

Before destructive operations, credential changes, secret inspection, migrations, release sync, or irreversible deploy actions, confirm the action is actually part of the user's requested path. If the route is requested but fails, first try to restore that route; report the concrete blocker before choosing a different path.

## Independent Review

Use an independent reviewer or agent only when a fresh view can change scope, confidence, or completion: broad guidance changes, public-surface edits, high-stakes claims, or qualitative judgment.

Keep the prompt narrow: ask for the strongest remaining defect, unsupported claim, role-boundary problem, missing verification, or completion-report gap. Treat the result as input, not proof; verify it against the workspace and matched local checks. If no independent review tool is available, do a clean self-review and report that limit only when it affects confidence.

## Completion Report

For non-trivial work, report:

1. What original problem or user path was protected.
2. What changed or was concluded.
3. What evidence checked it: command, diff, source, render, log, or static reasoning.
4. What remains outside the current task, if naming it prevents misunderstanding.
5. Whether this wiki changed or a pending wiki update remains.

## Scenarios

### One-Off Request

Situation: The user asks for a time check, short translation, single command output, or similarly bounded result.

Judgment: The important thing is the result itself.

Action: Answer directly. Do not narrate wiki routing or turn the request into a preference update.

Verify: Use the direct source of truth, such as the command output or translated sentence.

### Code Change

Situation: The user asks for a feature, bugfix, refactor, or review.

Judgment: Preserve the requested behavior and the local codebase's existing contract. Do not widen the task because a broader cleanup is tempting.

Action: Read the relevant local files, make the smallest coherent change, and touch neighboring code only when leaving it would keep the same defect alive.

Verify: Run the focused tests, build, lint, reproduction, or diff inspection that actually supports the claim.

### Document Or Wiki Edit

Situation: A document sounds wrong, repeats itself, has unclear route boundaries, or needs this wiki applied to another workspace.

Judgment: The durable result is the future reader's next action, not proof that the wiki was consulted.

Action: Put each rule in the one maintained file future readers will use. For a target workspace, edit existing files future agents will read, such as `AGENTS.md`, README, prompts, or maintained docs. Do not copy this wiki as prose.

Verify: Check nearby entrypoints, stale links, duplication, empty files, and the changed document's main reading path.

### Research Or Evidence Summary

Situation: The user asks for source-backed explanation, paper review, market/context research, or another claim that depends on evidence.

Judgment: Evidence should narrow the claim. It should not decorate a generic answer.

Action: Keep source facts close to the claim they support, separate fact from interpretation, and name uncertainty where it changes the conclusion.

Verify: Check that every strong claim has support, that dates and source scope are clear, and that unsupported caveats or guesses were not promoted to conclusions.

### Counterexample Or Scope Pressure

Situation: During work, new evidence shows that the current plan is incomplete, a user correction is right, or the fix may need neighboring files.

Judgment: When the signals conflict, decide in this order:

1. If using the current output would mislead the user, reader, command, route, or test, it is the same failure.
2. If a user correction changes what must be preserved, reset the task lens before choosing scope.
3. If new evidence overturns the current claim, it is the same failure even when more sources are needed. If the new sources are only needed to make a new claim, it is a different task.
4. If the current output remains usable after naming the limit, and the new work needs a separate deliverable, audience, feature, source set, or design decision, it is a different task.

Conflict checks:

- Code: If the same user path, test, command, public API meaning, or local invariant still fails, it is the same defect. If fixing it needs a new API, dependency, or behavior contract that the current bugfix can name but not require, split it out.
- Documents: If the reader would keep the same wrong understanding, unsupported judgment, next action, or entrypoint, it is the same defect. If the change only improves wording without changing what the reader can understand, decide, or do, keep it out.
- Research: If new evidence changes the conclusion, confidence, scope, or baseline facts behind the current claim, handle it now. If it only opens a new claim, source set, or comparison, name it as a separate task.
- Local guidance application: If future agents or maintained automation still read the wrong local guidance, it is the same defect. If the fix needs a new maintained surface or project policy, split it out.

Action: First restate what the current task must preserve. If the counterexample keeps the same failure alive, fix the smallest affected area and continue. If it changes the protected thing, revise the task lens and continue. If it creates a different task, finish the current part, name the boundary, and ask only for the decision that cannot be inferred.

Verify: Show the evidence that justified the expansion, lens change, or boundary stop.
