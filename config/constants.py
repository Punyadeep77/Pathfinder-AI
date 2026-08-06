APP_NAME = "Pathfinder AI"

VERSION = "1.0"

VERDICTS = [
    "Highly Recommended",
    "Recommended",
    "Neutral",
    "High Risk",
    "Not Recommended Currently"
]

# ==========================
# DATASET SCHEMA
# ==========================

REQUIRED_ROLE_COLUMNS = [
    "role_id",
    "role_name",
    "industry",
    "domain",
    "role_description",
    "entry_level",
    "minimum_experience_years",
    "average_salary_lpa",
    "market_demand_score",
    "competition_score",
    "growth_score",
    "automation_risk_score",
    "preparation_months",
    "coding_intensity",
    "mathematics_intensity",
    "communication_intensity",
    "work_life_balance",
    "work_mode",
    "travel_required",
    "client_interaction",
    "leadership_required",
    "networking_required",
    "shift_type",
    "remote_opportunity",
    "required_skills",
    "preferred_skills",
    "recommended_certifications",
    "portfolio_required",
    "future_growth_roles",
    "role_characteristics"
]

NUMERIC_COLUMNS = [
    "role_id",
    "minimum_experience_years",
    "average_salary_lpa",
    "market_demand_score",
    "competition_score",
    "growth_score",
    "automation_risk_score",
    "preparation_months",
    "coding_intensity",
    "mathematics_intensity",
    "communication_intensity",
    "work_life_balance"
]

LIST_COLUMNS = [
    "required_skills",
    "preferred_skills",
    "recommended_certifications",
    "future_growth_roles",
    "role_characteristics"
]

TEXT_COLUMNS = [
    "role_name",
    "industry",
    "domain",
    "role_description",
    "entry_level",
    "work_mode",
    "travel_required",
    "client_interaction",
    "leadership_required",
    "networking_required",
    "shift_type",
    "remote_opportunity",
    "portfolio_required"
]

# ==========================
# VALID VALUES
# ==========================

YES_NO_VALUES = {
    "Yes",
    "No"
}

SKILL_LEVELS = {
    "Beginner",
    "Intermediate",
    "Advanced",
    "Expert"
}

# ==========================
# SCORE LIMITS
# ==========================

MIN_SCORE = 0
MAX_SCORE = 100