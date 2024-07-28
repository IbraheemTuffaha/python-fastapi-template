from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from app.routers import dummy


app = FastAPI()

app.include_router(dummy.router)


@app.get("/up")
async def up() -> str:
    return "ok"


@app.get("/")
async def root() -> RedirectResponse:
    return RedirectResponse(url="/docs")
