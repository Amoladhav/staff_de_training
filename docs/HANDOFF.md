# Training handoff

Updated 2026-10-19 (America/Los_Angeles), CLI/caller checkpoint 20.

## Objective and working style
Workspace /home/amola/projects/staff_de_training; branch feature/orders-loader-validation.
Read root/starter AGENTS.md and 01_PROJECT_INSTRUCTIONS.md, tracker/current logs.
Owner prioritizes fast robust/reliable/efficient/scalable pipeline delivery. Use
coherent increments; agent routine implementation/verification, learner contracts,
tradeoffs/debugging/review and Git writes. Avoid test-per-turn microsteps. Explain
important flow briefly. Preserve existing edits/.venv, paths and credential boundaries.
One learner-facing shell command per block. Do not equate agreement with guidance.
Do not expand custom validator/framework; its brittle status totals/SQL mutation
can be consolidated during CI work. Scale requires representative measurements.

## Verified acceptance
- Atomic loader plus three real-DuckDB tests committed b80610d. CLI/caller increment
  remains uncommitted: selected errors stderr/1, success 0, unexpected propagation;
  five CLI tests plus three loader tests passed at checkpoint 16.
- Legacy script delegates to CLI. Runtime validator calls module with explicit
  inputs; disposable WSL load/reject/freshness/dbt baseline 3 models+5 tests,
  injected failure 1 fail+7 skips, recovery 3+5 and preview passed. Evidence:
  /tmp/staff_de_dbt_v2_xqprpvzd/summary.json/logs. This is source-checkout evidence.
- Checkpoint 20: added orders-load console entry point. Wheel at
  /tmp/staff_de_orders_release/dist/orders_pipeline-0.1.0-py3-none-any.whl verified
  byte-for-byte against source modules; entry-point and metadata inspected.
  Build attempt hit read-only cache lock; escalation declined. Artifact was present
  and owner supplied its listing; do not claim rejected agent build succeeded.
- Installed wheel offline using /tmp cache into existing temporary acceptance env:
  /tmp/staff_de_uv_acceptance.p3WuP2/venv. Isolated import from site-packages;
  real orders-load outside checkout without PYTHONPATH publishes exact rows (0),
  rejects count (1), preserves full accepted snapshot. Three loader tests pass
  against installed package. uv pip check confirms seven compatible packages;
  offline lock check passes. Evidence /tmp/staff_de_orders_release/acceptance.json.
  Parent tool output included stream-fd permission warnings, but checks exited 0.
- Project .venv/database untouched. Native Windows/macOS/cloud/hosted CI and scale
  remain unverified. Source dbt and installed loader/CLI acceptance are separate.

## Exact next action and Git scope
Guide learner stage/diff/check/commit for coherent CLI/caller/package increment:
pyproject.toml, src/orders_pipeline/cli.py, tests/test_cli.py,
training_analytics/load_orders.py, scripts/validate_dbt_runtime.py,
docs/bash_commands.md, docs/powershell_commands.md, docs/DATAFLOW_TRACKER.md,
docs/HANDOFF.md, starter 04_PROGRESS_DASHBOARD.md, 13_SESSION_LOG.md,
14_DECISIONS_LOG.md. Proposed message: feat: integrate validated orders CLI and package.
Review entire selected diff; it contains earlier uncommitted runbook/continuity work.
Root/starter AGENTS.md and master plan delivery-scope edits remain outside this
code checkpoint; do not discard. No agent staging/commit/push. Last verified HEAD
b80610d on feature/orders-loader-validation; remote tracking not refreshed.
Commands supplied are not execution evidence; verify owner commit before advancing.
Then branch/PR integration and useful orchestration work; no more CLI microtests.

## Continuity
Checkpoint 20, scheduled qualitative review: fresh thread useful after learner
check-in at this delivery boundary; optional, continuing is fine. Next review 25.
Do not reset counter unless new thread confirmed. Previous history retained in logs.
