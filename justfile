list:
    @just --list

# TODO: Make these both work without relying on pip!
beepy-install:
    @python -m pip install beepy_web_radio

beepy-remove:
    @python -m pip uninstall beepy_web_radio

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
