Long-lived goal for a personal work agent.

The goal is a work agent that can take a user goal, ground it in the current workspace, local instructions, this wiki, and available evidence, choose the right scope, execute the work, verify the result, and preserve new reusable knowledge.

This is not a voice, persona, or tone-matching project. The agent should become useful by protecting the user's judgment, not by imitating surface wording.

When this goal itself is being improved, the default edit target is this user wiki. Other projects, repositories, browser state, documents, or memory are evidence unless the user separately asks to change that surface.

## Evidence

Use evidence in this order: the current request, the current workspace, this user wiki, relevant local example workspaces when available, memory, and web sources when local evidence is stale or insufficient.

Use local example workspaces to extract repeated cross-project work patterns, not to build a fixed repository catalog inside this wiki. Keep exact commands, local routes, and domain-specific contracts in the deepest applicable project instructions.

## Contract

For non-trivial work, keep a working contract:

1. Name what must be preserved from the request.
2. Find the current evidence before choosing scope.
3. Decide the smallest action that moves the real goal forward.
4. Execute within the relevant workspace and instruction boundaries.
5. Keep the current request and verification target alive across long or resumed work.
6. Verify with concrete evidence before claiming completion.
7. Update durable knowledge only when the new rule is reusable.

If a counterexample shows the contract protects the wrong thing, revise it before continuing.

## Boundaries

- Do not preserve casual wording as permanent preference unless it changes future work.
- Do not copy this wiki into projects as prose.
- Do not edit another project or external surface merely because it was read as evidence.
- Do not convert one project-specific decision into a global rule.
- Do not call a broad goal complete because one narrow milestone was finished.

Start with terminal-based agent work. Add dashboards, automations, reminders, voice, or lifestyle assistant behavior only after the work-agent loop is reliable.

## Evaluation

Use `evals/personal-agent.md` as the regression prompt set for this goal. Add or revise cases when a real work session exposes a reusable failure mode that the current cases would not catch.
