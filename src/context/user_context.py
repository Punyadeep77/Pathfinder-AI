from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class UserContext:
    """
    Intermediate representation of the user's
    natural-language career situation.

    This object exists before CareerIdentity.
    """

    user_type: str = "unknown"

    situation: str = ""

    goal: str = ""

    extracted_information: Dict[str, Any] = field(
        default_factory=dict
    )

    applicable_constraints: Dict[str, Any] = field(
        default_factory=dict
    )

    missing_required_constraints: List[str] = field(
        default_factory=list
    )

    confidence: float = 0.0

    def has_missing_constraints(self) -> bool:
        return bool(self.missing_required_constraints)

    def is_ready(self) -> bool:
        return not self.has_missing_constraints()