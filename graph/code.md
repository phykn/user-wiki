Confirmed principles for code edits, refactoring, bug fixes, and test writing.

## Before Implementation

- State only assumptions that affect behavior, API, data ownership, user-facing outcome, verification, or risk.
- Surface multiple interpretations only when choosing among them changes implementation or verification.
- If there is a simpler approach, say so.
- Read the deepest applicable local instructions before choosing structure, tests, or ownership.
- Do not list every possible technique or architecture. Tie coding questions and proposals to the user's intent, the current codebase, and the decision that would change the implementation.
- Ask before coding only when the answer changes behavior, API, data ownership, user-facing outcome, or verification target.
- If something is unclear, identify the confusion point and ask only the question that resolves it.

## Simplicity

- Do not add features that were not requested.
- Do not create an abstraction for code used only once.
- Do not add unrequested flexibility or configurability.
- Do not add defensive code for impossible situations.
- If the implementation grows large, look again for a smaller solution.
- Prefer the smallest implementation that preserves the user's important intent and resolves the real structural cause over a broader design that only demonstrates knowledge.

## Edit Scope

- Keep changes tied to the requested problem and the affected neighborhood it relies on.
- If local structure blocks the requested behavior or makes the result incoherent, clean that neighborhood enough to make the requested work coherent and maintainable.
- If a broader structure is clearly the durable fix and the local patch would preserve the wrong shape, prefer the broader structure and report why the scope expanded.
- Do not edit neighboring code, comments, or formatting without a reason.
- Do not refactor code that is unrelated to the requested problem.
- Follow the existing style.
- Do not delete unrelated dead code; mention it if needed.
- Clean up unused imports, variables, and functions introduced by your changes.

## Structure Cleanup

- If several files for the same sub-concept have accumulated, consider grouping them into a folder or package.
- Even when cleaning up structure, preserve existing public paths when possible.

## Generated Output Fixes

- For generated output problems, do not first add more post-processing correction logic.
- When possible, fix the source contract, prompt, or data first.

## Success Criteria

- Turn work into a verifiable goal.
- For bug fixes, reproduce the issue before fixing it.
- If a verifiable test exists, create or update it first.
- For refactoring, confirm behavior is the same before and after.
- For multi-step work, keep a short verification method for each step.
- For public-surface or release-facing changes, verify the related README, wrappers, manifests, generated assets, or deploy/sync state that users actually consume.
