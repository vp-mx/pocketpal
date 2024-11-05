"""This module contains the functions to perform actions on the address book."""

import pickle

from models.address_book import AddressBook, Record
from utils.error_handlers import input_error

FILE_PKL = "address_book.pkl"


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
def change_contact(args: list[str], book: "AddressBook") -> str:
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
    if len(args) != 1:
        return "Invalid command format. Use: phone [name]"
    if record := book.find(args[0]):
        return record.all_phones
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


def save_data(book: "AddressBook", filename: str = FILE_PKL) -> None:
    """Saves the address book to a file.

    param: book: AddressBook object to save.
    param: filename: File name to save the data.
    """

    with open(filename, "wb") as pkl_file:
        pickle.dump(book, pkl_file)


def load_data(filename: str = FILE_PKL):
    """Loads the address book from a file.

    param: filename: File name to load the data.
    return: AddressBook object.
    """
    try:
        with open(filename, "rb") as pkl_file:
            return pickle.load(pkl_file)
    except FileNotFoundError:
        return AddressBook()
