from collections.abc import Callable, Generator
from typing import Any

import pytest

from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client() -> Generator[TestClient, Any, None]:
    yield TestClient(app)
    app.dependency_overrides = {}


def override_dependency(dependency: Callable[..., Any], mocked_response: Any) -> None:
    app.dependency_overrides[dependency] = lambda: mocked_response
