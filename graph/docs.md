Confirmed preferences for text artifacts that people read and execute, such as documents, wikis, prompts, and work instructions.

## Names

- Keep filenames as short noun forms when possible.
- If the path, folder, or parent context already distinguishes the type, do not repeat the type prefix in the filename.
- If a filename already acts as the document title, do not repeat the same title as the first line of the body.
- Remove prefixes unless meaning becomes ambiguous or a collision in the same space requires a qualifier.
- In Obsidian graphs or similar wikis where the base filename appears as a node name, avoid names that look like duplicate nodes even if they are in different folders.
- Before finishing a document or graph node, check whether the filename states its role as simply as possible.

## Duplication

- Do not repeat information already provided by the filename, path, parent context, title, or preceding sentence.
- Treat writing the same information twice like code duplication: one side can change and create inconsistency.
- When repeated explanation appears, remove one instance or turn it into a new non-repeating judgment criterion.
- Keep usage restrictions only where needed; do not add long preventive restrictions before an actual problem has appeared.

## Wording

- Use easier words when meaning is not reduced.
- When explaining functionality, prefer action wording the user can follow directly over abstractions.
- Before writing, identify the reader, what they can already see, what they need to decide or do next, and what evidence they can inspect.
- For visible artifacts, do not assume the reader knows internal shorthand. At first mention, show the concrete object, action, and output clearly enough that the sentence can stand alone.
- Do not write to display what the AI knows. If a detail does not help the reader understand the current object, judge it, or act on it, remove it.
- In self-representing artifacts, avoid outside-evaluator framing that tells the reader what is important. Prefer the person's own work flow, choices, evidence, and resulting effect.
- README or first-screen documents should first tell the user what the project is, why it matters, and whether they need it, before explaining internal structure.
- Role statements should state the real purpose directly instead of circling around it.
- Use direct and intuitive wording so that readers or executors without context are not confused.
- Process documents should have procedures clear enough to follow immediately after reading.
- If a list of rules leaves the execution order unclear, rewrite it into actual action order such as check, judge, write, extract, and verify.
- Use easy English words for work folder names and runtime artifact folder names when possible.
- Do not elevate a device that worked well for one task into a general rule for every document or graph. Keep case-specific devices as conditional criteria or effects from the input.

## Evidence-Driven Explanation

- When using a strong example as a writing model, extract the transferable structure rather than the domain details.
- A strong explanatory node should usually move through: starting condition, practical advantage, limit, cost or burden of alternatives, supported claim, and next question.
- Put evidence directly under the claim it supports. Do not collect sources as a detached bibliography that the reader has to connect alone.
- Use caveats when they protect the claim from overreach. A good caveat narrows the claim; it should not weaken the whole document into vagueness.
- Prefer compact problem summaries that state what is available, what is needed, and what makes the gap hard.

## Document Graph

- Before creating or keeping a document or graph node, first decide whether the judgment is difficult enough to require an independent node.
- If a short branch in the parent procedure is enough, do not leave it as an independent node.
- A node may remain independent if removing it would make the next judgment longer or scatter it across multiple nodes.
- A node should have one core function and one visible work product.
- If the next node has no artifact to read immediately, or only looks like preprocessing, treat it as an absorption candidate.
- Separate candidate generation from candidate selection. A generation node should produce only a named candidate list, and a selection node should apply pass criteria from the first candidate onward.
- If the previous node produced candidate order, do not create a separate filter node that repeats the same judgment.
- A route-selection node should only choose the next node to read.
- A route-selection node should distinguish default routes, conditional routes, and return routes, and one failure state should have only one return point.
- Close the main execution path first; read auxiliary nodes only when the main execution path is actually blocked.
- In a procedure graph, if a route-selection node or top-level router owns the next move, lower-level nodes should not repeat the next node. They should state only their own work and artifact.

## File Artifacts

- When a process result is a file, route by the file that should remain and the next file to read; do not invent a separate pass/fail value just for routing.
- Do not mix rule documents and runtime work files in the same folder. Define a separate location for work files.
- Do not create work folders or work files during rule cleanup; create them only at actual execution time.
- If there may be multiple input files, split summaries by original file, and align summary filenames with the original filenames.

## Sources and Interpretation

- For source-like material such as external profiles, paper lists, or source lists, first preserve the full list as one baseline node.
- Do not mix processed interpretations such as claims, priorities, or positioning into the baseline list. Put them in a separate branch node or claim document.

## Process Records

- A record document meant to reproduce the user's work method later should record the judgment process, not a result log.
- These documents should prioritize the question order, judgment criteria, and next-action selection method that led to the conclusion, rather than the user's conclusion itself.
- Rather than saving the user's words as answer sentences, convert them into questions and branch procedures that can be reused in the same situation.

## Checks

- Before finishing a document or graph node, reduce unnecessary wording, duplicate sections, and prohibition sentences that repeat the same boundary.
- After structural document cleanup, inspect neighboring entrypoints, links, and role boundaries enough to ensure the same overlap or stale route has not been left around the edited node.
- After cleaning up a document graph, check for broken wikilinks, stale filename references, references to deleted nodes, and work files created in the rule folder.
- Confirm that the main execution path reads from beginning to end.
