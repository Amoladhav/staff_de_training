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
