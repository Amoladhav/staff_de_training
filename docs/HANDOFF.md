# Training handoff

Updated 2026-10-19 (America/Los_Angeles), orchestration readiness checkpoint 1.

## Objective and constraints
Finish loader branch integration, then deliver local orchestration in coherent
increments. Read root/starter AGENTS.md and 01_PROJECT_INSTRUCTIONS.md. Preserve
learner edits, existing .venv/database, paths and credential boundaries. Agent may
implement routine integration and bounded checks; Git writes/publication are
learner-led. One command per fenced block. Tracker owns status/evidence/count.

## Verified state
- HEAD: 1ce364e (owner committed instruction/curriculum changes during this turn).
  Local tracking ref: 63311ad; branch ahead one. CLI/package commit 63311ad and
  earlier loader/tests b80610d verified. Live remote/PR state not refreshed.
- Six documentation/runbook files remain modified by this checkpoint.
- Prior installed acceptance and source dbt JSON re-inspected; passed within their
  documented bounds. No tests rerun this turn. See DATAFLOW_TRACKER.md.
- Owner commit deleted scripts/validate_dbt_runtime.py; stale runbook commands
  corrected this turn. Repeatable pipeline acceptance needs replacement during
  orchestration work. Do not resurrect brittle SQL-mutation/status-count harness.
- Airflow not installed in project venv; official Airflow 3.3.2 prerequisites list
  Python 3.14 support. No environment changes, DAG implementation or execution.
- Native Windows/macOS, hosted CI, cloud and scale remain unverified.

## Exact next action
Learner reviews remaining docs/instructions, commits and completes the loader PR;
verify merge, synchronize main, then create feature/orders-orchestration from main.
Earlier async request to branch from current feature was premature and withdrawn.
No agent Git writes. Do not discard dirty changes or assume commands executed.

Next implementation: separate Airflow environment; manual serial load → freshness
→ dbt build → success gate with explicit paths and isolated database. Prove success,
rejection/downstream blocking and recovery. Define immutable batch identity before
retries/backfills; shared DuckDB requires serialized runs and controlled writers.

## Continuity
Confirmed new thread, checkpoint 1; review at 5. Prior CLI/caller review 20 retained
in tracker/log. No new handoff recommendation needed.
