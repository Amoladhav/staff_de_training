# Decisions Log

Record decisions that materially change the plan.

## D-018 — Professional feature implementation (2026-10-15)
- Owner requires professional engineering as features are added, not only conceptual production context.
- Use maintainable structure, explicit configuration, validation, error handling/logging, meaningful tests, reproducibility, and operational/recovery documentation proportionate to scope.
- Keep teaching in small reviewable steps; identify prototype limitations and refactor before expanding them into orchestration/cloud features.

## D-017 — Required cloud implementation and Airflow (2026-10-15)
- Owner requires actual cloud implementation after local validation, plus real-life Airflow orchestration.
- Updated agent rules, master plan and capstone acceptance to require both environments and explicit evidence.
- Sequence: dbt foundations, local orchestrated pipeline, then cloud implementation integrated with Azure/Databricks; gradual Python exposure for DAGs.
- Preserve $200/month ceiling and below-$150 target; select and cost hosting before provisioning. No cloud resources or schedules activated by this planning change.

## D-016 — Explicit dbt deployment and CI/CD curriculum (2026-10-15)
- Owner requests professional dbt model deployment flow and CI/CD as required learning.
- Added a sequenced hands-on module to the master plan and concrete capstone evidence requirements.
- Teach after modeling/testing foundations, then extend with incremental recovery and Databricks integration; do not interrupt the current first-tests exercise.
- Curriculum planned only; no hosted CI, deployment, or cloud execution configured.

## D-015 — Professional implementation context
- Explain real-team authoring, scaffolding/generation, review, and deployment practices alongside each concept.
- Distinguish a minimal training example from production conventions; do not imply all companies use one workflow.
- Proactively identify what is generated versus maintained by engineers, including model properties YAML.

## D-014 — Teach dbt from the beginning
- Owner requests a blank-slate dbt course covering everything needed progressively.
- For dbt, explain before asking comprehension questions; this refines D-013's pre-topic probing rule.
- Preserve small chunks and hands-on practice, building toward Staff-level depth.

## D-013 — Small chunks and knowledge probes (2026-10-13)
- Explicit owner request: ask focused probing questions about the current topic before teaching or advancing.
- If the learner demonstrates understanding, proceed; otherwise explain the role-relevant concepts to Staff Data Engineer depth and check understanding.
- Keep each chunk manageable, including environment setup. Canonical teaching rules updated in AGENTS.md.

## D-012 — Current owner preferences and canonical workspace (2026-10-13)
- Supersedes D-001 fixed session durations: use fast competency checkpoints.
- Refines D-004 sequencing: setup → dbt → Databricks with gradual Python → deeper Python.
- Canonical workspace is `/home/amola/projects/staff_de_training`; preserve the existing training-note subfolder.
- Retain OneDrive originals as a snapshot; WSL edits do not automatically sync to OneDrive.
- Cloud allowance is $200/month with a target below $150; billing readiness and budget alerts remain unverified.

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

## D-016 — Living dataflow and developer workflow tracker (2026-10-15)
- Owner requests diagrams and per-work-item developer workflows in a Markdown file with TBD, In Progress, and Done statuses.
- Canonical tracker: ../docs/DATAFLOW_TRACKER.md. Agent updates it after every advancing training step and synchronizes checkpoint documents.
- Keep intended architecture distinct from implemented execution, evidence provenance explicit, and local/cloud acceptance separate.

## D-017 — Proactive thread transition prompts (2026-10-16)
- Assess thread length/output/repetition at checkpoints; use qualitative signals unless telemetry is available.
- Save handoff, tracker and relevant logs before recommending a switch; supply summary and ready-to-paste resume prompt.
- Continue when the owner prefers; do not fabricate context percentages or promise advance compaction notice.

## Five-checkpoint continuity reviews — 2026-10-16
- Owner requests thread-length assessment every five checkpoints with summary and new-thread resume prompt near a useful transition threshold.
- Persist counter in tracker; use qualitative accumulated-history/phase-change assessment unless actual telemetry is available. Five is the review cadence, not a capacity limit. Permit earlier warnings; no automatic-compaction guarantee.

## D-018 — Git checkpoints throughout delivery (2026-10-16)
- Owner mandates professional production lifecycle. Establish one workspace-root repository now, before further pipeline changes, preserving existing paths.
- Use meaningful baseline and feature commits with diff review and verification; teach learner-led operations. Bring repository foundation portion of W08 forward.
- Add actual hosted PR/CI and protected integration in W09 before deployment; distinguish local simulation from real enforcement. Baseline records known limitations and does not imply production readiness.

### D-018 clarification — complete branching lifecycle
- Use short-lived feature branches from main after initial baseline; teach all review, validation, staging, commit, PR/CI, conflict, merge/cleanup and release/recovery steps.
- Hosted feature PRs default to squash merge; local reviewed merge is explicitly simulation. No independent peer approval claimed for solo/tutor review.
