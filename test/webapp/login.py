from fastapi import APIRouter
from fastapi import Request, Form, Response
from fastapi.templating import Jinja2Templates
from config import login_url
import requests

templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)

@router.get("/login")
def login(request: Request):
    return templates.TemplateResponse("login/login.html", {"request": request})


@router.post("/login")
def user_login(response: Response, username=Form(), password=Form()):
    data = {"username": username, "password": password}
    url = login_url
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    r = requests.Session()
    r.post(url=url, headers=headers, data=data)
    response.set_cookie(key="jwt", value=r.cookies.get_dict().get("jwt"))