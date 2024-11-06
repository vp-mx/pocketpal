"""This module contains functions to save, load and delete the address book and notes book from a file."""

import os
import pickle
from pathlib import Path
from typing import TYPE_CHECKING, Union

if TYPE_CHECKING:
    from address_book import AddressBook
    from notes import NoteBook

FOLDER_FOR_PKL = Path().home() / "PocketPal"
ADDRESS_BOOK_FILE = "pocket-pal-book.pkl"
NOTES_FILE = "pocket-pal-notes.pkl"


def save_data(book: Union["AddressBook", "NoteBook"], file_name: str) -> None:
    """Saves the address book to a file.

    param: book: AddressBook object to save.
    param: filename: File name to save the data.
    """
    filepath = FOLDER_FOR_PKL / file_name
    os.makedirs(filepath.parent, exist_ok=True)
    with open(filepath, "wb") as pkl_file:
        pickle.dump(book, pkl_file)


def load_data(filename):
    """Loads the address book from a file.

    param: filename: File name to load the data.
    return: AddressBook object.
    """
    try:
        filepath = FOLDER_FOR_PKL / filename
        with open(filepath, "rb") as pkl_file:
            return pickle.load(pkl_file)
    except FileNotFoundError:
        return None


def delete_data(filename):
    """Deletes the address or notes book from a file.

    param: filename: File name to delete the data.
    """
    try:
        filepath = FOLDER_FOR_PKL / filename
        os.remove(filepath)
    except FileNotFoundError:
        pass
