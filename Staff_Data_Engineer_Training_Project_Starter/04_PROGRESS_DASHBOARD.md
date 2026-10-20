# Progress Dashboard

Last updated: 2026-10-19

## Current Work
- Orchestration readiness checkpoint 1: owner CLI/package commit `63311ad` verified on `feature/orders-loader-validation`; finish its PR/integration before branching from updated main.
- Prior source and installed acceptance JSON inspected; no rerun. Deleted validator references corrected in runbooks. Owner committed instruction/curriculum edits as `1ce364e`; branch ahead one, six checkpoint/runbook files remain modified.
- Airflow runtime/DAG and repeatable pipeline acceptance next; no installation or execution. Platform/cloud/hosted CI/performance pending.
- [Tracker](../docs/DATAFLOW_TRACKER.md) owns evidence/count; [handoff](../docs/HANDOFF.md) owns exact next action. Review at checkpoint 5.

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
