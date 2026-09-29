
---

# 4. `docs/CURRENT_STATE.md`

This one needs to be different from the others.

**Do not pretend this is a permanent specification.** It is a live project status file.

Use this initial version:

```markdown
# Pathfinder AI — Current State

> This file describes the current implementation state.
> Update it when meaningful project work is completed.
> Do not use it as a replacement for source code inspection.

Last major project direction update: September 2026.

---

# 1. Current Product Direction

Pathfinder is currently being developed toward **Version 2**.

Current V2 direction:

- natural-language-first
- multi-domain
- local-first
- evidence-driven
- decision-intelligence oriented
- personalized dashboard
- market-data pipeline
- analytics / ML where justified
- LLM explanation/discussion layer

The old form-based base-level specification is superseded.

---

# 2. Repository

Repository:

`Pathfinder-AI`

GitHub:

`https://github.com/Punyadeep77/Pathfinder-AI.git`

Primary branch:

`main`

The repository is the source of truth for implementation.

---

# 3. Known Base-Level Work

The project has an existing base implementation and data pipeline.

Known completed/implemented areas include:

- project structure
- seed-data generation
- seed career-role dataset
- skill taxonomy
- ETL pipeline
- dataset validation
- preprocessing / transformation
- SQLite database setup
- database loading
- configuration
- logging
- Career Identity logic
- Reality logic
- Career Verdict logic
- supporting models/services
- tests

Historical project work generated:

- 24 representative career roles
- 91 skills

The exact current implementation must always be verified against the repository before modifying code.

---

# 4. Existing Decision Architecture

The established conceptual decision flow is:

```text
Natural User Input
        ↓
Input Understanding
        ↓
User-Type Detection
        ↓
Profile / Constraint Extraction
        ↓
Missing Information Check
        ↓
Targeted Clarification
        ↓
Career Identity
        ↓
Market Reality
        ↓
Career Evaluation / Verdict
        ↓
Evidence
        ↓
Dashboard
        ↓
Explore More Options
        ↓
LLM Discussion