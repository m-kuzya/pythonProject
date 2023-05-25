from flask import make_response, render_template, request

from api.base import api_router
from fastapi_users import FastAPIUsers
from fastapi import FastAPI, Depends

from auth.auth import auth_backend
from auth.database import User
from auth.manager import get_user_manager
from auth.schemas import ShowUser, UserCreate
from webapp.base import api_router as web_app_router


def include_router(app):
    app.include_router(api_router)
    app.include_router(web_app_router)

def start_application():
    app = FastAPI(title="Some Titile", version="Some Version", openapi_url="/auth/openapi.json")
    include_router(app)
    return app


app = start_application()

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(ShowUser, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

current_user = fastapi_users.current_user()
current_superuser = fastapi_users.current_user(active=True, superuser=True)


@app.get("/superuser-route")
def protected_route(user: User = Depends(current_superuser)):
    return f"Круто, ты админ, обычным юзерам сюда ходу нет"


@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Привет, {user.email}, ты авторизован, у гостей сюда нет входа"


@app.get("/unprotected-route")
def unprotected_route():
    return "Привет добряк, с авторизацией аль без нее"

