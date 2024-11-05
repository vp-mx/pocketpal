"""Module for storing classes related to the notes"""
from collections import UserDict
from datetime import datetime
from typing import Optional, List


class Note:
    """Class representing a note."""

    def __init__(self, title: str, body: str, tags: Optional[List[str]] = None) -> None:
        """Initialize the note.

        :param title: The title of the note.
        :param body: The body of the note.
        :param tags: A list of tags for the note.
        """

        self.title = title
        self.body = body
        self.creation_date = datetime.now()
        self._tags = tags if tags else []

    def edit(self, new_body: str) -> None:
        """Edit the note by changing the body."""

    def attach_to_contact(self, contact_name: str) -> None:
        """Attach the note to a contact."""

    def add_tag(self, tag: str) -> None:
        """Add a tag to the note."""

    def remove_tag(self, tag: str) -> None:
        """Remove a tag from the note."""


class NoteBook(UserDict):
    """Class representing a collection of notes."""

    def add(self, title: str, body: str, tags: Optional[List[str]] = None) -> None:
        """Add a new note to the notebook."""

    def delete(self, title: str) -> None:
        """Delete a note from the notebook by title."""

    def edit(self, title: str, new_body: str) -> None:
        """Edit the body of an existing note."""

    def search(self, query: str) -> List[Note]:
        """Search for notes containing the query in their title or body."""

    def add_tag(self, title: str, tag: str) -> None:
        """Add a tag to a note."""

    def remove_tag(self, title: str, tag: str) -> None:
        """Remove a tag from a note."""
