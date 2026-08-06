from src.exceptions.base import PathfinderException


class RecommendationError(PathfinderException):
    """
    Raised when recommendation generation fails.
    """
    pass