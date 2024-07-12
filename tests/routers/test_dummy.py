from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_capitalize_endpoint() -> None:
    response = client.post("/dummy/capitalize", json={"text": "hello"})
    assert response.status_code == 200
    assert response.json() == {"text": "HELLO"}
