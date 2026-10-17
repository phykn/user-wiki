Boundaries, scope, and verification for work in a workspace. Whether to edit or deliver at all is decided by the defaults in [[index]].

## Workspace

- Before working, read the target's instruction files from its root down to each path you touch. A more specific file overrides a general one only inside its own folder.
- Keep existing and unrelated changes. Stage only the files for the requested work.
- Do not look into sibling repositories unless the user names them or asks for a comparison across projects. From such examples, take the repeated pattern, not project-specific commands or contracts.
- Read secret values only when the task needs them, and never repeat them.
- An approved delivery route stays approved. If it fails, try to fix it and report the blocker before switching to a different route.

## Scope

- Solve the problem the user asked about. A smaller or more polished result that solves a different problem is not an improvement.
- Fix the cause with the smallest complete change. Also fix nearby code or text when the same user path, claim, command, test, or invariant would otherwise stay wrong. Leave out unrelated cleanup and extra features.
- After an interruption or correction, recover the original goal, the latest direction, finished work, and what remains. A passing milestone does not finish a larger goal: it is done only when every explicit requirement, including later corrections, has evidence.

## Verify And Report

- Pick checks from the project's instructions, docs, manifests, and existing tests, matched to what changed and what you claim. Stop once the evidence is enough.
- Report the result, its evidence, and limits that matter. Say which checks ran and what was only reviewed by reading.
