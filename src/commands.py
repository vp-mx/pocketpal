"""Module to store the commands and their information."""

from dataclasses import dataclass
from enum import Enum
from typing import Optional

from actions import add_contact
from error_handlers import InputArgsError


@dataclass
class Command:
    """Dataclass to store command information."""

    cli_name: str
    description: str
    run: callable
    args_len: int
    input_help: str

    def validate_args(self, args: Optional[list[str]] = None):
        """Validates the number of arguments.

        param: args: List of arguments.
        raises: InputArgsError: If the number of arguments is incorrect.
        """
        if args is None and self.args_len == 0:
            return
        if args is None or len(args) != self.args_len:
            raise InputArgsError(self.input_help)


class Commands(Enum):
    """Enum to store all the commands."""

    ADD = Command(
        cli_name="add",
        description="Adds a contact to the address book.",
        run=add_contact,
        args_len=2,
        input_help="add [name] [phone]",
    )
    EXIT = Command(
        cli_name="exit",
        description="Exits the assistant bot.",
        run=lambda: "Good bye!",
        args_len=0,
        input_help="exit",
    )

    @classmethod
    def get_command(cls, command_name: str) -> Optional["Commands"]:
        """Returns the command based on the cli command name.

        param: command_name: The name of the command.
        return: Optional[Command]: The command object.
        """
        for command in cls:
            if command.value.cli_name == command_name:
                return command
        return None

    @classmethod
    def get_commands_list(cls) -> list[str]:
        """Returns a list of all the command names.

        return: list[str]: List of command names.
        """
        return [command.value.cli_name for command in cls]
