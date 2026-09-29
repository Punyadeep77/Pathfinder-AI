
---

# 3. `docs/DECISIONS.md`

This one is the **most important** for preventing Codex from going backwards.

```markdown
# Pathfinder AI — Frozen Decisions

This file contains current project decisions.

These decisions are authoritative unless explicitly changed by the project owner.

Historical documentation may describe older approaches. Historical descriptions do not override this file.

---

# 1. Product Identity

**Status: FROZEN**

Pathfinder AI is an:

> Evidence-Driven Career Decision-Intelligence Platform.

It is not being redesigned as:

- a generic chatbot
- a career quiz
- a generic roadmap generator
- a simple skill-gap calculator

---

# 2. UX: Natural-Language-First

**Status: FROZEN**

Pathfinder is **natural-language-first**.

The user describes their situation naturally.

The system understands the input, extracts structured information, identifies missing information, and asks only necessary clarification questions.

Pathfinder must NOT be redesigned into a long form-based career questionnaire.

Older documentation that describes a large Streamlit form is historical/superseded.

A structured form may exist for specific internal/admin/debugging purposes if explicitly required, but it is not the primary user experience.

---

# 3. Discover Before Recommend

**Status: FROZEN**

The system should not require the user to select a target career before Pathfinder evaluates them.

The user's situation should be understood first.

Career directions should then be evaluated against that situation.

---

# 4. Evidence Before Recommendation

**Status: FROZEN**

Recommendations must have traceable reasons.

The system should expose relevant evidence instead of producing unsupported conclusions.

---

# 5. Negative Preferences

**Status: FROZEN**

Negative preferences are meaningful constraints.

If a user explicitly says they do not want something fundamental to a career, that information must materially affect evaluation.

Examples:

- no sales
- no heavy networking
- no frequent travel
- no night shifts
- no heavy coding
- no client-facing work

A fundamental conflict should not simply become a small score penalty.

---

# 6. Reality Over Motivation

**Status: FROZEN**

If the user's target is unrealistic under their current:

- skills
- timeline
- available learning capacity
- experience
- constraints

Pathfinder should say so and explain why.

The system should not produce motivational recommendations that ignore feasibility.

---

# 7. Primary Recommendations vs Exploration

**Status: FROZEN**

Pathfinder should distinguish:

1. primary recommendations produced by the decision system
2. additional options the user can explore

The "Explore More Options" capability must not be confused with the primary verdict.

---

# 8. Multi-Domain V2

**Status: FROZEN**

Version 2 is multi-domain.

It is not restricted to IT/software careers.

The underlying architecture should therefore remain domain-neutral.

The initial implementation/data may contain technology-heavy data where appropriate, but the schema and engines should not assume that every career is an IT role.

---

# 9. V2 Scope

**Status: FROZEN**

V2 is the complete local-first college project.

V2 should provide:

- natural-language user interaction
- user-type detection
- profile/context extraction
- targeted clarification
- career evaluation
- evidence
- market-data pipeline
- ETL
- database
- useful analytics/ML where justified
- personalized dashboard
- Explore More Options
- LLM-based explanation/discussion

V2 does not need production/business infrastructure.

---

# 10. V3 Scope

**Status: FROZEN**

V3 is future production/business/industry scope.

Do not implement V3 infrastructure during V2 unless explicitly requested.

Potential V3 concerns include:

- production scale
- commercial product requirements
- large-scale infrastructure
- continuous data pipelines
- advanced ML
- authentication
- scalability
- business operations

---

# 11. LLM Role

**Status: FROZEN**

The LLM is not the final career decision-maker.

It may:

- understand natural language
- extract information
- ask clarification questions
- explain Pathfinder's results
- discuss evidence
- answer follow-up questions using verified Pathfinder information

The core career evaluation must remain controlled by Pathfinder's structured decision system.

---

# 12. ML Role

**Status: FROZEN**

ML is supportive.

Do not add ML just to label the project "AI."

Use ML when there is a meaningful analytical/predictive problem and enough data to justify it.

The core decision logic should remain explainable.

---

# 13. Market Data

**Status: FROZEN**

Market data is a supply-chain problem.

The conceptual pipeline is:

```text
Source
→ Collection / Scraping
→ Raw Data
→ ETL
→ Database
→ Analytics / ML
→ Decision System