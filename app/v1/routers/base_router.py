from fastapi import APIRouter

from app.v1.routers.users import users_router


router = APIRouter(prefix="/v1")
router.include_router(users_router.router, prefix="/users", tags=["Users"])
