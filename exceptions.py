from typing import Dict


class TodoistException(Exception):
    """Custom exception class for the todoist API."""

    def __init__(self, e: Exception):
        super().__init__(message=str(e))
        self.message = str(e)
        self.type = type(e).__name__

    def serialize(self) -> Dict[str, str]:
        return dict(message=self.message, type=self.type)


class GoogleException(Exception):
    """Custom exception class for the google gemini bot."""

    def __init__(self, e: Exception):
        super().__init__(message=str(e))
        self.message = str(e)
        self.type = type(e).__name__

    def serialize(self) -> Dict[str, str]:
        return dict(message=self.message, type=self.type)
