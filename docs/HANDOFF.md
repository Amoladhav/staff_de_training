# Training checkpoint

Updated: 2026-10-16 (America/Los_Angeles).

## Objective and instructions

Read root AGENTS.md, then the linked training AGENTS.md and
01_PROJECT_INSTRUCTIONS.md. Canonical workspace:
`/home/amola/projects/staff_de_training`; retain the existing training-note folder.
Teach setup → dbt → Databricks with gradual Python → deeper Python, incorporating
local Airflow after dbt foundations and cloud orchestration with the cloud track.

Learner is experienced in enterprise data engineering/Linux, new to dbt and
PowerShell. Teach dbt from the beginning at experienced-engineer depth: small
chunks, mechanisms, configuration paths, generated artifacts, professional
team practices and authoring/generation workflow. Explain first, then use brief
comprehension checks. Use short `dbt ...` commands with the active venv, normally
from `training_analytics`. Explain each PowerShell operation with purpose, exact
command, Bash equivalent, and reliable help discovery. Use underscores in names.

## Required delivery scope

Owner explicitly requires local implementation followed by actual cloud
implementation, including real Airflow orchestration. See the required modules
in 02_MASTER_TRAINING_PLAN.md and acceptance in 09_CAPSTONE_PLAN.md.
Cover ingestion, freshness/completeness, dbt builds/tests, downstream gating,
CI/CD, scheduling, retries/idempotency, backfills, alerts and failure/recovery.
Distinguish planned, local-verified and cloud-verified results. Cloud-hosted
Airflow and target-platform execution remain required and unimplemented.

## Verified evidence and learner progress

- Existing WSL copy matched all 18 OneDrive source files before documentation
  changes. Originals retained unchanged; WSL edits do not auto-sync to OneDrive.
- WSL Python 3.14.4; project-local .venv verified. Installed dbt-core 1.12.0 and
  dbt-duckdb 1.11.0 inspected. VS Code WSL: Ubuntu confirmed by learner.
- dbt debug validated project/profile and local dev.duckdb connection, schema main.
- first_orders table and completed_orders view introduced; ref resolution and
  target/compiled SQL plus manifest dependencies inspected. Learner viewed lineage.
- Deliberate duplicate produced unique-test failure; SQL restored afterward.
- Four tests on first_orders (ID unique/not_null, status accepted_values/not_null)
  verified passing in run_results.json at the last inspection.
- Learner supplied sample_orders seed preview with three rows and completed_orders
  preview with orders 1 and 3 after ref-based model instructions. Do not infer all
  build/test statuses from preview alone; inspect current artifacts if needed.
- Explained source() logical-to-physical YAML mapping, missing declaration versus
  missing physical table, and freshness versus validity and completeness.
- Clarified that dbt rebuild does not ingest missing upstream data. Source freshness and prototype ingestion have since been exercised; see the
  current checkpoint below. Completeness checks remain unimplemented.

## Current next step and verified checkpoint

Read `DATAFLOW_TRACKER.md` for the intended dataflow, per-item developer workflow,
TBD/In Progress/Done statuses, and evidence. Owner now requires an update after
every training step; linked AGENTS.md records the maintenance rule.

- `load_orders.py` is a full-replacement teaching prototype adding `loaded_at`.
- `models/sources.yml` maps commerce.orders to dev.raw.orders and now configures
  loaded_at freshness: warn after 5 minutes, error after 10 minutes.
- Learner initially selected user-installed dbt 2.0.8 despite active venv;
  reactivation restored dbt Core 1.12.0 / DuckDB adapter 1.11.0. Persistent PATH
  startup ordering remains unverified.
- Learner supplied Core ERROR STALE output and later reported PASS after reload.
- Latest inspected sources.json: Core 1.12.0, status warn, checked at
  2026-10-16 04:32:23 UTC (October 15 Pacific), newest load 04:26:19 UTC.
  This later warning does not contradict the earlier learner-reported PASS.
- Explained that loaded_at is explicitly created by the Python SQL, not dbt;
  first_orders does not select it. Logical dbt selection uses commerce.orders,
  while SQL accesses physical dev.raw.orders.
- Source preview output supplied at new-thread checkpoint 3: IDs 1–3, statuses and amounts match the fixture; all rows share loaded_at 2026-10-15T21:26:19.750278-07:00. Command:
  `dbt show --inline "select * from {{ source('commerce', 'orders') }}" --limit 10`
- Full source-backed build/test acceptance remains pending; earlier four passing
  tests do not prove it. Freshness-versus-completeness reasoning needs follow-up.

Additional diagnostic supplied on October 16; learner returned aggregate output at new-thread checkpoint 2: actual_rows=3, distinct_orders=3, latest_load=2026-10-15T21:26:19.750278-07:00. Completeness reasoning remains pending. Diagnostic:
`dbt show --inline "select count(*) as actual_rows, count(distinct order_id) as distinct_orders, max(loaded_at) as latest_load from {{ source('commerce', 'orders') }}"`
Fixture file inspected: three orders, IDs 1–3. No automated completeness gate yet.
Owner reaffirmed proactive thread-length monitoring and saved summaries/resume
prompts; root AGENTS.md now spells out the checkpoint procedure.

Exact next action: learner commits the checkpoint-3 review record on
`docs/publish-checkpoint`, pushes the branch and opens a hosted PR against main.
Review the PR before integration; then create a distinct runtime feature branch.
Do not repeat repository init/creation or the original push. Each shell command
must be separately copyable in its own fenced block.

Checkpoint 23 publication evidence:
- Owner reported push, then supplied GitHub JSON confirming private=true,
  default_branch=main and Amoladhav/staff_de_training.
- Inspected origin URL: https://github.com/Amoladhav/staff_de_training.git.
- Local main and cached origin/main both equal
  4150ae092d563ecd59020c075f741f1d61e6e717 (merge commit).
- Agent live metadata query was declined before execution; live remote SHA was
  not queried. Do not relabel cached refs as independently verified remote state.
- Four modified checkpoint docs are uncommitted and excluded from that revision.

Pending acceptance: dbt runtime selection/reproducibility (successful artifact
uses 2.0.8, prior intended Core 1.12.0), W05 completeness reasoning, W06/W07
negative-case source test blocking and recovery, hosted PR/CI/branch protection.
Publication is not production readiness. W08 remains In Progress.


Owner requires professional implementation as features grow: reusable structure,
configuration, validation, logging/error handling, meaningful tests and operational
recovery documentation. Label the current loader a prototype. Refactor before
expanding it into orchestration/cloud features; preserve learner-led practice.
Explain full-replacement behavior and the fact that reloading unchanged data
refreshes load time without proving business-data recency or completeness.

Local DuckDB has file-based access without database credentials; cloud
identity/secrets/permissions implementation must precede the cloud connection lab.
No active tool processes or known blockers at the handoff. A learner-started docs
server may still be running; its lifecycle was not inspected or changed.

## Environment and pending setup

Linux Python/Git paths verified previously. az resolved to the Windows Azure CLI
under /mnt/c; native Linux CLI unverified. PowerShell saved $training remains
unverified. Windows tool versions/settings and Azure login were supplied in the
owner's earlier handoff, not rechecked. Keep Linux/Windows environments separate.

Azure allowance: $200/month ceiling, target below $150. Trial pursuit abandoned.
Billing readiness and budget setup unverified; alerts do not enforce a hard cap.
Cost and select a compatible cloud architecture before provisioning; use bounded
lab windows and teardown. No cloud resources, schedules, CI integrations or
notifications were activated by the curriculum updates.

## Git and worktree

Git inspected at checkpoint 23: main 4150ae0, cached origin/main same SHA,
origin configured to Amoladhav/staff_de_training, docs/command-format removed.
Four files modified: docs/DATAFLOW_TRACKER.md, docs/HANDOFF.md, numbered dashboard
04 and session log 13. No new branch/stage/commit by agent. Private repository
and push supported by learner report/metadata; no hosted PR or CI evidence.
Existing 17 :Zone.Identifier metadata files were left unchanged.
OneDrive source snapshot location:
`/mnt/c/Users/amola/OneDrive/Documents/Staff_Data_Engineer/Staff_Data_Engineer_Training_Project_Starter`.

## Thread continuity state

Owner confirmed a new Git/runtime thread on 2026-10-16. Initialized counter at
zero; current checkpoint is 3, next scheduled review 5. Previous thread ended at
23 with a scheduled review at 20 and early qualitative handoff recommendation at
23. Fresh thread: continue; no capacity estimate or guaranteed compaction warning.

Checkpoint 3 verification: docs/publish-checkpoint at c0ed731; main and cached
origin/main at 4150ae0. Worktree clean before checkpoint-3 documentation updates.
Four-file branch diff passes whitespace check. Commit this review record before
pushing the branch and opening the PR. Commands assigned, no agent Git mutation
or live remote query. Hosted CI and independent peer approval remain pending.

## Continuation prompt

Resume training in /home/amola/projects/staff_de_training. Read AGENTS.md and linked
instructions, docs/HANDOFF.md and docs/DATAFLOW_TRACKER.md. This is a new thread;
initialize its counter and review every five checkpoints. Verify Git state, then
continue the learner-led docs/publish-checkpoint branch for four uncommitted
checkpoint files, followed by runtime reproducibility on a separate feature branch.
Do not repeat setup or repo creation. Private GitHub repo is
Amoladhav/staff_de_training; last inspected main/cached origin/main were 4150ae0.
Provide each shell command in a separate block. Preserve pending dbt failure/
recovery and required local/cloud/Airflow scope.
