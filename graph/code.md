Confirmed preferences that change how code work is scoped and verified.

## Decide

- State only assumptions that change behavior, API, data ownership, user-visible outcome, verification, or risk.
- Ask only when the answer changes one of those decisions.
- Read the applicable local instruction chains before choosing structure, ownership, or commands.

## Scope

Prefer the smallest coherent change that preserves the user's intent and fixes the structural cause.

Touch neighboring code when leaving it unchanged would preserve the same failing path, command, test, public meaning, or local invariant. Broaden the structure only when a local patch would keep the wrong ownership or shape; report why.

Do not use a new API, dependency, behavior contract, or unrelated cleanup to solve a narrower request without a separate decision.

For generated-output problems, fix the source data, prompt, or contract before adding correction layers when feasible.

## Refactor

- Map responsibilities before moving code. Each module should have one clear reason to change, and neighboring modules should have distinct ownership.
- Prefer high cohesion and low coupling. Keep behavior with the data or lifecycle that owns it, and avoid passing unrelated concerns through shared config, metadata, or utility layers.
- Keep the structure shallow without sacrificing discoverability. Add a directory when it creates a useful boundary; remove one when it only repeats context already established by its parent.
- Keep local variable names short and conventional, such as `cfg`, `vol`, `idx`, and `img`. Keep descriptive names for public APIs and domain concepts.
- Name functions with concise verb phrases. Use singular and plural names consistently, such as `prob` for one value and `probs` for a collection.
- Use the same name and public call shape for the same operation across related classes and modules. Avoid parallel APIs that differ only because their implementations differ.
- Keep the main path linear and visible. Use small helpers when they isolate a real concept, repeated operation, or error boundary, not merely to reduce line count.
- Keep functions and methods in the order a reader encounters them during execution. Put one-use behavior with the class or lifecycle that owns it instead of creating a distant utility.
- Avoid unnecessary keyword-only separators, wrappers, helper classes, aliases, and configuration options. Keep them only when they prevent real ambiguity, duplication, or misuse.
- When replacing internal behavior, remove the stale path instead of retaining a legacy alias unless a verified external consumer requires compatibility.
- Write comments only to explain why. Never restate what the code does.
- Separate external contracts from internal structure. Preserve required behavior and artifacts such as public APIs, file formats, or model checkpoints; avoid compatibility layers for internal paths unless a real consumer needs them.
- Treat a boundary change as one coherent update: move files, update imports and callers, adjust tests and docs, and remove stale paths together.

## Verify

- Reproduce a bug before fixing it when reproduction is safe and practical. Otherwise state the static evidence and remaining risk.
- When a focused regression test is suitable, make it demonstrate the failure and the fix.
- For refactoring, compare behavior before and after.
- Match verification to the affected surface: focused test, build, lint, reproduction, rendered output, public wrapper, manifest, or delivery state.
