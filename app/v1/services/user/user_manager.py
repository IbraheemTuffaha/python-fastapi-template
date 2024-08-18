from app.v1.models import User


class UserManager:
    _users: dict[str, User] = {}

    def create_user(self, user: User) -> User:
        if user.username in self._users:
            raise ValueError(f"User with username '{user.username}' already exists")
        self._users[user.username] = user
        return user

    def get_user(self, username: str) -> User:
        if username not in self._users:
            raise ValueError(f"User with username '{username}' does not exist")
        return self._users[username]

    def list_users(self) -> list[User]:
        return list(self._users.values())

    def update_user(self, username: str, user: User) -> User:
        if username not in self._users:
            raise ValueError(f"User with username '{username}' does not exist")
        self._users[username] = user
        return user

    def delete_user(self, username: str) -> User:
        if username not in self._users:
            raise ValueError(f"User with username '{username}' does not exist")
        return self._users.pop(username)
