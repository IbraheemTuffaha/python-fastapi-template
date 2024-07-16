from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from app.v1.routers import router as v1_router


app = FastAPI()

app.include_router(v1_router)


@app.get("/up")
async def up() -> str:
    return "ok"


@app.get("/")
async def root() -> RedirectResponse:
    return RedirectResponse(url="/docs")
