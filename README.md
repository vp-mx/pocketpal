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

### Contribution

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/vp-mx/pocketpal.git
   ```
2. Create a virtual environment in the project directory: `python -m venv .venv`
3. Activate the virtual environment:
    - Mac, Linux
   ```bash
   source .venv/bin/activate
   ```
    - Windows
   ```bash
   .venv\Scripts\activate
   ```
4. Install the required packages: `pip install -r requirements.txt`
5. Make changes to the code
6. Run the application: `python src` and test your changes
7. Create a new branch
   ```bash
    git checkout -b <branch_name>
   ```
8. Commit your changes:

   ```bash
   git commit -m "Your message"
   ```

9. Push to the branch: 
   ```bash
   git push origin <branch_name>
   ```
10. Create a pull request on GitHub, add reviewers, and wait for approval
11. Merge the pull request
12. Profit!

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
Pre-commit hooks are configured to automatically run `black`, `isort` and `pylint` to ensure consistent formatting and code quality..

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

Skip pre-commit checks before a commit:

```bash
git commit --no-verify
```
