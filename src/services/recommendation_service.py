from src.engines.reality.reality_engine import RealityEngine
from src.engines.verdict.verdict_engine import VerdictEngine

from src.models.career_identity import CareerIdentity
from src.models.career_role import CareerRole

from src.database.models import get_all_roles

class RecommendationService:
    """
    Coordinates the Reality Engine and Verdict Engine
    to evaluate multiple careers and return ranked results.
    """
    def __init__(self):
        self.reality_engine = RealityEngine()
        self.verdict_engine = VerdictEngine()

    def evaluate_role(self,
    user: CareerIdentity,
    role: CareerRole):
        
        evidence = self.reality_engine.evaluate(user,role)
        verdict = self.verdict_engine.generate_verdict(role.role_name,evidence)

        return verdict
    
    def evaluate_all_roles(self,
    user: CareerIdentity,
    roles: list[CareerRole]):
        results = []
        for role in roles:
            verdict = self.evaluate_role(user,role)
            results.append(verdict)

        results.sort(key=lambda verdict: verdict.skill_match,reverse=True)
        return results
    
    def build_role(self, row):
        return CareerRole(
            role_id=row["role_id"],
            role_name=row["role_name"],
            industry=row["industry"],
            domain=row["domain"],
            role_description=row["role_description"],
            entry_level=row["entry_level"],
            minimum_experience_years=row["minimum_experience_years"],
            average_salary_lpa=row["average_salary_lpa"],
            market_demand_score=row["market_demand_score"],
            competition_score=row["competition_score"],
            growth_score=row["growth_score"],
            automation_risk_score=row["automation_risk_score"],
            preparation_months=row["preparation_months"],
            coding_intensity=row["coding_intensity"],
            mathematics_intensity=row["mathematics_intensity"],
            communication_intensity=row["communication_intensity"],
            work_life_balance=row["work_life_balance"],
            work_mode=row["work_mode"],
            travel_required=row["travel_required"],
            client_interaction=row["client_interaction"],
            leadership_required=row["leadership_required"],
            networking_required=row["networking_required"],
            shift_type=row["shift_type"],
            remote_opportunity=row["remote_opportunity"],
            required_skills=row["required_skills"].split("|"),
            preferred_skills=row["preferred_skills"].split("|"),
            recommended_certifications=row["recommended_certifications"].split("|"),
            portfolio_required=row["portfolio_required"],
            future_growth_roles=row["future_growth_roles"].split("|"),
            role_characteristics=row["role_characteristics"].split("|")
        )
    def load_roles(self):
        rows = get_all_roles()
        roles = []

        for row in rows:
            roles.append(self.build_role(row))

        return roles
    
    def recommend(self, user: CareerIdentity):
        roles = self.load_roles()
        return self.evaluate_all_roles(user, roles)