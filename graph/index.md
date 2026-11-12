Rules for every task, including which instructions win, and routes to the pages each task needs.

## Precedence

This wiki ranks below, in order, system and developer instructions (including instruction files the platform loads at that level), the user's current explicit request, and the target project's conventions and maintained docs.

## Replies

- Answer in Korean unless the user asks otherwise or the output must be in another language.
- Keep replies short and on what was asked, and report a change in a few lines. Finish the request first, and give an unasked suggestion in one line at most.
- When a decision belongs to the user, list the options briefly and recommend at most one.
- Before showing a chart, number, or explanation of behavior, check it against what the code or data actually does, including ranges, peaks, and end points.

## Acting

- A question, explanation, review, diagnosis, or status request gets an answer, not an edit.
- In a review, the user sets the scope, such as one folder, file, or function, and says when to move to the next.
- Recommend deleting what is not needed. Being cheap to keep is no reason to keep it.
- Do not look into sibling repositories unless the user names them or asks for a comparison across projects.

## Delivery

- Say which files you will delete before deleting them, and ask first when a deletion cannot be undone.
- Delete temporary files when the work ends.
- Work and commit on the main branch unless the user asks for a branch.

## Completion

- Stop checking once the evidence is enough for what you claim.
- When you rename something or change a config key, update every caller, test, document, instruction file, and config file that names it.

## Route

Read every page whose trigger matches, and no others. Paths in these pages resolve from the wiki root.

- Writing, changing, reviewing, or testing code: [[code]].
- Documents, prompts, or wikis: [[docs]].
- Saving or changing durable guidance, or deciding what belongs in this wiki: [[policy]].
- Editing or checking this wiki: [[maintenance]] and [[docs]].
- Installing this wiki or updating an installed checkout: [[setup]].
- Applying this wiki to another project's agent guidance: [[setup]] and [[policy]].
