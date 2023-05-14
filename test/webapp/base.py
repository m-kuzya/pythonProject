from fastapi import APIRouter
from api import login as route_login
from webapp import users as route_users

api_router = APIRouter()
api_router.include_router(route_login.router, prefix="/login", tags=["login"])
api_router.include_router(route_users.router, prefix="", tags=["users-webapp"])
