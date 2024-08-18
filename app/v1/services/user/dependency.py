from app.v1.services.user.user_manager import UserManager


def get_user_manager() -> UserManager:
    return UserManager()
