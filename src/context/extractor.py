from pathlib import Path
import pandas as pd
import re

from config.logging_config import get_logger

logger = get_logger(__name__)


class ContextExtractor:
    """
    Extracts structured career information from
    natural-language user input.

    This is the initial extraction layer.
    """

    def _extract_skills(self, text, information):
        """
        Extracts skills and attempts to infer proficiency
        from natural-language context.
        """

        base_dir = Path(__file__).resolve().parent.parent.parent

        taxonomy_file = (
            base_dir
            / "data"
            / "seed"
            / "skill_taxonomy.csv"
        )

        if not taxonomy_file.exists():
            logger.warning(
                "Skill taxonomy file not found."
            )
            return

        taxonomy = pd.read_csv(taxonomy_file)

        proficiency_patterns = {
            "Expert": [
                "expert",
                "expertise",
                "highly proficient",
                "advanced expert",
            ],
            "Advanced": [
                "advanced",
                "strong in",
                "very good at",
                "very good in",
                "proficient in",
            ],
            "Intermediate": [
                "intermediate",
                "comfortable with",
                "comfortable in",
                "good at",
                "good in",
            ],
            "Beginner": [
                "beginner",
                "basic",
                "basics of",
                "beginning",
                "learning",
                "just started",
            ],
        }

        lowered_text = text.lower()

        for skill in taxonomy["skill_name"].dropna():

            skill_name = str(skill).strip()

            if not skill_name:
                continue

            pattern = (
                r"(?<!\w)"
                + re.escape(skill_name)
                + r"(?!\w)"
            )

            match = re.search(
                pattern,
                text,
                re.IGNORECASE
            )

            if not match:
                continue

            proficiency = "Unknown"

            # Look around the skill mention for proficiency clues.
            start = max(0, match.start() - 60)
            end = min(len(text), match.end() + 60)

            surrounding_text = lowered_text[start:end]

            for level, phrases in proficiency_patterns.items():

                if any(
                    phrase in surrounding_text
                    for phrase in phrases
                ):
                    proficiency = level
                    break

            information["skills"][skill_name] = proficiency

    def _extract_situation_and_goal(self, text, information):
        lowered = text.lower()

        information["situation"] = text

        goal_patterns = [
            "looking for",
            "want to become",
            "want a career in",
            "want to switch",
            "want to change",
            "trying to move into",
            "interested in",
        ]

        for phrase in goal_patterns:
            if phrase in lowered:
                start = lowered.index(phrase)
                information["goal"] = text[start:].strip()
                break

    def extract(self, text: str) -> dict:
        if not text or not text.strip():
            return {}

        text = text.strip()

        information = {
            "name": None,
            "education": None,
            "branch": None,
            "current_year": None,
            "cgpa": None,
            "experience_years": None,
            "timeline_months": None,
            "learning_hours_week": None,
            "skills": {},
            "positive_preferences": [],
            "negative_preferences": [],
            "career_interests": [],
            "existing_offer_lpa": None,
            "existing_offer_label": None,
            "user_type": None,
            "confidence": 0.0,
        }

        self._extract_education(text, information)
        self._extract_branch(text, information)
        self._extract_year(text, information)
        self._extract_cgpa(text, information)
        self._extract_experience(text, information)
        self._extract_timeline(text, information)
        self._extract_learning_hours(text, information)
        self._extract_existing_offer(text, information)
        self._extract_skills(text, information)
        self._extract_situation_and_goal(text, information)
        
        self._detect_user_type(text, information)
        self._extract_preferences(text, information)
        self._extract_career_interests(text, information)

        if str(information["branch"]).lower() == "mechanical":
            information["career_interests"].append("Mechanical Engineering")

        information["confidence"] = self._calculate_confidence(
            information
        )

        logger.info(
            "Natural-language context extraction completed."
        )

        return information

    def _extract_education(self, text, information):
        patterns = [
            r"\b(B\.?Tech|BTech|B\.?E\.?|BE)\b",
            r"\b(M\.?Tech|MTech|M\.?E\.?|ME)\b",
            r"\b(MBA)\b",
            r"\b(BCA)\b",
            r"\b(MCA)\b",
            r"\b(LLB|LLM)\b",
            r"\b(MBBS)\b",
            r"\b(BDS)\b",
        ]

        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)

            if match:
                information["education"] = match.group(1)
                break

    def _extract_branch(self, text, information):
        patterns = [
            r"(?:branch|speciali[sz]ation)\s*(?:is|:)?\s*(Mechanical(?: Engineering)?|Computer Science(?: and Engineering)?|Data Science|Civil(?: Engineering)?|Electrical(?: Engineering)?|Electronics(?: and Communication)?|Information Technology)\b",
            r"(?:B\.?Tech|B\.?E\.?|BE)\s+(?:in\s+)?(Mechanical(?: Engineering)?|Computer Science(?: and Engineering)?|Data Science|Civil(?: Engineering)?|Electrical(?: Engineering)?|Electronics(?: and Communication)?|Information Technology)\b",
        ]

        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                information["branch"] = match.group(1).strip(" .,")
                return

    def _extract_year(self, text, information):
        match = re.search(
            r"\b(1st|2nd|3rd|4th)\s*(?:year|yr)\b",
            text,
            re.IGNORECASE,
        )

        if match:
            information["current_year"] = match.group(1) + " Year"
        elif re.search(r"\b(final year|vii\s*(?:sem|semester)|viii\s*(?:sem|semester))\b", text, re.IGNORECASE):
            information["current_year"] = "Final Year"

    def _extract_cgpa(self, text, information):
        match = re.search(
            r"(?:\b(\d+(?:\.\d+)?)\s*(?:cgpa|c\.g\.p\.a)\b|\b(?:cgpa|c\.g\.p\.a)\s*(?:is|:)?\s*(\d+(?:\.\d+)?)\b)",
            text,
            re.IGNORECASE,
        )

        if match:
            value = match.group(1) or match.group(2)
            information["cgpa"] = float(value)

    def _extract_experience(self, text, information):
        match = re.search(
            r"(\d+(?:\.\d+)?)\s*(?:years?|yrs?)\s*(?:of\s*)?(?:work\s*)?experience",
            text,
            re.IGNORECASE,
        )

        if match:
            information["experience_years"] = float(match.group(1))

    def _extract_timeline(self, text, information):
        matches = re.findall(r"(\d+)\s*(?:-|to)?\s*(\d+)?\s*(months?|mos?)", text, re.IGNORECASE)
        if matches:
            # A user may have separate campus and off-campus deadlines. Use
            # the longest stated preparation runway for role feasibility.
            information["timeline_months"] = max(
                int(end or start) for start, end, _ in matches
            )

    def _extract_learning_hours(self, text, information):
        match = re.search(
            r"(\d+)\s*(?:hours?|hrs?)\s*(?:per|a|/)?\s*week",
            text,
            re.IGNORECASE,
        )

        if match:
            information["learning_hours_week"] = int(match.group(1))

    def _extract_existing_offer(self, text, information):
        match = re.search(
            r"(?:(TCS\s+Ninja)\s+)?offer\s+(?:of|at)\s*"
            r"(\d+(?:\.\d+)?)\s*(?:lpa|lakh(?:s)?\s+per\s+annum)",
            text,
            re.IGNORECASE,
        )
        if match:
            information["existing_offer_lpa"] = float(match.group(2))
            information["existing_offer_label"] = match.group(1) or "Current offer"

    def _detect_user_type(self, text, information):
        """
        Detects the user's primary type using multiple
        contextual signals rather than relying on one keyword.
        """

        lowered = text.lower()

        student_signals = [
            "student",
            "btech",
            "b.tech",
            "b.e",
            "college",
            "university",
            "semester",
            "year of study",
            "placements",
            "campus placement",
        ]

        fresher_signals = [
            "fresher",
            "fresh graduate",
            "just graduated",
            "recent graduate",
            "no experience",
            "0 years experience",
            "looking for my first job",
            "looking for first job",
            "first job",
            "first role",
        ]

        working_signals = [
            "working professional",
            "currently working",
            "my current job",
            "my job",
            "working as",
            "employed",
            "years of experience",
            "yrs of experience",
        ]

        switch_signals = [
            "career switch",
            "switch career",
            "switching career",
            "career change",
            "change my career",
            "change careers",
            "switch jobs",
            "job switch",
            "move into",
            "transition into",
            "transition to",
            "move from",
        ]

        if any(signal in lowered for signal in switch_signals):
            information["user_type"] = "career_switcher"
            return

        if any(signal in lowered for signal in fresher_signals):
            information["user_type"] = "fresher"
            return

        if (
            information.get("experience_years") is not None
            and information["experience_years"] > 0
        ):
            if any(
                signal in lowered
                for signal in switch_signals
            ):
                information["user_type"] = "career_switcher"
            else:
                information["user_type"] = "experienced_professional"

            return

        if any(
            signal in lowered
            for signal in working_signals
        ):
            information["user_type"] = "working_professional"
            return

        if any(
            signal in lowered
            for signal in student_signals
        ):
            information["user_type"] = "student"
            return

        information["user_type"] = "unknown"

    def _extract_preferences(self, text, information):
        lowered = text.lower()

        negative_patterns = {
            "no_networking": ["no networking", "avoid networking", "don't want networking", "do not want networking", "heavy networking"],
            "no_client_facing": ["no client-facing", "no client facing", "avoid client-facing", "avoid client facing"],
            "no_travel": ["no travel", "avoid travel", "don't want to travel", "do not want to travel", "frequent travel"],
            "no_night_shifts": ["no night shift", "no night shifts", "avoid night shifts"],
            "no_heavy_coding": ["no heavy coding", "avoid heavy coding", "don't want coding", "do not want coding"],
        }

        for preference, phrases in negative_patterns.items():
            if any(phrase in lowered for phrase in phrases):
                information["negative_preferences"].append(preference)

    def _calculate_confidence(self, information):
        fields = [
            "education",
            "current_year",
            "cgpa",
            "experience_years",
            "timeline_months",
            "learning_hours_week",
            "user_type",
        ]

        detected = sum(
            information[field] is not None
            for field in fields
        )

        return round(detected / len(fields), 2)

    def _extract_career_interests(self, text, information):
        """
        Extracts explicit career interests from role names and domains.
        """

        base_dir = Path(__file__).resolve().parent.parent.parent

        roles_file = (
            base_dir
            / "data"
            / "seed"
            / "seed_roles.csv"
        )

        if not roles_file.exists():
            logger.warning("Career roles dataset not found.")
            return

        roles = pd.read_csv(roles_file)
        lowered_text = text.lower()

        candidates = set()

        # Domains
        for value in roles["domain"].dropna():
            candidates.add(str(value).strip())

        # Specific career roles
        for value in roles["role_name"].dropna():
            candidates.add(str(value).strip())

        # Longest matches first prevents shorter terms
        # from interfering with more specific ones.
        candidates = sorted(
            candidates,
            key=len,
            reverse=True
        )

        for item in candidates:

            if not item:
                continue

            pattern = (
                r"(?<!\w)"
                + re.escape(item)
                + r"(?!\w)"
            )

            if re.search(pattern, text, re.IGNORECASE):
                if item not in information["career_interests"]:
                    information["career_interests"].append(item)
