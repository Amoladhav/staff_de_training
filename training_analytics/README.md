# Training analytics

Local orders pipeline for Staff Data Engineer training. The canonical workspace
is `/home/amola/projects/staff_de_training`; this directory contains the dbt
project. Run the referenced recipes one step at a time.

## Verified environment

Migrated on 2026-10-17 (America/Los_Angeles) to **dbt 2.0.8**, installed as the
`dbt` Python distribution. WSL Python is 3.14.4. Direct requirements are:

- `dbt==2.0.8`: v2 engine with built-in DuckDB adapter; replaces Python Core v1
  and the separately installed `dbt-duckdb` adapter.
- `duckdb==1.5.6`: Python database library used by `load_orders.py`, independent
  of the DuckDB driver embedded in dbt v2.
- `pytz==2026.5`: required when the loader retrieves timezone-aware timestamps;
  formerly an indirect dependency of Core v1.

The seven-package snapshot includes pip 26.2.1 and matches a recreated WSL venv.
Both the active and recreated environments passed dependency checks and the
validation script's fresh-database workflow: fixture load, connection, freshness,
3 successful models/5 passing tests, deliberately failed source-count test with
7 downstream skips (exit 1), restored success (exit 0), and consumer preview.
The project SQL and source/profile mappings required no v2 rewrite. The project
requires dbt >=2.0.8,<2.1.0; requirements pin the exact validated release.

This is local fixture acceptance, not Windows/macOS, hosted CI, production batch
completeness, publication isolation, or cloud acceptance. Previous Core 1.12.0
results remain historical evidence in the session log, not the active runtime.

## Configuration and artifacts

| File | Ownership and purpose |
| --- | --- |
| `../requirements.txt` | Handwritten pins for the v2 engine and Python loader dependencies. |
| `../requirements_snapshot.txt` | Generated installed-package snapshot including pip and transitive dependencies. Not a solver lockfile; no artifact hashes or cross-platform guarantee. |
| `dbt_project.yml` | Project configuration; selects profile `training_analytics` and bounds the v2 runtime. |
| `profiles.example.yml` | Committed template; reads required `DBT_DUCKDB_PATH` through Jinja. |
| `profiles.yml` | Local ignored configuration. Existing developer profile is retained. |
| `models/sources.yml` | Maps logical `commerce.orders` to physical `dev.raw.orders`; defines freshness thresholds. |
| `target/`, `logs/` | Generated dbt artifacts and logs, ignored by Git. |
| `dev.duckdb` | Local database, ignored by Git. |
| `../scripts/validate_dbt_runtime.py` | Authored acceptance runner; copies sanitized inputs to a temporary project and preserves separate success/failure/recovery artifacts. |
| `../scripts/dbt_completion.bash` | Authored Bash completion for common v2 commands/options; replaces the old Click recipe. |

The database name `dev` is declared in source configuration. The verified recipes
use a database file named `dev.duckdb`; changing the file name/location requires
checking the resolved catalog and source mapping.

## Repeat the verified WSL workflow

Use [Bash command reference](../docs/bash_commands.md):

1. **Section 1 — Configure this session**: select project/branch and the existing runtime.
2. **Section 3 — dbt development loop**: debug, inspect selection, compile, build/test and preview.
3. **Section 4 — Clean-environment check**: install the snapshot in a fresh Python
   environment, compare versions, then run the acceptance script against a fresh disposable database.
4. **Section 5 — Integration check**: deliberately replace the fictional raw fixture,
   check freshness, build/test and preview. This is a local write-path exercise.

The runbooks describe reusable commands, not a claim that every optional command
or platform has been validated. Follow the tracker for actual acceptance.

The runbooks copy the profile template under the venv and set `DBT_PROFILES_DIR`,
the variable documented by v2 CLI help. An explicit `--profiles-dir` takes
precedence. Use absolute DBT_DUCKDB_PATH values to avoid path-resolution ambiguity.
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
includes review/integration of this migration, loader refactoring, real local
Airflow, production batch contracts, and the required cloud implementation.

## Repeatable migration acceptance

From the workspace root with the project venv active (WSL Bash):

```bash
python scripts/validate_dbt_runtime.py
```

The script creates a fresh temporary project and a new `dev.duckdb`, invokes the
same interpreter's sibling dbt executable, and retains the printed evidence path.
Separate baseline/failure/recovery directories preserve run_results.json; command
exit codes and node statuses are asserted. It copies the loader instead of
changing its fixed database path, so the developer database is untouched.
It disables usage reporting, version polling and service-backed state for these
local checks. dbt still writes local lease/cache files under ~/.dbt, requiring
filesystem access there. No platform login or cloud credentials are needed.
Native PowerShell equivalent, after activating its own Windows venv:

```powershell
python.exe scripts/validate_dbt_runtime.py
```

That native Windows execution remains unverified. Do not equate a portable-looking
command with a completed platform gate.

## Migration and rollback boundaries

The former `dbt-core`/`dbt-duckdb` requirements must not be mixed into this v2 venv.
For an existing v1 environment, prepare a separate clean venv from the v2
requirements and verify it before switching; installing new requirements alone
does not uninstall the old packages. Retain this checkout's established `.venv`
path for daily use. The owner already replaced its runtime before this migration.

The prior v1 declarations are available in Git at `1756d63`. If rollback is
needed, reproduce that revision in a separate environment/checkout; reverting
requirements does not downgrade an environment or undo database writes. This
migration validated disposable databases; it did not rewrite the developer DB.

The Click `_DBT_COMPLETE=bash_source` activation is obsolete for v2. Follow the
Bash runbook to source the repository completion script and replace the old
startup block. No shell startup files were modified automatically. The helper
covers common commands/options, not dynamic model names.

References: [v2 installation](https://docs.getdbt.com/docs/local/install-dbt),
[DuckDB in v2](https://docs.getdbt.com/docs/local/connect-data-platform/duckdb-setup?version=2),
[v2 migration guide](https://docs.getdbt.com/docs/dbt-versions/dbt-upgrade/upgrading-to-v2?version=2).
