from src.models.career_role import CareerRole

def test_career_role():
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
        travel_required="No",
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
    print(role)
    print(role.total_required_skills())
    print(role.requires_skill("Python"))
    print(role.total_preferred_skills())

if __name__ == "__main__":
    test_career_role()