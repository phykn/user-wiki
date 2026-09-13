Confirmed preferences that change how code work is scoped and verified.

## Scope

Follow [[workflow]] for scope and verification. Add an API, dependency, or behavior contract only when needed for the requested outcome.

For generated-output problems, fix the source data, prompt, or contract before adding correction layers when feasible.

## Errors

Keep exception handling tied to a concrete failure path, contract, cleanup requirement, or recovery path. When its purpose is unclear, inspect before judging; missing evidence alone does not make it a defect. Avoid speculative robustness layers.

## Refactor

- Give modules distinct responsibilities. Keep behavior with the data or lifecycle that owns it; avoid routing unrelated concerns through shared config, metadata, or utilities.
- Keep the structure shallow without sacrificing discoverability. Add a directory when it creates a useful boundary; remove one when it only repeats context already established by its parent.
- Keep local variable names short and conventional, such as `cfg`, `vol`, `idx`, and `img`. Keep descriptive names for public APIs and domain concepts.
- Name functions with concise verb phrases. Use singular and plural names consistently, such as `prob` for one value and `probs` for a collection.
- Use the same name and public call shape for the same operation across related classes and modules.
- Keep the main path linear and visible. Use small helpers when they isolate a real concept or repeated operation, not merely to reduce line count.
- Keep functions and methods in the order a reader encounters them during execution. Put one-use behavior with the class or lifecycle that owns it instead of creating a distant utility.
- Avoid unnecessary keyword-only separators, wrappers, helper classes, aliases, and configuration options. Keep them only when they prevent real ambiguity, duplication, or misuse.
- Write comments to explain why; omit restatements of readable code.
- Preserve external contracts such as public APIs, file formats, and model checkpoints. Remove stale internal paths and aliases unless a real consumer needs compatibility.
- Treat a boundary change as one coherent update: move files, update imports and callers, adjust tests and docs, and remove stale paths together.

## Verify

- Reproduce a bug before fixing it when reproduction is safe and practical. Otherwise state the static evidence and remaining risk.
- When a focused regression test is suitable, make it demonstrate the failure and the fix.
- For refactoring, compare behavior before and after.
