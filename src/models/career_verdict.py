from dataclasses import dataclass, field
from typing import List

@dataclass
class CareerVerdict:
    """
    Represents the evidence produced after evaluating
    a CareerIdentity against a CareerRole.
    """
    
    role_name: str
    skill_match: float
    missing_skills: List[str] = field(default_factory=list)
    timeline_feasible: bool = False
    experience_match: bool = False
    market_demand_score: int = 0
    competition_score: int = 0
    growth_score: int = 0
    automation_risk_score: int = 0
    average_salary_lpa: float = 0.0
    final_score: float = 0.0
    verdict: str = ""
    strengths: List[str] = field(default_factory=list)
    limitations: List[str] = field(default_factory=list)
    reasons: List[str] = field(default_factory=list)
    risks: List[str] = field(default_factory=list)

    def is_recommended(self) -> bool:
        return self.verdict in ("Highly Recommended","Recommended")
    
    def total_missing_skills(self) -> int:
        return len(self.missing_skills)
    
    def has_risks(self) -> bool:
        return len(self.risks) > 0