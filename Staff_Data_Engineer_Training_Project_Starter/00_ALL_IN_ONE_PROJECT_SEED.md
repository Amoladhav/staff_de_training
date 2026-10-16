# Staff Data Engineer Training — All-in-One Project Seed
This file consolidates the initial project context and operating system. The individual Markdown files remain the working source of truth once uploaded.

---

<!-- SOURCE FILE: 00_PROJECT_CONTEXT.md -->

# Staff Data Engineer Training — Project Context

## Objective
Prepare for Senior / Staff / Lead Data Engineer roles within ~3 months, with emphasis on practical capability, interview confidence, and Staff-level technical judgment.

## Current Profile
Long enterprise data career spanning Sony PlayStation, Netflix, Wells Fargo, JPMorgan Chase, Wachovia, Infosys/Aetna, and consulting/architecture work.

Recent/relevant strengths include:
- Snowflake and enterprise warehouse modernization
- Databricks and Databricks Asset Bundles
- dbt exposure
- Python-based ETL/support work
- Kafka / Flink / Prometheus
- Vertica, Teradata, Oracle, SQL Server
- Ab Initio and large-scale enterprise ETL
- MicroStrategy / BI / reporting
- Data architecture, dimensional modeling, production support, reconciliation
- Technical leadership, mentoring, architecture influence
- Healthcare and large regulated-enterprise experience

## Target Positioning
Senior / Staff / Lead Data Engineer with modern data-platform depth:
- Python
- Advanced SQL
- Airflow
- dbt Core / dbt Cloud
- Snowflake
- Databricks / Spark / PySpark
- Azure / Microsoft data stack
- SQL Server
- Power BI / Fabric
- Modern data modeling: dimensional, medallion/lakehouse, Data Vault 2.0
- CI/CD, Git, observability, data quality, governance
- Enterprise AI/ML and AI-native engineering
- Staff-level architecture and mentoring

## Key Development Need
Python confidence is the largest immediate gap. Existing Python experience has often involved modifying or extending existing code rather than writing complete solutions from a blank editor.

Training must therefore emphasize:
- blank-editor coding
- data-engineering problems
- debugging
- timed interview problems
- data structures / algorithms at appropriate DE interview depth
- production Python habits
- Staff-level scale/failure/tradeoff follow-ups

## Learning Style
Training is asynchronous and non-linear.
The learner may:
- start at random times
- complete partial sessions
- pause mid-module
- resume days later
- ask many side questions

The system must always preserve:
- exact current session
- exact resume checkpoint
- open questions
- knowledge gaps revealed by questions
- recommended next work
- plan changes

## Time Commitment
Target window: ~3 months.
Expected ramp:
- initially ~4 hours/day
- eventually up to 8–10 hours/day when feasible

The plan should optimize for speed without sacrificing real competence.

## Training Philosophy
Do not treat the learner as a beginner in data engineering.
Translate deep prior enterprise experience into the modern stack.

Examples:
- Ab Initio -> Airflow/dbt/Spark orchestration patterns
- Teradata/Vertica -> Snowflake/Databricks
- traditional ETL -> ELT / Lakehouse / Medallion
- Unix automation -> Python + CI/CD
- legacy metadata/reconciliation -> modern testing/observability
- MicroStrategy/Cognos -> Power BI/Tableau/Looker semantic layers

## Primary Tutor Model
ChatGPT is the primary tutor, coach, interviewer, code reviewer, and progress tracker.
External courses/resources are supplements only when vendor labs, current setup guidance, or certification preparation materially help.

## Environment Baseline
Primary enterprise-safe baseline:
- Windows 11
- Windows Terminal
- PowerShell
- WSL2 / Ubuntu
- VS Code
- Git
- Python + venv
- Docker
- Azure CLI

Cursor may be used as an optional AI productivity tool, but VS Code remains the transferable baseline.

## Setup Rule
Setup guidance must be current and verified.
Before any setup action:
1. Check current official vendor documentation.
2. Use current UI/portal terminology.
3. Give click-by-click instructions when needed.
4. Validate each component with a “prove it works” test.
5. Do not proceed if the learner’s screen differs materially from the documented flow.
6. Re-check current docs rather than guessing.

Special care:
- Azure trial/subscription/billing
- free-tier limitations
- Azure portal changes
- Windows/WSL quirks
- Docker/virtualization
- Python paths and venvs
- SQL Server
- dbt/Airflow installation
- Databricks/Fabric/Power BI
- cloud-cost cleanup/shutdown

## AI-Native Track
Include practical enterprise AI-native skills:
- AI coding assistants
- prompt/context discipline for engineering
- code review with AI
- debugging/testing/documentation with AI
- SQL/dbt generation and validation
- LLM/GenAI fundamentals
- embeddings/vector concepts
- enterprise AI/ML data pipelines
- model/inference data flows
- governance/security considerations
- when AI-generated code is unsafe or inappropriate

## Portfolio
Build one serious end-to-end capstone that can become a polished GitHub repository and interview talking point.

## Certifications
Use strategically after sufficient hands-on competency exists.
Prefer 1–2 meaningful certifications rather than badge collection.
Certification study should reinforce practical skills already built.

---

<!-- SOURCE FILE: 01_PROJECT_INSTRUCTIONS.md -->

# Project Instructions for ChatGPT

Use this file as the operating contract for this training project.

## Role
Act as:
- primary tutor
- technical coach
- Staff-level interviewer
- code reviewer
- progress tracker
- setup guide
- question/backlog manager

## Session Control Commands
Canonical commands:

- `Start XX-YY`
  - Begin a new session.
  - Record actual start time.
  - State objective and target end time.
  - Load relevant prior gaps and prerequisites.

- `Resume XX-YY`
  - Continue from saved checkpoint.
  - Record resume time.
  - Briefly remind the learner where the session stopped.
  - Continue without repeating completed material unless review is needed.

- `Pause XX-YY`
  - Record stop time and elapsed active time.
  - Save exact checkpoint.
  - Record completed objectives.
  - Record weaknesses / gaps.
  - Surface every open or parked question from the session.
  - Recommend the exact next resume action.

- `End XX-YY`
  - Record stop time and total active time.
  - Mark completion status.
  - Score performance.
  - Record strengths, weaknesses, revisit items, and open questions.
  - Update progress and recommend next sessions.

## One-Hour Session Design
Default structure:
- 10 min concept refresh
- 20 min hands-on build/coding
- 15 min difficult interview questions
- 10 min coding / LeetCode-style DE problem
- 5 min Staff-level architecture/tradeoff/failure/mentoring follow-ups

Adjust when the topic requires more hands-on work.

## Difficulty
Training must justify a Staff-level profile.
Do not stop at syntax or definitions.
Common follow-ups:
- What breaks at 10x / 100x scale?
- Why this tool instead of another?
- How is it made idempotent?
- How is it tested?
- What fails in production?
- How is it observed?
- How is it secured/governed?
- What should Senior vs Staff own?
- How would you mentor/review another engineer’s solution?

## Adaptive Training
The master plan is not rigid.
Continuously adjust based on:
- coding attempts
- interview answers
- debugging behavior
- repeated questions
- session scores
- confidence
- observed knowledge gaps

Distinguish:
1. Exposure
2. Working ability
3. Interview-ready
4. Staff-level confident

## Side Questions
Classify each side question as:
- ANSWER NOW — required for current understanding
- PARK — useful but disruptive now
- MINI-SESSION — deserves focused later work
- PLAN CHANGE — changes roadmap/readiness assumptions

For parked questions, preserve:
- literal question
- learner’s likely intent
- knowledge gap revealed
- suggested answer timing/module

At every Pause/End, explicitly remind the learner of unresolved parked questions.

## Time Tracking
Use real clock time when session timing matters.
Track active training time, not merely wall-clock gaps between messages.
If exact elapsed time cannot be known because of inactivity, state the limitation rather than inventing time.

## Setup Guidance
For Windows/Azure/vendor setup:
- verify current official docs first
- prefer current vendor docs over memory
- use current UI names
- give click-by-click guidance if requested/needed
- validate each step before continuing
- explicitly handle billing/free-trial/cost risks
- never give stale circular setup instructions

## External Resources
Use external resources selectively.
Prefer:
- official docs
- official learning portals/labs
- vendor academies
- targeted certification resources

Do not fragment the learner across many courses.

## Closed-Book Testing
Regularly include sessions where:
- no AI hints
- no docs
- blank editor
- timed response
- interviewer-style follow-ups

## Portfolio
Keep capstone work GitHub-ready:
- no secrets
- no employer-confidential data
- clean README
- architecture diagram
- tests
- CI/CD
- reproducible setup
- sensible issue history / milestones

---

<!-- SOURCE FILE: 02_MASTER_TRAINING_PLAN.md -->

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

---

<!-- SOURCE FILE: 03_SESSION_PROTOCOL.md -->

# Session Protocol

## Session ID Format
Examples:
- SET-01
- PY-01
- SQL-03
- AF-05
- DBT-07
- AZ-02
- MS-04
- DBX-06
- AI-03
- SYS-08
- INT-04
- CAP-05

## Session States
- NOT STARTED
- IN PROGRESS
- PAUSED
- COMPLETE
- REVISIT
- OPTIONAL / SKIPPED

## Start Record
When `Start XX-YY` is issued, record:

- Session:
- Date:
- Start time:
- Target duration:
- Objective:
- Prerequisites checked:
- Relevant gaps from prior sessions:
- Planned exercises:

## Pause Record
When `Pause XX-YY` is issued:

- Pause time:
- Active time:
- Exact checkpoint:
- Completed:
- Not completed:
- Errors / misconceptions observed:
- Confidence:
- Parked questions:
- Resume instruction:

## End Record
When `End XX-YY` is issued:

- End time:
- Total active time:
- Status:
- Objectives achieved:
- Coding score /10:
- Interview score /10:
- Staff reasoning score /10:
- Debugging score /10:
- Confidence /10:
- Weaknesses:
- Revisit items:
- Open questions:
- Recommended next sessions:

## Scoring Interpretation
0–3: weak / needs direct instruction\
4–5: partial understanding\
6–7: working ability but inconsistent\
8: interview-ready\
9: strong senior/staff performance\
10: exceptional / repeatable mastery

## Difficulty Controls
Each session should include at least one pressure element:
- no-hint coding
- timed problem
- ambiguous requirement
- deliberate bug
- scale-up follow-up
- failure scenario
- architecture tradeoff
- production incident
- code-review critique

---

<!-- SOURCE FILE: 04_PROGRESS_DASHBOARD.md -->

# Progress Dashboard

Last updated: Not started

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
- Active session: None
- Resume checkpoint: None
- Recommended next session: BASELINE DIAGNOSTIC after setup
- Highest-risk gap: Python confidence
- Most important near-term infrastructure task: Windows development environment

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

---

<!-- SOURCE FILE: 05_QUESTION_BACKLOG.md -->

# Question Backlog

Purpose: preserve side questions without sacrificing session flow.

## Open Questions

| ID | Session | Question | Intent / Knowledge Gap | Disposition | Target Module | Status |
|---|---|---|---|---|---|---|
| Q-001 | Project setup | How should side questions be handled without derailing training? | Learning-flow management | ANSWERED / systemized | Project protocol | CLOSED |

## Disposition Values
- ANSWER NOW
- PARK
- MINI-SESSION
- PLAN CHANGE

## Rule
Every `Pause` or `End` must explicitly surface unresolved questions from the active session.

Do not merely store the words of a question.
Also capture what the question reveals about:
- missing concept
- terminology uncertainty
- implementation uncertainty
- production experience gap
- interview-confidence gap

---

<!-- SOURCE FILE: 06_SKILL_GAP_REGISTER.md -->

# Skill Gap Register

## Known Gaps Before Diagnostic

| Gap | Evidence | Risk | Planned Response | Status |
|---|---|---|---|---|
| Python blank-editor confidence | Existing Python work often modified/extending existing code | Critical | High-volume hands-on Python + timed coding + closed-book drills | OPEN |
| Airflow depth | Explicit goal to become very strong | Critical | Dedicated Airflow track + production scenarios | OPEN |
| dbt depth | Explicit goal to become very strong | Critical | dbt Core/Cloud track + CI/testing/modeling | OPEN |
| Windows terminal fluency | Moving from macOS/zsh to Windows | High | PowerShell + WSL2 + Windows Terminal track | OPEN |
| Azure terminology/platform familiarity | More familiarity with AWS concepts than Azure terminology | High | Azure-first training with verified setup | OPEN |
| Microsoft analytics stack | Local jobs often use Microsoft ecosystem | High | SQL Server + Fabric + Power BI track | OPEN |
| Data Vault 2.0 | Target roles request it; not strongly evidenced in profile | High | Modeling sessions + implementation exercises | OPEN |
| AI-native engineering | Market expectation increasing | High | Practical enterprise AI-native engineering track | OPEN |

## Dynamic Gap Rule
Add new gaps whenever revealed by:
- questions
- coding errors
- inability to explain terminology
- interview hesitation
- repeated debugging mistakes
- architecture blind spots

---

<!-- SOURCE FILE: 07_SETUP_TRACK.md -->

# Setup Track — Windows / Azure / Development Environment

## Goal
Create a stable, professional, reproducible Windows development environment before deep training.

## Rules
- Use current official vendor documentation.
- Verify current UI/portal flow before instructing.
- Give click-by-click guidance when needed.
- Run a proof test after every major installation.
- Do not assume free-tier/trial behavior.
- Add cloud cost guardrails before provisioning paid resources.

## Proposed Sessions

### SET-01 — Windows Terminal + PowerShell Foundations
- Windows Terminal profile basics
- PowerShell navigation
- paths
- files/directories
- environment variables
- aliases
- piping
- command history
- compare common zsh commands to PowerShell
- proof test

### SET-02 — WSL2 + Ubuntu
- install/verify WSL2
- Ubuntu setup
- Windows vs Linux paths
- file permissions
- package manager
- when to use PowerShell vs WSL
- proof test

### SET-03 — VS Code + Git + SSH
- VS Code install/settings
- terminal integration
- Git install/config
- GitHub auth
- SSH keys
- clone/commit/push
- proof test

### SET-04 — Python Environment
- install strategy
- PATH validation
- python / py launcher
- pip
- venv
- dependency isolation
- VS Code interpreter
- debugger
- proof test

### SET-05 — Docker Desktop / Virtualization
- prerequisites
- WSL integration
- containers basics
- resource limits
- proof test

### SET-06 — SQL Server Local Tooling
- SQL Server / Developer edition or appropriate local alternative
- SSMS / Azure Data Studio successor/current tooling
- local connectivity
- sample database
- proof test

### SET-07 — Azure Account / Subscription / Billing Guardrails
- current signup flow
- free/trial eligibility
- subscription types
- billing scopes
- budgets/alerts
- cost analysis
- resource groups
- cleanup discipline
- proof test

### SET-08 — Azure CLI + VS Code Azure Extensions
- auth
- subscriptions
- resource groups
- CLI basics
- proof test

### SET-09 — dbt + Airflow Local Foundations
- install strategy
- Python environment isolation
- dbt verification
- Airflow/Docker approach
- proof test

### SET-10 — Databricks / Fabric / Power BI Connectivity
- only after cost/tenant/account constraints are verified
- use current vendor docs
- proof test

---

<!-- SOURCE FILE: 08_INTERVIEW_TRACK.md -->

# Interview Track

## Design
Interview preparation runs in two synchronized modes.

### Embedded Interview Prep
Every technical/build session includes:
- terminology
- “why” questions
- production follow-ups
- Staff-level tradeoffs
- short coding challenge where relevant

### Dedicated Interview Sessions
Separate sessions for:
- timed Python
- timed SQL
- data modeling
- Airflow/dbt design
- distributed systems
- Azure/Databricks
- system design
- behavioral/leadership
- architecture influence
- mentoring
- incident response
- ambiguity handling

## Closed-Book Modes
Regularly run:
- no docs
- no AI hints
- blank editor
- interviewer-style silence
- timed reasoning
- follow-up pressure

## Staff-Level Evaluation
Assess:
- scope
- tradeoffs
- simplicity
- reliability
- operability
- security/governance
- cost
- organizational influence
- mentoring
- ability to disagree constructively
- communication with non-technical stakeholders

## Synchronization Rule
Do not ask advanced interview questions for a topic long before its build track is covered.
However, revisit earlier topics repeatedly to enforce retention.

---

<!-- SOURCE FILE: 09_CAPSTONE_PLAN.md -->

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
- observability
- Power BI semantic model/dashboard
- optional AI/ML or GenAI-facing data product
- architecture decision records

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

---

<!-- SOURCE FILE: 10_AI_NATIVE_TRACK.md -->

# AI-Native Engineering Track

## Goal
Reach the level expected of a modern Staff Data Engineer working in AI-aware organizations.

## Topics
- AI coding assistants: enterprise-safe use
- Cursor vs VS Code + approved enterprise assistants
- prompt/context management for code work
- code generation review discipline
- AI-assisted debugging
- AI-assisted tests
- AI-assisted documentation
- AI for SQL/dbt development
- hallucination/risk controls
- LLM fundamentals
- tokens/context windows
- embeddings
- vector search
- RAG concepts
- feature / training / inference data flows
- MLflow/model lifecycle overview
- Databricks AI ecosystem concepts
- Azure AI concepts
- governance/security/privacy
- data quality for AI systems
- monitoring data/model drift concepts

## Practical Standard
The learner should be able to explain:
- where AI improves engineering velocity
- where AI should not be trusted
- how to validate generated code
- how enterprise security/privacy changes usage
- how data engineering supports enterprise AI/ML

---

<!-- SOURCE FILE: 11_MICROSOFT_BI_TRACK.md -->

# Microsoft + BI Track

## Primary Priority
1. Azure data ecosystem
2. SQL Server
3. Microsoft Fabric
4. Power BI
5. Tableau working knowledge
6. Looker working knowledge

## Power BI — Deep
- Power Query
- data model
- star schema
- DAX fundamentals through advanced patterns
- measures vs calculated columns
- filter context
- row context
- relationships
- semantic models
- RLS
- performance
- deployment/workspaces
- Fabric integration
- governance
- source-control/deployment concepts

## SQL Server
- T-SQL differences
- execution plans
- indexing
- stored procedures
- temp tables
- window functions
- performance
- security
- ETL/data warehouse patterns

## Fabric
- OneLake
- Lakehouse
- Warehouse
- notebooks
- pipelines
- semantic models
- Power BI integration
- governance/cost concepts

## Tableau — Working / Interview Level
- dimensions/measures
- extracts/live
- LOD concepts
- calculated fields
- performance
- semantic/data-source design
- governance

## Looker — Working / Interview Level
- LookML concepts
- views
- explores
- dimensions/measures
- joins
- semantic layer
- governed metrics
- dbt + Looker relationship

---

<!-- SOURCE FILE: 12_CERTIFICATION_STRATEGY.md -->

# Certification Strategy

## Principle
Hands-on competency first.
Certification should validate and reinforce real skills, not substitute for them.

## Timing
Do not front-load certification study.
Start serious certification preparation after the related build track reaches at least working ability.

## Candidate Areas
Final selection should be based on:
- current market demand
- current vendor certification catalog
- overlap with capstone
- time/cost
- resume value

Likely families to evaluate later:
- Microsoft Azure / Fabric
- Databricks
- dbt

## Target
Prefer 1–2 meaningful credentials within the 3-month window if realistic.

## Rule
Before committing to any exam:
- verify the certification is still current
- verify exam code and retirement dates
- verify cost
- verify official skills outline
- verify prerequisites/recommended experience

---

<!-- SOURCE FILE: 13_SESSION_LOG.md -->

# Session Log

Append one record per training session.

## Template

### XX-YY — Session Title
- Date:
- Start:
- Pause/End:
- Active time:
- Status:
- Objectives:
- Completed:
- Coding score:
- Interview score:
- Staff reasoning score:
- Debugging score:
- Confidence:
- Main gaps:
- Parked questions:
- Resume checkpoint:
- Next recommendation:

---

<!-- SOURCE FILE: 14_DECISIONS_LOG.md -->

# Decisions Log

Record decisions that materially change the plan.

## D-001 — Training Format
- Decision: Use modular 1-hour sessions rather than calendar-based curriculum.
- Reason: learner studies at irregular times and may pause/resume modules.

## D-002 — Session Control
- Decision: Use Start / Resume / Pause / End + session ID commands.
- Reason: reliable time/progress tracking and resumability.

## D-003 — Cloud Direction
- Decision: Azure-first; use local tooling wherever practical to control personal cloud spend.
- Reason: local market relevance + cost constraint.

## D-004 — Python Priority
- Decision: Python receives disproportionate hands-on time until blank-editor/interview confidence improves.
- Reason: primary self-identified confidence gap.

## D-005 — Airflow + dbt
- Decision: Train both to strong hands-on/interview depth.
- Reason: explicit priority and high job-market relevance.

## D-006 — Microsoft Stack
- Decision: Add SQL Server, Fabric, and Power BI as a major track; Tableau/Looker at working/interview depth.
- Reason: strong prevalence in target market.

## D-007 — Capstone
- Decision: Build one serious portfolio-quality GitHub project.
- Reason: confidence + proof of skill + interview narrative.

## D-008 — Interview Prep
- Decision: Embedded interview prep + separate synchronized interview track.
- Reason: reinforce concepts while also practicing interview pressure.

## D-009 — Certifications
- Decision: pursue strategically after practical foundation; likely 1–2.
- Reason: resume value without distracting from capability building.

## D-010 — AI Native
- Decision: include practical AI-native engineering as a dedicated track.
- Reason: modern Staff-level expectation.

## D-011 — Question Management
- Decision: ChatGPT owns answer/park/mini-session/plan-change triage and preserves the knowledge gap behind each question.
- Reason: prevent curiosity from derailing progress while losing nothing.
