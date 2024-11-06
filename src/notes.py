"""Module for storing classes related to the notes"""

from collections import UserDict
from datetime import datetime
from typing import List, Optional
from address_book import AddressBook, Record
from uuid import uuid4


class Note:
    """Class representing a note."""

    def __init__(self, title: str, body: str, tags: Optional[List[str]] = None, contacts: Optional[List[str]] = None) -> None:
        """Initialize the note.

        :param title: The title of the note.
        :param body: The body of the note.
        :param tags: A list of tags for the note.
        :param contacts: A list of contacts if the note is attached to a contact.
        """

        self.id = uuid4
        self.title = title
        self.body = body
        self.creation_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._tags = tags if tags else []
        self._contacts = contacts if contacts else []

    def edit(self, new_body: str) -> None:
        """Edit the note by adding something to the body."""
        self.body = self.body+' '+new_body

    def replace(self, new_body: str) -> None:
        """Edit the note by replacing the body."""
        self.body = new_body

    def attach_to_contact(self, contact_name: str) -> None:
        """Attach the note to a contact."""
        self._contacts.append(contact_name)

    def add_tag(self, tag: str) -> None:
        """Add a tag to the note."""
        if len(tag) < 0 and len(tag) > 20:
            raise ValueError("Tag must be between 1 and 20 characters")
        self._tags.append(tag)

    def remove_tag(self, tag: str) -> None:
        """Remove a tag from the note."""
        self._tags.remove(tag)

    def __repr__(self):
        return f"{self.id}-{self.__class__.__name__} ({self.title}, {self.creation_date}, {self.body}, {self._tags}, {self._contacts})"


my_note = Note('title', 'something here as body', [
               'tag1', 'tag2'], ['contact1', 'contact2'])
print(my_note)


class NoteBook(UserDict):
    """Class representing a collection of notes."""

    def add(self, title: str, body: str, tags: Optional[List[str]] = None, contacts: Optional[List[str]] = None) -> None:
        """Add a new note to the notebook."""
        self.data[title] = Note(title, body, tags, contacts)

    def delete(self, title: str) -> None:
        """Delete a note from the notebook by title."""
        if not title in self.data:
            return KeyError(f"Note with title {title} not found")
        del self.data[title]

    def edit(self, title: str, new_body: str) -> None:
        """Edit the body of an existing note."""
        if not title in self.data:
            return KeyError(f"Note with title {title} not found")
        return self.data[title].edit(new_body)

    def replace(self, title: str, new_body: str) -> None:
        """Edit the body of an existing note."""
        if not title in self.data:
            return KeyError(f"Note with title {title} not found")
        return self.data[title].replace(new_body)

    def search(self, query: str) -> List[Note]:
        """Search for notes containing the query in their title or body."""
        if query == "":
            return list(self.data.values())
        return [note for note in self.data.values() if query in note.title or query in note.body or query in note._tags or query in note._contacts]

    def add_tag(self, title: str, tag: str) -> None:
        """Add a tag to a note."""
        self.data[title].add_tag(tag)

    def remove_tag(self, title: str, tag: str) -> None:
        """Remove a tag from a note."""
        self.data[title].remove_tag(tag)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.data})"
