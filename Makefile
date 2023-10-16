#################################################################################
# GLOBALS                                                                       #
#################################################################################

PYTHON_INTERPRETER = python3
PIP = ./.venv/bin/pip3 

#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Export dependencies for prod
freeze:
	poetry export --without-hashes -o requirements.txt

f: freeze

## Install development & testing environment
env:
	poetry install
	poetry run pre-commit install

## Run OkGPT bot
run:
	poetry run python -m app

r: run

## Test python environment is setup correctly
test_env:
	$(PYTHON_INTERPRETER) test_environment.py

## Lint and test
pretty:
	poetry run pre-commit run --all-files

p: pretty

## Delete all compiled Python files
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
