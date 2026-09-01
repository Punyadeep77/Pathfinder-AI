from src.engines.identity.identity_engine import IdentityEngine
from src.context.clarification import ClarificationGenerator
from config.logging_config import get_logger

from src.context.user_context import UserContext
from src.context.constraint_policy import ConstraintPolicy
from src.context.extractor import ContextExtractor


logger = get_logger(__name__)


class ContextEngine:
    """
    Coordinates natural-language extraction and
    constraint resolution.

    Flow:

    User text
        ↓
    ContextExtractor
        ↓
    UserContext
        ↓
    Constraint validation
    """

    def __init__(self):
        self.identity_engine = IdentityEngine()
        self.clarification_generator = ClarificationGenerator()
        self.extractor = ContextExtractor()
        self.constraint_policy = ConstraintPolicy()

    def understand(self, text: str) -> UserContext:
        """
        Converts natural-language user input into
        structured UserContext.
        """

        extracted_information = self.extractor.extract(text)

        user_type = extracted_information.get(
            "user_type",
            "unknown"
        )

        situation = extracted_information.get(
            "situation",
            ""
        )

        goal = extracted_information.get(
            "goal",
            ""
        )

        return self.build_context(
            extracted_information=extracted_information,
            situation=situation,
            goal=goal,
        )

    def detect_user_type(
        self,
        extracted_information: dict
    ) -> str:

        user_type = extracted_information.get("user_type")

        if user_type:
            return user_type

        return "unknown"

    def build_context(
        self,
        extracted_information: dict,
        situation: str = "",
        goal: str = "",
    ) -> UserContext:

        user_type = self.detect_user_type(
            extracted_information
        )

        applicable_constraints = (
            self.constraint_policy.get_applicable_constraints(
                user_type
            )
        )

        required_constraints = (
            self.constraint_policy.get_required_constraints(
                user_type,
                goal
            )
        )

        missing_required_constraints = []

        for constraint in required_constraints:

            value = extracted_information.get(
                constraint
            )

            if value is None or value == "":
                missing_required_constraints.append(
                    constraint
                )

        context = UserContext(
            user_type=user_type,
            situation=situation,
            goal=goal,
            extracted_information=extracted_information,
            applicable_constraints={
                constraint: extracted_information.get(
                    constraint
                )
                for constraint in applicable_constraints
                if extracted_information.get(
                    constraint
                ) is not None
            },
            missing_required_constraints=(
                missing_required_constraints
            ),
            confidence=extracted_information.get(
                "confidence",
                0.0
            ),
        )

        logger.info(
            f"User context built. "
            f"Type: {user_type}"
        )

        if context.has_missing_constraints():

            logger.info(
                "Missing required constraints: "
                f"{context.missing_required_constraints}"
            )

        else:

            logger.info(
                "All required constraints available."
            )

        return context

    def build_identity(self, context: UserContext):
        """
        Converts a resolved UserContext into the existing
        CareerIdentity used by Pathfinder's decision engines.
        """

        if context.has_missing_constraints():
            raise ValueError(
                "Cannot build CareerIdentity. "
                f"Missing: {context.missing_required_constraints}"
            )

        data = context.extracted_information

        profile = {
            "name": data.get("name") or "User",
            "education": data.get("education") or "NA",
            "branch": data.get("branch") or "NA",
            "current_year": data.get("current_year") or "NA",
            "cgpa": data.get("cgpa") or 0.0,
            "experience_years": (
                data.get("experience_years")
                if data.get("experience_years") is not None
                else 0.0
            ),
            "timeline_months": (
                data.get("timeline_months")
                if data.get("timeline_months") is not None
                else 0
            ),
            "learning_hours_week": (
                data.get("learning_hours_week")
                if data.get("learning_hours_week") is not None
                else 0
            ),
            "skills": data.get("skills") or {},
            "positive_preferences": (
                data.get("positive_preferences") or []
            ),
            "negative_preferences": (
                data.get("negative_preferences") or []
            ),
            "career_interests": (
                data.get("career_interests") or []
            ),
        }

        return self.identity_engine.build_identity(profile)

    def resolve_missing_constraints(
        self,
        context: UserContext,
        additional_information: dict,
    ) -> UserContext:

        context.extracted_information.update(
            additional_information
        )

        return self.build_context(
            extracted_information=(
                context.extracted_information
            ),
            situation=context.situation,
            goal=context.goal,
        )

    def get_clarification(self, context: UserContext) -> str | None:
        """
        Returns the next minimal clarification question,
        or None when the context is ready.
        """

        return self.clarification_generator.generate(
            context.missing_required_constraints
        )