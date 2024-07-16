from fastapi import APIRouter

from .dummy import router as dummy_router


router = APIRouter(prefix="/v1")
router.include_router(dummy_router, prefix="/dummy", tags=["Dummy"])
