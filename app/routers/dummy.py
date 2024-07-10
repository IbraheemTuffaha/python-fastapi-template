from fastapi import APIRouter

router = APIRouter()


@router.get("/ping", name="ping")
def ping() -> str:
    return "pong"
