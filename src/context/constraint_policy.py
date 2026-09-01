from typing import Dict, List


class ConstraintPolicy:
    """
    Determines which constraints are relevant and required
    for a user based on their type, situation, and goal.
    """

    USER_TYPES = {
        "student",
        "fresher",
        "working_professional",
        "career_switcher",
        "job_seeker",
        "experienced_professional",
        "unknown",
    }

    COMMON_CONSTRAINTS = [
        "education",
        "skills",
        "career_interests",
        "positive_preferences",
        "negative_preferences",
        "timeline_months",
        "learning_hours_week",
    ]

    TYPE_SPECIFIC_CONSTRAINTS: Dict[str, List[str]] = {
        "student": [
            "education",
            "branch",
            "current_year",
            "skills",
            "timeline_months",
        ],
        "fresher": [
            "education",
            "branch",
            "skills",
            "timeline_months",
        ],
        "working_professional": [
            "education",
            "skills",
            "experience_years",
            "career_interests",
            "timeline_months",
        ],
        "career_switcher": [
            "education",
            "skills",
            "experience_years",
            "career_interests",
            "timeline_months",
        ],
        "job_seeker": [
            "education",
            "skills",
            "experience_years",
            "career_interests",
        ],
        "experienced_professional": [
            "education",
            "skills",
            "experience_years",
            "career_interests",
        ],
        "unknown": [
            "education",
            "skills",
            "career_interests",
        ],
    }

    def get_applicable_constraints(
        self,
        user_type: str
    ) -> List[str]:
        """
        Returns constraints relevant to the detected user type.
        """

        if user_type not in self.USER_TYPES:
            user_type = "unknown"

        return self.TYPE_SPECIFIC_CONSTRAINTS[user_type]

    def get_required_constraints(
        self,
        user_type: str,
        goal: str = ""
    ) -> List[str]:
        """
        Returns the minimum constraints required before
        generating a recommendation.
        """

        return self.get_applicable_constraints(user_type)

    def get_optional_constraints(
        self,
        user_type: str
    ) -> List[str]:
        """
        Returns constraints that can improve recommendations
        but are not mandatory.
        """

        applicable = self.get_applicable_constraints(user_type)

        return [
            constraint
            for constraint in self.COMMON_CONSTRAINTS
            if constraint not in applicable
        ]