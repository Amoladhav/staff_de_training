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

Use [Bash command reference](../docs/bash_commands.md):

1. **Section 1 — Configure this session**: select project/branch and the existing runtime.
2. **Section 3 — dbt development loop**: debug, inspect selection, compile, build/test and preview.
3. **Section 4 — Clean-environment check**: install the snapshot in a fresh Python
   environment, compare versions, then run selected models/tests against existing data.
4. **Section 5 — Integration check**: deliberately replace the fictional raw fixture,
   check freshness, build/test and preview. This is a local write-path exercise.

The runbooks describe reusable commands, not a claim that every optional command
or platform has been validated. Follow the tracker for actual acceptance.

The verified exercise used `/tmp/staff_de_training_profiles/profiles.yml`. The
runbook uses a template copy under the venv and sets `DBT_ENGINE_PROFILES_DIR`
explicitly for concise Core commands.
The `.example.yml` file is not loaded automatically. An unset `DBT_DUCKDB_PATH`
causes template configuration to fail; set it in the invoking process.

## Data flow and deliberate writes

`seeds/sample_orders.csv` is a fictional three-order fixture. `load_orders.py`
fully replaces `raw.orders` and stamps `loaded_at`. `first_orders` and
`base_commerce_orders` read that source; `completed_orders` reads `first_orders`.

**Bash section 5** is the deliberate manual load/freshness/build/preview recipe. The loader
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

[PowerShell command reference](../docs/powershell_commands.md) uses native
Windows tools and a separate Windows environment/profile/database. Section 1
configures canonical file access through a UNC path. Native execution remains
unverified. Section 5 explains the loader path limitation that must be resolved
before Windows integration acceptance.

## Review and continuation

Use runbook **section 2** to start/resume a branch, **section 6** to review and
commit, **section 7** to publish a PR, and **section 8** to merge/synchronize.
**Section 9** records the future deployment sequence and Azure account commands;
no hosted CI or deployment implementation is implied.

[Dataflow tracker](../docs/DATAFLOW_TRACKER.md) records acceptance and pending
work. [Handoff](../docs/HANDOFF.md) records the exact next action. Remaining work
includes negative-case failure/recovery, loader refactoring, real local Airflow,
and the required cloud implementation.
