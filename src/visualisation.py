"""Module for visualisation helper functions."""

import itertools
from enum import Enum
from typing import Optional

from rich.table import Table


class OutputStyle(Enum):
    """Enum for output styles."""

    SUCCESS = "green"
    ERROR = "red"
    WARNING = "yellow"
    INFO = "magenta"


def create_rich_table_to_print(
    columns: list[str], data: list[list[str]], columns_style: Optional[list[str]] = None
) -> Table:
    """Creates a table object with the given columns and data using rich.

    param: columns: List of column names.
    param: data: List of lists, where each inner list corresponds to a row of data.
    """
    table = Table(show_header=True, header_style="bold magenta")
    column_styles = columns_style or itertools.cycle(["cyan", "green", "yellow", "blue", "red", "magenta", "white"])

    for column, style in zip(columns, column_styles):
        table.add_column(column, style=style)
    for row in data:
        table.add_row(*row)
    return table
