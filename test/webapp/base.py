from fastapi import APIRouter
from webapp import login as route_login
from webapp import users as route_users
from webapp import homepage as route_homepage

api_router = APIRouter()
api_router.include_router(route_login.router, prefix="", tags=["login"])
api_router.include_router(route_users.router, prefix="", tags=["register"])
api_router.include_router(route_homepage.router, prefix="", tags=["homepage"])

