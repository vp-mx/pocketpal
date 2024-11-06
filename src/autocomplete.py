from prompt_toolkit import PromptSession 
from prompt_toolkit.completion import Completer, Completion 
from prompt_toolkit.document import Document


commands = [
    "hello",

    "menu",

    "add",
    "phone",
    "change",
    "all",
    
    # Email-related commands
    "add-email",
    "edit-email",
    "remove-email",
    "show-email",
    
    # Birthday-related commands
    "add-birthday",
    "show-birthday",
    "birthdays",

    
    "close",
    "exit",    
]
class CommandCompleter(Completer):
    def get_completions(self, document: Document, complete_event) -> iter:

        if ' ' in document.text:
            parts = document.text.split()
            if len(parts) > 1:
                return
        
        for command in commands:
            if command.startswith(document.text):
                yield Completion(command, start_position=-len(document.text))


session = PromptSession(completer=CommandCompleter())
