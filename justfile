list:
    @just --list

# TODO: Make these both work without relying on pip!
beepy-install:
    @sudo apt install python3-venv
    @python3 -m pip install pipx --force  # For upgrades
    @pipx install beepy_web_radio

beepy-remove:
    @pipx uninstall beepy_web_radio

run *args:
    @poetry run beepy_web_radio {{args}}

# Run the tests
test:
    @poetry run pytest tests

# Initialize the application
init:
    poetry install
    echo "Application initialized successfully."
    poetry run pre-commit install
    echo "Pre-commit hooks set up."
