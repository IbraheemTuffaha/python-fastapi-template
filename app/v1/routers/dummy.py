from fastapi import APIRouter

from app.v1.serializers import dummy as dummy_serializer


router = APIRouter()


@router.post("/capitalize", response_model=dummy_serializer.CapitalizeOut)
async def capitalize(request: dummy_serializer.CapitalizeIn) -> dict[str, str]:
    return {"text": request.text.upper()}
