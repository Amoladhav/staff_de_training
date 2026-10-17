# Progress Dashboard

Last updated: 2026-10-16

## Overall Status

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

## Current Work
- Ongoing Git/runtime thread checkpoint 30; PR #2 integration verified at c31160a. Scheduled qualitative review recommends optional saved handoff before another implementation phase; next review 35 if continuing.
- Active checkpoint: W08 repository foundation — In Progress, moved ahead of further pipeline changes; W05–W07 remaining acceptance preserved.
- Current work-item statuses, diagrams, developer workflows and evidence: [Dataflow tracker](../docs/DATAFLOW_TRACKER.md). This supersedes older setup-next-step notes below.
- Next action: Review the Markdown command-runbook migration, then create docs/developer-runbooks from current main before staging/committing. PR #2 integration is locally verified at c31160a; do not repeat runtime setup or merge. After docs integration, resume W06/W07 negative-case source test blocking and recovery on a separate feature branch.
- Then: bounded failure/recovery, batch completeness contract and source-backed build/test acceptance.
- Azure billing/budget readiness and PowerShell saved variable remain unverified.

### Setup evidence
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
