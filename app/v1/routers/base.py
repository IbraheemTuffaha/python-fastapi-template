from fastapi import APIRouter

from app.v1.routers.dummy import router as dummy_router


router = APIRouter(prefix="/v1")
router.include_router(dummy_router, prefix="/dummy", tags=["Dummy"])
