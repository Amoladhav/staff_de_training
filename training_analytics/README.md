# Training analytics

Local orders pipeline for Staff Data Engineer training. The canonical workspace
is `/home/amola/projects/staff_de_training`; this directory contains the dbt
project. Run the referenced recipes one step at a time.

## Verified environment

On 2026-10-16 (America/Los_Angeles), the recreated WSL environment used Python
3.14.4, dbt Core 1.12.0, dbt-duckdb 1.11.0 and DuckDB 1.5.6. Its 60 installed
package versions matched the recorded snapshot exactly. Dependency checks and
profile connection checks passed. The selected source-backed build completed
with 3 successful models and 5 passing tests under Core 1.12.0.

This verifies package reproduction and execution against the existing local
DuckDB database. It does not prove a fresh database bootstrap, Windows/macOS
compatibility, negative-case blocking/recovery, freshness or production readiness.

## Configuration and artifacts

| File | Ownership and purpose |
| --- | --- |
| `../requirements.txt` | Handwritten direct dependency pins for the engine, adapter and loader. |
| `../requirements_snapshot.txt` | Generated installed-package snapshot including pip and transitive dependencies. Not a solver lockfile; no artifact hashes or cross-platform guarantee. |
| `dbt_project.yml` | Project configuration; selects profile `training_analytics`. |
| `profiles.example.yml` | Committed template; reads required `DBT_DUCKDB_PATH` through Jinja. |
| `profiles.yml` | Local ignored configuration. Existing developer profile is retained. |
| `models/sources.yml` | Maps logical `commerce.orders` to physical `dev.raw.orders`; defines freshness thresholds. |
| `target/`, `logs/` | Generated dbt artifacts and logs, ignored by Git. |
| `dev.duckdb` | Local database, ignored by Git. |

The database name `dev` is declared in source configuration. The verified recipes
use a database file named `dev.duckdb`; changing the file name/location requires
checking the resolved catalog and source mapping.

## Repeat the verified WSL workflow

Use [Bash command reference](../docs/bash_commands.txt):

1. **B01**: enter the workspace, activate the existing environment and check Git/runtime.
2. **B02**: diagnose executable selection if `dbt --version` differs from the intended runtime.
3. **B03**: review direct dependencies; regenerate the snapshot only after intentional reviewed changes.
4. **B04**: reproduce packages in a new environment and compare installed versions.
   `/tmp/staff_de_training_repro` already exists from the verified exercise;
   inspect/reuse it, or choose a new unused path for a new clean-install proof.
5. **B06 steps 01–05**: copy the existing template into a temporary profile
   directory and validate the connection. Skip template creation step 00 when
   the file exists. The recipe supplies `DBT_DUCKDB_PATH` for that process only.
6. **B06 step 06**: build source descendants and their tests with the recreated
   runtime and template. This writes model relations using the existing raw table.

The temporary profile is `/tmp/staff_de_training_profiles/profiles.yml`. Explicit
`--project-dir` and `--profiles-dir` remove reliance on ambient profile discovery.
The `.example.yml` file is not loaded automatically. An unset `DBT_DUCKDB_PATH`
causes template configuration to fail; set it in the invoking process.

## Data flow and deliberate writes

`seeds/sample_orders.csv` is a fictional three-order fixture. `load_orders.py`
fully replaces `raw.orders` and stamps `loaded_at`. `first_orders` and
`base_commerce_orders` read that source; `completed_orders` reads `first_orders`.

**B07** is the deliberate manual load/freshness/build/preview recipe. The loader
is a teaching prototype: its database path is fixed beside the script, and it
does not consume `DBT_DUCKDB_PATH`. Do not point dbt at another database and assume
the loader follows. Reloading unchanged data refreshes `loaded_at`; it does not
prove business-data recency or batch completeness.

The singular count test asserts exactly three rows for this fixture. Other tests
check order ID uniqueness/non-null and status accepted values/non-null. Future
production completeness needs a batch contract and independent expected counts.
`dbt build` acceptance does not include the separate freshness command. Failures
must stop manual progression; automated orchestration and publication gating
remain future work.

## Native Windows reference

[PowerShell command reference](../docs/powershell_commands.txt) uses native
Windows tools and a separate Windows environment/profile/database. **P00**
verifies tools and access to canonical files through a configurable UNC path.
Native Windows execution remains unverified. The current loader's fixed database
path must be addressed before the Windows pipeline recipe in **P07** is enabled.
Do not reuse a Linux virtual environment or assume the Linux package snapshot is
a tested Windows resolution.

## Review and continuation

Use **B11/P11** for the current runtime branch review/commit; **B08/P08** covers
the subsequent hosted PR and integration workflow. No hosted CI or protected
branch acceptance is implied by local checks.

[Dataflow tracker](../docs/DATAFLOW_TRACKER.md) records acceptance and pending
work. [Handoff](../docs/HANDOFF.md) records the exact next action. Remaining work
includes negative-case failure/recovery, loader refactoring, real local Airflow,
and the required cloud implementation.
