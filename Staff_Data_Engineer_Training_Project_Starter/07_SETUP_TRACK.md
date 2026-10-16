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
- Follow `AGENTS.md`: teach each PowerShell operation through its Linux/Bash parallel and relevant help/discovery technique.
- Verify continuing the same project from both PowerShell and WSL, with one canonical working copy and explicit execution environment.

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
- compare familiar Linux/Bash commands to PowerShell, including syntax and help discovery
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
