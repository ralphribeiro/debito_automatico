from fastapi import FastAPI
import uvicorn

from app.api.api_v1.api import api_router
from app.core import config


app = FastAPI(
    title=config.PROJECT_NAME,
    version="0.1",
    docs_url=f"{config.API_V1_STR}/docs",
    redoc_url=None,
    openapi_url=f"{config.API_V1_STR}/openapi.json",
)

app.include_router(api_router, prefix=config.API_V1_STR)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8000)
