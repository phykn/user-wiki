# Work Continuity Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make the user wiki keep the latest request and verification target alive during long or resumed work.

**Architecture:** Put the working rule in `graph/workflow.md`, where execution behavior is owned. Add only a short goal-level reinforcement in `graph/agent.md`, and add one regression case in `evals/personal-agent.md` so future reviews can catch the failure.

**Tech Stack:** Markdown wiki documents, existing Python wiki check scripts, git.

---

### Task 1: Add The Quiet Resume Rule To Workflow

**Files:**
- Modify: `graph/workflow.md`

- [ ] **Step 1: Confirm the current workflow has no explicit resume rule**

Run:

```powershell
rg -n "resume|resumed|context transition|latest user" graph/workflow.md
```

Expected: either no output, or only incidental wording that does not define a long-work or resumed-work rule.

- [ ] **Step 2: Insert a `Long Or Resumed Work` section after `Agentic Work Loop`**

Add this section after the paragraph that ends with `scope, route, or verification.`:

```markdown
## Long Or Resumed Work

When work runs long, resumes after interruption, or continues after a context transition, recover the task before taking the next action:

1. Use the latest user message as the current steering input.
2. Keep the original request, later corrections, current scope, important constraints, and needed evidence in view.
3. If the latest user message conflicts with an older interpretation, follow the latest message.
4. If recovery leaves two possible next actions or proof targets, ask the narrow question that chooses between them.

This is an internal steering check, not a visible ritual. Show only the short status or correction that helps the user understand the next action.
```

- [ ] **Step 3: Strengthen the completion rule inside `Multi-Step Work`**

Find this paragraph:

```markdown
Do not claim a milestone is done until the evidence covers that milestone's actual scope.
```

Replace it with:

```markdown
Do not claim a milestone is done until the evidence covers that milestone's actual scope. Before a final report after long, resumed, or corrected work, compare the result with the original request and later corrections. If matched evidence is missing, say what was checked and what remains unverified instead of calling the work complete.
```

- [ ] **Step 4: Reread the changed workflow area**

Run:

```powershell
Get-Content -LiteralPath 'graph/workflow.md' | Select-Object -Skip 20 -First 70
```

Expected: the new section appears after `Agentic Work Loop`, uses plain wording, and does not duplicate the `Completion Report` section.

### Task 2: Reinforce The Agent Contract Without Duplicating Procedure

**Files:**
- Modify: `graph/agent.md`

- [ ] **Step 1: Add one contract item for continuity**

In `## Contract`, after item 4, insert:

```markdown
5. Keep the current request and verification target alive across long or resumed work.
```

Then renumber the existing items so the final list becomes:

```markdown
1. Name what must be preserved from the request.
2. Find the current evidence before choosing scope.
3. Decide the smallest action that moves the real goal forward.
4. Execute within the relevant workspace and instruction boundaries.
5. Keep the current request and verification target alive across long or resumed work.
6. Verify with concrete evidence before claiming completion.
7. Update durable knowledge only when the new rule is reusable.
```

- [ ] **Step 2: Reread the contract**

Run:

```powershell
Get-Content -LiteralPath 'graph/agent.md' | Select-Object -Skip 10 -First 30
```

Expected: `agent.md` states the goal-level expectation once and does not repeat the workflow procedure.

### Task 3: Add A Regression Case For Lost Continuity

**Files:**
- Modify: `evals/personal-agent.md`

- [ ] **Step 1: Insert a case after `Goal Completion Audit`**

Add:

```markdown
### Resumed Work Continuity

Input: a long task resumes after interruption, compaction, tool failure, or a later user correction.

Expected behavior: recover the latest user request, original goal, agreed scope, important constraints, and matched verification target before taking the next action; continue from that recovered task; and claim completion only when evidence covers the recovered scope.

Failure signals: continuing an older plan after the user changed direction, losing a prior constraint, repeating already-settled discussion, treating a partial milestone as the whole task, or saying the work is complete without matched evidence.
```

- [ ] **Step 2: Reread the surrounding eval cases**

Run:

```powershell
Get-Content -LiteralPath 'evals/personal-agent.md' | Select-Object -Skip 15 -First 45
```

Expected: the new case is distinct from `Goal Completion Audit`: it catches continuity loss during resumed work, while `Goal Completion Audit` catches broad-goal closure mistakes.

### Task 4: Verify Wiki Structure And Scope

**Files:**
- Inspect: `graph/workflow.md`
- Inspect: `graph/agent.md`
- Inspect: `evals/personal-agent.md`
- Inspect: `docs/superpowers/specs/2026-06-21-work-continuity-design.md`

- [ ] **Step 1: Check wikilinks**

Run:

```powershell
rg -n '\[\[' graph
```

Expected: existing wiki links still point to maintained graph nodes. No new broken link is introduced by this change.

- [ ] **Step 2: Run the wiki checker**

Run:

```powershell
python scripts/check-wiki.py
```

Expected: the checker exits 0.

- [ ] **Step 3: Run the checker tests**

Run:

```powershell
python scripts/test-check-wiki.py
```

Expected: the tests exit 0.

- [ ] **Step 4: Check whitespace**

Run:

```powershell
git diff --check
```

Expected: no whitespace errors.

- [ ] **Step 5: Inspect the final diff**

Run:

```powershell
git diff -- graph/workflow.md graph/agent.md evals/personal-agent.md docs/superpowers/plans/2026-06-21-work-continuity.md
```

Expected: only the planned files changed; wording is plain; `workflow.md` owns procedure; `agent.md` only reinforces the contract; `evals/personal-agent.md` has one new case.

- [ ] **Step 6: Check git state**

Run:

```powershell
git status --short --branch
```

Expected: `graph/workflow.md`, `graph/agent.md`, `evals/personal-agent.md`, and this plan are changed or added. Existing unrelated `graph/docs.md` remains unstaged and should not be included in this task.

### Task 5: Commit Only The Work-Continuity Files

**Files:**
- Stage: `graph/workflow.md`
- Stage: `graph/agent.md`
- Stage: `evals/personal-agent.md`
- Stage: `docs/superpowers/plans/2026-06-21-work-continuity.md`

- [ ] **Step 1: Stage only the related files**

Run:

```powershell
git add -- graph/workflow.md graph/agent.md evals/personal-agent.md docs/superpowers/plans/2026-06-21-work-continuity.md
```

Expected: `graph/docs.md` remains unstaged.

- [ ] **Step 2: Confirm staged scope**

Run:

```powershell
git diff --cached --name-only
```

Expected:

```text
docs/superpowers/plans/2026-06-21-work-continuity.md
evals/personal-agent.md
graph/agent.md
graph/workflow.md
```

- [ ] **Step 3: Commit the implementation**

Run:

```powershell
git commit -m "Improve wiki work continuity rules"
```

Expected: one commit containing only the work-continuity implementation files.
