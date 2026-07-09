from dataclasses import dataclass
from typing import List

@dataclass
class CareerRole:
    """
    Represents one career available in Pathfinder.
    """

    role_id: int
    role_name: str
    industry: str
    domain: str
    role_description: str
    entry_level: str
    minimum_experience_years: float
    average_salary_lpa: float
    market_demand_score: int
    competition_score: int
    growth_score: int
    automation_risk_score: int
    preparation_months: int
    coding_intensity: int
    mathematics_intensity: int
    communication_intensity: int
    work_life_balance: int
    work_mode: str
    travel_required: str
    client_interaction: str
    leadership_required: str
    networking_required: str
    shift_type: str
    remote_opportunity: str
    required_skills: List[str]
    preferred_skills: List[str]
    recommended_certifications: List[str]
    portfolio_required: str
    future_growth_roles: List[str]
    role_characteristics: List[str]

    def total_required_skills(self) -> int:
        return len(self.required_skills)
    
    def requires_skill(self, skill_name: str) -> bool:
        return skill_name in self.required_skills
    
    def total_preferred_skills(self) -> int:
        return len(self.preferred_skills)
    
    def has_characteristic(self, characteristic: str) -> bool:
        return characteristic in self.role_characteristics