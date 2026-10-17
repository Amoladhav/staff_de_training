# Training checkpoint

Updated: 2026-10-16 (America/Los_Angeles).

## Objective and canonical instructions

Workspace: `/home/amola/projects/staff_de_training`. Read root AGENTS.md and
`Staff_Data_Engineer_Training_Project_Starter/AGENTS.md` plus
`01_PROJECT_INSTRUCTIONS.md`. Preserve existing paths and filenames.
Continue learner-led, competency-based Staff DE training: setup, dbt, Databricks
with gradual Python, then deeper Python. Required local and actual cloud Airflow
and pipeline implementation remain in scope; local evidence is not cloud acceptance.

## Exact next action

Finalize PR #2: commit the four checkpoint notes through B11 CHANGED CODE, push feature branch, review final PR diff, then squash-merge/delete branch if review is satisfactory. Switch main, pull --ff-only and inspect status/log. Hosted checks reported absent by owner; this is local/tutor-reviewed integration, not CI or independent peer approval. All operations assigned, not executed by agent.

Use `COMMIT_MSG='docs: record runtime PR acceptance'`. Review staged notes before
commit. Current four modified files: tracker, handoff, numbered dashboard 04 and
session log 13. These notes contain the final integration assignment, not a claim
that merge already occurred. After owner confirmation, inspect actual Git state
and record integration in the next development checkpoint; do not reopen this PR
merely to log its completion.

## Verified results

- Canonical WSL Python 3.14.4; intended dbt Core 1.12.0, dbt-duckdb 1.11.0,
  DuckDB 1.5.6. Earlier bare dbt 2.0.8 differed from venv runtime. Learner reports
  recovery; exact earlier PATH/cache cause was not established.
- Root requirements.txt declares the three direct dependencies.
- requirements_snapshot.txt records 60 installed packages including pip 25.1.1;
  installed-state snapshot, not solver lock or hashed artifact manifest.
- `/tmp/staff_de_training_repro` exists. Independent metadata comparison matched
  all 60 package names/versions exactly; learner pip check passed. Do not recreate
  this existing environment blindly; /tmp can disappear between host sessions.
- `training_analytics/profiles.example.yml` uses required DBT_DUCKDB_PATH.
  Temporary copy exists at `/tmp/staff_de_training_profiles/profiles.yml`.
  Debug log and learner output confirm template connection success.
- `training_analytics/target/run_results.json`: Core 1.12.0, generated
  2026-10-17T00:12:52.832704Z (October 16 Pacific), build selection
  source:commerce.orders+, temporary profile, 3 successful models and 5 passing
  tests/zero failures. Owner supplied matching PASS=8 summary.
- Runtime README now explains configuration, repeatable workflow and limitations.
- Bash reference syntax and whitespace checks pass; numbered flows checked.
  Native Windows PowerShell recipes have not been executed/parsed in Windows.

## Git / publication state

Last inspected: `fix/runtime-reproducibility`, HEAD `99d7858`, aligned with cached
origin feature ref. Runtime commit `503461e`; README-only commit `6a464f2`;
generic-flow commit `99d7858`. Local main at previously inspected `191dd10`.
Owner reported PR #2 OPEN and no checks reported. No live remote/PR query by
agent this checkpoint. Four documentation modifications above remain uncommitted.
No agent staging, commit, push or merge for PR #2. No CI/branch-protection evidence.

## Working preferences and command references

- Learner experienced in enterprise DE/Linux, new to dbt/PowerShell. Explain
  mechanisms and professional ownership in small chunks; preserve hands-on work.
- One shell command per fenced block in chat; label shell and execution directory.
- Maintain docs/bash_commands.txt and docs/powershell_commands.txt as generic
  flows with pre-rendered figlet banners, # comments and sequential steps.
  VARIABLES declares PROJECT_ROOT, BR_NAME, COMMIT_MSG and runtime paths once per
  shell. Use flow references; keep task-specific state in tracker/handoff.
- B12/P12 NEW CODE starts a new feature; B11/P11 CHANGED CODE stages/reviews/commits;
  B08/P08 PUBLISH handles PR/integration. B06/P06 copies profiles; B05/P05 validates.
- PowerShell must use native Windows commands only. UNC accesses existing files;
  Windows environment/profile/database are separate. Native Windows pipeline is
  gated because loader ignores DBT_DUCKDB_PATH and writes beside its script.
- User owns remote/provider/credential operations. No secret inspection or pushes
  by agent. Git helper repair success remains unconfirmed separately.

## Pending acceptance and constraints

- W08 remains In Progress: branch integration pending; loader remains prototype.
- W05 freshness/completeness reasoning; W06/W07 deliberately failing source-count
  build, downstream skip/block observation and restored success still pending.
- Source count=3 is fixture-specific, not production batch completeness. The
  loader fully replaces raw.orders and stamps loaded_at; it ignores env DB path.
- Source YAML names catalog dev, schema raw, table orders. Keep database filename
  dev.duckdb until catalog/path configuration is deliberately generalized.
- No real hosted CI, protected-branch acceptance, local Airflow or cloud pipeline.
  Azure native Linux CLI/billing/budget readiness unverified. Budget ceiling
  $200/month, target below $150; alerts are not hard spending caps.
- Windows, WSL and macOS remain separate validation gates. Preserve OneDrive
  source snapshot; canonical WSL edits do not sync it automatically.

## Thread continuity

Confirmed Git/runtime thread 2026-10-16. Counted checkpoint 29; review at 25:
finish current Git publication boundary then reassess before another feature.
Next scheduled review 30. Qualitative assessment, no context percentage or
compaction-warning guarantee. Confirmed new thread resets count; compaction does not.

## Resume prompt

Resume Staff DE training in /home/amola/projects/staff_de_training. Read AGENTS.md,
its linked instructions, docs/HANDOFF.md and docs/DATAFLOW_TRACKER.md. Verify Git
and owner PR #2 integration evidence; do not repeat completed runtime setup.
Continue from the exact next action above. Preserve generic command references,
learner-led operations and pending negative-case/local/cloud/Airflow acceptance.
