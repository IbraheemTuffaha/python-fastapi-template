from fastapi.testclient import TestClient


def test_create_user(client: TestClient) -> None:
    user_data = {"username": "testuser", "email": "test@example.com"}
    response = client.post("/v1/users/", json=user_data)
    assert response.status_code == 200
    assert response.json() == user_data


def test_get_user(client: TestClient) -> None:
    # First, create a user
    user_data = {"username": "getuser", "email": "get@example.com"}
    client.post("/v1/users/", json=user_data)

    # Then, retrieve the user
    response = client.get("/v1/users/getuser")
    assert response.status_code == 200
    assert response.json() == user_data


def test_list_users(client: TestClient) -> None:
    # Create two users
    user1 = {"username": "user1", "email": "user1@example.com"}
    user2 = {"username": "user2", "email": "user2@example.com"}
    client.post("/v1/users/", json=user1)
    client.post("/v1/users/", json=user2)

    # List all users
    response = client.get("/v1/users/")
    assert response.status_code == 200
    assert len(response.json()) >= 2
    assert user1 in response.json()
    assert user2 in response.json()


def test_update_user(client: TestClient) -> None:
    # First, create a user
    original_data = {"username": "updateuser", "email": "original@example.com"}
    client.post("/v1/users/", json=original_data)

    # Then, update the user
    updated_data = {"username": "updateuser", "email": "updated@example.com"}
    response = client.put("/v1/users/updateuser", json=updated_data)
    assert response.status_code == 200
    assert response.json() == updated_data


def test_delete_user(client: TestClient) -> None:
    # First, create a user
    user_data = {"username": "deleteuser", "email": "delete@example.com"}
    client.post("/v1/users/", json=user_data)

    # Then, delete the user
    response = client.delete("/v1/users/deleteuser")
    assert response.status_code == 200
    assert response.json() == user_data

    # Verify the user is deleted
    response = client.get("/v1/users/deleteuser")
    assert response.status_code == 404


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
