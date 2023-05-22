from fastapi import APIRouter
from auth.schemas import ShowUser
from auth.schemas import UserCreate

router = APIRouter()


@router.post("/", response_model=ShowUser)
def create_user(user: UserCreate):
    return user
