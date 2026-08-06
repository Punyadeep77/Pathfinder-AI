from src.exceptions.base import PathfinderException


class DatabaseError(PathfinderException):
    """
    Base database exception.
    """
    pass


class DatabaseConnectionError(DatabaseError):
    """
    Raised when database connection fails.
    """
    pass


class DatabaseImportError(DatabaseError):
    """
    Raised when importing data into the database fails.
    """
    pass