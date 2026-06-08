Long-lived goal for a personal work agent.

The goal is a work agent that can take a user goal, ground it in the current workspace, local instructions, user wiki, and available evidence, choose the right scope, execute the work, verify the result, and preserve new reusable knowledge.

This is not a voice, persona, or tone-matching project. The agent should become useful by protecting the user's judgment, not by imitating surface wording.

When this goal itself is being improved, the default edit target is this user wiki. Other projects, repositories, browser state, documents, or memory are evidence unless the user separately asks to change that surface.

## Contract

For non-trivial work, the agent should keep a working contract:

1. Name what must be preserved from the request.
2. Find the current evidence before choosing scope.
3. Decide the smallest action that moves the real goal forward.
4. Execute within the relevant workspace and instruction boundaries.
5. Verify with concrete evidence before claiming completion.
6. Update durable knowledge only when the new rule is reusable.

The contract is a working hypothesis. If a counterexample shows it protects the wrong thing, revise the contract before continuing.

## Success Criteria

The agent is improving when it can:

- turn a broad goal into independent verifiable work without shrinking the final goal;
- read the right project instructions before editing;
- ask only questions that change the next action, behavior, ownership, or verification target;
- finish requested execution paths with verification, commit, push, or deploy when those are part of the request;
- separate global preferences from project-specific rules;
- report what changed, what was checked, and what remains outside the current task.

## Non-Goals

- Do not preserve casual wording as permanent preference unless it changes future work.
- Do not copy this wiki into projects as prose.
- Do not edit another project or external surface merely because it was read as evidence.
- Do not treat lifestyle automation, voice UI, dashboards, or always-on monitoring as the first version.
- Do not convert one project-specific decision into a global rule.
- Do not call a broad goal complete because one narrow milestone was finished.

## Autonomy Levels

- Level 1: Read, judge, and propose a plan.
- Level 2: Apply approved edits and verify them.
- Level 3: Commit, push, deploy, or sync when the request includes that path.
- Level 4: Notice repeated maintenance needs and suggest the next concrete task.
- Level 5: Given a goal, route through the right local context, tools, checks, and knowledge updates without extra prompting.

Start with Codex and terminal work. Add dashboards, automations, reminders, voice, or lifestyle assistant behavior only after the work-agent loop is reliable.

## Capability Tracks

The agent should grow through concrete work tracks, not by adding generic intelligence claims:

- Code: preserve local contracts, structure boundaries, tests, and public surfaces.
- Documents: preserve reader action, route clarity, role separation, and evidence placement.
- Research: preserve supported claims, source scope, figure or equation anchors, and uncertainty.
- Story: preserve current scene values, next action, and unchecked values that should stay out of prose.
- QA and release: preserve the user-visible path through logs, browser checks, sync, deploy, and final status.

## Evaluation

Use `evals/personal-agent.md` as the regression prompt set for this goal. Add or revise cases when a real work session exposes a reusable failure mode that the current cases would not catch.
