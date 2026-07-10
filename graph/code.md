Confirmed preferences that change how code work is scoped and verified.

## Decide

- State only assumptions that change behavior, API, data ownership, user-visible outcome, verification, or risk.
- Ask only when the answer changes one of those decisions.
- Read the deepest applicable local instructions before choosing structure, ownership, or commands.

## Scope

Prefer the smallest coherent change that preserves the user's intent and fixes the structural cause.

Touch neighboring code when leaving it unchanged would preserve the same failing path, command, test, public meaning, or local invariant. Broaden the structure only when a local patch would keep the wrong ownership or shape; report why.

Do not use a new API, dependency, behavior contract, or unrelated cleanup to solve a narrower request without a separate decision.

For generated-output problems, fix the source data, prompt, or contract before adding correction layers when feasible.

## Verify

- Reproduce a bug before fixing it when reproduction is safe and practical. Otherwise state the static evidence and remaining risk.
- When a focused regression test is suitable, make it demonstrate the failure and the fix.
- For refactoring, compare behavior before and after.
- Match verification to the affected surface: focused test, build, lint, reproduction, rendered output, public wrapper, manifest, or delivery state.
