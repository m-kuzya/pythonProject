from auth.manager import create as create_new_user
from auth.database import get_user_db as get_db
from fastapi import APIRouter, Depends, Request, responses, status
from fastapi.templating import Jinja2Templates
from auth.schemas import UserCreate, ShowUser
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from webapp.users_form import UserCreateForm
import requests

templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)


@router.get("/register")
def register(request: Request):
    return templates.TemplateResponse("register/register.html", {"request": request})


@router.post("/auth/register")
async def create_user(request: Request):
    form = UserCreateForm(request)
    await form.load_data()
    if await form.is_valid():
        user = UserCreate(
            username=form.username, email=form.email, password=form.password
        )
    return user