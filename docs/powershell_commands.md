# PowerShell · native Windows development runbook

Windows Python, Git, GitHub CLI and Azure CLI only. [Bash counterpart](bash_commands.md) uses matching section numbers. Native Windows execution is not yet verified.

**Flow:** [configure](#1-configure-this-session) → [branch](#2-start-or-resume-a-branch) → [build/test](#3-dbt-development-loop) → [portability](#4-clean-environment-check) → [integration](#5-integration-check) → [commit](#6-review-and-commit) → [PR](#7-push-and-open-a-pr) → [merge](#8-merge-and-synchronize) → [deploy](#9-deploy-and-verify).

Run one command at a time; stop on failure. Variables last for the current terminal. Change project/branch values once, then reuse the commands. Current results live in [the tracker](DATAFLOW_TRACKER.md).

## 1. Configure this session

Use the existing checkout via UNC, or substitute an established Windows checkout. The Windows venv and database are separate from Linux. The UNC share must be accessible; run Git writes from only one OS at a time.

```powershell
$env:PROJECT_ROOT = '\\wsl.localhost\Ubuntu\home\amola\projects\staff_de_training'
```

```powershell
$env:BR_NAME = 'feature/describe_change'
```

```powershell
$WindowsVenv = Join-Path $env:LOCALAPPDATA "staff_de_training\venv"
```

```powershell
Set-Location -LiteralPath $env:PROJECT_ROOT
```

```powershell
& "$WindowsVenv\Scripts\Activate.ps1"
```

```powershell
$env:DBT_ENGINE_PROFILES_DIR = Join-Path $WindowsVenv "profiles"
```

```powershell
$env:DBT_DUCKDB_PATH = Join-Path $env:LOCALAPPDATA "staff_de_training\dev.duckdb"
```

```powershell
New-Item -ItemType Directory -Force -Path $env:DBT_ENGINE_PROFILES_DIR
```

```powershell
Copy-Item training_analytics\profiles.example.yml "$env:DBT_ENGINE_PROFILES_DIR\profiles.yml"
```

```powershell
dbt.exe --version
```

<details>
<summary>First-time Windows environment setup or blocked activation</summary>

Inspect installed tools and Python before creating the Windows venv. Create only if the selected directory is absent.

```powershell
Get-Command python.exe, git.exe, gh.exe -All
```

```powershell
python.exe --version
```

```powershell
Test-Path -LiteralPath $WindowsVenv
```

```powershell
python.exe -m venv $WindowsVenv
```

```powershell
& "$WindowsVenv\Scripts\python.exe" -m pip install -r "$env:PROJECT_ROOT\requirements.txt"
```

If activation is blocked by execution policy, use explicit executables (`& "$WindowsVenv\Scripts\dbt.exe"`) instead of changing machine policy. Do not reuse the Linux `.venv`.

</details>

## 2. Start or resume a branch

**New work:** start from a clean `main`. For existing work, skip to the resume command.

```powershell
Set-Location -LiteralPath $env:PROJECT_ROOT
```

```powershell
git.exe status --short --branch
```

```powershell
git.exe switch main
```

```powershell
git.exe pull --ff-only
```

```powershell
git.exe switch -c $env:BR_NAME
```

**Resume an existing branch:**

```powershell
git.exe switch $env:BR_NAME
```

Implement the change, then run sections 3–5 as appropriate. Documentation-only edits need diff/link checks, not a database rebuild.

## 3. dbt development loop

Native connection checks can run after setup. Build/test/preview below require `raw.orders` in the **Windows** database; see section 5 before running them.

```powershell
Set-Location "$env:PROJECT_ROOT\training_analytics"
```

```powershell
dbt.exe debug
```

```powershell
dbt.exe ls --select "source:commerce.orders+"
```

```powershell
dbt.exe compile --select first_orders
```

```powershell
dbt.exe build --select "first_orders+"
```

Tests only:

```powershell
dbt.exe test --select first_orders
```

Consumer preview:

```powershell
dbt.exe show --select completed_orders --limit 10
```

When external package declarations exist/change:

```powershell
dbt.exe deps
```

Browse documentation:

```powershell
dbt.exe docs generate
```

```powershell
dbt.exe docs serve --port 8080
```

Stop the docs server with Ctrl+C. Inspect `target/compiled/`, `target/run_results.json` and `logs/dbt.log` for failures.

## 4. Clean-environment check

Generate and review a **Windows-specific** snapshot after a successful native install. Do not overwrite the Linux snapshot. This proves reproduction on Windows only; test Linux/macOS separately.

```powershell
$WindowsSnapshot = Join-Path $env:LOCALAPPDATA "staff_de_training\requirements_windows_snapshot.txt"
```

```powershell
python.exe -m pip check
```

```powershell
python.exe -m pip freeze --all | Set-Content -Encoding ascii -LiteralPath $WindowsSnapshot
```

```powershell
$ReproDir = Join-Path $env:TEMP ("staff_de_repro_" + [guid]::NewGuid().ToString("N"))
```

```powershell
python.exe -m venv $ReproDir
```

```powershell
& "$ReproDir\Scripts\python.exe" -m pip install -r $WindowsSnapshot
```

```powershell
& "$ReproDir\Scripts\python.exe" -m pip check
```

```powershell
& "$ReproDir\Scripts\python.exe" -m pip freeze --all | Set-Content -Encoding ascii "$ReproDir\reproduced.txt"
```

```powershell
Compare-Object (Get-Content $WindowsSnapshot) (Get-Content "$ReproDir\reproduced.txt")
```

```powershell
& "$ReproDir\Scripts\dbt.exe" --version
```

No `Compare-Object` output means matching package lines. It does not use Bash `diff` exit codes.

## 5. Integration check

**Pending native Windows support.** The current loader writes `dev.duckdb` beside its script and ignores `DBT_DUCKDB_PATH`. Running it through the UNC checkout would target the shared Linux database, while this runbook targets a separate Windows database.

The required native sequence is **fixture load → freshness → build/test → preview**. Add runnable loader commands after its database path becomes configurable and that behavior is tested. Do not treat connection/package checks as Windows integration acceptance.

## 6. Review and commit

From the repository root. Stage tracked changes only when all belong to this commit; add new files by explicit path.

```powershell
Set-Location -LiteralPath $env:PROJECT_ROOT
```

```powershell
git.exe diff
```

```powershell
git.exe add -u
```

For a new file, replace the example path:

```powershell
git.exe add -- path/to/new_file
```

```powershell
git.exe diff --cached
```

```powershell
git.exe diff --cached --check
```

```powershell
git.exe commit -m "Describe the completed change"
```

```powershell
git.exe status --short --branch
```

## 7. Push and open a PR

```powershell
git.exe push -u origin $env:BR_NAME
```

Create once; supply the problem, change, validation and remaining limitations in the prompts.

```powershell
gh.exe pr create --base main --head $env:BR_NAME
```

```powershell
gh.exe pr diff $env:BR_NAME
```

```powershell
gh.exe pr checks $env:BR_NAME
```

No checks reported means no hosted validation was reported—not a CI pass.

## 8. Merge and synchronize

After final review and any required checks, with a clean worktree:

```powershell
gh.exe pr merge $env:BR_NAME --squash --delete-branch
```

```powershell
git.exe switch main
```

```powershell
git.exe pull --ff-only
```

```powershell
git.exe status --short --branch
```

```powershell
git.exe log -3 --oneline
```

## 9. Deploy and verify

**Not configured in this repository yet.** A local `dbt build` is not a deployment.

The delivery sequence is: approved merged revision → CI artifact/environment → staging ingestion and dbt checks → production approval → deployment → smoke checks and monitoring → rollback/forward fix if needed. Add the real commands here when the deployment target and pipeline exist; do not substitute a generic `--target prod` command for that workflow.

Record the revision to be released:

```powershell
git.exe rev-parse HEAD
```

### Azure account context

For an installed, authenticated CLI. Bash must resolve native Linux `az`; PowerShell must use native Windows `az`.

```powershell
Get-Command az -All
```

```powershell
az account list --output table
```

```powershell
az account set --subscription "SUBSCRIPTION_ID"
```

```powershell
az account show --output table
```

Account selection does not provision or deploy anything.

## Troubleshooting and shell equivalents

| Task | PowerShell | Bash equivalent |
| --- | --- | --- |
| Change directory | `Set-Location` | `cd` |
| Inspect file | `Get-Content` | `cat` |
| Copy file | `Copy-Item` | `cp` |
| Locate tool | `Get-Command -All` | `type -a` |
| Compare package lists | `Compare-Object` | `diff` |
| Last external exit code | `$LASTEXITCODE` | `$?` |

Locate competing runtimes:

```powershell
Get-Command dbt, python -All
```

Inspect native Git helpers; a Linux-only helper in shared `.git/config` needs a scoped repair:

```powershell
git.exe config --show-origin --get-all credential.helper
```

Cmdlet help and external-tool help:

```powershell
Get-Help Copy-Item -Examples
```

```powershell
dbt.exe --help
```


## References

[dbt profile configuration](https://docs.getdbt.com/docs/local/profiles.yml) · [dbt workflow guidance](https://docs.getdbt.com/best-practices/best-practice-workflows) · [Python environments](https://docs.python.org/3.14/library/venv.html) · [Azure account commands](https://learn.microsoft.com/en-us/cli/azure/account)
