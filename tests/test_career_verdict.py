from src.models.career_verdict import CareerVerdict

def test_career_verdict():
    verdict = CareerVerdict(
        role_name="Data Analyst",
        skill_match=85.0,
        missing_skills=[
            "Power BI"
        ],
        timeline_feasible=True,
        experience_match=True,
        market_demand_score=88,
        competition_score=72,
        growth_score=90,
        automation_risk_score=20,
        average_salary_lpa=7.5,
        verdict="Recommended",

        strengths=[
            "Strong Python",
            "Strong SQL"
        ],

        limitations=[
            "Power BI Missing"
        ],

        reasons=[
            "Good technical readiness",
            "Timeline is achievable"
        ],

        risks=[
            "Competition is moderately high"
        ]

    )
    print(verdict)

if __name__ == "__main__":
    test_career_verdict()