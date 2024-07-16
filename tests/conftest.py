from typing import Any, Callable, Generator

import pytest

from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client() -> Generator[TestClient, Any, None]:
    """
    Returns a TestClient instance for testing the FastAPI application
    and clears any dependency overrides after the test.

    Yields:
        TestClient: A TestClient instance for testing the FastAPI application.

    Example:
        ```def test_ping_endpoint(client: TestClient) -> None:
            response = client.get("/ping")
            assert response.status_code == 200
        ```
    """
    yield TestClient(app)
    app.dependency_overrides = {}
    print("Tests: Application dependency overrides cleared.")


def override_dependency(dependency: Callable[..., Any], mocked_response: Any):
    """
    Overrides a dependency with a mocked response.

    Parameters:
        dependency (Callable[..., Any]): The dependency to override.
        mocked_response (Any): The mocked response to use.

    Returns:
        None

    Example:
        `override_dependency(get_data, mocked_data)`
    """
    app.dependency_overrides[dependency] = lambda: mocked_response
