from fastapi import APIRouter, Depends, HTTPException, status

from app.v1.dependencies import get_user_manager
from app.v1.models import User
from app.v1.services import UserManager


router = APIRouter()


@router.post("/")
async def create_user(user: User, user_manager: UserManager = Depends(get_user_manager)) -> User:
    try:
        return user_manager.create_user(user)
    except ValueError as ex:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(ex))


@router.get("/{username}")
async def get_user(username: str, user_manager: UserManager = Depends(get_user_manager)) -> User:
    try:
        return user_manager.get_user(username)
    except ValueError as ex:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(ex))


@router.get("/")
async def list_users(user_manager: UserManager = Depends(get_user_manager)) -> list[User]:
    return user_manager.list_users()


@router.put("/{username}")
async def update_user(username: str, user: User, user_manager: UserManager = Depends(get_user_manager)) -> User:
    try:
        return user_manager.update_user(username, user)
    except ValueError as ex:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(ex))


@router.delete("/{username}")
async def delete_user(username: str, user_manager: UserManager = Depends(get_user_manager)) -> User:
    try:
        return user_manager.delete_user(username)
    except ValueError as ex:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(ex))
