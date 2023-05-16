from auth.manager import create as create_new_user
from auth.database import get_user_db as get_db
from fastapi import APIRouter
from fastapi import Depends
from auth.schemas import ShowUser
from auth.schemas import UserCreate
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/", response_model=ShowUser)
def create_user(user: UserCreate):
    return user
