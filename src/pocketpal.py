"""Main module to run the assistant bot."""

from prompt_toolkit import PromptSession

from actions import (
    add_birthday,
    birthdays,
    change_contact,
    load_data,
    remove_contact,
    save_data,
    show_all,
    show_birthday,
    show_phone,
)
from autocomplete import CommandCompleter
from commands import Commands
from error_handlers import InputArgsError


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

    book = load_data()
    session = PromptSession(completer=CommandCompleter())
    print("Welcome to the assistant bot!")
    while True:
        user_input = session.prompt("Enter a command: ")
        if not user_input.strip():
            continue
        command, args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            save_data(book)
            break
        command_object = Commands.get_command(command)
        if command_object:
            try:
                command_object.value.validate_args(args)
            except InputArgsError as e:
                print(e)
                continue
            print(command_object.value.run(args, book))
            if command in (Commands.EXIT,):
                save_data(book)
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
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
