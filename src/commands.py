"""Module to store the commands and their information."""

from dataclasses import dataclass
from enum import Enum, auto
from typing import Callable, Optional

from actions import (
    add_address,
    add_birthday,
    add_contact,
    add_email,
    birthdays,
    change_phone,
    edit_email,
    remove_contact,
    remove_email,
    search_by_partial_name,
    show_all,
    show_birthday,
    show_email,
    show_phone,
)
from error_handlers import InputArgsError


class Source(Enum):
    """Enum to store the source where to apply command."""

    ADDRESS_BOOK = auto()
    NOTES = auto()


@dataclass
class Command:
    """Dataclass to store command information."""

    cli_name: str
    description: str
    run: Callable[[...], str]
    args_len: int
    input_help: str
    source: Source

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
        source=Source.ADDRESS_BOOK,
    )
    ADD_ADDRESS = Command(
        cli_name="add-address",
        description="Adds an address to a contact.",
        run=add_address,
        args_len=2,
        input_help="add-address [name] [address]",
        source=Source.ADDRESS_BOOK,
    )
    ADD_BIRTHDAY = Command(
        cli_name="add-birthday",
        description="Adds a birthday to a contact.",
        run=add_birthday,
        args_len=2,
        input_help="add-birthday [name] [birthday]",
        source=Source.ADDRESS_BOOK,
    )
    ADD_EMAIL = Command(
        cli_name="add-email",
        description="Adds an email to a contact.",
        run=add_email,
        args_len=2,
        input_help="add-email [name] [email]",
        source=Source.ADDRESS_BOOK,
    )
    BIRTHDAYS = Command(
        cli_name="birthdays",
        description="Shows upcoming birthdays.",
        run=birthdays,
        args_len=0,
        input_help="birthdays",
        source=Source.ADDRESS_BOOK,
    )
    CHANGE_PHONE = Command(
        cli_name="change",
        description="Changes contact's phone.",
        run=change_phone,
        args_len=3,
        input_help="change [name] [old_phone] [new_phone]",
        source=Source.ADDRESS_BOOK,
    )
    CLOSE = Command(
        cli_name="close",
        description="Closes the assistant bot.",
        run=lambda *_: "Good bye!",
        args_len=0,
        input_help="close",
        source=Source.ADDRESS_BOOK,
    )
    EXIT = Command(
        cli_name="exit",
        description="Exits the assistant bot.",
        run=lambda *_: "Good bye!",
        args_len=0,
        input_help="exit",
        source=Source.ADDRESS_BOOK,
    )
    EDIT_EMAIL = Command(
        cli_name="edit-email",
        description="Edits the email of a contact.",
        run=edit_email,
        args_len=3,
        input_help="edit-email [name] [old_email] [new_email]",
        source=Source.ADDRESS_BOOK,
    )
    SEARCH_BY_PARTIAL_NAME = Command(
        cli_name="search",
        description="Searches for contacts by partial name.",
        run=search_by_partial_name,
        args_len=1,
        input_help="search [partial_name]",
        source=Source.ADDRESS_BOOK,
    )
    HELLO = Command(
        cli_name="hello",
        description="Greets the user.",
        run=lambda *_: "How can I help you?",
        args_len=0,
        input_help="hello",
        source=None,
    )
    REMOVE_CONTACT = Command(
        cli_name="remove",
        description="Removes a contact from the address book.",
        run=remove_contact,
        args_len=1,
        input_help="remove [name]",
        source=Source.ADDRESS_BOOK,
    )
    REMOVE_EMAIL = Command(
        cli_name="remove-email",
        description="Removes the email of a contact.",
        run=remove_email,
        args_len=2,
        input_help="remove-email [name] [email]",
        source=Source.ADDRESS_BOOK,
    )
    SHOW_ALL = Command(
        cli_name="all",
        description="Shows all contacts in the address book.",
        run=lambda args, book: show_all(book),
        args_len=0,
        input_help="all",
        source=Source.ADDRESS_BOOK,
    )
    SHOW_BIRTHDAY = Command(
        cli_name="show-birthday",
        description="Shows the birthday of a contact.",
        run=show_birthday,
        args_len=1,
        input_help="show-birthday [name]",
        source=Source.ADDRESS_BOOK,
    )
    SHOW_EMAIL = Command(
        cli_name="show-email",
        description="Shows the email of a contact.",
        run=show_email,
        args_len=1,
        input_help="show-email [name]",
        source=Source.ADDRESS_BOOK,
    )
    SHOW_PHONE = Command(
        cli_name="phone",
        description="Shows the phone number of a contact.",
        run=show_phone,
        args_len=1,
        input_help="phone [name]",
        source=Source.ADDRESS_BOOK,
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
