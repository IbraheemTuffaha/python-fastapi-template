from fastapi.testclient import TestClient


def test_create_duplicate_user(client: TestClient) -> None:
    user_data = {"username": "duplicate", "email": "duplicate@example.com"}
    client.post("/v1/users/", json=user_data)

    # Try to create a user with the same username
    response = client.post("/v1/users/", json=user_data)
    assert response.status_code == 409


def test_get_nonexistent_user(client: TestClient) -> None:
    response = client.get("/v1/users/nonexistent")
    assert response.status_code == 404


def test_update_nonexistent_user(client: TestClient) -> None:
    user_data = {"username": "nonexistent", "email": "nonexistent@example.com"}
    response = client.put("/v1/users/nonexistent", json=user_data)
    assert response.status_code == 404


def test_delete_nonexistent_user(client: TestClient) -> None:
    response = client.delete("/v1/users/nonexistent")
    assert response.status_code == 404


def test_create_user_invalid_data(client: TestClient) -> None:
    response = client.post("/v1/users/", json={"username": "", "email": "not-an-email"})
    assert response.status_code == 422


def test_update_user_username_mismatch(client: TestClient) -> None:
    user_data = {"username": "u1", "email": "u1@example.com"}
    client.post("/v1/users/", json=user_data)
    updated_data = {"username": "u2", "email": "new@example.com"}
    response = client.put("/v1/users/u1", json=updated_data)
    assert response.status_code == 400
