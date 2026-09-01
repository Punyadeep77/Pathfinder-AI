from config.logging_config import get_logger


logger = get_logger(__name__)


class ClarificationGenerator:
    """
    Generates minimal clarification questions for
    missing essential user information.
    """

    QUESTIONS = {
        "name": "What should I call you?",
        "education": "What is your current or highest education qualification?",
        "branch": "What is your branch or specialization?",
        "current_year": "Which year of study are you currently in?",
        "skills": "What skills do you currently have?",
        "experience_years": "How many years of professional experience do you have?",
        "timeline_months": "Roughly how many months do you have to prepare?",
        "learning_hours_week": "How many hours per week can you realistically spend preparing?",
        "career_interests": "Which career areas are you currently interested in?",
    }

    def generate(
        self,
        missing_constraints: list[str]
    ) -> str | None:

        if not missing_constraints:
            return None

        constraint = missing_constraints[0]

        question = self.QUESTIONS.get(
            constraint,
            f"Please provide your {constraint.replace('_', ' ')}."
        )

        logger.info(
            f"Clarification required for: {constraint}"
        )

        return question