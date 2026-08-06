"""
Base exception class for Pathfinder AI.
"""


class PathfinderException(Exception):
    """
    Base exception inherited by all custom exceptions.
    """

    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message