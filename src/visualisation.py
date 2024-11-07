"""Module for visualisation helper functions."""

import itertools
from typing import TYPE_CHECKING, Optional

from rich.table import Table

if TYPE_CHECKING:
    from commands import Commands


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


def get_commands_table(cmds: type["Commands"]) -> Table:
    """Returns a table with all the commands and their descriptions.

    Note: For helper it stores into ths module due to circular imports. For Notes and AddressBook
    similar helper functions should be stored in their respective modules.

    return: Table: The table with the commands.
    """
    columns = ["Command Name", "Description", "Input Help"]
    data = [[command.value.cli_name, command.value.description, command.value.input_help] for command in cmds]
    data = sorted(data, key=lambda x: x[0])
    return create_rich_table_to_print(columns, data)
