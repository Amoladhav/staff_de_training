# Bash · development runbook

WSL/Linux. [Native Windows counterpart](powershell_commands.md) uses the same section numbers.

**Flow:** [configure](#1-configure-this-session) → [branch](#2-start-or-resume-a-branch) → [build/test](#3-dbt-development-loop) → [portability](#4-clean-environment-check) → [integration](#5-integration-check) → [commit](#6-review-and-commit) → [PR](#7-push-and-open-a-pr) → [merge](#8-merge-and-synchronize) → [deploy](#9-deploy-and-verify).

Run one command at a time; stop on failure. Variables last for the current terminal. Change project/branch values once, then reuse the commands. Current results live in [the tracker](DATAFLOW_TRACKER.md).

## 1. Configure this session

Existing Python environment assumed. Set the branch to the task you are starting or resuming.

```bash
export PROJECT_ROOT='/home/amola/projects/staff_de_training'
```

```bash
export BR_NAME='feature/describe_change'
```

```bash
cd "$PROJECT_ROOT"
```

```bash
source .venv/bin/activate
```

```bash
export DBT_ENGINE_PROFILES_DIR="$PROJECT_ROOT/.venv/profiles"
```

```bash
export DBT_DUCKDB_PATH="$PROJECT_ROOT/training_analytics/dev.duckdb"
```

```bash
mkdir -p "$DBT_ENGINE_PROFILES_DIR"
```

```bash
cp training_analytics/profiles.example.yml "$DBT_ENGINE_PROFILES_DIR/profiles.yml"
```

```bash
dbt --version
```

Use the template copy above; the original ignored `profiles.yml` stays untouched. This Core profile variable keeps later commands short.

<details>
<summary>First-time Python setup or dependency changes</summary>

Create only when `.venv` is absent. Choose an installed compatible Python; the verified Linux baseline is Python 3.14.4.

```bash
python3 --version
```

```bash
python3 -m venv "$PROJECT_ROOT/.venv"
```

```bash
"$PROJECT_ROOT/.venv/bin/python" -m pip install -r "$PROJECT_ROOT/requirements.txt"
```

After an intentional dependency change, validate and refresh the snapshot:

```bash
python -m pip check
```

```bash
python -m pip freeze --all > "$PROJECT_ROOT/requirements_snapshot.txt"
```

A snapshot captures installed packages; it is not a solver lock or a cross-platform guarantee.

</details>

## 2. Start or resume a branch

**New work:** start from a clean `main`. For existing work, skip to the resume command.

```bash
cd "$PROJECT_ROOT"
```

```bash
git status --short --branch
```

```bash
git switch main
```

```bash
git pull --ff-only
```

```bash
git switch -c "$BR_NAME"
```

**Resume an existing branch:**

```bash
git switch "$BR_NAME"
```

Implement the change, then run sections 3–5 as appropriate. Documentation-only edits need diff/link checks, not a database rebuild.

## 3. dbt development loop

Work from the dbt project directory. Use a narrow selection while editing; expand to source descendants before commit.

```bash
cd "$PROJECT_ROOT/training_analytics"
```

```bash
dbt debug
```

```bash
dbt ls --select "source:commerce.orders+"
```

```bash
dbt compile --select first_orders
```

```bash
dbt build --select "first_orders+"
```

**Common alternatives** — choose what you need; do not run every command on every edit.

Tests only, without rebuilding models:

```bash
dbt test --select first_orders
```

Preview model output:

```bash
dbt show --select completed_orders --limit 10
```

Refresh external dbt packages **only if package declarations exist/change**:

```bash
dbt deps
```

Generate browsable docs:

```bash
dbt docs generate
```

```bash
dbt docs serve --port 8080
```

`docs serve` stays in the foreground; stop with Ctrl+C. Inspect `target/compiled/`, `target/run_results.json` and `logs/dbt.log` when debugging.

## 4. Clean-environment check

Use after dependency/runtime changes. This checks reproduction on the current OS; repeat separately on Windows/macOS for portability evidence.

```bash
cd "$PROJECT_ROOT"
```

```bash
export REPRO_DIR="$(mktemp -d /tmp/staff_de_repro.XXXXXX)"
```

```bash
python -m venv "$REPRO_DIR"
```

```bash
"$REPRO_DIR/bin/python" -m pip install -r requirements_snapshot.txt
```

```bash
"$REPRO_DIR/bin/python" -m pip check
```

```bash
"$REPRO_DIR/bin/python" -m pip freeze --all > "$REPRO_DIR/reproduced.txt"
```

```bash
diff -u requirements_snapshot.txt "$REPRO_DIR/reproduced.txt"
```

```bash
"$REPRO_DIR/bin/dbt" build --project-dir "$PROJECT_ROOT/training_analytics" --select "source:commerce.orders+" --target-path "$REPRO_DIR/target" --log-path "$REPRO_DIR/logs"
```

No diff means equal package versions. The final build uses the existing development database; it is a clean **Python environment**, not a fresh database test.

## 5. Integration check

**Local write path:** fictional fixture → raw table → freshness → models/tests → consumer preview. Requires the configured database to match the loader’s fixed path. The loader fully replaces `raw.orders`.

```bash
cd "$PROJECT_ROOT/training_analytics"
```

```bash
test "$DBT_DUCKDB_PATH" = "$PROJECT_ROOT/training_analytics/dev.duckdb"
```

```bash
python load_orders.py
```

```bash
dbt source freshness
```

```bash
dbt build --select "source:commerce.orders+"
```

```bash
dbt show --select completed_orders --limit 10
```

Expected fixture build: **3 models + 5 tests**. Freshness is a separate command; a fresh timestamp does not prove batch completeness. Deliberate bad-input blocking and recovery still require their own acceptance exercise.

## 6. Review and commit

From the repository root. Stage tracked changes only when all belong to this commit; add new files by explicit path.

```bash
cd "$PROJECT_ROOT"
```

```bash
git diff
```

```bash
git add -u
```

For a new file, replace the example path:

```bash
git add -- path/to/new_file
```

```bash
git diff --cached
```

```bash
git diff --cached --check
```

```bash
git commit -m "Describe the completed change"
```

```bash
git status --short --branch
```

## 7. Push and open a PR

```bash
git push -u origin "$BR_NAME"
```

Create once; supply the problem, change, validation and remaining limitations in the prompts.

```bash
gh pr create --base main --head "$BR_NAME"
```

```bash
gh pr diff "$BR_NAME"
```

```bash
gh pr checks "$BR_NAME"
```

No checks reported means no hosted validation was reported—not a CI pass.

## 8. Merge and synchronize

After final review and any required checks, with a clean worktree:

```bash
gh pr merge "$BR_NAME" --squash --delete-branch
```

```bash
git switch main
```

```bash
git pull --ff-only
```

```bash
git status --short --branch
```

```bash
git log -3 --oneline
```

## 9. Deploy and verify

**Not configured in this repository yet.** A local `dbt build` is not a deployment.

The delivery sequence is: approved merged revision → CI artifact/environment → staging ingestion and dbt checks → production approval → deployment → smoke checks and monitoring → rollback/forward fix if needed. Add the real commands here when the deployment target and pipeline exist; do not substitute a generic `--target prod` command for that workflow.

Record the revision to be released:

```bash
git rev-parse HEAD
```

### Azure account context

For an installed, authenticated CLI. Bash must resolve native Linux `az`; PowerShell must use native Windows `az`.

```bash
command -v az
```

```bash
az account list --output table
```

```bash
az account set --subscription "SUBSCRIPTION_ID"
```

```bash
az account show --output table
```

Account selection does not provision or deploy anything.

## Troubleshooting

Wrong runtime:

```bash
type -a dbt
```

```bash
"$PROJECT_ROOT/.venv/bin/dbt" --version
```

Dependency mismatch:

```bash
python -m pip check
```

Git authentication configuration (not stored credentials):

```bash
git config --show-origin --get-all credential.helper
```

Command discovery:

```bash
dbt --help
```


## References

[dbt profile configuration](https://docs.getdbt.com/docs/local/profiles.yml) · [dbt workflow guidance](https://docs.getdbt.com/best-practices/best-practice-workflows) · [Python environments](https://docs.python.org/3.14/library/venv.html) · [Azure account commands](https://learn.microsoft.com/en-us/cli/azure/account)
