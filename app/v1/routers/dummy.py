from fastapi import APIRouter

from app.v1.serializers import dummy as dummy_serializer


router = APIRouter()


@router.post("/capitalize")
async def capitalize(request: dummy_serializer.Capitalize) -> dummy_serializer.Capitalize:
    return dummy_serializer.Capitalize(text=request.text.upper())
