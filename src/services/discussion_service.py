class EvidenceDiscussionService:
    """Answers follow-up questions using verified verdict evidence only.

    It deliberately cannot create or override career verdicts. An external LLM
    can be added later as a presentation layer over the same evidence.
    """

    def answer(self, question: str, verdict) -> str:
        lowered = question.lower()
        if any(word in lowered for word in ("why", "reason", "recommend")):
            return " ".join(verdict.reasons)
        if any(word in lowered for word in ("skill", "learn", "gap")):
            return "Missing skills: " + (
                ", ".join(verdict.missing_skills) or "none identified"
            ) + "."
        if any(word in lowered for word in ("risk", "constraint", "avoid")):
            return "Risks: " + (
                "; ".join(verdict.risks) or "none identified"
            ) + "."
        if any(word in lowered for word in ("time", "timeline", "month")):
            return (
                f"Timeline match: {verdict.timeline_match_score}%; "
                f"gap: {verdict.timeline_gap_months} month(s)."
            )
        return f"{verdict.role_name}: {verdict.verdict}. " + " ".join(verdict.reasons)
