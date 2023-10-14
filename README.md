# Template Data Science Project
## How to set up
### Set up the Python environment
#### Set up Poetry
Install Poetry package manager:

```console
curl -sSL https://install.python-poetry.org | python3 -
```
Check Poetry is properly installed:
```console
poetry --version
```
Set up Poetry config:
```console
poetry config virtualenvs.in-project true
```

#### Set up Python environment
Install all the Python packages and git pre-commit hooks locally within the project folder, in `.venv` subfolder. This will use `pyproject.toml` for the list of required packages.

(in the project folder)
```console
poetry install
poetry run pre-commit install
```
OR simply
```console
make env
```

Update or create `requirements.txt`:
```console
make freeze
```
(not required to run the code locally but may be useful for cloud installations)

### Environment variables
The code requires some credentials and API keys to run. There are two ways of providing them:
- environment variables. Provide the env variables listed in `template.env`. This option is more convenient for a cloud installation.
- `.env` file in the project root. You should manually create it. I do not provide my own `.env` file because of security reasons, but I put `template.env` as a template for the keys required. This option is better suited for a local installation.
