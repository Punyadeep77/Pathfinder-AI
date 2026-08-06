from src.exceptions.base import PathfinderException


class DatasetValidationError(PathfinderException):
    """
    Raised when a dataset fails validation.
    """
    pass


class MissingColumnError(DatasetValidationError):
    """
    Raised when required columns are missing.
    """
    pass


class InvalidDataError(DatasetValidationError):
    """
    Raised when invalid values are found.
    """
    pass