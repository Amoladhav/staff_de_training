# Progress Dashboard

Last updated: 2026-10-18

## Current Work
- Checkpoint 16: three durable loader tests reviewed and agent-run suite passes, exit 0. Covers success, count rejection/preservation and injected publication failure with explicit rollback/error identity/restored snapshot. Formatting-only cleanup afterward.
- Local loader/package/tests/continuity-notes commit recommended; learner staging and staged review next. CLI scaffold, legacy caller and wider planning/runbooks remain unstaged for later review. No agent Git writes.
- W08 In Progress: remaining durable coverage, CLI/callers, logging and rebuilt-package/pipeline acceptance pending. Source checks are not installed-package/hosted CI/cloud acceptance. Hex/Fivetran optional.
- [Tracker](../docs/DATAFLOW_TRACKER.md) owns evidence/flow; [handoff](../docs/HANDOFF.md) refreshed. Count 16; last review 15: continue through verification/commit, reassess before CLI; next review 20.

## Historical readiness baseline

| Track | Planned | Complete | In Progress | Readiness | Confidence | Status |
|---|---:|---:|---:|---|---:|---|
| SET - Environment | TBD | 0 | 0 | Exposure | TBD | RED |
| PY - Python | TBD | 0 | 0 | Exposure | TBD | RED |
| SQL - SQL | TBD | 0 | 0 | TBD | TBD | TBD |
| AF - Airflow | TBD | 0 | 0 | Exposure | TBD | RED |
| DBT - dbt | TBD | 0 | 0 | Exposure | TBD | RED |
| AZ - Azure | TBD | 0 | 0 | Exposure | TBD | RED |
| MS - Microsoft Stack | TBD | 0 | 0 | Exposure | TBD | RED |
| DBX - Databricks/Spark | TBD | 0 | 0 | TBD | TBD | TBD |
| MOD - Modeling | TBD | 0 | 0 | TBD | TBD | TBD |
| AI - AI Native | TBD | 0 | 0 | Exposure | TBD | RED |
| BI - BI/Semantic | TBD | 0 | 0 | TBD | TBD | TBD |
| SYS - System Design | TBD | 0 | 0 | TBD | TBD | TBD |
| INT - Interview | TBD | 0 | 0 | Exposure | TBD | RED |
| CAP - Capstone | TBD | 0 | 0 | Not started | TBD | RED |
| CERT - Certification | TBD | 0 | 0 | Not started | TBD | RED |

## Status Meaning
- RED: weak / not interview-ready
- YELLOW: usable but inconsistent
- GREEN: interview-ready
- BLUE: Staff-level confident

### Historical setup evidence
- WSL copy of all 18 OneDrive source files verified byte-for-byte before documentation updates; original retained.
- Linux Python 3.14.4, venv/ensurepip imports, Linux Git path verified.
- Azure CLI still resolves to Windows; native Linux CLI not verified.
- VS Code `WSL: Ubuntu` indicator confirmed by learner on 2026-10-13.
- Learner verified Linux `.venv`: Python 3.14.4 and pip 25.1.1 both resolve inside the project environment.
- PowerShell saved `$training`, current full source-backed build/test acceptance, Azure upgrade and budget configuration remain pending.
- Other readiness scores above are baseline placeholders, not new competency assessments.

## Revisit Queue
None yet.

## Open Questions
See `05_QUESTION_BACKLOG.md`.

## Evidence of Skill
Track concrete proof:
- code written independently
- timed problems solved
- architecture designs defended
- GitHub artifacts
- certification/labs
- mock-interview performance

### dbt connection checkpoint
- Installed in Linux `.venv`: dbt-core 1.12.0, dbt-duckdb 1.11.0.
- Learner output confirms project/profile validation and local DuckDB connection passed.
- first_orders execution and its unique/not_null data tests verified; completed_orders preview confirmed by learner.

Bash CLI completion verified through installed dbt completion protocol; session activation supplied. Failure/recovery execution remains pending.

Active side issue: learner reports completion failure; interactive shell/runtime/registration diagnostics pending. Isolated Bash check passes, not learner acceptance.

Completion diagnosis: learner resolves user-bin dbt first and _complete_it registration. Session PATH/Click correction assigned; confirmation pending. Feature branch verified locally.

Standalone dbt removal instructions supplied at owner request; execution unconfirmed. Project venv preserved.
