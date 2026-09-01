import ast
from config.logging_config import get_logger

from src.exceptions.recommendation_exceptions import (
    RecommendationError,
)
from src.engines.reality.reality_engine import RealityEngine
from src.engines.verdict.verdict_engine import VerdictEngine

from src.models.career_identity import CareerIdentity
from src.models.career_role import CareerRole

from src.database.models import get_all_roles

logger = get_logger(__name__)

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
            verdict = self.evaluate_role(user, role)
            verdict.final_score = self.calculate_final_score(verdict)
            results.append(verdict)

        results.sort(key=lambda verdict: verdict.final_score,reverse=True)
        
        return results
    
    def calculate_final_score(self, verdict):
        score = 0.0

        # Skill Match (35%)
        score += verdict.skill_match * 0.35

        # Career Interest Alignment (15%)
        score += verdict.career_interest_match * 0.15

        # Market Demand (15%)
        score += verdict.market_demand_score * 0.15

        # Growth (10%)
        score += verdict.growth_score * 0.10

        # Timeline Match (10%)
        score += verdict.timeline_match_score * 0.10

        # Experience (5%)
        if verdict.experience_match:
            score += 5

        # Competition (5%)
        score += (100 - verdict.competition_score) * 0.05

        # Automation Risk (5%)
        score += (100 - verdict.automation_risk_score) * 0.05

        return round(score, 2)

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
            required_skills=(row["required_skills"] or "").split("|"),
            preferred_skills=(row["preferred_skills"] or "").split("|"),
            recommended_certifications=(row["recommended_certifications"] or "").split("|"),
            portfolio_required=row["portfolio_required"],
            future_growth_roles=(row["future_growth_roles"] or "").split("|"),
            role_characteristics=(ast.literal_eval(row["role_characteristics"])
                if row["role_characteristics"].strip().startswith("[")
                else row["role_characteristics"].split("|")),
        )
    
    def load_roles(self):
        rows = get_all_roles()
        roles = []

        for row in rows:
            roles.append(self.build_role(row))

        return roles
    
    def recommend(self, user: CareerIdentity):
        """
        Generates ranked career recommendations.
        """

        logger.info("Generating career recommendations...")

        try:
            roles = self.load_roles()
            recommendations = self.evaluate_all_roles(user, roles)

            logger.info(
                f"Generated {len(recommendations)} career recommendations."
            )

            return recommendations

        except Exception as e:
            logger.exception("Recommendation generation failed.")
            raise RecommendationError(str(e)) from e