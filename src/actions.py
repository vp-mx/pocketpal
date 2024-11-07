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
    if len(args) != 2:
        return "Invalid command format. Use: add [name] [phone]"
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
    if len(args) != 1:
        return "Invalid command format. Use: remove [name]"
    if book.find(args[0]):
        book.delete(args[0])
        return "Contact removed."
    return "Contact not found."


@input_error
def change_phone(args: list[str], book: "AddressBook") -> str:
    """Changes the phone number of a contact in the address book.

    param: args: List with 3 values: name, old phone, new phone.
    param: book: AddressBook object to modify.
    return: str: Result message.
    """
    if len(args) != 3:
        return "Invalid command format. Use: change [name] [old phone] [new phone]"
    name, old_phone, new_phone = args
    if record := book.find(name):
        record.edit_phone(old_phone, new_phone)
        return "Phone number updated."
    return "Contact not found."


@input_error
def show_phone(args: list[str], book: "AddressBook") -> str:
    """Shows the phone number of a contact from the address book.

    param: args: List with 1 value: name.
    param: book: AddressBook object to read from.
    return: str: Result message.
    """
    name = args[0]
    if len(args) != 1:
        return "Invalid command format. Use: phone [name]"
    if record := book.find(name):
        return f"{name}'s phones: {record.all_phones}"
    return "Contact not found."


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
    if len(args) != 2:
        return "Invalid command format. Use: add-birthday [name] [birthday]"
    name, birthday = args
    if record := book.find(name):
        record.add_birthday(birthday)
        return "Birthday added."
    return "Contact not found."


@input_error
def show_birthday(args: list[str], book: "AddressBook") -> str:
    """Shows the birthday of a contact from the address book.

    param: args: List with 1 value: name.
    param: book: AddressBook object to read from.
    return: str: Result message.
    """
    if len(args) != 1:
        return "Invalid command format. Use: show-birthday [name]"
    if record := book.find(args[0]):
        return str(record.birthday) if record.birthday else "N/A"
    return "Contact not found."


@input_error
def birthdays(book: "AddressBook") -> str:
    """Shows all birthdays in next 7 days.

    param: book: AddressBook object to read from.
    return: str: Result message.
    """
    return book.get_upcoming_birthdays()


@input_error
def add_address(args: list[str], book: "AddressBook") -> str:
    """Adds an address to a contact in the address book.
    param: args: List with 2 values: name and address.
    param: book: AddressBook object to modify.
    return: str: Result message.
    """
    if len(args) != 2:
        return "Invalid command format. Use: add-address [name] [address]"
    name, address = args
    if record := book.find(name):
        record.add_address(address)
        return "Address added."
    return "Contact not found."


@input_error
def add_email(args, book):
    """Add an email to a contact.

    param: args: List with 2 values - name and email.
    param: book: AddressBook object to read from.
    return: str: Result message.
    """

    name, email = args

    record = book.find(name)

    if record:
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
    if len(args) != 3:
        return "Invalid command format. Use: edit-email [name] [old email] [new email]"

    name, old_email, new_email = args
    record = book.find(name)
    if record:
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

    record = book.find(name)
    if record:
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

    record = book.find(name)
    if record:
        return (
            "Contact doesn't have any emails"
            if not record.emails
            else "; ".join(email.value for email in record.emails)
        )

    return f"Contact '{name}' doesn't exist."


def add_note(args: list[str], book: "AddressBook", notes_book: "NoteBook") -> str:
    """Adds a note to a contact in the address book.

    param: args: List with 2 values: name and note.
    param: book: AddressBook object to modify.
    param: notes_book: NoteBook object to modify.
    return: str: Result message.
    """
    if len(args) != 2:
        return "Invalid command format. Use: add-note [name] [note]"
    name, note = args
    if record := book.find(name):
        note_title = f"note-{len(notes_book.values())}"
        record.add_note(note_title)
        notes_book.add(note_title, note)
        notes_book.attach_to_contact(note_title, name)
        return "Note added."
    return "Contact not found."


def edit_note(args: list[str], notes_book: "NoteBook") -> str:
    """Edits a note in the notes dictionary.

    param: args: List with 2 values: note title and new body.
    param: notes_book: Notes dictionary to modify.
    return: str: Result message.
    """
    if len(args) != 2:
        return "Invalid command format. Use: edit-note [note title] [new body]"
    note_title, new_body = args
    if note_in_notebook := notes_book.find(note_title):
        notes_book.edit(note_title, new_body)
        return f"Note edited to -{note_in_notebook.body}."
    return "Note not found."


def replace_note(args: list[str], notes_book: "NoteBook") -> str:
    """Edits a note in the notes dictionary.

    param: args: List with 2 values: note title and new body.
    param: notes_book: Notes dictionary to modify.
    return: str: Result message.
    """
    if len(args) != 2:
        return "Invalid command format. Use: replace-note [note title] [new body]"
    note_title, new_body = args
    if note_in_notebook := notes_book.find(note_title):
        notes_book.replace(note_title, new_body)
        return f"Note replaced to -{note_in_notebook.body}."
    return "Note not found."


def show_all_notes(notes_book: "NoteBook") -> str:
    """Shows all notes from the notes dictionary.

    param: notes_book: Notes dictionary to read from.
    return: str: Result message.
    """
    return notes_book.show_all()


def show_all_notes_contact(name: str, notes_book: "NoteBook") -> str:
    """Shows all notes from the notes dictionary.

    param: notes_book: Notes dictionary to read from.
    return: str: Result message.
    """
    return notes_book.show_all_for_contact(name)


def add_note_tag(args: list[str], notes_book: "NoteBook") -> str:
    """Adds a tag to a note in the notes dictionary.

    param: args: List with 2 values: note title and tag.
    param: notes_book: Notes dictionary to modify.
    return: str: Result message.
    """
    if len(args) != 2:
        return "Invalid command format. Use: add-tag [note title] [tag]"

    note_title, tag = args
    if note_in_notebook := notes_book.find(note_title):
        notes_book.add_tag(note_title, tag)
        return f"Tag added to note -{note_in_notebook.title}."
    return "Note not found."


def remove_note_tag(args: list[str], notes_book: "NoteBook") -> str:
    """Removes a tag from a note in the notes dictionary.
    param: args: List with 2 values: note title and tag.
    param: notes_book: Notes dictionary to modify.
    return: str: Result message.
    """
    if len(args) != 2:
        return "Invalid command format. Use: remove-tag [note title] [tag]"

    note_title, tag = args
    if note_in_notebook := notes_book.find(note_title):
        notes_book.remove_tag(note_title, tag)
        return f"Tag {tag} removed from note -{note_in_notebook.title}."
    return "Note not found."


def attach_to_contact(args: list[str], notes_book: "NoteBook") -> str:
    """Attaches a note to a contact in the notes dictionary.
    param: args: List with 2 values: note title and contact name.
    param: notes_book: Notes dictionary to modify.
    return: str: Result message.
    """
    if len(args) != 2:
        return "Invalid command format. Use: attach-to-contact [note title] [contact name]"

    note_title, contact_name = args
    if note_in_notebook := notes_book.find(note_title):
        notes_book.attach_to_contact(note_title, contact_name)
        return f"Note {note_in_notebook} attached to-{note_in_notebook.contacts}."
    return "Note not found."


def search_in_notes(args: list[str], notes_book: "NoteBook") -> str:
    """Searches for notes containing the query in their title or body.

    param: args: List with 1 value: query.
    param: notes_book: Notes dictionary to read from.
    return: str: Result message.
    """
    if len(args) != 1:
        return "Invalid command format. Use: search [query]"
    return notes_book.search(args[0])


def delete_note(args: list[str], notes_book: "NoteBook") -> str:
    """Deletes a note from the notes dictionary.

    param: args: List with 1 value: note title.
    param: notes_book: Notes dictionary to modify.
    return: str: Result message.
    """
    if len(args) != 1:
        return "Invalid command format. Use: delete-note [note title]"
    if note_in_notebook := notes_book.find(args[0]):
        notes_book.delete(args[0])
        return f"Note {note_in_notebook.title} deleted."
    return "Note not found."


def find_by_tag(args: list[str], notes_book: "NoteBook") -> list[str]:
    """Finds all notes with a specific tag.

    param: args: List with 1 value: tag.
    param: notes_book: Notes dictionary to read from.
    return: list: Result message.
    """
    if len(args) != 1:
        return "Invalid command format. Use: find-by-tag [tag]"
    return notes_book.find_by_tag(args[0])
