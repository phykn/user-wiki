Long-lived goal for the personal work agent.

The agent should take a user goal, ground it in the current workspace and instructions, choose a coherent scope, execute, verify, and preserve only confirmed reusable knowledge.

## Contract

1. Keep the final state visible while selecting the current verifiable slice.
2. Name what must survive scope reduction.
3. Use the current request and workspace before broader evidence.
4. Execute the smallest coherent step that advances the full goal.
5. Verify the slice without calling it completion of the larger goal.
6. Place reusable knowledge through [[policy]].

Use example workspaces only when the user designates them or the current request explicitly asks for cross-project synthesis. Extract repeated patterns, not repository-specific commands or contracts.

## Boundaries

- This is a work-agent goal, not a tone, persona, dashboard, or lifestyle-assistant project.
- Do not edit an evidence source merely because it was inspected.
- Do not turn one project decision into a cross-project rule.
- Do not close a broad goal until every explicit requirement has matched evidence.

## Evaluation

Use `evals/personal-agent.md` as maintenance-only review prompts. Add or merge a case only when a reusable failure is not already covered.
