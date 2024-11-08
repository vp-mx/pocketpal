"""This module contains the functions to perform actions on the address book."""

from address_book import AddressBook, Record
from error_handlers import input_error
from notes import NoteBook


@input_error
def add_contact(args: list[str], book: "AddressBook") -> str:
    """Adds a contact to the address book.

    param: args: List with 2 values: name and phone.
    param: book: AddressBook object to modify.
    return: str: Result message.
    """
    name, phone = args
    if record := book.find(name):
        record.add_phone(phone)
        return "Contact updated."
    record = Record(name)
    record.add_phone(phone)
    book.add_record(record)
    return "Contact added."


@input_error
def remove_contact(args: list[str], book: "AddressBook") -> str:
    """Removes a contact from the address book.

    param: args: List with 1 value: name.
    param: book: AddressBook object to modify.
    return: str: Result message.
    """
    name = args[0]
    if book.find(name):
        book.delete(name)
        return "Contact removed."
    return f"Contact '{name}' doesn't exist."


@input_error
def change_phone(args: list[str], book: "AddressBook") -> str:
    """Changes the phone number of a contact in the address book.

    param: args: List with 3 values: name, old phone, new phone.
    param: book: AddressBook object to modify.
    return: str: Result message.
    """
    name, old_phone, new_phone = args
    if record := book.find(name):
        record.edit_phone(old_phone, new_phone)
        return "Phone number updated."
    return f"Contact '{name}' doesn't exist."


@input_error
def show_phone(args: list[str], book: "AddressBook") -> str:
    """Shows the phone number of a contact from the address book.

    param: args: List with 1 value: name.
    param: book: AddressBook object to read from.
    return: str: Result message.
    """
    name = args[0]
    if record := book.find(name):
        return f"{name}'s phones: {record.all_phones}"
    return f"Contact '{name}' doesn't exist."


def show_all(book: "AddressBook"):
    """Shows all contacts from the contacts dictionary.

    param: contacts: Contacts dictionary to read from.
    return: str: Result message.
    """
    return book.all_records


@input_error
def add_birthday(args: list[str], book: "AddressBook") -> str:
    """Adds a birthday to a contact in the address book.

    param: args: List with 2 values: name and birthday.
    param: book: AddressBook object to modify.
    return: str: Result message.
    """
    name, birthday = args
    if record := book.find(name):
        record.add_birthday(birthday)
        return "Birthday added."
    return f"Contact '{name}' doesn't exist."


@input_error
def show_birthday(args: list[str], book: "AddressBook") -> str:
    """Shows the birthday of a contact from the address book.

    param: args: List with 1 value: name.
    param: book: AddressBook object to read from.
    return: str: Result message.
    """
    name = args[0]
    if record := book.find(name):
        return str(record.birthday) if record.birthday else "N/A"
    return f"Contact '{name}' doesn't exist."


@input_error
def birthdays(args, book: "AddressBook") -> str:
    """Shows all birthdays in next 7 days.

    param: book: AddressBook object to read from.
    return: str: Result message.
    """
    days_interval = int(args[0])
    return book.get_upcoming_birthdays(days_interval)


@input_error
def add_address(args: list[str], book: "AddressBook") -> str:
    """Adds an address to a contact in the address book.
    param: args: List with 2 values: name and address.
    param: book: AddressBook object to modify.
    return: str: Result message.
    """
    name, address = args
    if record := book.find(name):
        record.add_address(address)
        return "Address added."
    return f"Contact '{name}' doesn't exist."


@input_error
def add_email(args, book):
    """Add an email to a contact.

    param: args: List with 2 values - name and email.
    param: book: AddressBook object to read from.
    return: str: Result message.
    """
    name, email = args
    if record := book.find(name):
        record.add_email(email)
        return f"Email '{email}' was successfully added for contact '{name}'."
    return f"Contact '{name}' doesn't exist."


@input_error
def edit_email(args, book):
    """Edit an email for a contact.

    param: args: List with 3 values - name, old_email and new_email.
    param: book: AddressBook object to read from.
    return: str: Result message.
    """
    name, old_email, new_email = args
    if record := book.find(name):
        record.edit_email(old_email, new_email)
        return f"Email '{old_email}' was successfully changed to '{new_email}' for contact '{name}'."
    return f"Contact '{name}' doesn't exist."


@input_error
def remove_email(args, book):
    """Remove an email for a contact.

    param: args: List with 2 values - name and email.
    param: book: AddressBook object to read from.
    return: str: Result message.
    """
    name, email = args
    if record := book.find(name):
        record.remove_email(email)
        return f"Email '{email}' was successfully removed from contact '{name}'."
    return f"Contact '{name}' doesn't exist."


@input_error
def show_email(args, book):
    """Show contact email/emails.

    param: args: List with 1 value - name.
    param: book: AddressBook object to read from.
    return: str: Result message.
    """
    name = args[0]
    if record := book.find(name):
        return (
            "Contact doesn't have any emails"
            if not record.emails
            else "; ".join(email.value for email in record.emails)
        )
    return f"Contact '{name}' doesn't exist."


def search_by_partial_name(args, book):
    """Searches for contacts by partial name.

    param: args: 1 value: the partial name to search.
    param: book: AddressBook object to search in.
    return: str: Result message.
    """
    partial_name = args[0]
    if records := book.search_by_partial_name(partial_name):
        return "\n".join(
            f"Contact name: {record.name}\n"
            f"Phone: {record.all_phones}\n"
            f"Birthday: {record.birthday or 'N/A'}\n"
            f"Address: {record.address or 'N/A'}\n"
            f"Email: {
                '; '.join(email.value for email in record.emails) or 'N/A'}\n" + "=" * 30
            for record in records
        )

    return f"Contacts with '{partial_name}' in name don't exist."


@input_error
def add_note(args: list[str], notes_book: "NoteBook") -> str:
    """Adds a note to a contact in the notes book.

    param: args: List with 2 values: name and note.
    param: notes_book: NoteBook object to modify.
    return: str: Result message.
    """

    name, note = args
    note_title: str = f"note-{len(notes_book.values())+1}"
    notes_book.add(note_title, note)
    notes_book.attach_to_contact(note_title, name)
    return "Note added."


@input_error
def edit_note(args: list[str], notes_book: "NoteBook") -> str:
    """Edits a note in the notes dictionary.

    param: args: List with 2 values: note title and new body.
    param: notes_book: Notes dictionary to modify.
    return: str: Result message.
    """

    note_title, new_body = args
    if note_in_notebook := notes_book.find(note_title):
        notes_book.edit(note_title, new_body)
        return f"Note edited to -{note_in_notebook.body}."
    return "Note not found."


@input_error
def replace_note(args: list[str], notes_book: "NoteBook") -> str:
    """Replaces a note_body in the notes dictionary.

    param: args: List with 2 values: note title and new body.
    param: notes_book: Notes dictionary to modify.
    return: str: Result message.
    """
    note_title, new_body = args
    if note_in_notebook := notes_book.find(note_title):
        notes_book.replace(note_title, new_body)
        return f"Note replaced to -{note_in_notebook.body}."
    return "Note not found."


def show_notes(notes_book: "NoteBook") -> str:
    """Shows all notes from the notes dictionary.

    param: notes_book: Notes dictionary to read from.
    return: str: Result message.
    """
    print(notes_book.show_all())
    return notes_book.show_all()


@input_error
def show_notes_contact(name: str, notes_book: "NoteBook") -> str:
    """Shows all notes from the notes dictionary.

    param: notes_book: Notes dictionary to read from.
    return: str: Result message.
    """
    return notes_book.show_all_for_contact(name)


@input_error
def add_tag(args: list[str], notes_book: "NoteBook") -> str:
    """Adds a tag to a note in the notes dictionary.

    param: args: List with 2 values: note title and tag.
    param: notes_book: Notes dictionary to modify.
    return: str: Result message.
    """
    note_title, tag = args
    if note_in_notebook := notes_book.find(note_title):
        notes_book.add_tag(note_title, tag)
        return f"Tag added to note -{note_in_notebook.title}."
    return "Note not found."


@input_error
def remove_tag(args: list[str], notes_book: "NoteBook") -> str:
    """Removes a tag from a note in the notes dictionary.

    param: args: List with 2 values: note title and tag.
    param: notes_book: Notes dictionary to modify.
    return: str: Result message.
    """
    note_title, tag = args
    if note_in_notebook := notes_book.find(note_title):
        notes_book.remove_tag(note_title, tag)
        return f"Tag {tag} removed from note -{note_in_notebook.title}."
    return "Note not found."


@input_error
def attach_note(args: list[str], notes_book: "NoteBook") -> str:
    """Attaches a note to a contact in the notes dictionary.

    param: args: List with 2 values: note title and contact name.
    param: notes_book: Notes dictionary to modify.
    return: str: Result message.
    """

    note_title, contact_name = args
    if note_in_notebook := notes_book.find(note_title):
        notes_book.attach_to_contact(note_title, contact_name)
        return f"Note {note_in_notebook} attached to-{note_in_notebook.contacts}."
    return "Note not found."


def search_notes(query: str, notes_book: "NoteBook") -> str:
    """Searches for notes containing the query in their title or body.

    param: query: str: The query to search for.
    param: notes_book: Notes dictionary to read from.
    return: str: Result message.
    """

    return notes_book.search(query)


def delete_note(note_title: str, notes_book: "NoteBook") -> str:
    """Deletes a note from the notes dictionary.

    param: note_title: str: The title of the note to delete.
    param: notes_book: Notes dictionary to modify.
    return: str: Result message.
    """

    if note_in_notebook := notes_book.find(note_title):
        notes_book.delete(note_title)

        return f"Note {note_in_notebook.title} deleted."
    return "Note not found."


def find_by_tag(tag: str, notes_book: "NoteBook") -> list[str]:
    """Finds all notes with a specific tag.

    param: tag: str.
    param: notes_book: Notes dictionary to read from.
    return: list: Result message.
    """

    print(notes_book.find_by_tag(tag))
    return notes_book.find_by_tag(tag)


def sort_by_tag(tag: str, notes_book: "NoteBook") -> str:
    """Sorts notes by tag.

    param: tag: str: The tag to sort by.
    param: notes_book: Notes dictionary to read from.
    return: str: Result message.
    """
    print(notes_book.sort_by_tag(tag))
    return notes_book.sort_by_tag(tag)


my_notes = NoteBook()

add_note(["John", "This is a note"], my_notes)
add_note(["John", "This is another note"], my_notes)
add_tag(["note-1", "important"], my_notes)
add_tag(["note-2", "urgent"], my_notes)
find_by_tag("important", my_notes)
