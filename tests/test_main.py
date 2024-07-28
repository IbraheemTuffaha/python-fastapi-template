from fastapi.testclient import TestClient


def test_up_endpoint(client: TestClient) -> None:
    response = client.get("/up")
    assert response.status_code == 200
    assert response.json() == "ok"


def test_root_endpoint(client: TestClient) -> None:
    response = client.get("/", follow_redirects=False)
    assert response.status_code == 307
    assert response.headers["location"] == "/docs"
