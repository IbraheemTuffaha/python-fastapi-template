from fastapi.testclient import TestClient


def test_capitalize_endpoint(client: TestClient) -> None:
    response = client.post("/v1/dummy/capitalize", json={"text": "hello"})
    assert response.status_code == 200
    assert response.json() == {"text": "HELLO"}
