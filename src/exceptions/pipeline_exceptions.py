from src.exceptions.base import PathfinderException


class PipelineError(PathfinderException):
    """
    Base ETL pipeline exception.
    """
    pass


class ETLError(PipelineError):
    """
    Raised when ETL execution fails.
    """
    pass