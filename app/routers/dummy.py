from fastapi import APIRouter

from app.requests import CapitalizeRequest
from app.responses import CapitalizeResponse


router = APIRouter(prefix="/dummy")


@router.post("/capitalize")
async def capitalize(request: CapitalizeRequest) -> CapitalizeResponse:
    return CapitalizeResponse(text=request.text.upper())
