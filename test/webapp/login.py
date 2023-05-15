from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Request
from fastapi.templating import Jinja2Templates
from webapp.login_form import LoginForm


templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)


@router.get("/login")
def login(request: Request):
    return templates.TemplateResponse("login/login.html", {"request": request})


@router.post("/login")
async def login(request: Request):
    form = LoginForm(request)
    await form.load_data()
    if await form.is_valid():
        try:
            form.__dict__.update(msg="Login Successful :)")
            response = templates.TemplateResponse("login/login.html", form.__dict__)
            return response
        except HTTPException:
            form.__dict__.update(msg="")
            form.__dict__.get("errors").append("Incorrect Email or Password")
            return templates.TemplateResponse("login/login.html", form.__dict__)
    return templates.TemplateResponse("login/login.html", form.__dict__)