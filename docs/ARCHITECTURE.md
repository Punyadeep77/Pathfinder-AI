
---

# 3. `docs/ARCHITECTURE.md`

Your current architecture file is **too short** for Codex. Replace the whole file with:

```markdown
# Pathfinder AI — Architecture

## 1. Architecture Principle

Pathfinder is a decision-intelligence system.

It separates:

1. user understanding
2. profile construction
3. market intelligence
4. career evaluation
5. evidence generation
6. presentation
7. natural-language explanation

The LLM is not the core decision engine.

---

## 2. Primary Product Flow

```text
                    USER
                     │
                     ▼
          Natural-Language Situation
                     │
                     ▼
             Input Understanding
                     │
                     ▼
            User-Type Detection
                     │
                     ▼
       Profile / Constraint Extraction
                     │
                     ▼
          Missing Information Check
                     │
              ┌──────┴──────┐
              │             │
           Missing        Complete
              │             │
              ▼             │
     Targeted Clarification │
              │             │
              └──────┬──────┘
                     ▼
              Career Identity
                     │
                     ▼
              Market Reality
                     │
                     ▼
          Career Evaluation / Verdict
                     │
                     ▼
              Evidence Layer
                     │
                     ▼
          Personalized Dashboard
                     │
              ┌──────┴──────┐
              │             │
              ▼             ▼
     Primary Results   Explore More
                            Options
                              │
                              ▼
                       LLM Discussion