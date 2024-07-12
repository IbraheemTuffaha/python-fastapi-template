from fastapi import FastAPI

from app.routers import dummy


app = FastAPI()

app.include_router(dummy.router)


@app.get("/ping")
async def ping() -> str:
    return "pong"
