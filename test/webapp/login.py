from fastapi import APIRouter
from fastapi import Request, Form, Response
from fastapi.templating import Jinja2Templates
import requests
from auth.auth import get_jwt_strategy, cookie_transport
import json


templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)


@router.get("/login")
def login(request: Request):
    return templates.TemplateResponse("login/login.html", {"request": request})


@router.post("/login")
def user_login(username=Form(), password=Form()):
    data = {"username": username, "password": password}
    url = "http://127.0.0.1:8000/auth/login"
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    r = requests.Session()
    r.post(url=url, headers=headers, data=data)
    mycookies = r.cookies
    return mycookies