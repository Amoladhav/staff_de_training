# Portfolio Capstone Plan

## Goal
Build one end-to-end, portfolio-quality data platform project that:
- builds confidence
- exercises the modern stack
- supports Staff-level interview stories
- can be shown as a GitHub repository

## Tentative Architecture
Possible components:
- public/API/file source
- Python ingestion
- validation + logging
- local/cloud landing zone
- SQL/Snowflake/Databricks-style storage
- dbt transformations
- dimensional + medallion layers
- Airflow orchestration
- data quality tests
- CI/CD
- Required dbt delivery evidence: a reviewed SQL/YAML change, isolated CI build
  and test checks, approved code promotion, production-style execution and
  artifacts, plus a demonstrated failure/recovery scenario. Follow the dbt
  professional delivery module in `02_MASTER_TRAINING_PLAN.md`; distinguish
  local simulation from hosted CI and live warehouse acceptance.
- observability
- Power BI semantic model/dashboard
- optional AI/ML or GenAI-facing data product
- architecture decision records

## Required local and cloud acceptance

- Deliver the representative pipeline locally, then in a real cloud environment.
- Implement Airflow orchestration for ingestion, readiness/freshness/completeness,
  dbt builds/tests, downstream gating, monitoring, and recovery.
- Demonstrate a deployed cloud Airflow DAG and analytical workload with verified
  success and representative failure/recovery runs; local simulation is a
  separate milestone, not cloud acceptance.
- Preserve sanitized evidence, architecture/configuration explanations, CI/CD
  workflow, runbooks, cost tracking, and teardown steps. Follow the detailed
  local-to-cloud/Airflow module in `02_MASTER_TRAINING_PLAN.md`.

## Required Git lifecycle evidence

- Reviewed baseline commit with explicit prototype limitations.
- Focused feature branches and meaningful commits with checks and sanitized evidence.
- Reproducible runtime/profile template and documented configuration ownership.
- Real pull request, failing/passing hosted CI, required review/checks and integration.
- Deploy an identified approved revision; verify output and exercise recovery.
- Keep local review exercises distinct from hosted PR/CI and cloud deployment.

## GitHub Quality Bar
Repository should include:
- README
- architecture diagram
- setup instructions
- sample config
- `.env.example`
- no secrets
- data dictionary
- tests
- CI
- issue/milestone structure where useful
- screenshots
- design tradeoffs
- cost-conscious cloud setup/teardown instructions

## Staff-Level Evidence
Capstone should demonstrate:
- architecture decisions
- failure handling
- idempotency
- incremental loads
- data quality
- scalability reasoning
- observability
- security/governance thinking
- cost awareness
- documentation
- maintainability
