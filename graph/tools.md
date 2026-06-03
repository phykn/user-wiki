Minimal commands used repeatedly for user-wiki cleanup.

## Reading

- `rg --files graph`: Check the document list.
- `Get-Content -LiteralPath '<filename>'`: Read related documents.

## Checks

- `Get-ChildItem -Force -File graph | Select-Object Mode,Length,Name`: Check for empty documents.
- `rg '<search term>' graph`: Check duplicate rules, stale wording, and filename references.
- `rg -n "^# " graph`: Check top-level headings that duplicate filenames.
- Wikilink check:

```powershell
$files = Get-ChildItem -File graph -Filter *.md | ForEach-Object { $_.BaseName }
$links = Select-String -Path graph\*.md -Pattern '(?<!\\)\[\[([^\]]+)\]\]' -AllMatches | ForEach-Object { $_.Matches } | ForEach-Object { $_.Groups[1].Value }
$links | Where-Object { $_ -notin $files } | Sort-Object -Unique
```

## Edits

- `apply_patch`: Minimally edit only the needed documents.

## Final Checks

- Re-read only the related documents.
- Check for empty documents, broken links, stale filenames, and duplicate rules.
- Check that the roles of `intuition.md`, `policy.md`, `workflow.md`, and `theory.md` are not mixed.
