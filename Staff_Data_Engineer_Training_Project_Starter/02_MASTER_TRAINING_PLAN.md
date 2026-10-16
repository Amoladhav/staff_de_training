# Master Training Plan

## Design
This is a modular, dependency-aware curriculum.
Do NOT interpret it as Day 1 / Day 2 / Week 3.
Sessions can be started, paused, resumed, or reordered when prerequisites allow.

## Tracks

| Code | Track | Priority | Goal |
|---|---|---|---|
| SET | Windows / Dev Environment / Setup | Critical | Stable professional development environment |
| PY | Python for Data Engineering | Critical | Blank-editor confidence + interview fluency |
| SQL | Advanced SQL | Critical | Maintain expert-level practical/interview fluency |
| AF | Apache Airflow | Critical | Strong hands-on + architecture/interview depth |
| DBT | dbt Core / Cloud | Critical | Strong hands-on analytics engineering depth |
| AZ | Azure Data Platform | High | Strong working knowledge of Azure data ecosystem |
| MS | SQL Server / Fabric / Power BI | High | Microsoft-stack competence for local market |
| DBX | Databricks / Spark / PySpark | High | Modern distributed data engineering depth |
| MOD | Data Modeling / Data Vault / Lakehouse | High | Staff-level modeling and architecture |
| DE | Data Engineering Systems | High | CDC, orchestration, data quality, observability |
| AI | AI-Native / Enterprise AI-ML Data | High | Modern AI-facing data engineering competence |
| BI | Reporting / Semantic Layer | Medium-High | Power BI deep; Tableau/Looker working knowledge |
| SYS | Staff System Design | Critical | Staff-level architecture and tradeoff ability |
| INT | Dedicated Interview Track | Critical | Timed coding + design + behavioral/leadership |
| CAP | Portfolio Capstone | Critical | End-to-end GitHub-ready evidence of skill |
| CERT | Certifications | Medium | 1–2 strategic credentials after real capability |

## Initial Priority Order
Current owner-directed sequence supersedes the original ordering below:
setup → dbt with SQL → Databricks with gradual Python exposure → deeper Python.
Introduce professional workflow context throughout; complete dbt deployment
foundations before expanding them on Databricks.

### Mandatory Git checkpoints and production delivery lifecycle

Owner requirement strengthened 2026-10-16: Git is part of each implementation
step, not deferred until the orchestration or cloud modules. Establish one repo
at /home/amola/projects/staff_de_training, including maintained project code,
fictional fixtures, training instructions and sanitized engineering notes.
Preserve the existing training folder. Do not create nested repositories.

Immediate sequence (supersedes deferring all W08 work until after W07):
1. Repository foundation now: review ignore rules, initialize main, inspect
   untracked files, choose explicit paths to stage, inspect staged diff and
   establish an honest baseline commit. Document prototype limitations, current
   dbt 2.0.8 artifact evidence versus intended Core runtime, and pending failure
   evidence. Baseline is a checkpoint, not a production release.
2. On a feature branch, resolve and record the chosen runtime/dependencies,
   replace scaffold README with verified run instructions, preserve a sanitized
   profile template and verify reproduction. Do not freeze whichever global
   runtime happens to be on PATH.
3. Continue completeness/build failure and recovery on a focused branch; inspect
   diff, run bounded checks, record sanitized evidence, review, then commit and
   integrate the passing change. Intentional failures must be restored before
   integration. A WIP commit on a feature branch is permitted when labeled.
4. Refactor ingestion only after batch/write semantics are agreed. Repeat the
   same branch → change → checks → review → commit → integration cycle.
5. Add a hosted remote, real pull request and required CI checks in W09; until
   then, explicitly label local review/merge exercises as local simulations.
   Establish isolated targets and protected integration before deployed/cloud
   changes. No remote or protection is presumed to exist.

Meaningful commit boundaries: repository baseline; reproducible runtime/setup;
source contract plus tests and failure evidence; loader validation/safe writes;
CI configuration; Airflow DAG and recovery; cloud deployment configuration and
runbook. Split independently reviewable work; do not commit after every command
or combine unrelated features merely because they occurred in one session.
Keep routine tracker updates coherent with the change they document.

Before each integration, review git status and staged diff, exclude secrets,
local profiles, virtual environments, databases, logs and generated dbt outputs;
retain fictional fixtures and sanitized evidence summaries. Record revision,
command, runtime, expected/observed behavior and unresolved limits. Git commits
are authoring evidence, passing checks are validation evidence, PR approval is
review evidence, and deployed revision/output is deployment evidence.

Later acceptance: real PR with failing then passing CI; deployment of an
identified approved revision; isolated target verification; runtime monitoring;
rollback or forward-fix exercise. Explain that reverting code does not undo data
writes. Record cloud evidence separately from local checks. Learner performs
focused Git steps, agent reviews; do not silently complete the Git lab for them.

### Required branch-to-release procedure

Owner clarified 2026-10-16: teach and practice branching and the complete delivery
sequence, not only commits. Use short-lived feature branches from main for this
project; a permanent develop branch is not required. Explain alternatives later.

1. Define the change, acceptance criteria, impact and recovery approach in a
   tracked work item. Inspect working tree before switching branches.
2. Establish the initial reviewed baseline on main (bootstrap exception only).
   Thereafter update clean local main from its upstream when a remote exists,
   then create a descriptive feature/fix/docs branch before editing.
3. Author focused changes with tests/config/docs. Inspect unstaged diff; run
   relevant validation in the agreed runtime. Stage explicit paths or hunks,
   review staged diff and status for scope/secrets/artifacts, then commit.
   Keep temporary failure injection on the branch and restore before integration.
4. Push the branch once a remote is configured; open a PR documenting problem,
   behavior, validation and risks. Run isolated CI; demonstrate a failed check,
   correction and passing rerun. Address review comments and inspect final diff.
5. Resolve conflicts on the feature branch; rerun affected checks after resolution
   or substantive review changes. Do not force-push shared main. Teach ordinary
   merge first; introduce rebase/force-with-lease only with concrete need and
   explicit explanation of history changes and collaboration impact.
6. Integrate after checks/review. Use squash merge for hosted feature PRs unless
   preserving individual commits has a clear reason. For local training use a
   reviewed local merge and label it a simulation, not PR approval. Explain the
   different commit history rather than pretending the mechanisms are identical.
7. Update local main, verify integrated revision and clean status, then remove
   merged feature branches. Preserve useful sanitized validation evidence.
8. For deployable milestones, identify the release revision/tag, promote through
   isolated environments, verify deployment/run output and monitor. Practice
   rollback or forward fix; code reversion does not reverse database writes.

Configure branch protection/required status checks and PR review when hosted CI
is introduced; verify enforcement rather than assume it. A solo learner cannot
supply independent peer approval: label tutor review/local simulation honestly,
and record any unavailable hosted approval requirement as a limitation.

Agent instruction: at each implementation exercise identify the current branch,
next diff/check/commit boundary and evidence required for integration. Do not
silently create branches, commits or merge the learner's exercise for them.
Agent-maintained training notes may be prepared separately and reviewed as docs
changes. Repository setup and Git skills remain learner-led.

### dbt professional delivery and operations (required)

Added explicitly on 2026-10-15. Previously CI/CD appeared only as a broad
capstone requirement. This is a hands-on learning outcome, not optional reading.

Take up after models, ref/source dependencies, YAML properties, tests, and
materializations are understood. Introduce Git/environment fundamentals earlier
as needed; revisit recovery after incremental models and schema changes.

1. Development workflow: repository layout, feature branches, SQL/YAML changes
   reviewed together, naming conventions, generated versus maintained files,
   pinned dependencies, and reproducible execution environments.
2. Environment configuration: developer, isolated PR/CI, staging, and production
   targets; schema isolation; service identities and secret injection; access
   control; distinguish promoting code from copying data or generated artifacts.
3. Pull-request CI: dependency installation, parsing/compilation, selected model
   builds and tests, required checks and approvals, artifact retention, temporary
   schema cleanup, and limits of local DuckDB versus warehouse validation.
4. Efficient CI: state selection, manifest provenance, deferral, modified models
   and downstream impact, comparison with full builds, and situations requiring
   broader validation. Explain the actual configuration and commands.
5. Production deployment: deploy an approved revision, configure production
   jobs and schedules or orchestration, distinguish deployment from execution,
   and compare managed dbt platform jobs with dbt Core plus external CI and
   orchestration. Use one concrete implementation for the lab; verify current
   official guidance before choosing/configuring the tooling.
6. Operations and recovery: logs, run results, lineage/docs, freshness and test
   alerts, ownership, retry/idempotency, concurrent runs, incremental backfills,
   schema evolution, and why reverting Git does not reverse database changes.
7. Acceptance lab: introduce a failing change, observe CI block it, correct it,
   promote an approved change, verify target/output/artifacts, and demonstrate
   recovery from a failed production-style run. Begin with local simulation;
   label hosted CI and live warehouse validation separately until evidenced.

For each stage, teach authoring/templates, configuration locations, execution
mechanisms, professional review practices, and Staff-level failure tradeoffs in
small chunks. Cloud labs remain subject to billing guardrails and the owner's
$200/month ceiling with a target below $150. Adding this curriculum does not
activate jobs, provisioning, or paid services.

### Required local-to-cloud pipeline and Airflow implementation

Owner requirement, 2026-10-15: implement locally first, then implement and verify
the representative pipeline in the cloud. Cloud execution is required, not an
optional conceptual extension. Follow foundations with local Airflow, then
integrate cloud deployment with the Azure/Databricks track. Introduce enough
Python for DAG authoring gradually; deeper Python remains a later track.

- Build a real DAG coordinating bounded batch ingestion into a landing area,
  source availability, load freshness and batch completeness checks, dbt
  transformations/tests, downstream publication gating, and notification tasks.
- Teach Airflow's scheduler, metadata database, workers/executor, DAG parsing,
  task isolation, and connections separately from the analytical database.
  Explain where each component executes locally and in the cloud.
- Author and review Python DAGs and configuration; cover task dependencies,
  data intervals/logical dates, schedules/time zones, catchup/backfills, timeouts,
  retries with idempotent writes, concurrency, and avoiding heavy data in XCom.
- Use explicit ingestion completion evidence/load timestamps and reconciliation
  checks; prevent stale or partial batches from silently producing reports.
- Exercise missing input, stale/partial batches, schema drift, test failures,
  late arrivals, task failures, reruns and recovery without duplicate writes.
  Define expected task states, downstream blocking, alert ownership, and recovery
  steps; verify each exercised scenario with evidence.
- Implement CI for DAG loading/validation and dbt changes, reproducible runtime
  dependencies, versioned deployment, secret injection/service identities,
  centralized logs and artifacts, and a clear operational runbook.
- For cloud: select a costed Azure-oriented architecture and Airflow hosting
  approach; implement storage, ingestion, a compatible analytical target,
  cloud-hosted Airflow execution, and cloud job monitoring. Reuse core logic but
  explicitly adapt credentials, storage paths, compute, networking, and runtime
  dependencies. Do not count local Airflow calling a cloud database as proof of
  cloud-hosted orchestration.
- Verify representative end-to-end success and failure/recovery paths in both
  environments. Record scenario, expected behavior, local evidence, cloud
  evidence, and remaining gaps. Include cleanup/teardown and measured cost.
- Before cloud provisioning, verify billing guardrails and current official
  setup guidance; estimate total concurrent costs against the $200/month ceiling
  and below-$150 target. Use bounded lab windows and teardown. If the proposed
  architecture does not fit, redesign within budget rather than omit cloud work.

This is curriculum scope, not confirmation that cloud resources, schedules,
notifications, or CI integrations have been created or activated.

### Original ordering (historical)
1. SET
2. PY + SQL in parallel
3. AF + DBT
4. AZ/MS + DBX
5. MOD/DE/SYS
6. AI/BI
7. CAP continuously once foundations exist
8. INT continuously, synchronized with completed skills
9. CERT after practical foundation is established

## Suggested Session Volume (Adaptive)
These are starting estimates, not fixed commitments.

| Track | Initial Session Estimate |
|---|---:|
| SET | 6–10 |
| PY | 18–28 |
| SQL | 8–12 |
| AF | 10–14 |
| DBT | 10–14 |
| AZ | 8–12 |
| MS | 8–12 |
| DBX | 10–14 |
| MOD | 8–10 |
| DE | 8–12 |
| AI | 8–12 |
| BI | 6–10 |
| SYS | 10–14 |
| INT | 12–20 |
| CAP | 15–25 |
| CERT | As needed |

The curriculum may shorten strong areas and expand weak areas.

## Baseline Diagnostic
Run AFTER project setup.
Create diagnostic sessions for:
- Python
- SQL
- data modeling
- system design
- Airflow/dbt awareness
- Windows/terminal
- Azure/Microsoft stack
- Databricks/Spark
- AI-native concepts

Diagnostic results must update:
- skill-gap register
- session counts
- recommended order
- confidence/readiness scores

## Completion Standard
A topic is not “done” because it was explained.
Completion requires evidence such as:
- independent implementation
- debugging success
- closed-book answer
- timed coding
- architecture defense
- production failure reasoning
- clear explanation to an interviewer
