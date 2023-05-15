from api import login as route_login
from api import user as route_users
from fastapi import APIRouter


api_router = APIRouter()
api_router.include_router(route_users.router, prefix="/register", tags=["register"])
api_router.include_router(route_login.router, prefix="/login", tags=["login"])
