Confirmed preferences for writing, refactoring, and verifying code.

## Scope

- Add an API, dependency, or behavior contract only when the requested outcome needs it.
- When generated output is wrong, fix the source data, prompt, or contract first when you can, before adding a layer that corrects the output.

## Errors

- Add exception handling only for a concrete failure, contract, cleanup, or recovery path.
- When existing handling has no obvious purpose, investigate before calling it a defect.

## Structure

- Give modules distinct responsibilities. Keep behavior with the data or lifecycle that owns it; avoid routing unrelated concerns through shared config, metadata, or utilities.
- Keep folders, files, and dependencies straightforward and easy to follow, with useful boundaries and little nesting. Accept broad coordinated changes when the structural benefit justifies them.
- Keep the main path linear and visible. Use small helpers when they isolate a real concept or repeated operation, not merely to reduce line count.
- Keep functions and methods in the order a reader encounters them during execution. Put one-use behavior with the class or lifecycle that owns it instead of creating a distant utility.
- Avoid unnecessary keyword-only separators, wrappers, helper classes, aliases, and configuration options. Keep them only when they prevent real ambiguity, duplication, or misuse.

## Names And Comments

- Keep local variable names short and conventional, such as `cfg`, `vol`, `idx`, and `img`. Keep descriptive names for public APIs and domain concepts.
- Name functions with concise verb phrases. Use singular and plural names consistently, such as `prob` for one value and `probs` for a collection.
- Use the same name and public call shape for the same operation across related classes and modules.
- Show purpose through names and structure. Keep comments short and limited to why: a constraint, workaround, or decision the code cannot show. Write no file-top docstrings or comments that restate the code, and leave no commented-out code or placeholder TODOs.

## Refactor

- When refactoring is requested, also fix potential bugs supported by concrete code paths or evidence in the affected scope.
- Remove stale internal paths and aliases unless a real consumer needs compatibility.
- When refactoring, remove comments and docstrings that restate the code. If code reads a docstring, such as `__doc__` for CLI help, move its text to that use.
- For refactoring, compare behavior before and after, distinguishing intentional bug fixes from unintended changes.
