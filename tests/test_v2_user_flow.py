from src.context.context_engine import ContextEngine
from src.engines.reality.reality_engine import RealityEngine
from src.models.career_identity import CareerIdentity
from src.models.career_role import CareerRole
from src.services.recommendation_service import RecommendationService


def role(**overrides):
    values = {
        "role_id": 1,
        "role_name": "Network Engineer",
        "industry": "Information Technology",
        "domain": "Networking",
        "role_description": "Builds and maintains networks.",
        "entry_level": "Yes",
        "minimum_experience_years": 0,
        "average_salary_lpa": 6.8,
        "market_demand_score": 70,
        "competition_score": 65,
        "growth_score": 68,
        "automation_risk_score": 40,
        "preparation_months": 6,
        "coding_intensity": 1,
        "mathematics_intensity": 1,
        "communication_intensity": 3,
        "work_life_balance": 4,
        "work_mode": "Office",
        "travel_required": "Medium",
        "client_interaction": "Low",
        "leadership_required": "No",
        "networking_required": "Medium",
        "shift_type": "Day",
        "remote_opportunity": "Low",
        "required_skills": ["Networking"],
        "preferred_skills": [],
        "recommended_certifications": [],
        "portfolio_required": "No",
        "future_growth_roles": [],
        "role_characteristics": ["Networking"],
    }
    values.update(overrides)
    return CareerRole(**values)


def identity(**overrides):
    values = {
        "name": "User", "education": "BTech", "branch": "CSE",
        "current_year": "3rd Year", "cgpa": 8.0, "experience_years": 0,
        "timeline_months": 8, "learning_hours_week": 20,
        "skills": {"Networking": "Intermediate"},
        "positive_preferences": [], "negative_preferences": [],
        "career_interests": ["Networking"],
    }
    values.update(overrides)
    return CareerIdentity(**values)


def test_networking_constraint_is_a_fundamental_conflict():
    evidence = RealityEngine().evaluate(
        identity(negative_preferences=["no_networking"]), role()
    )
    assert evidence["negative_preference_conflict"] is True
    assert evidence["negative_preference_conflicts"] == ["Requires meaningful networking"]


def test_clarification_values_are_converted_to_model_types():
    engine = ContextEngine()
    context = engine.understand(
        "I have a BTech and Python. I want to switch career to Data Analyst in 8 months."
    )
    resolved = engine.resolve_missing_constraints(context, {"experience_years": "2"})
    assert resolved.extracted_information["experience_years"] == 2.0


def test_final_year_mechanical_profile_uses_longest_placement_runway():
    context = ContextEngine().understand(
        "I am a BTech Mechanical student in VII semester. I have 1 month for "
        "campus placement and 6-7 months off campus. I have a TCS Ninja offer "
        "of 3.46 LPA."
    )
    assert context.extracted_information["branch"] == "Mechanical"
    assert context.extracted_information["current_year"] == "Final Year"
    assert context.extracted_information["timeline_months"] == 7
    assert context.extracted_information["existing_offer_lpa"] == 3.46
    assert "Mechanical Engineering" in context.extracted_information["career_interests"]


def test_primary_and_exploration_are_separate():
    service = RecommendationService()
    approved = service.evaluate_role(identity(), role(role_name="Approved Role"))
    approved.verdict = "Recommended"
    rejected = service.evaluate_role(
        identity(negative_preferences=["no_networking"]), role()
    )
    primary, exploration = service.split_primary_and_exploration([approved, rejected])
    assert primary == [approved]
    assert exploration == [rejected]
