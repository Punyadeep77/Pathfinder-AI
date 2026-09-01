from src.models.career_identity import CareerIdentity
from src.models.career_role import CareerRole

class RealityEngine:
    """
    Compares a CareerIdentity with a CareerRole and
    produces evidence-based readiness metrics.
    """

    def calculate_skill_match(self,
    user: CareerIdentity,
    role: CareerRole) -> float:
        required = role.required_skills
        matched = 0
        for skill in required:
            if user.has_skill(skill):
                matched += 1
        if not required:
            return 0.0
        return round(
            (matched / len(required)) * 100,2)
    

    def missing_skills(self,
    user: CareerIdentity,
    role: CareerRole)-> list[str]:
        missing = []
        for skill in role.required_skills:
            if not user.has_skill(skill):
                missing.append(skill)
        return missing
    

    def timeline_gap_months(
    self,
    user: CareerIdentity,
    role: CareerRole) -> int:
        """
        Returns the number of additional months required
        beyond the user's available preparation timeline.
        """

        return max(
            0,
            role.preparation_months - user.timeline_months
        )


    def timeline_match_score(
        self,
        user: CareerIdentity,
        role: CareerRole) -> float:
        """
        Calculates how well the user's available timeline
        matches the role's preparation requirement.

        100 = fully feasible
        Lower values = increasing timeline gap
        """

        required = role.preparation_months
        available = user.timeline_months

        if required <= 0:
            return 100.0

        if available >= required:
            return 100.0

        return round(
            (available / required) * 100,
            2
        )


    def timeline_feasible(
        self,
        user: CareerIdentity,
        role: CareerRole) -> bool:

        return user.timeline_months >= role.preparation_months


    def experience_match(self,
    user: CareerIdentity,
    role: CareerRole) -> bool:
        return (user.experience_years >= role.minimum_experience_years)
    

    def market_demand(self, role: CareerRole) -> int:
        return role.market_demand_score
    

    def competition_level(self, role: CareerRole) -> int:
        return role.competition_score
    

    def growth_potential(self, role: CareerRole) -> int:
        return role.growth_score
    

    def automation_risk(self, role: CareerRole) -> int:
        return role.automation_risk_score


    def salary_range(self, role: CareerRole) -> float:
        return role.average_salary_lpa


    def portfolio_required(self, role: CareerRole) -> str:
        return role.portfolio_required

    def career_interest_match(self, user: CareerIdentity, role: CareerRole) -> float:
        """
        Measures how strongly the user's stated career
        interests align with the role.

        Returns:
            100.0 = direct role/domain match
            50.0  = related domain match
            0.0   = no detected interest match
        """

        if not user.career_interests:
            return 0.0

        interests = [
            str(interest).strip().lower()
            for interest in user.career_interests
            if interest
        ]

        role_name = role.role_name.lower()
        domain = role.domain.lower()

        # Direct role match
        for interest in interests:
            if interest == role_name:
                return 100.0

        # Domain match
        for interest in interests:
            if interest == domain:
                return 100.0

        # Partial relationship
        for interest in interests:
            if interest in role_name or interest in domain:
                return 50.0

        return 0.0

    def negative_preference_conflict(self,
    user: CareerIdentity,
    role: CareerRole) -> bool:
        for preference in user.negative_preferences:
            if role.has_characteristic(preference):
                return True
        return False


    def evaluate(self,
    user: CareerIdentity,
    role: CareerRole) -> dict:        
       
        skill_match = self.calculate_skill_match(user,role)
        missing = self.missing_skills(user,role)
        timeline = self.timeline_feasible(user,role)
        timeline_gap = self.timeline_gap_months(user, role)
        timeline_score = self.timeline_match_score(user, role)
        experience = self.experience_match(user,role)
        market_demand = self.market_demand(role)
        competition = self.competition_level(role)
        growth = self.growth_potential(role)
        automation = self.automation_risk(role)
        salary = self.salary_range(role)
        portfolio = self.portfolio_required(role)
        interest_match = self.career_interest_match(user,role)
        negative_conflict = self.negative_preference_conflict(user, role)

        return {
            "skill_match": skill_match,
            "missing_skills": missing,
            "timeline_feasible": timeline,
            "timeline_gap_months": timeline_gap,
            "timeline_match_score": timeline_score,
            "experience_match": experience,
            "market_demand_score": market_demand,
            "competition_score": competition,
            "growth_score": growth,
            "automation_risk_score": automation,
            "average_salary_lpa": salary,
            "portfolio_required": portfolio,
            "career_interest_match": interest_match,
            "negative_preference_conflict": negative_conflict
        }
            

