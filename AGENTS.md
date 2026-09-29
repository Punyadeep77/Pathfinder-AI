# Pathfinder AI — Codex Instructions

## 1. Source of Truth

Use this authority order:

1. Actual repository code and data
2. `docs/DECISIONS.md`
3. `docs/CURRENT_STATE.md`
4. `docs/ARCHITECTURE.md`
5. `docs/PROJECT_CONTEXT.md`
6. `README.md`
7. `docs/archive/` — historical reference only

If historical documentation conflicts with current decisions, current decisions win.

---

## 2. Project Identity

Pathfinder AI is an evidence-driven career decision-intelligence platform.

It is NOT:
- a generic chatbot
- a career quiz
- a generic roadmap generator
- a simple skill-gap calculator

Its purpose is to understand a person's actual situation and evaluate career directions using structured career data and labor-market evidence.

---

## 3. Current Product Direction

Pathfinder V2 is natural-language-first.

The user describes their situation naturally.

The system should:

1. understand the input
2. detect user type
3. extract profile, skills, goals, constraints and preferences
4. identify genuinely missing information
5. ask only necessary clarification questions
6. evaluate career options
7. produce evidence-backed results
8. present results through a personalized dashboard
9. allow exploration of additional options
10. provide LLM-based explanation/discussion

Do NOT redesign Pathfinder as a long form-based questionnaire.

Older form-based documentation is historical.

---

## 4. Frozen Product Decisions

Read `docs/DECISIONS.md` before making architectural or product changes.

Important frozen decisions include:

- natural-language-first UX
- discover before recommend
- evidence before recommendation
- negative preferences are meaningful constraints
- reality over motivation
- multi-domain V2
- primary recommendations separate from Explore More Options
- LLM is not the final decision-maker
- ML is supportive and justified
- V2 is local-first
- V3 production/business infrastructure is out of scope unless explicitly requested

Do not silently change these decisions.

---

## 5. Engineering Behavior

Before changing code:

1. Inspect the relevant existing implementation.
2. Understand its interfaces and dependencies.
3. Reuse existing architecture where appropriate.
4. Make the smallest change that solves the requested task.
5. Run relevant tests/checks.
6. Report what changed and what was verified.

Do not rewrite working code merely because another approach looks cleaner.

Do not introduce unnecessary frameworks, abstractions, files, dependencies, or architecture.

---

## 6. Scope Discipline

Work only on the current requested task.

Do not:
- expand scope
- redesign unrelated modules
- implement V3 infrastructure
- add speculative features
- refactor unrelated code
- reopen frozen decisions

If a genuine architectural problem blocks the task, explain it briefly and ask before changing the architecture.

---

## 7. Token Efficiency

Optimize for useful work per context window.

- Read `AGENTS.md` first.
- Read only the documentation relevant to the current task.
- Inspect only the source files needed for the task.
- Do not repeatedly reread unchanged files.
- Prefer targeted searches over full-repository exploration.
- Do not produce unnecessary summaries.
- Do not restate project context already present in the repository.
- Do not generate large documentation unless requested.
- Keep plans concise.
- Keep final reports concise.

Do not spend tokens rediscovering Pathfinder's history when the repository already contains the relevant decision.

---

## 8. Documentation Rules

### `docs/DECISIONS.md`

Frozen product and architecture decisions.

Change only when the project owner explicitly changes a decision.

### `docs/ARCHITECTURE.md`

Current technical architecture.

Change only when architecture actually changes.

### `docs/PROJECT_CONTEXT.md`

Stable explanation of what Pathfinder is and why it exists.

Keep relatively stable.

### `docs/CURRENT_STATE.md`

Live implementation status.

Update after meaningful milestones.

Do not treat documentation as proof that code exists. Verify the actual repository.

---

## 9. Historical Documentation

`docs/archive/` contains historical project material.

It may contain older designs, including the previous form-based V1/base-level specification.

Use it for historical context only.

Never let archived documentation override current decisions.

---

## 10. LLM and Decision Logic

The LLM may:

- understand natural language
- extract structured information
- ask clarification questions
- explain verified results
- discuss evidence

The LLM must not independently invent or override Pathfinder's core career verdict.

The decision system remains responsible for the actual evaluation.

---

## 11. Market Data

The intended pipeline is:

Source
→ Collection / Scraping
→ Raw Data
→ ETL
→ Database
→ Analytics / ML
→ Decision System

Keep data collection separate from decision logic.

Decision engines should depend on normalized data rather than one specific source.

---

## 12. Default Development Workflow

For each implementation task:

1. Understand the exact task.
2. Inspect relevant files.
3. Give a short implementation plan if the task is non-trivial.
4. Implement.
5. Test.
6. Update `CURRENT_STATE.md` if the project state materially changed.
7. Report the result briefly.

Do not modify files merely because an improvement is noticed.

---

## 13. When Requirements Are Ambiguous

For small implementation details, use the existing architecture and conventions.

For major architectural or product decisions, ask before changing them.

Never silently choose a new architecture when a frozen decision already exists.