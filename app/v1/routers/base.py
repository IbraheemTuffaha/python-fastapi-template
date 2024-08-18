from fastapi import APIRouter

from app.v1.routers.users import router as users_router


router = APIRouter(prefix="/v1")
router.include_router(users_router, prefix="/users", tags=["Users"])
