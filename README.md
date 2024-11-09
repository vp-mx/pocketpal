# PocketPal

### Description

PocketPal is a terminal application that allows users to create, read, update, and delete contacts.

Users can also view all contacts, view contact by name, and search for contacts by keyword.
Also implemented opportunity to save notes separate from contacts.
User can save, edit, delete and search note by title.
Also added opportunity to add tags to any note, delete tag and find note by tag.

### Installation

1. Install app using pip

   ```bash
   pip install git+https://github.com/vp-mx/pocketpal.git
   ```

2. Run PocketPal

   ```bash
   python -m pocketpal
   ```

3. Enjoy!


### Usage

Write a command in the terminal to interact with the application. User can use the next commands:


| Command             | Description                                  | Usage                                                           |
|---------------------|----------------------------------------------|-----------------------------------------------------------------|
| `add`               | Adds a contact to the address book.          | `add <name> <phone>` (Use `_` to separate first and last names) |
| `add-address`       | Adds an address to a contact.                | `add-address <name> <address>`                                  |
| `add-birthday`      | Adds a birthday to a contact.                | `add-birthday <name> <birthday>`                                |
| `add-email`         | Adds an email to a contact.                  | `add-email <name> <email>`                                      |
| `all`               | Shows all contacts in the address book.      | `all`                                                           |
| `birthdays`         | Shows upcoming birthdays.                    | `birthdays <days_interval>`                                     |
| `change`            | Changes contact's phone.                     | `change <name> <old_phone> <new_phone>`                         |
| `edit-email`        | Edits the email of a contact.                | `edit-email <name> <old_email> <new_email>`                     |
| `phone`             | Shows the phone number of a contact.         | `phone <name>`                                                  |
| `remove`            | Removes a contact from the address book.     | `remove <name>`                                                 |
| `remove-email`      | Removes the email of a contact.              | `remove-email <name> <email>`                                   |
| `search`            | Searches for contacts by partial name.       | `search <partial_name>`                                         |
| `show-birthday`     | Shows the birthday of a contact.             | `show-birthday <name>`                                          |
| `show-email`        | Shows the email of a contact.                | `show-email <name>`                                             |
| `add-note`          | Adds a note.                                 | `add-note <title> <note>`                                       |
| `add-tag`           | Adds a tag to a note.                        | `add-tag <note_title> <tag>`                                    |
| `delete-note`       | Deletes a note.                              | `delete-note <note>`                                            |
| `edit-note`         | Edits a note.                                | `edit-note <note_title> <new_body>`                             |
| `find-by-tag`       | Finds notes by tag.                          | `find-by-tag <tag>`                                             |
| `remove-tag`        | Removes a tag from a note.                   | `remove-tag <note_title> <tag>`                                 |
| `replace-note`      | Replaces a note.                             | `replace-note <note_title> <new_body>`                          |
| `search-notes`      | Searches notes.                              | `search-notes <query>`                                          |
| `show-notes`        | Shows all notes.                             | `show-notes`                                                    |
| `show-notes-contact`| Shows all notes of a contact.                | `show-notes-contact <name>`                                     |
| `sort-by-tag`       | Sorts notes by tag.                          | `sort-by-tag <tag>`                                             |
| `attach-note`       | Attaches a note to a contact.                | `attach-note <note_title> <contact_name>`                       |
| `cleanup`           | Cleans up dump files from the system.        | `cleanup <all \| address-book \| notes>`                        |
| `import`            | Imports contacts and notes from a CSV file.  | `import`                                                        |
| `close`             | Closes the assistant bot.                    | `close`                                                         |
| `exit`              | Exits the assistant bot.                     | `exit`                                                          |
| `help`              | Shows the list of available commands.        | `help`                                                          |
