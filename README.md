# PocketPal

### Description
PocketPal is a terminal application that allows users to create, read, update, and delete contacts. Users can also view all contacts, view contact by name, and search for contacts by keyword. Also implemented opportunity to save notes separate from contacts. User can save, edit, delete and search note by title. Also added opportunity to add tags to any note, delete tag and find note by tag.

### Installation

1. Clone the repository
2. Create a virtual environment in the project directory: `python -m venv .venv`
3. Activate the virtual environment: `source .venv/bin/activate`
4. Install the required packages: `pip install -r requirements.txt`
5. Run the application: `python main.py`
6. Enjoy!

### Usage

Write a command in the terminal to interact with the application. User can use the next commands:

- `hello`: Print a greeting message.
- `close` or `exit`: Save data and exit the application.
- `add <name> <phone>`: Add a new contact.
- `change <name> <new_phone>`: Change an existing contact's phone number.
- `phone <name>`: Show the phone number of a contact.
- `all`: Show all contacts.
- `add-birthday <name> <date>`: Add a birthday to a contact.
- `show-birthday <name>`: Show the birthday of a contact.
- `birthdays`: Show upcoming birthdays within the next 7 days.

### Code style

This project follows the PEP 8 code style.
pre-commit hooks are set up to run `black` and `pylint` before each commit.

### Pre Commit

To install pre-commit hooks, run the following command:

Install the required packages: `pip install pre-commit`

Then, run the following command:
```bash
pre-commit install
```
To perform the pre-commit checks manually, run the following command:
```bash
pre-commit run --all-files
```
To force pre-commit checks to run even if nothing has changed in the files, run the following command:
```bash
pre-commit run --all-files --show-diff-on-failure
```
Skip pre-commit checks before a commit:
```bash
git commit --no-verify
```
