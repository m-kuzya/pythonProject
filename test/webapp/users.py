from auth.manager import create as create_new_user
from auth.database import get_user_db as get_db
from fastapi import APIRouter, Depends, Request, responses, status
from fastapi.templating import Jinja2Templates
from auth.schemas import UserCreate
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from webapp.users_form import UserCreateForm


templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)


@router.get("/register")
def register(request: Request):
    return templates.TemplateResponse("register/register.html", {"request": request})


@router.post("/register")
async def register(request: Request):
    form = UserCreateForm(request)
    await form.load_data()
    if await form.is_valid():
        user = UserCreate(
            username=form.username, email=form.email, password=form.password
        )
        try:
            user = create_new_user
            print(responses)
            return responses.RedirectResponse(
                "/?msg=Successfully-Registered", status_code=status.HTTP_302_FOUND
            )  # default is post request, to use get request added status code 302
        except IntegrityError:
            form.__dict__.get("errors").append("Duplicate username or email")
            return templates.TemplateResponse("register/register.html", form.__dict__)
    return templates.TemplateResponse("register/register.html", form.__dict__)
