from src.engines.verdict.verdict_engine import VerdictEngine
from src.engines.reality.reality_engine import RealityEngine
from src.models.career_identity import CareerIdentity
from src.models.career_role import CareerRole

def test_verdict_engine():

    user = CareerIdentity(
        name="Punyadeep",
        education="B.Tech",
        branch="Data Science",
        current_year="3rd Year",
        cgpa=7.92,
        experience_years=0,
        
        skills={
            "Python":"Intermediate",
            "SQL":"Beginner",
            "Pandas":"Intermediate"
        },
        
        timeline_months=8,
        learning_hours_week=20,
        positive_preferences=[
            "Analytics",
            "AI"
        ],
        
        negative_preferences=[
            "DevOps",
            "Networking"
        ],
        
        career_interests=[
            "Data Science",
            "Machine Learning"
        ]
    )

    role = CareerRole(
        role_id=1,
        role_name="Data Analyst",
        industry="IT",
        domain="Analytics",
        role_description="Analyze business data",
        entry_level="Yes",
        minimum_experience_years=0,
        average_salary_lpa=6.5,
        market_demand_score=88,
        competition_score=75,
        growth_score=90,
        automation_risk_score=25,
        preparation_months=6,
        coding_intensity=3,
        mathematics_intensity=3,
        communication_intensity=4,
        work_life_balance=4,
        remote_opportunity="High",
        work_mode="Hybrid",
        travel_required="Low",
        client_interaction="Medium",
        leadership_required="No",
        networking_required="Low",
        shift_type="Day",

        role_characteristics=[
            "Analytical Thinking",
            "Office Work",
            "Low Travel"
        ],

        required_skills=[
            "Python",
            "SQL",
            "Pandas"
        ],

        preferred_skills=[
            "Power BI",
            "Statistics"
        ],

        recommended_certifications=[
            "Google Data Analytics"
        ],

        portfolio_required="Yes",

        future_growth_roles=[
            "Senior Data Analyst",
            "Analytics Engineer"
        ]

    )

    reality = RealityEngine()

    evidence = reality.evaluate(user, role)

    engine = VerdictEngine()

    verdict = engine.generate_verdict(
        role.role_name,
        evidence
    )

    print(verdict)


if __name__ == "__main__":
    test_verdict_engine()