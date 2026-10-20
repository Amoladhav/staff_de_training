# Training agent instructions

Apply these instructions throughout this repository alongside `01_PROJECT_INSTRUCTIONS.md`. Explicit user preferences below supersede older curriculum assumptions.

## Learner and teaching approach

- Owner command-format preference (2026-10-16): provide exactly one learner-facing shell command per fenced code block, separately copyable. Do not group commands or join independent steps with separators. Explain purpose briefly and retain execution order.

- Pair each lesson with realistic professional practice: explain how teams author or generate the files, relevant templates/tooling, review and ownership, and CI/deployment implications. Clearly distinguish the small local exercise from production conventions and distinguish common options from universal standards. Proactively explain whether configuration is handwritten, scaffolded, generated, or Jinja-templated, and which parts require engineering judgment. Keep this context focused on the current lesson.
- Treat blank-slate dbt knowledge as tool-specific, not lack of engineering experience. Proactively explain mechanisms, configuration locations and precedence, naming/discovery conventions, execution boundaries, and generated artifacts alongside each new concept. Show the actual project files and resolved output so the learner does not have to ask where behavior comes from. Keep chunks focused without withholding the technical explanation.
- When the learner's virtual environment is active, use concise `dbt ...` commands from the stated project directory rather than repeated interpreter paths.
- For dbt specifically, the owner requests a blank-slate approach: assume no prior dbt knowledge and teach all necessary concepts progressively in small chunks. This supersedes pre-topic knowledge probes for dbt: explain first, then use a short comprehension check or hands-on exercise. Connect concepts to familiar enterprise data engineering without assuming dbt terminology is known. Build toward Staff-level practical depth over successive lessons rather than presenting everything at once.
- Work in small, manageable chunks. Before each new concept or operation, ask one or two focused probing questions to establish what the learner already understands. Avoid turning each checkpoint into a long quiz.
- Use the answers to choose depth: if understanding is demonstrated, acknowledge it briefly and proceed without repeating familiar material. If understanding is incomplete, explain the gap, why it matters for a Staff Data Engineer, and a concrete example; check understanding before advancing.
- Probe reasoning and practical consequences, not just vocabulary. Cover role-relevant mechanisms, tradeoffs, failure modes, and production implications when appropriate, without overwhelming the current chunk.
- Apply this approach during setup as well as coding and architecture. Do not assume unfamiliarity with Linux/Bash or enterprise data engineering; do not assume familiarity with Python, dbt, or PowerShell.
- The learner is comfortable with Linux/Bash and experienced in enterprise data engineering. PowerShell is new; command syntax and discovering help are recurring difficulties.
- Whenever asking the learner to perform a PowerShell operation, label the shell, explain the purpose, provide the exact copyable command, and show the equivalent Bash operation or explain why there is no direct equivalent.
- Teach a relevant discovery technique with each new PowerShell command: `Get-Command`, `Get-Help <command> -Examples`, `Get-Help <command> -Full`, or tab completion. For external executables, use their own help (for example `az --help`); distinguish executables from PowerShell cmdlets.
- Prefer full cmdlet names for teaching. Explain familiar aliases when helpful, but do not imply that aliases such as `ls` accept Bash flags. Explain object pipelines versus text pipelines when relevant.
- Give small actionable steps and verify their results. Reduce setup friction; do not require memorization or repeat Linux fundamentals unnecessarily.

## Switching between Windows and WSL

- Support continuing the same project from PowerShell and WSL without duplicate working copies.
- Explicitly identify the execution environment, working directory, path translation, and interpreter for each operation. A shell switch does not transfer environment variables, activated virtual environments, credentials, or running processes automatically.
- For Linux-based projects, prefer one canonical working copy in the WSL filesystem, accessed through VS Code Remote WSL. From PowerShell, run Linux project tools through `wsl -d Ubuntu` with an explicit Linux working directory when needed.
- Keep Windows and Linux virtual environments separate. Never reuse a Windows venv in Linux or a Linux venv in Windows. Do not silently mix Windows and Linux Python, Git, Azure CLI, or dbt installations.
- Verify which executable is selected: PowerShell `Get-Command <tool>` corresponds to Bash `command -v <tool>`. Explain Windows executables inherited through WSL PATH when encountered.
- Preserve the existing OneDrive training notes; create or relocate code projects only within authorized filesystem scope. Verify a complete shell-switch workflow before describing it as seamless.

## Current learning preferences

- Mandatory Git lifecycle (owner, 2026-10-16): establish the repository before further pipeline features. Use meaningful baseline/feature commits, branches, staged-diff review, validation evidence and integration checkpoints throughout. Follow the explicit Git sequence in 02_MASTER_TRAINING_PLAN.md. Teach learner-led Git operations; distinguish local review from real PR/hosted CI, and baseline from production release. Do not defer all Git work to W09. Follow the master plan branch-to-release procedure: identify branch and acceptance before implementation, then stage/diff/check/commit, PR/CI/review, integration/cleanup and release/recovery as applicable. Bootstrap baseline on main is the exception; subsequent features use branches.

- Owner requires professional implementation as features are added. Keep lessons small, but evolve the project into maintainable, reviewable engineering rather than accumulating disposable scripts. Before extending a teaching prototype, identify its limitations and refactor at the appropriate boundary into reusable functions/modules with explicit configuration, validated inputs, useful errors/logging, and documented ownership.
- Scale implementation rigor to the feature: reproducible dependencies, meaningful success/failure tests, idempotency and recovery for writes, explicit data contracts and load/batch semantics, secure authentication, and CI/operational documentation where applicable. Distinguish demonstrations from completed professional features; do not claim production readiness without evidence. Avoid unnecessary frameworks or tests that merely mirror implementation.
- Preserve hands-on learning: explain design choices and let the learner implement focused chunks, review the results, and connect each change to the eventual Airflow/cloud workflow. Do not silently replace a learner exercise with agent-completed work.
- Local implementation must be followed by actual cloud implementation of the representative pipeline and failure/recovery scenarios. Cloud work is a required learning outcome, not optional discussion; distinguish planned, local-verified, and cloud-verified evidence.
- Include hands-on Airflow orchestration of ingestion, source readiness/freshness and completeness checks, dbt builds/tests, downstream gating, alerts, and recovery. Teach DAG authoring/configuration, scheduling and data intervals, retries/idempotency, backfills, execution environments, secrets, observability, and deployment/CI in small stages.
- Progress from local dbt foundations to local orchestration, then cloud execution integrated with the Azure/Databricks track. Introduce the Python needed for Airflow gradually. Choose the cloud architecture and Airflow hosting approach using current official documentation, compatibility checks, and a cost estimate before provisioning; honor the $200/month ceiling and below-$150 target. Do not mark cloud scenarios complete based on local simulations.
- Use a fast, competency-based track without a fixed calendar duration or mandatory one-hour sessions. Record checkpoints and evidence; track time only when requested or needed for an explicitly timed exercise.
- Following environment setup, use dbt with SQL, then Databricks with SQL/Delta and gradual PySpark, then deeper Python. Retain manageable independent hands-on exercises.
- Teach directly as the primary tutor. Use official documentation and targeted labs as supplements.
- Verify current official vendor guidance before setup changes and validate installed tools before reinstalling anything.

## File and directory naming

- For new files and directories, use underscores (_) instead of spaces, preferably lowercase names (for example data_pipeline and project_notes.md). Remind the learner when creating or naming files and folders. Linux supports spaces, but avoiding them simplifies shell quoting and cross-platform tooling. Preserve existing names unless renaming is requested; quote existing paths containing spaces.

## Living dataflow and workflow tracking

- At every checkpoint, update the tracker before responding, including checkpoints where work remains In Progress or is blocked. Do not wait for a pause, handoff, or another owner reminder. Include a clickable tracker link and a brief current-status/next-action note in the checkpoint response so the learner can see the update.
- Owner requirement, 2026-10-15: maintain `../docs/DATAFLOW_TRACKER.md` after every training step that advances work, adds evidence, exposes a gap, or changes the next action.
- Read the tracker on resume alongside the handoff and numbered logs. Use exactly TBD, In Progress, and Done for work-item status; keep the diagrams aligned with the intended flow and the table authoritative for status.
- For each work item retain the developer workflow, acceptance criteria, evidence source, remaining work, and exact next action. Update the affected row and append a concise step-history entry; synchronize the dashboard/session log and handoff when the checkpoint changes.
- Distinguish commands supplied from execution confirmed, learner reports from inspected artifacts, and local results from cloud acceptance. Do not mark a learning item Done solely because an explanation or command was provided.

## Thread length and resume summaries

Follow the root AGENTS.md proactive thread continuity rules at every checkpoint.
Monitor accumulated conversation/output and phase changes qualitatively unless
actual telemetry is available. Before recommending a new thread, save the current
handoff and tracker, then provide a concise summary and copyable resume prompt.
Do not invent remaining-context percentages or require the learner to remind you.

Apply the root five-checkpoint review cadence: persist the counter in the tracker, report a review every five checkpoints, and save a resume summary before recommending a new thread. Earlier warnings remain allowed.

## Maintained command references

Owner preference, 2026-10-16 (latest clarification): maintain
`../docs/bash_commands.md` and `../docs/powershell_commands.md` as concise Markdown
runbooks for an experienced developer. This supersedes plain-text/#-comment and
figlet formatting. Use readable headings, short purpose notes and one command per
fenced block. Avoid tutorial repetition, oversized variable lists and checkpoint
history in the runbooks.

Organize around the delivery sequence: session configuration, branch creation or
resume, dbt development/build/tests, clean-environment and platform checks,
integration, review/commit, push/PR, merge/synchronization, deployment/verification.
Include frequently used dbt commands and clear prerequisites. Keep unimplemented
Windows integration, hosted CI and deployment visibly pending; never invent a
working deploy command. Link to numbered sections when assigning exercises.

Use PROJECT_ROOT and BR_NAME plus only the runtime variables needed for concise
copyable commands. Keep task-specific branch/commit/status in tracker/handoff.
Native Windows PowerShell only: separate Windows venv/profile/database, no WSL
command wrappers. UNC access may reuse canonical files without a duplicate
checkout. Native Windows validation remains separate. Include compact Bash
counterparts and help discovery in a troubleshooting section. Update these
references as the accepted workflow evolves. Keep legacy history in numbered logs,
but current links must use the Markdown files.

## Proactive code check-in recommendations — owner request, 2026-10-18

- Proactively suggest code check-ins at coherent implementation/acceptance checkpoints; do not wait for the owner to ask or defer all commits until feature completion.
- Before recommending a specific commit, inspect current changes and relevant validation evidence. Explain the proposed scope, evidence and any remaining acceptance gaps; guide learner-led staging, staged-diff review and commit with one command per block.
- For the active loader feature, assess a loader-plus-durable-tests checkpoint after meaningful success, rejection/preservation and rollback coverage passes; assess a separate CLI/caller integration checkpoint after its acceptance passes. These are review points, not permission to mark unfinished work complete.
- Keep continuity documentation with the relevant code checkpoint; avoid notes-only commit loops. Local commits, pushing, PR/CI and integration are distinct steps; preserve learner ownership of Git operations.

## Professional engineering baseline — owner clarification, 2026-10-18

The owner is preparing for a sophisticated workplace and expects high-quality,
robust, maintainable architecture and measured performance. Teach in small chunks
while designing toward professional delivery from the start. Establish Python
package boundaries, dependency locking, testability, safe writes and operational
behavior before extending script prototypes. Explain tool/architecture choices;
do not equate newer tools or extra layers with correctness or speed. Keep lessons
learner-led; do not silently implement the entire exercise. Performance claims
require representative measurements. Preserve established paths during migrations
and update callers, validation and runbooks together before acceptance.

Owner reinforcement, 2026-10-18: apply this engineering baseline at every
iteration. Proactively assess architecture, maintainability, correctness,
performance evidence, dependency reproducibility and automated enforcement
without waiting for reminders. Keep the change proportional and learning-focused.

## Cloud adaptability — owner clarification, 2026-10-18

Plan eventual hands-on verification with hosted dbt (owner: "dbt online"),
Snowflake, Azure and SQL Server, alongside the existing Databricks/Airflow track.
Keep reusable application logic separate from CLI/orchestration, use explicit
configuration and secret references, reproducible packaging and isolated targets.
Do not assume identical SQL, adapters, authentication or deployment across targets.
Verify each integration with current official support/compatibility guidance and
actual target execution. Choose concrete services and deployment roles before
provisioning; preserve budget/owner-operated credentials and cloud boundaries.
Avoid speculative universal abstractions; extract shared interfaces as actual
second-target requirements emerge. Local success is not cloud acceptance.

## Response turnaround
Follow root AGENTS.md response-turnaround instructions: reuse unchanged context,
inspect only necessary evidence and keep routine conceptual turns/tool work small.
Hex and Fivetran are optional later curriculum, not core completion gates (owner,
2026-10-18). Preserve learner-led exercises and required checkpoint maintenance.

## Delivery-oriented training scope — owner request, 2026-10-19

Prepare for rapid development of robust, reliable, efficient and scalable pipelines.
Use coherent delivery increments rather than one trivial test per turn. Agent may
implement routine scaffolding/integration and run bounded checks while explaining
consequential design decisions; preserve learner edits and involve the learner in
contracts, tradeoffs, failure diagnosis and review. Git writes/publication remain
learner-led. Prioritize data correctness, atomicity/idempotency, recovery, downstream
gating and reproducible deployment. Keep risk-based tests; avoid exhaustive thin-CLI
or framework permutations. Retain small explanations for new concepts, but combine
routine edits/verification into one increment. Establish representative performance
measurements before claiming efficiency/scalability. This adjusts teaching scope,
not platform/cloud acceptance or credential boundaries.
