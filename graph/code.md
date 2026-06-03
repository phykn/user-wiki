Confirmed principles for code edits, refactoring, bug fixes, and test writing.

## Before Implementation

- State assumptions.
- If there are multiple interpretations, surface them instead of silently choosing one.
- If there is a simpler approach, say so.
- If something is unclear, identify the confusion point and ask.

## Simplicity

- Do not add features that were not requested.
- Do not create an abstraction for code used only once.
- Do not add unrequested flexibility or configurability.
- Do not add defensive code for impossible situations.
- If the implementation grows large, look again for a smaller solution.

## Edit Scope

- Change only lines directly related to the request.
- Do not edit neighboring code, comments, or formatting without a reason.
- Do not refactor code that is not broken.
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
