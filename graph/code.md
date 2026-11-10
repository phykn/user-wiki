Confirmed preferences for writing and refactoring code.

## Fixes And Error Handling

- When generated output is wrong, fix the source data, prompt, or contract first when you can, before adding a layer that corrects the output.
- Add exception handling only for a concrete failure, contract, cleanup, or recovery path.
- When existing handling has no obvious purpose, investigate before calling it a defect.

## Structure

- Keep behavior, including one-use behavior, with the data, class, or lifecycle that owns it. Avoid routing unrelated concerns through shared config, metadata, or distant utilities.
- Divide folders and files along clear boundaries, so each one's role is evident from where it sits.
- Accept broad coordinated changes when the structural benefit justifies them.
- Keep the main path linear and visible. Use small helpers when they isolate a real concept or repeated operation, not merely to reduce line count.
- Keep functions and methods in the order a reader encounters them during execution.
- Avoid unnecessary keyword-only separators, wrappers, helper classes, aliases, and configuration options. Keep them only when they prevent real ambiguity, duplication, or misuse.

## Names And Comments

- Keep local variable names short and conventional, such as `cfg`, `vol`, `idx`, and `img`. Keep descriptive names for public APIs and domain concepts.
- Use singular and plural names consistently, such as `prob` for one value and `probs` for a collection.
- Write no file-top docstrings or comments that restate the code, and leave no commented-out code or placeholder TODOs. When refactoring, also delete existing comments and docstrings that restate the code; if code reads a docstring, such as `__doc__` for CLI help, move its text to that use.

## Refactor

- When refactoring is requested, also fix potential bugs supported by concrete code paths or evidence in the affected scope.
- Remove stale internal paths and aliases unless a real consumer needs compatibility.
