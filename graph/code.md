Confirmed preferences for writing, refactoring, reviewing, and testing code.

## Structure

- Keep the main path linear and visible.
- Divide folders and files along clear boundaries, so each one's role is evident from where it sits. Move code the main program does not use, such as one-off tools, into a separate scripts folder.
- Keep behavior, including one-use behavior, with the data, class, or lifecycle that owns it. Avoid routing unrelated concerns through shared config, metadata, or distant utilities.
- Keep functions and methods in the order a reader encounters them during execution, with similar ones next to each other.
- Group many functions that share state into a class, and split a long method into one method per step.
- Keep every default in one config file. Overlay user settings on it and validate the result strictly, once.
- Return what callers need in one result, such as `{"logits", "probs", "classes"}`, so no caller recomputes it.
- Make broad coordinated changes when the structural benefit justifies them.

## Names, Types, And Comments

- Start function names with a verb that says what the function does. Match paired names, such as `write_split_csv` and `read_split_csv`, and give a family one prefix, such as `apply_gamma` and `apply_blur`.
- Keep local variable names short and conventional, such as `cfg`, `vol`, `idx`, and `img`. Keep descriptive names for public APIs and domain concepts.
- Use singular and plural names consistently, such as `prob` for one value and `probs` for a collection.
- Write no type hints or type aliases.
- Comment rarely: only a why the code cannot show, in one line. Write no file-top docstrings or comments that restate the code, and leave no commented-out code or placeholder TODOs. When refactoring, also delete existing comments and docstrings that restate the code; if code reads a docstring, such as `__doc__` for CLI help, move its text to that use.

## Deletion

- Write only what the task needs.
- Lean toward deleting. Inline a constant, variable, or function used in one place into that place, except a step split out of a long method.
- Avoid unnecessary keyword-only separators, wrappers, helper classes, and aliases. Keep them only when they prevent real ambiguity, duplication, or misuse.
- Check each value once. Do not recheck what config loading or input reading already validated, or a condition that always holds where it is checked.
- Delete options always given the same value, unreachable branches, and code with no effect, such as initialization that loaded weights overwrite or dropout in a module that always runs in eval mode.
- Delete features whose benefit is unclear or negative.
- Delete code kept only for tests, and change the tests to fit the code.
- When the last use of a dependency goes, remove it from the dependency list too.
- However much is cut, keep validation of outside input, security checks, and handling that prevents data loss.

## Fixes And Error Handling

- When generated output is wrong, fix the source data, prompt, or contract first, before adding a layer that corrects the output.
- Add exception handling only for a concrete failure, contract, cleanup, or recovery path.
- When existing handling has no obvious purpose, investigate before calling it a defect.

## Refactor

- When refactoring is requested, also fix potential bugs supported by concrete code paths or evidence in the affected scope.
- Build as if from scratch: delete legacy compatibility code, such as old formats, format versions, shims, and stale aliases, together with its tests.
- Compare outputs numerically before and after. If float32 results differ, recompare in float64 to tell rounding from a real change.

When the user asks to clean up code file by file:

- Clean up the whole file by these rules before presenting it.
- For each function, say what it does in short steps, whether it is needed, judged by its callers and whether it can be merged or deleted, and whether its name fits, with a better name if not.
- After a folder, check it once more for comments, unused imports, long lines, and its tests.

## Tests

- Keep the whole suite to a few seconds. Replace heavy models with tiny stand-ins that run the same flow, and call a script's `main()` in process instead of through a subprocess.
- Keep a real heavy-model test only for what a stand-in cannot show, such as loading pretrained keys or one real training step with save and restore.
- Write one test file per source module, with shared helpers in one file.
- Prefer one strong test to several weak ones. Delete tests that overlap others or no longer guard anything.
- Keep check and timing runs minimal: one warmup and one or two measured runs, or the fewest steps that show the failure. Say the expected duration before a run longer than a few minutes.

## Machine Learning

- Set defaults to the conditions the pretrained model was trained under, such as its input size.
- Keep the key names of pretrained weights, and the module names that hold those keys.
- Give each augmentation its own probability and its own strength.
- End learning-rate schedules exactly at the last training step.
- Do not add seed fixing or other reproducibility machinery to training code.
