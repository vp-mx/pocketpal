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
