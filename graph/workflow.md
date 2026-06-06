How to proceed after the judgment in [[intuition]].

Default response language is Korean unless the user asks otherwise, or code, identifiers, source quotes, or an external format require another language.

Ask only when the answer changes the next action, implementation choice, claim, or risk. If the available evidence already decides the route, proceed.

Prefer concrete verification: commands run, reproduced behavior, rendered output, checked sources, or inspected diffs. If verification cannot run, say what static reasoning proves and what risk remains.

When this wiki changes, or when a target-repository task leaves a pending wiki update, report that naturally in the completion summary.

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

Situation: A document sounds wrong, repeats itself, has unclear route boundaries, or needs this wiki applied to another repository.

Judgment: The durable result is the future reader's next action, not proof that the wiki was consulted.

Action: Put each rule in the one maintained file future readers will use. For a target repository, edit existing files future agents will read, such as `AGENTS.md`, README, prompts, or maintained docs. Do not copy this wiki as prose.

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
- Repository application: If future agents or maintained automation still read the wrong local guidance, it is the same defect. If the fix needs a new maintained surface or project policy, split it out.

Action: First restate what the current task must preserve. If the counterexample keeps the same failure alive, fix the smallest affected area and continue. If it changes the protected thing, revise the task lens and continue. If it creates a different task, finish the current part, name the boundary, and ask only for the decision that cannot be inferred.

Verify: Show the evidence that justified the expansion, lens change, or boundary stop.
