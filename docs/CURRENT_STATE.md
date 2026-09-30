# Pathfinder AI — Current State

> This file records the current implementation state. Source code remains the
> authority for runtime behavior.

Last updated: October 2026.

## Implemented V2 flow

- Natural-language-first Streamlit dashboard.
- Rule-based extraction of profile, skills, career interests, and meaningful
  negative preferences.
- User-type detection and one-at-a-time targeted clarification.
- Type-safe conversion of clarification answers before decision evaluation.
- SQLite-backed evaluation of the current seed career dataset.
- Explainable verdict evidence: skills, interest alignment, timeline,
  experience gap, market demand, growth, salary, limitations, and risks.
- Fundamental conflicts such as meaningful networking, client-facing work,
  travel, non-day shifts, and heavy coding are excluded from primary
  recommendations.
- Separate Primary Recommendations, Explore More Options, and evidence-only
  follow-up discussion views.

## Data and decision scope

The repository currently contains 29 seed roles and a 101-skill taxonomy. It
now includes five entry-level mechanical/manufacturing roles alongside the
technology roles. Broader multi-domain coverage remains future work.

The current discussion feature is local and evidence-only. It preserves the
frozen decision that an LLM must not make or override career verdicts. An LLM
provider integration remains future work.

## Verification

`python -m pytest -q` passes 9 tests, including natural-language constraint,
clarification type-conversion, and primary-versus-exploration regression tests.
