"""This module contains the functions to perform actions on the address book."""

from address_book import AddressBook, Record
from notes import NoteBook
from error_handlers import input_error


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
            f"Contact name: {record.name}; "
            f"phone: {record.all_phones}; "
            f"birthday: {record.birthday or 'N/A'}; "
            f"address: {record.address or 'N/A'}; "
            f"email: {
                '; '.join(email.value for email in record.emails) or 'N/A'}"
            for record in records
        )
    return f"Contacts with '{partial_name}' in name doesn't exist."


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
        note_title = len(notes_book.data) + 1

        record.add_note(note_title)
        notes_book.add(note_title, note)
        notes_book.attach_to_contact(note_title, name)

        return "Note added."
    return "Contact not found."
