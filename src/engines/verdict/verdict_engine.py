from src.models.career_verdict import CareerVerdict

class VerdictEngine:
    """
    Converts evidence from the Reality Engine
    into an explainable career verdict.
    """
    
    def generate_verdict(self,
    role_name: str,
    evidence: dict) -> CareerVerdict:
        skill_match = evidence["skill_match"]
        missing_skills = evidence["missing_skills"]
        timeline_feasible = evidence["timeline_feasible"]
        experience_match = evidence["experience_match"]
        market_demand_score = evidence["market_demand_score"]
        competition_score = evidence["competition_score"]
        growth_score = evidence["growth_score"]
        automation_risk_score = evidence["automation_risk_score"]
        average_salary_lpa = evidence["average_salary_lpa"]
        portfolio_required = evidence["portfolio_required"]
        negative_preference_conflict = evidence["negative_preference_conflict"]

        strengths = []
        limitations = []
        reasons = []
        risks = []

        if skill_match >= 80:
            strengths.append("Strong technical skill match.")

        if timeline_feasible:
            strengths.append("Preparation timeline is realistic.")

        if experience_match:
            strengths.append("Experience requirement satisfied.")

        if market_demand_score >= 70:
            strengths.append("High market demand.")

        if growth_score >= 70:
            strengths.append("Strong future growth potential.")

        
        if missing_skills:
            limitations.append(
                f"Missing Skills: {', '.join(missing_skills)}")

        # if portfolio_required == "Yes":
        #     limitations.append("Portfolio required.")

        if not experience_match:
            limitations.append("Experience requirement not satisfied.")

        
        if automation_risk_score >= 70:
            risks.append("High automation risk.")

        if competition_score >= 80:
            risks.append("Very high competition.")

        if not timeline_feasible:
            risks.append("Current timeline is not realistic.")

        if negative_preference_conflict:
            risks.append("Conflicts with your negative preferences.")

        
        reasons.append(
            f"Technical skill match is {skill_match}%.")

        reasons.append(
            f"Market demand is {market_demand_score}/100.")

        reasons.append(
            f"Growth potential is {growth_score}/100.")
        
        
        if negative_preference_conflict:
            verdict = "Not Recommended Currently"

        elif not timeline_feasible:
            verdict = "High Risk"

        elif skill_match >= 80 and experience_match:
            verdict = "Highly Recommended"

        elif skill_match >= 60:
            verdict = "Recommended"

        elif skill_match >= 40:
            verdict = "Neutral"

        else:
            verdict = "Not Recommended Currently"
        

        return CareerVerdict(
            role_name=role_name,
            skill_match=skill_match,
            missing_skills=missing_skills,
            timeline_feasible=timeline_feasible,
            experience_match=experience_match,
            market_demand_score=market_demand_score,
            competition_score=competition_score,
            growth_score=growth_score,
            automation_risk_score=automation_risk_score,
            average_salary_lpa=average_salary_lpa,
            verdict=verdict,
            strengths=strengths,
            limitations=limitations,
            reasons=reasons,
            risks=risks
        )