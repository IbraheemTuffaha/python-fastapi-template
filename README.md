<div align="center">

  [![pytest Action](https://github.com/IbraheemTuffaha/python-fastapi-template/actions/workflows/pytest.yml/badge.svg)](https://github.com/IbraheemTuffaha/python-fastapi-template/actions/workflows/pytest.yml)
  [![format Action](https://github.com/IbraheemTuffaha/python-fastapi-template/actions/workflows/format.yml/badge.svg)](https://github.com/IbraheemTuffaha/python-fastapi-template/actions/workflows/format.yml)
  [![Python Version](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2FIbraheemTuffaha%2Fpython-fastapi-template%2Fmain%2Fpyproject.toml&query=tool.poetry.dependencies.python&label=python&color=greenlime)](https://github.com/IbraheemTuffaha/python-fastapi-template/blob/main/pyproject.toml)
  [![GitHub License](https://img.shields.io/github/license/IbraheemTuffaha/python-fastapi-template?color=greenlime)](https://github.com/IbraheemTuffaha/python-fastapi-template/blob/main/LICENSE)
  [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=IbraheemTuffaha_python-fastapi-template&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=IbraheemTuffaha_python-fastapi-template)
</div>

# Python FastAPI Template

A template for a Python FastAPI service:
- [x] [Poetry](https://python-poetry.org/docs/basic-usage/) for dependency management
- [x] [FastAPI](https://fastapi.tiangolo.com/) for building the API
- [x] [Devcontainer](https://code.visualstudio.com/docs/devcontainers/tutorial) for development environment
- [x] [Docker](https://www.docker.com/) for containerization
- [x] [Black](https://black.readthedocs.io/) & [isort](https://pycqa.github.io/isort/) for code formatting
- [x] [pre-commit](https://pre-commit.com/) for code quality checks
- [x] [Github Actions](https://github.com/features/actions) for CI/CD
- [x] [pytest](https://docs.pytest.org/) for testing
- [ ] [Kamal](https://kamal-deploy.org/) for deployment (TODO: add Kamal deploy action)

## Build and run locally

Using `python3.12` install `poetry`:
```
pip install poetry
```

Then install dependencies
```
poetry install
```

Run locally
```
poetry run uvicorn app.main:app --port 8000 --reload
```

## Run tests
```
poetry run pytest
```

## Build and run using Docker

```
docker build -t app .
docker run -p 8000:8000 -it app
```

### Notes
- If you face an issue with **git ssh access** while pushing new changes, run `ssh-add $HOME/.ssh/<your ssh key>` in terminal outside the devcontainer.

- If you face an issue during **devcontainer build**, make sure the repo is marked as trusted in VSCode. Check `Source Control` tab in the sidebar to mark the repo safe, then rebuild the devcontainer.

## Sample CRUD API

The `/v1` directory contains a sample API router demonstrating basic CRUD operations for users:

- Endpoints: Create, Read, Update, Delete users
- Router setup: `app/v1/routers/base.py` and `app/v1/routers/users.py`
- User model: `app/v1/models/user.py`
- User management: `app/v1/services/user/user_manager.py`

Use the samples as a starting point for your own API endpoints. View available endpoints at `http://localhost:8000/docs`.
