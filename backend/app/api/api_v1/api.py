from fastapi import APIRouter

from app.api.api_v1.routes import ola_mundo
from app.api.api_v1.routes import login
from app.api.api_v1.routes import users

api_router = APIRouter()

api_router.include_router(ola_mundo.router, tags=["olamundo"])
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])