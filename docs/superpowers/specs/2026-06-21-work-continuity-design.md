Purpose

Improve the user wiki so agents do not lose the current request during long or resumed work, and do not claim completion without evidence.

The change should borrow structure from durable rule systems, not their language. The wiki should use short, plain instructions that change behavior at the moment of work.

Problem

The wiki already has good judgment rules, but the failure is happening inside the work loop:

- Long or resumed work can drift away from the user's latest request.
- The agent may treat a partial result as completion.
- The agent may say work is done without checking evidence that matches the request.
- Showing a large visible protocol to the user is not the goal. The behavior should work quietly unless a short status note is useful.

Design

Keep the main behavior in `graph/workflow.md`.

Add a quiet resume check for long work, interrupted work, or context transitions:

- Before taking the next action, recover the latest user request, current scope, important constraints, and the evidence needed for completion.
- If the latest user message changes the task, let it override older interpretations.
- Do not expose this as a long checklist by default. Use it to steer the next action.

Add a completion check before final reports:

- Compare the result against the original request and any later corrections.
- Name completion only when evidence supports it.
- If evidence is missing, say what was checked and what remains unverified.
- Do not use a narrow passing check as proof for a broader goal.

Use `graph/agent.md` only for a short purpose-level reinforcement:

- The personal work agent should keep the current request and verification target alive across long or resumed work.
- Detailed procedure stays in `workflow.md`.

Add a regression case to `evals/personal-agent.md`:

- A long or resumed task should continue from the latest request, preserve the agreed scope, and avoid completion claims without matched evidence.

Do not create a new core-rules document for this change. The existing graph already has the right owners, and a new node would add another route without solving the loop failure.

Acceptance Criteria

- `workflow.md` contains a clear, plain-language rule for resumed or long-running work.
- `workflow.md` contains a clear completion gate tied to request and evidence.
- `agent.md` mentions the continuity expectation without duplicating the workflow procedure.
- `evals/personal-agent.md` has a regression case that would catch the observed failure.
- No legalistic language is introduced.
- No new graph node is created unless implementation evidence shows the existing owners cannot hold the rule cleanly.

Verification

For this wiki edit, run:

- `rg -n '\[\[' graph`
- `python scripts/check-wiki.py`
- `python scripts/test-check-wiki.py`
- `git diff --check`
- `git status --short --branch`

Also reread the changed sections to check that the main route is still clear and that the new rule is not duplicated across documents.
