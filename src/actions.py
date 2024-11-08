"""This module contains the functions to perform actions on the address book."""

from typing import TYPE_CHECKING

from address_book import AddressBook, Record
from custom_console import console, print_to_console
from error_handlers import NotFoundWarning, input_error
from visualisation import OutputStyle, create_rich_table_to_print

if TYPE_CHECKING:
    from commands import Commands


@input_error
def add_contact(args: list[str], book: "AddressBook") -> None:
    """Adds a contact to the address book.

    param: args: List with 2 values: name and phone.
    param: book: AddressBook object to modify.
    return: str: Result message.
    """
    name, phone = args
    if record := book.find(name):
        record.add_phone(phone)
        print_to_console(f"Phone number '{phone}' added to contact '{name}'.", style=OutputStyle.SUCCESS)
    else:
        record = Record(name)
        record.add_phone(phone)
        book.add_record(record)
        print_to_console(f"Contact '{name}' added with phone number '{phone}'.", style=OutputStyle.SUCCESS)


@input_error
def remove_contact(args: list[str], book: "AddressBook") -> None:
    """Removes a contact from the address book.

    param: args: List with 1 value: name.
    param: book: AddressBook object to modify.
    return: str: Result message.
    """
    name = args[0]
    if not book.find(name):
        raise NotFoundWarning(f"Contact '{name}'")

    book.delete(name)
    print_to_console("Contact removed.", style=OutputStyle.SUCCESS)


@input_error
def change_phone(args: list[str], book: "AddressBook") -> None:
    """Changes the phone number of a contact in the address book.

    param: args: List with 3 values: name, old phone, new phone.
    param: book: AddressBook object to modify.
    return: str: Result message.
    """
    name, old_phone, new_phone = args
    record = book.find(name)
    if not record:
        raise NotFoundWarning(f"Contact '{name}'")

    record.edit_phone(old_phone, new_phone)
    console.print("Phone number updated.", style="green")


@input_error
def show_phone(args: list[str], book: "AddressBook") -> None:
    """Shows the phone number of a contact from the address book.

    param: args: List with 1 value: name.
    param: book: AddressBook object to read from.
    return: str: Result message.
    """
    name = args[0]
    record = book.find(name)
    if not record:
        raise NotFoundWarning(f"Contact '{name}'")

    print_to_console(f"{name}'s phones: {record.all_phones}", style=OutputStyle.SUCCESS)


def show_all(book: "AddressBook") -> None:
    """Shows all contacts from the contacts dictionary.

    param: contacts: Contacts dictionary to read from.
    return: str: Result message.
    """
    columns = ["Name", "Phones", "Birthday", "Address", "Emails", "Notes"]
    data = [
        [record.contact_name, record.all_phones, record.birthday, record.address, record.all_emails, record.all_notes]
        for record in book.data.values()
    ]
    data = sorted(data, key=lambda x: x[0])
    console.print(create_rich_table_to_print(columns, data))


@input_error
def add_birthday(args: list[str], book: "AddressBook") -> None:
    """Adds a birthday to a contact in the address book.

    param: args: List with 2 values: name and birthday.
    param: book: AddressBook object to modify.
    return: str: Result message.
    """
    name, birthday = args
    record = book.find(name)
    if not record:
        raise NotFoundWarning(f"Contact '{name}'")

    record.add_birthday(birthday)
    print_to_console("Birthday added.")


@input_error
def show_birthday(args: list[str], book: "AddressBook") -> None:
    """Shows the birthday of a contact from the address book.

    param: args: List with 1 value: name.
    param: book: AddressBook object to read from.
    return: str: Result message.
    """
    name = args[0]
    record = book.find(name)
    if not record:
        raise NotFoundWarning(f"Contact '{name}'")

    if record.birthday:
        print_to_console(str(record.birthday), style=OutputStyle.SUCCESS)
    else:
        print_to_console("N/A", style=OutputStyle.WARNING)


@input_error
def birthdays(args, book: "AddressBook") -> None:
    """Shows all birthdays in next 7 days.

    param: book: AddressBook object to read from.
    return: str: Result message.
    """
    days_interval = int(args[0]) if args else 7
    print_to_console(book.get_upcoming_birthdays(days_interval))


@input_error
def add_address(args: list[str], book: "AddressBook") -> None:
    """Adds an address to a contact in the address book.
    param: args: List with 2 values: name and address.
    param: book: AddressBook object to modify.
    return: str: Result message.
    """
    name, address = args
    record = book.find(name)
    if not record:
        raise NotFoundWarning(f"Contact '{name}'")

    record.add_address(address)
    print_to_console("Address added.", style=OutputStyle.SUCCESS)


@input_error
def add_email(args, book) -> None:
    """Add an email to a contact.

    param: args: List with 2 values - name and email.
    param: book: AddressBook object to read from.
    return: str: Result message.
    """
    name, email = args
    record = book.find(name)
    if not record:
        raise NotFoundWarning(f"Contact '{name}'")

    record.add_email(email)
    print_to_console(f"Email '{email}' was successfully added for contact '{name}'.", style=OutputStyle.SUCCESS)


@input_error
def edit_email(args, book) -> None:
    """Edit an email for a contact.

    param: args: List with 3 values - name, old_email and new_email.
    param: book: AddressBook object to read from.
    return: str: Result message.
    """
    name, old_email, new_email = args
    record = book.find(name)
    if not record:
        raise NotFoundWarning(f"Contact '{name}'")
    record.edit_email(old_email, new_email)
    print_to_console(
        f"Email '{old_email}' was successfully changed to '{new_email}' for contact '{name}'.",
        style=OutputStyle.SUCCESS,
    )


@input_error
def remove_email(args, book) -> None:
    """Remove an email for a contact.

    param: args: List with 2 values - name and email.
    param: book: AddressBook object to read from.
    return: str: Result message.
    """
    name, email = args
    record = book.find(name)
    if not record:
        raise NotFoundWarning(f"Contact '{name}'")

    record.remove_email(email)
    print_to_console(f"Email '{email}' was successfully removed from contact '{name}'.", style=OutputStyle.SUCCESS)


@input_error
def show_email(args, book) -> None:
    """Show contact email/emails.

    param: args: List with 1 value - name.
    param: book: AddressBook object to read from.
    return: str: Result message.
    """
    name = args[0]
    record = book.find(name)
    if not record:
        raise NotFoundWarning(f"Contact '{name}'")
    text = "Contact doesn't have any emails" if not record.emails else "; ".join(email.value for email in record.emails)
    print_to_console(text, style=OutputStyle.SUCCESS)


@input_error
def search_by_partial_name(args, book) -> None:
    """Searches for contacts by partial name.

    param: args: 1 value: the partial name to search.
    param: book: AddressBook object to search in.
    return: str: Result message.
    """
    partial_name = args[0]
    records = book.search_by_partial_name(partial_name)
    if not records:
        raise NotFoundWarning(f"Contacts with '{partial_name}' in name")
    text = "\n".join(
        f"Contact name: {record.name}\n"
        f"Phone: {record.all_phones}\n"
        f"Birthday: {record.birthday or 'N/A'}\n"
        f"Address: {record.address or 'N/A'}\n"
        f"Email: {'; '.join(email.value for email in record.emails) or 'N/A'}\n" + "=" * 30
        for record in records
    )
    print_to_console(text, style=OutputStyle.SUCCESS)


def print_commands_table(cmds: type["Commands"]) -> None:
    """Returns a table with all the commands and their descriptions.

    Note: For helper it stores into ths module due to circular imports. For Notes and AddressBook
    similar helper functions should be stored in their respective modules.

    return: Table: The table with the commands.
    """
    columns = ["Command Name", "Description", "Input Help"]
    data = [[command.value.cli_name, command.value.description, command.value.input_help] for command in cmds]
    data = sorted(data, key=lambda x: x[0])
    console.print(create_rich_table_to_print(columns, data))


@input_error
def edit_note(args: list[str], notes_book: "NoteBook") -> None:
    """Edits a note in the notes dictionary.

    param: args: List with 2 values: note title and new body.
    param: notes_book: Notes dictionary to modify.
    return: str: Result message.
    """

    note_title, new_body = args
    if note_in_notebook := notes_book.find(note_title):
        notes_book.edit(note_title, new_body)
        print_to_console(f"Note edited to -{note_in_notebook.body}.", style=OutputStyle.SUCCESS)
    else:
        raise NotFoundWarning(f"Note with title '{note_title}'")


@input_error
def replace_note(args: list[str], notes_book: "NoteBook") -> None:
    """Replaces a note_body in the notes dictionary.

    param: args: List with 2 values: note title and new body.
    param: notes_book: Notes dictionary to modify.
    return: str: Result message.
    """
    note_title, new_body = args
    note_in_notebook = notes_book.find(note_title)
    if not note_in_notebook:
        raise NotFoundWarning(f"Note with title '{note_title}'")
    notes_book.replace(note_title, new_body)
    print_to_console(f"Note replaced to -{note_in_notebook.body}.", style=OutputStyle.SUCCESS)


def show_notes(notes_book: "NoteBook") -> None:
    """Shows all notes from the notes dictionary.

    param: notes_book: Notes dictionary to read from.
    return: str: Result message.
    """
    print_to_console(str(notes_book.show_all()))


@input_error
def show_notes_contact(name: str, notes_book: "NoteBook") -> None:
    """Shows all notes from the notes dictionary.

    param: notes_book: Notes dictionary to read from.
    return: str: Result message.
    """
    print_to_console(str(notes_book.show_all_for_contact(name)))


@input_error
def add_tag(args: list[str], notes_book: "NoteBook") -> None:
    """Adds a tag to a note in the notes dictionary.

    param: args: List with 2 values: note title and tag.
    param: notes_book: Notes dictionary to modify.
    return: str: Result message.
    """
    note_title, tag = args
    note_in_notebook = notes_book.find(note_title)
    if not note_in_notebook:
        raise NotFoundWarning(f"Note with title '{note_title}'")

    notes_book.add_tag(note_title, tag)
    print_to_console(f"Tag added to note -{note_in_notebook.title}.", style=OutputStyle.SUCCESS)


@input_error
def remove_tag(args: list[str], notes_book: "NoteBook") -> None:
    """Removes a tag from a note in the notes dictionary.

    param: args: List with 2 values: note title and tag.
    param: notes_book: Notes dictionary to modify.
    return: str: Result message.
    """
    note_title, tag = args
    note_in_notebook = notes_book.find(note_title)
    if not note_in_notebook:
        raise NotFoundWarning(f"Note with title '{note_title}'")
    notes_book.remove_tag(note_title, tag)
    print_to_console(f"Tag {tag} removed from note -{note_in_notebook.title}.", style=OutputStyle.SUCCESS)


@input_error
def attach_note(args: list[str], notes_book: "NoteBook") -> None:
    """Attaches a note to a contact in the notes dictionary.

    param: args: List with 2 values: note title and contact name.
    param: notes_book: Notes dictionary to modify.
    return: str: Result message.
    """

    note_title, contact_name = args
    note_in_notebook = notes_book.find(note_title)
    if not note_in_notebook:
        raise NotFoundWarning(f"Note with title '{note_title}'")
    notes_book.attach_to_contact(note_title, contact_name)
    print_to_console(f"Note {note_in_notebook} attached to-{note_in_notebook.contacts}.", style=OutputStyle.SUCCESS)


def search_notes(query: str, notes_book: "NoteBook") -> None:
    """Searches for notes containing the query in their title or body.

    param: query: str: The query to search for.
    param: notes_book: Notes dictionary to read from.
    return: str: Result message.
    """

    print_to_console(str(notes_book.search(query)))


def delete_note(note_title: str, notes_book: "NoteBook") -> None:
    """Deletes a note from the notes dictionary.

    param: note_title: str: The title of the note to delete.
    param: notes_book: Notes dictionary to modify.
    return: str: Result message.
    """

    if note_in_notebook := notes_book.find(note_title):
        notes_book.delete(note_title)

        print_to_console(f"Note {note_in_notebook.title} deleted.")
    raise NotFoundWarning(f"Note with title '{note_title}'")


def find_by_tag(tag: str, notes_book: "NoteBook") -> list[str]:
    """Finds all notes with a specific tag.

    param: tag: str.
    param: notes_book: Notes dictionary to read from.
    return: list: Result message.
    """

    return notes_book.find_by_tag(tag)


def sort_by_tag(tag: str, notes_book: "NoteBook") -> str:
    """Sorts notes by tag.

    param: tag: str: The tag to sort by.
    param: notes_book: Notes dictionary to read from.
    return: str: Result message.
    """

    return notes_book.sort_by_tag(tag)


@input_error
def add_note(args: list[str], notes_book: "NoteBook") -> None:
    """Adds a note to a contact in the notes book.

    param: args: List with 2 values: name and note.
    param: notes_book: NoteBook object to modify.
    return: str: Result message.
    """

    name, note = args
    note_title: str = f"note-{len(notes_book.values()) + 1}"
    notes_book.add(note_title, note)
    notes_book.attach_to_contact(note_title, name)
    print_to_console("Note added.")
