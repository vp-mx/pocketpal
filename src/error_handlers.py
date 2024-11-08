"""Module to handle errors in the helper functions."""

from functools import wraps
from typing import Callable, Optional, Union

from rich.text import Text

from custom_console import print_to_console
from visualisation import OutputStyle


class HelperError(BaseException):
    """Base exception for helper errors."""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


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


class NotFoundWarning(BaseException):
    """Exception for not existing object"""

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)


def input_error(func: Callable[..., Union[str, "Text"]]) -> Callable[..., Union[str, "Text"]]:
    """Decorator to handle errors in the input."""

    @wraps(func)
    def inner(*args, **kwargs) -> Optional[Union[str, "Text"]]:
        try:
            return func(*args, **kwargs)
        except (HelperError, InputArgsError) as e:
            print_to_console(e.message, style=OutputStyle.ERROR)
            return None
        except NotFoundWarning as e:
            print_to_console(e.message, style=OutputStyle.WARNING)
            return None
        except (ValueError, KeyError, TypeError, IndexError):
            print_to_console("Error: Invalid input. Check it and try again.", style=OutputStyle.ERROR)
            return None

    return inner
