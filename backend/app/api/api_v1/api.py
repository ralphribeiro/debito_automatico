from fastapi import APIRouter

from app.api.api_v1.routes import ola_mundo


api_router = APIRouter()

api_router.include_router(ola_mundo.router, tags=["olamundo"])