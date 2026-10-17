# Training handoff

Updated: 2026-10-16 (America/Los_Angeles).

## Objective and instructions

Canonical workspace: `/home/amola/projects/staff_de_training`. Read root AGENTS.md,
linked `Staff_Data_Engineer_Training_Project_Starter/AGENTS.md` and
`01_PROJECT_INSTRUCTIONS.md`, then tracker and numbered logs. Preserve existing
paths. Continue learner-led Staff DE training: setup → dbt → Databricks with gradual
Python → deeper Python, including required local and actual cloud Airflow/pipeline
implementation. Local validation is not cloud or native-platform acceptance.

## Exact next action

Review the Markdown command-runbook migration, then create docs/developer-runbooks from current main before staging/committing. PR #2 integration is locally verified at c31160a; do not repeat runtime setup or merge. After docs integration, resume W06/W07 negative-case source test blocking and recovery on a separate feature branch.

Latest user request: concise Markdown command references for an experienced
working developer, covering branch → build/test → portability/integration →
commit/push/PR → merge → deployment. Rewrite is complete, awaiting review/commit.
Do not repeat the obsolete plain-text/figlet exercise.

## Git and worktree

Inspected main and cached origin/main at `c31160a` (PR #2 squash merge); feature
branch absent locally. Worktree was clean before this documentation rewrite.
Current changes: delete docs/bash_commands.txt and docs/powershell_commands.txt;
add docs/bash_commands.md and docs/powershell_commands.md; update training README,
linked AGENTS.md, tracker, handoff and numbered dashboard/session/decision logs.
Changes are uncommitted on main, ready to carry onto docs/developer-runbooks.
No agent branch/stage/commit/push. Live remote metadata not queried this turn.
Owner previously reported no checks on PR #2; no hosted CI or independent approval
is claimed. Runtime commits are preserved in the merged revision.

## Verified evidence

- WSL Python 3.14.4; Core 1.12.0 / dbt-duckdb 1.11.0 / DuckDB 1.5.6.
- requirements.txt declares direct pins; requirements_snapshot.txt records 60
  packages including pip 25.1.1. Snapshot is not a solver/hash lock.
- Recreated `/tmp/staff_de_training_repro` matched all 60 installed versions;
  pip check passed. It was verified existing; /tmp may disappear between sessions.
- Template profiles.example.yml uses required DBT_DUCKDB_PATH. Temporary profile
  `/tmp/staff_de_training_profiles/profiles.yml` connection success confirmed by
  log and owner output. Runbooks now use a venv-local profile directory and the
  documented Core DBT_ENGINE_PROFILES_DIR variable for concise commands.
- Core 1.12.0 run_results.json at 2026-10-17T00:12:52.832704Z (October 16 Pacific):
  source:commerce.orders+ build, 3 successful models and 5 passing tests/zero
  failures. Owner supplied matching PASS=8 output.
- Markdown rewrite checks: Bash fenced commands parse with bash -n; every command
  has its own fence; local links/control characters checked. No pipeline execution
  for documentation edits. PowerShell parser/native execution unavailable.

## Command references and preferences

Use docs/bash_commands.md and docs/powershell_commands.md. Section numbers match:
1 configure; 2 branch; 3 dbt loop; 4 clean environment; 5 integration; 6 commit;
7 PR; 8 merge; 9 deployment/account context. Keep frequent commands concise and
copyable, one command per fence. Optional setup/troubleshooting is secondary.
Use PROJECT_ROOT/BR_NAME and minimal runtime variables. Keep historical evidence
in logs/tracker rather than turning references into tutorials/transcripts.
Native Windows commands only in PowerShell, separate Windows environment and DB;
UNC can access canonical source files. No Windows/WSL venv reuse or duplicate repo.
Learner owns remote, provider and credential operations; no secret inspection.

## Pending work and limitations

- Documentation branch review/commit/integration for this request.
- W05 completeness reasoning; W06/W07 deliberately failing source-count build,
  downstream skip/block observation and restored success. Do not infer these from
  the successful build or fixture-only count=3 test.
- W08 remains In Progress: loader is a full-replacement prototype, stamps loaded_at,
  ignores DBT_DUCKDB_PATH and writes beside its script. Refactor before expansion.
- source YAML expects dev.raw.orders; preserve dev.duckdb catalog until deliberately
  generalized. Clean Python reproduction uses existing DB, not fresh DB acceptance.
- Native Windows integration awaits configurable loader paths; docs mark this.
- No hosted CI, branch protection, actual deployment, local Airflow or cloud pipeline.
  Azure account recipes are references, not proof of login or resource provisioning.
  Budget ceiling $200/month, target below $150; alerts are not spending hard caps.
- Keep Windows/WSL/macOS validation separate. Preserve OneDrive source snapshot.

## Thread continuity

Ongoing Git/runtime thread checkpoint 30. Merged files held 26; conversation
establishes 27–29, so count restored rather than reset. Review 30: optional new
thread is useful after extensive runtime/Git/reference work and successful PR #2
integration. Next scheduled review 35 if continuing. Qualitative assessment only;
no context percentage or guaranteed compaction warning.

## Copyable resume prompt

Resume training in /home/amola/projects/staff_de_training. Read AGENTS.md and its
linked instructions, docs/HANDOFF.md and docs/DATAFLOW_TRACKER.md. This is a new
thread; initialize its counter. Verify main at/after c31160a and the uncommitted
Markdown command-reference migration. Continue learner-led docs/developer-runbooks
review/commit/integration, then source-test failure/recovery on a separate branch.
Do not repeat runtime setup or PR #2 merge. Maintain concise Markdown references,
native Windows distinction and required local/cloud/Airflow scope.
