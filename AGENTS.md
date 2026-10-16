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
