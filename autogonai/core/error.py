from typing import Optional

# Define custom error classes here
class APIError(Exception):
    """Base class for API errors."""

    def __init__(self, message: str, status_code: int):
        """Initialize APIError.

        Args:
            message (str): Error message.
            status_code (int): HTTP status code.
        """
        super().__init__(message)
        self.message = message
        self.status_code = status_code

# Authorization Errors
class UnauthorizedError(APIError):
    """Unauthorized Error."""

    # Display a custom message telling the user to provide a valid API key
    def __init__(self):
        """Initialize UnauthorizedError."""
        message = (
            "Unauthorized. Please provide a valid API key. "
            "You can generate an API key from https://console.autogon.ai/settings"
        )
        super().__init__(message, 401)