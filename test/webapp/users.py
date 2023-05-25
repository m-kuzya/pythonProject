from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from config import register_url
import requests
import json


templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)


@router.get("/register")
def register(request: Request):
    return templates.TemplateResponse("register/register.html", {"request": request})


@router.post("/register")
def register(email=Form(), password=Form()):
    data = {"email": email, "password": password}
    url = register_url
    response = requests.post(url, data=json.dumps(data)).json()
    return response