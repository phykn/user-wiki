Repeated shell commands for checking and maintaining this wiki.

## Read

- `rg --files graph`: List wiki documents.
- `rg --files evals`: List regression prompts for agent behavior.
- `rg -n '<search term>' graph`: Find duplicate rules, stale wording, and filename references.

## Check

- `rg -n '^# ' graph`: Find top-level headings that may duplicate filenames.
- `rg -n '\[\[' graph`: Inspect wikilinks before or after renaming documents.
- `git diff --check`: Check whitespace issues across root files and graph documents.
- `git status --short --branch`: Check added, modified, deleted files, and branch sync before finishing.
- PowerShell broken wikilink check:

```powershell
$files = Get-ChildItem -LiteralPath graph -Filter *.md
$names = @{}
foreach ($f in $files) { $names[$f.BaseName] = $true }
$missing = @()
foreach ($f in $files) {
  $text = Get-Content -LiteralPath $f.FullName -Raw
  [regex]::Matches($text, '\[\[([^\]|#]+)') | ForEach-Object {
    $target = $_.Groups[1].Value
    if (-not $names.ContainsKey($target)) { $missing += "$($f.FullName): $target" }
  }
}
if ($missing.Count) { $missing | Sort-Object -Unique; exit 1 } else { 'NO_BROKEN_WIKILINKS' }
```
