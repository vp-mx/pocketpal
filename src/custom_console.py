"""Custom console module for rich console."""

from typing import Union

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from visualisation import OutputStyle

console = Console()


def print_to_console(message: Union[str, Table, Text, Panel], style: OutputStyle = None) -> None:
    """Prints a message to the console with the given style.

    param: message: str: The message to print.
    param: style: str: The style to use.
    """
    console.print(message, style=style.value if style else None)
