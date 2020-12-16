from fastapi import APIRouter

from app.api.api_v1.routes import hello_world
from app.api.api_v1.routes import login
from app.api.api_v1.routes import users
from app.api.api_v1.routes import debits

api_router = APIRouter()

api_router.include_router(hello_world.router, tags=["Hello world!"])
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(debits.router, prefix="/debits", tags=["automatic debits"])