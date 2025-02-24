FROM python:3.12-slim

WORKDIR /code

# Install the application dependencies.
RUN --mount=from=ghcr.io/astral-sh/uv,source=/uv,target=/bin/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-cache

# Copy the application into the container.
COPY ./app /code/app

RUN groupadd -r nonroot && useradd -r -g nonroot nonroot
USER nonroot

CMD ["/code/.venv/bin/uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
