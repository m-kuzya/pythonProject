from register.users import create_new_user
from auth.database import get_user_db as get_db
from fastapi import APIRouter
from fastapi import Depends
from auth.schemas import UserRead
from auth.schemas import UserCreate
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/", response_model=UserRead)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user = create_new_user(user=user, db=db)
    return user
