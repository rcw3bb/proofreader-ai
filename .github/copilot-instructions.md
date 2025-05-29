Project info:
- Project name: proofreader-ai
- Project description: An AI-driven proofreading API.
- Version: 1.1.0
- Author name: Ron Webb
- Author email: ron@ronella.xyz
- Main package: proofreader_ai

Technology stack:
- Python `^3.13` for the scripting language
- Poetry `2.0` for dependency management

Poetry setup:
- Use `poetry init` to create the initial project structure.
- Use `poetry add` to add new dependencies.
- Use `poetry add --dev` to add new development dependencies.

Git setup:
- Create a `.gitignore` file to exclude IDE files, Python cache files, log files, and other unnecessary files.
- Create a `.gitattributes` file to ensure consistent line endings across different operating systems. Prefer LF line endings.

Dev dependencies:
- Black for code formatting
- Pylint for linting
- Pytest for testing
- Pytest-Cov for test coverage

Pylint setup: 
- Includes a default `.pylintrc` file for Pylint configuration.
- Do not disable missing docstrings (C0114, C0115, C0116).
- Use a max line length of 120 characters.

Project structure:
```
"Main package"/__init__.py
tests/__init__.py
.pylintrc
poetry.lock
pyproject.toml
CHANGELOG.md
README.md
```

Coding standards:
- Place all new modules into main package.
- Place all tests in the `tests` package, mirroring the main package structure where possible.
- The test modules should be named `test_*.py` and placed in the same directory as the module they are testing.
- The test packages must mirror the structure of the source code packages.
- Use relative imports within the package.
- Only add comments if the code is not self-explanatory.
- Always add docstrings to all modules, functions and classes. For modules, add author and since using application version.
- Use type hints for all function and method signatures.
- Avoid using deprecated types from the `typing` module. Use `collections.abc` instead.
- Use snake_case for functions and variables, PascalCase for classes, and UPPER_CASE for constants.
- Maintain a minimum test coverage of 80% for the project.
- To run tests with coverage and generate an HTML report, use:
  `poetry run pytest --cov=proofreader_ai tests --cov-report html`
- To format and lint the code in one step, use:
  `poetry run black proofreader_ai && poetry run pylint proofreader_ai`