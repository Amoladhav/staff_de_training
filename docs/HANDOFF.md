# Training handoff

Updated 2026-10-18 (America/Los_Angeles), durable-tests/CLI checkpoint 16 (resumed atomic-publication checkpoint 20).

## Objective and instructions
Continue feature/orders-loader-validation in /home/amola/projects/staff_de_training.
Read root/starter AGENTS.md and 01_PROJECT_INSTRUCTIONS.md, then tracker/current
numbered logs. Preserve learner edits and .venv. Owner n means next: inspect saved
source before advancing; edits may be made without explanation or not yet saved.
Small learner-led chunks, one shell command per block. Agent reviews/tests and
maintains notes; owner edits exercises and performs Git writes/publication/cloud
credentials. Reuse context; avoid redundant reads/checks/research for faster turns.
Proactively suggest coherent code check-ins after reviewing changes and passing
acceptance; learner performs Git operations. First assessment: loader plus durable
success/rejection/preservation/rollback tests; then CLI/caller integration.
Hex/Fivetran optional later; master plan owns broader role-aligned scope.

## Verified current source and acceptance
- src/orders_pipeline/loader.py: validates expected_rows int (not bool), non-negative;
  both paths must be Path objects; CSV must be a regular file; DB parent existing
  directory; existing destination must be regular file. Actual read/connect still
  validates permissions/format. No invented size/mtime/minimum-volume rules.
- Typed temporary orders_candidate, count/non-null/unique IDs and completed/pending
  status guards precede explicit BEGIN. Schema creation/replacement/COMMIT inside
  try, ROLLBACK then bare raise on Exception. Success print removed;
  learner return(rows_staged, candidate_timestamp) retained, a two-element tuple.
- Publication checkpoint 10: 12 disposable checks pass fresh/existing publication,
  seven input rejection cases, injected failure after actual replacement before
  commit (fresh/existing), repeat snapshot. Explicit rollback and original error
  propagation verified, old sentinel preserved or new schema rolled back.
- Checkpoints 12/15/17/19: eight count, three file, five destination and seven path
  type boundary checks pass with mocked connect. These are focused checks, not
  one full regression suite rerun against latest source.
- Checkpoint 20: two real disposable loads verify tuple matches persisted rows and
  max timestamp. Two rows returns (2, datetime); header-only expected-zero load
  returns (0, None). Empty snapshot accepted; no invented timestamp for no rows.
- Current thread checkpoint 10: both saved durable tests inspected and pass under
  existing WSL .venv, exit 0: count-rejection full snapshot preservation and exact
  successful publication/returned summary. Durable rollback and broader coverage
  remain pending. Temporary fixtures cleaned; project DB/.venv unchanged.
  Rebuilt wheel/full pipeline acceptance pending. Prior wheel only
  contains empty initializer; dependency/build notes retained in tracker.
- CLI parser-only; main wiring pending. Legacy training_analytics/load_orders.py
  still top-level, do not import. scripts/validate_dbt_runtime.py migration pending.

## Exact next action
Three durable tests pass (agent run, exit 0): success/data/tuple, count-rejection
preservation, and injected pre-COMMIT failure with actual replacement, explicit
rollback, original exception and restored complete snapshot. Learner code reviewed;
agent only trimmed trailing whitespace/added final newline in loader/test afterward.
Next learner stages package config/lock/build constraints, initializer/loader, test
and current continuity notes, then reviews staged diff before local commit.
Suggested message: feat: add validated atomic orders loader with regression tests.
CLI scaffold/legacy caller and broader planning/runbook edits remain unstaged for
later review. No Git writes by agent. Inspect staged scope before commit guidance.
Remaining: other guards/empty/repeat/fresh-target durable coverage, CLI/main/caller
migration, logging/diagnostics, validator/runbooks, rebuilt package/pipeline and
Git delivery. Local checkpoint is not feature completion; tuple retained.
Owner requests visual location/flow/pseudocode; Hex/Fivetran optional.

## Worktree and continuity
Checkpoint 20 verified feature/orders-loader-validation at 25afacd. Modified tracked
instructions/master plan/dashboard/session/decision logs, tracker/handoff/runbooks,
legacy learner loader; untracked build_constraints.txt, pyproject.toml, uv.lock, src/.
No Git writes, installs, remote refresh or cloud actions this thread. Preserve work;
carry notes with substantive delivery, no notes-only PR loop.

New confirmed thread counter 16; review 15: continue through rollback verification/
commit review, reassess handoff before CLI integration; next scheduled review 20. Prior atomic-publication review 20
recommended fresh thread before durable tests/CLI; owner resumed here. Continue
focused thread. Existing source/environment edits preserved; no Git writes.
