from src.models.career_identity import CareerIdentity

class IdentityEngine:
    """
    Builds a CareerIdentity object from raw user input.
    """
    def build_identity(self, profile_data: dict) -> CareerIdentity:
            return CareerIdentity(
            name=profile_data["name"],
            education=profile_data["education"],
            branch=profile_data["branch"],
            current_year=profile_data["current_year"],
            cgpa=profile_data["cgpa"],
            experience_years=profile_data["experience_years"],
            timeline_months=profile_data["timeline_months"],
            learning_hours_week=profile_data["learning_hours_week"],
            skills=profile_data["skills"],
            positive_preferences=profile_data["positive_preferences"],
            negative_preferences=profile_data["negative_preferences"],
            career_interests=profile_data["career_interests"]
        )