"""This module implements autocomplete functionality for the application."""

from prompt_toolkit.completion import Completer, Completion

from commands import Commands


class CommandCompleter(Completer):
    """
    Class for handling autocompletion using the prompt_toolkit library.
    """

    def __init__(self, book, notes):
        """Initialize the CommandCompleter class."""
        self.book = book
        self.notes = notes

    def get_completions(self, document, complete_event):

        text = document.text_before_cursor.strip()
        words = text.split()
        if len(words) == 1 and not document.text_before_cursor.endswith(" "):

            for command in Commands.get_commands_list():
                if document.text in command:
                    yield Completion(command, start_position=-len(document.text))

        elif (len(words) == 1 and document.text_before_cursor.endswith(" ")) or (
            len(words) == 2 and not document.text_before_cursor.endswith(" ")
        ):

            command = words[0]
            if command in [
                "add-address",
                "add-phone",
                "add-email",
                "add-birthday",
                "change",
                "edit-email",
                "edit-phone",
            ]:

                options = (
                    [rec.name.value for rec in self.book.values() if words[1] in rec.name.value]
                    if len(words) == 2
                    else [rec.name.value for rec in self.book.values()]
                )
            elif command in ["add-tag", "remove-tag", "delete-note", "edit-note"]:
                options = (
                    [note for note in self.notes.data.keys() if words[1] in note]
                    if len(words) == 2
                    else self.notes.data.keys()
                )
            elif command == "cleanup":
                options = ["all", "address-book", "notes"] if len(words) == 2 else []
            else:
                options = []
            for opt in options:
                yield Completion(opt, start_position=-(len(words[1]) if len(words) == 2 else 0))
