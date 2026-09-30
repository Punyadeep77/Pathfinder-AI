from dataclasses import dataclass, field
from typing import Dict, List

"""
Represents a user's complete career profile.

This object is created by the Identity Engine and consumed by the
Reality Engine and Career Verdict Engine.
"""

@dataclass
class CareerIdentity:
    
    # Basic Information
    name: str
    education: str
    branch: str
    current_year: str
    cgpa: float

    # Experience
    experience_years: float

    # Learning Constraints
    timeline_months: int
    learning_hours_week: int

    # Skills
    skills: Dict[str, str] = field(default_factory=dict)

    # Preferences
    positive_preferences: List[str] = field(default_factory=list)
    negative_preferences: List[str] = field(default_factory=list)
    career_interests: List[str] = field(default_factory=list)

    def total_skills(self) -> int:
        return len(self.skills)

    def has_skill(self, skill_name: str) -> bool:
        return skill_name in self.skills

    def get_skill_level(self, skill_name: str) -> str | None:
        return self.skills.get(skill_name)

    def experience_gap_years(self, role) -> float:
        return max(0.0, role.minimum_experience_years - self.experience_years)