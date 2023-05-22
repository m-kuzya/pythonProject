from fastapi import APIRouter
from fastapi import Request, Form
from fastapi.templating import Jinja2Templates
import requests
import json


templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)


@router.get("/login")
def login(request: Request):
    return templates.TemplateResponse("login/login.html", {"request": request})


@router.post("/login")
def user_login(username=Form(), password=Form()):
    url = 'http://127.0.0.1:8000/auth/login'
    data = {
        'username': username,
        'password': password,
    }
    header = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    response = requests.post(url=url, headers=header, data=data)
    return response