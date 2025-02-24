curl -LsSf https://astral.sh/uv/install.sh | sh
uv sync --frozen
uv run pre-commit install
