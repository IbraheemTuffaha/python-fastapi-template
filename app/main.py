from fastapi import FastAPI

from app.v1.routers import router as v1_router


app = FastAPI()

app.include_router(v1_router)


@app.get("/ping")
async def ping() -> str:
    return "pong"
