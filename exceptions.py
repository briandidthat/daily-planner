from typing import Dict


class BaseException(Exception):
    """Base exception class"""

    def __init__(self, message: str, type: str):
        self.message = message
        self.type = type
        super().__init__(message)

    def serialize(self) -> Dict[str, str]:
        return dict(message=self.message, type=self.type)


class GoogleException(BaseException):
    """Exceptions for Google Gemini API"""

    pass


class TodoistException(BaseException):
    """Exceptions for Todoist API"""

    pass


class ApiException(BaseException):
    """Exceptions for Fast API"""

    pass
