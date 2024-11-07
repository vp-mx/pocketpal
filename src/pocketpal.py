"""Main module to run the assistant bot."""

from prompt_toolkit import PromptSession
from rich.console import Console

from actions import (
    add_address,
    add_birthday,
    add_email,
    birthdays,
    change_contact,
    edit_email,
    remove_contact,
    remove_email,
    show_all,
    show_birthday,
    show_email,
    show_phone,
)
from address_book import AddressBook
from autocomplete import CommandCompleter
from commands import Commands, Source
from error_handlers import ExitApp, InputArgsError
from file_operations import ADDRESS_BOOK_FILE, NOTES_FILE, load_data, save_data
from notes import NoteBook


def parse_input(user_input: str) -> tuple[str, list[str]]:
    """Parses user input and returns the command and arguments.

    param: user_input: The user input.
    return: The command in lowercase and list of arguments.
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    args = [arg.strip() for arg in args if arg.strip()]
    return cmd, args


def main():
    """Main function to run the assistant bot."""

    book = load_data(ADDRESS_BOOK_FILE) or AddressBook()
    notes = load_data(NOTES_FILE) or NoteBook()
    console = Console()
    session = PromptSession(completer=CommandCompleter())
    console.print("Welcome to the assistant bot!", style="bold green")
    while True:
        try:
            user_input = session.prompt("Enter a command: ")
            if not user_input.strip():
                continue
            command, args = parse_input(user_input)
            if command_object := Commands.get_command(command):
                command_object.value.validate_args(args)
                object_to_modify = book if command_object.value.source == Source.ADDRESS_BOOK else notes
                print(command_object.value.run(args, object_to_modify))
                if command_object in (Commands.EXIT, Commands.CLOSE):
                    raise ExitApp
            elif command == "hello":
                print("How can I help you?")
            elif command == "change":
                print(change_contact(args, book))
            elif command == "remove":
                print(remove_contact(args, book))
            elif command == "phone":
                print(show_phone(args, book))
            elif command == "all":
                print(show_all(book))
            elif command == "add-birthday":
                print(add_birthday(args, book))
            elif command == "show-birthday":
                print(show_birthday(args, book))
            elif command == "birthdays":
                print(birthdays(book))
            elif command == "add-address":
                print(add_address(args, book))
            elif command == "add-email":
                print(add_email(args, book))
            elif command == "edit-email":
                print(edit_email(args, book))
            elif command == "remove-email":
                print(remove_email(args, book))
            elif command == "show-email":
                print(show_email(args, book))
            else:
                print("Invalid command.")
        except InputArgsError as input_args_error:
            console.print(input_args_error, style="bold red")
        except (KeyboardInterrupt, ExitApp):
            save_data(book, ADDRESS_BOOK_FILE)
            save_data(notes, NOTES_FILE)
            console.print("Data saved", style="bold blue")
            break


if __name__ == "__main__":
    main()
