"""Module to handle errors in the helper functions."""

from functools import wraps
from typing import Callable


class HelperError(BaseException):
    """Base exception for helper errors."""


def input_error(func: Callable[..., str]) -> Callable[..., str]:
    """Decorator to handle errors in the input."""

    @wraps(func)
    def inner(*args, **kwargs) -> str:
        try:
            return func(*args, **kwargs)
        except HelperError as e:
            return str(e)
        except (ValueError, KeyError, TypeError, IndexError):
            return "Error: Invalid input. Check it and try again."

    return inner
