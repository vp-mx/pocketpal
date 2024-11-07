"""Module to handle errors in the helper functions."""

from functools import wraps
from typing import Callable


class HelperError(BaseException):
    """Base exception for helper errors."""


class ExitApp(BaseException):
    """Exception for exit from app"""


class InternalError(BaseException):
    """Exception for managing internal errors"""

    def __init__(self) -> None:
        self.message = "Oops! Something went wrong. Ping the developer to fix it."
        super().__init__(self.message)


class InputArgsError(BaseException):
    """Base exception for helper errors."""

    def __init__(self, message: str) -> None:
        self.message = f"Wrong args for command. Example: {message}"
        super().__init__(self.message)


def input_error(func: Callable[..., str]) -> Callable[..., str]:
    """Decorator to handle errors in the input."""

    @wraps(func)
    def inner(*args, **kwargs) -> str:
        try:
            return func(*args, **kwargs)
        except HelperError as e:
            return str(e)
        except InputArgsError as e:
            return str(e)
        except (ValueError, KeyError, TypeError, IndexError):
            return "Error: Invalid input. Check it and try again."

    return inner
