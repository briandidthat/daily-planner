from typing import Dict


class DailyPlannerException(Exception):
    """Base exception class"""

    def __init__(self, message: str, type: str):
        self.message = message
        self.type = type
        super().__init__(message)

    def serialize(self):
        return dict(message=self.message, type=self.type)


class GoogleException(DailyPlannerException):
    pass


class TodoistException(DailyPlannerException):
    pass
