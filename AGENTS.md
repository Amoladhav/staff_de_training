# Staff data engineering training workspace

This WSL directory is the canonical working workspace. Preserve the existing
`Staff_Data_Engineer_Training_Project_Starter` folder and its filenames.

For all work here, read and follow:
- `Staff_Data_Engineer_Training_Project_Starter/AGENTS.md`
- `Staff_Data_Engineer_Training_Project_Starter/01_PROJECT_INSTRUCTIONS.md`

Resume from `docs/HANDOFF.md`, `docs/DATAFLOW_TRACKER.md`, and the numbered progress/session/decision logs. Update the dataflow tracker after every training step as specified in the linked agent instructions.
Use competency checkpoints without fixed session durations. Teach setup, then
dbt, then Databricks with gradual Python exposure, then deeper Python.

Before a useful thread transition, save a concise local handoff with verified
results, pending work, constraints, Git state, and the exact next action. Do not
invent context percentages or treat a handoff suggestion as cancellation.

## Proactive thread continuity

- At each checkpoint, assess thread length, accumulated tool output, repeated explanations/setup, and phase changes. Use exposed telemetry if available; otherwise explicitly treat this as a qualitative assessment, not a token count or context percentage.
- Before another substantial phase when a clean thread would help, proactively prompt the owner to start a new thread. Do not wait for a reminder or claim guaranteed warning before automatic compaction.
- First update docs/HANDOFF.md, docs/DATAFLOW_TRACKER.md, and relevant numbered logs. Save the objective, constraints/preferences, decisions, verified versus reported results, current Git/worktree state, active work, pending actions/blockers, and exact next step. Exclude credentials, raw data and transcripts.
- In the response, provide a short checkpoint summary, a clickable handoff link, and a ready-to-paste new-thread prompt naming this workspace and its canonical instructions.
- A transition recommendation is optional, not a cancellation. Continue if the owner prefers this thread, without repetitive reminders. On resume verify files and continue from the checkpoint without repeating completed setup or unknown state-changing commands.
- These instructions apply to agents loading this workspace; they do not change other machines, unrelated chats, or account-wide settings.

### Five-checkpoint review cadence

- Count one checkpoint per substantive assistant response that records learning progress, evidence, a decision, or an assigned exercise. Do not count tool calls, commentary messages, or multiple file edits separately.
- Maintain a thread label, counted checkpoints, last review checkpoint, next review checkpoint, assessment and recommendation in docs/DATAFLOW_TRACKER.md. Increment before the checkpoint response. Review explicitly at checkpoints 5, 10, 15, etc.; give a brief visible result even when continuing.
- Review accumulated thread length/output, repeated explanations, unresolved branches and upcoming phase changes. Use actual telemetry only if exposed. Otherwise the threshold is qualitative: recommend a handoff when accumulated history makes locating the current state harder, especially before another substantial phase. Five checkpoints is a review cadence, not a context-capacity limit.
- Keep the existing early-warning rule: do not wait for the fifth checkpoint if a handoff is already useful. Save the handoff, tracker and relevant logs first, then provide the summary/link/copyable resume prompt. No guarantee of warning before compaction.
- Initialize a new confirmed thread at zero and preserve the previous review summary. Compaction or a new date does not mean a new thread. If prior counts cannot be reconstructed reliably, state that and start an explicitly labeled baseline without inventing a historical total. Retain counts when continuing this thread.
- If the owner continues after a recommendation, continue work and assess on schedule without repeating the same switch prompt unless the situation materially changes.

## Copyable command formatting

- Owner preference, 2026-10-16: put each learner-facing shell command in its own
  fenced code block so it can be copied and run separately. Do not combine
  multiple commands in one block or join independent steps with shell separators.
- Explain each command's purpose briefly and preserve execution order.

## Focused resume and document maintenance

Owner request, 2026-10-18: reduce request turnaround without reducing teaching,
verification or continuity quality. Use this reading path:

1. On a new thread, read this file, the starter AGENTS.md and
   01_PROJECT_INSTRUCTIONS.md in full. Reuse those instructions within the thread
   unless they change; do not reload the whole curriculum for each reply.
2. Read docs/HANDOFF.md for the current objective, verified state and exact next
   action. Read the tracker through its work-item table; consult later evidence,
   diagrams and step history only when relevant to the active question.
3. Read Current Work in the numbered progress dashboard, the latest relevant
   session-log entries and applicable decision-log entries. Search headings first
   when locating older evidence. Historical records are not current assignments.
4. Verify only the live state needed for the next action. Expand inspection when
   evidence conflicts, a failure appears or the task crosses a new boundary.
   Preserve required acceptance checks; a summary never substitutes for evidence.

Document ownership: HANDOFF is the concise resume brief; DATAFLOW_TRACKER owns
work-item status, acceptance, evidence pointers and checkpoint count; the numbered
session/decision logs retain history and rationale; shell runbooks own reusable
commands; the master plan owns curriculum. Keep summaries consistent using short
updates and links rather than copying long histories into each file. Preserve
established filenames and historical records. Keep current state before history.
Do not weaken learner-led work, command formatting, platform/credential boundaries,
checkpoint cadence or professional teaching depth to optimize reading time.

## Response turnaround — owner request, 2026-10-18

- Keep routine teaching turns fast: reuse instructions and verified context already
  read in this thread. Read only changed learner files or the exact sections needed.
- For a conceptual answer, do not inspect Git, environments, dependencies or rerun
  tests unless the answer depends on current state. Browse only when required for
  current/uncertain facts; reuse sources already checked for the same lesson.
- Batch independent necessary reads and make one compact document-maintenance
  pass. Tracker owns current state/count; keep handoff/dashboard updates brief and
  link to detailed history instead of duplicating it. Preserve required updates.
- Give the focused answer or exercise promptly; avoid optional research, repeated
  summaries and tool calls that add no evidence. Preserve teaching depth, learner
  ownership, meaningful acceptance checks and five-checkpoint reviews.
- Do not claim measured speed improvements or change model/settings without
  evidence/authorization. Apply these workflow changes directly within this repo.

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
