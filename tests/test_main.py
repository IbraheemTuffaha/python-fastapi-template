from fastapi.testclient import TestClient


def test_ping_endpoint(client: TestClient) -> None:
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == "pong"
