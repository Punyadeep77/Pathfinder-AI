# Pathfinder AI — Project Context

## 1. Project Identity

Pathfinder AI is an evidence-driven career decision-intelligence platform.

Its purpose is to help a person determine which career directions actually fit their current situation by comparing:

- current skills
- education
- experience
- interests
- goals
- timeline
- available learning capacity
- work preferences
- negative preferences / constraints
- career requirements
- labor-market evidence

Pathfinder is a decision-support system, not merely an AI chatbot, career quiz, roadmap generator, or skill-gap calculator.

The core question is:

> Given a person's actual situation and available evidence, which career directions make sense for them right now?

---

## 2. Core Philosophy

### Discover Before You Learn

The system should not assume that a user's desired career is automatically the correct target.

It should first understand the person's situation and evaluate possible career directions.

### Evidence Before Recommendation

A recommendation must be explainable.

Relevant evidence may include:

- skill compatibility
- missing skills
- experience requirements
- preparation feasibility
- timeline feasibility
- work characteristics
- labor-market information
- user constraints

### Negative Preferences Matter

What a person explicitly does NOT want is important.

Examples:

- no sales
- no heavy networking
- no frequent travel
- no night shifts
- no highly coding-heavy role
- no client-facing work

Important negative preferences can act as constraints rather than merely reducing a score.

### Reality Over Motivation

Pathfinder should not give motivational recommendations that ignore feasibility.

If evidence indicates that a direction is unrealistic under the user's constraints, the system should explain the mismatch and identify realistic alternatives.

---

## 3. Current Product Direction

Pathfinder is natural-language-first.

The user describes their situation naturally instead of completing a long career questionnaire.

Example:

> "I'm a third-year CSE student. I know Python and SQL, I have about six months before placements, I don't want a job involving sales or excessive client interaction, and I'm confused between data analytics, data science and software roles."

Pathfinder should understand this input and extract structured information from it.

It should then ask only the clarification questions that are genuinely necessary.

### Current UX Flow

```text
Natural User Situation
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
Evidence + Recommendations
        ↓
Personalized Dashboard
        ↓
Explore More Options
        ↓
LLM Discussion