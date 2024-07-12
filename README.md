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
