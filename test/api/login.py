
from routes.hashing import Hasher
from routes.login import get_user
from auth.database import get_user_db as get_db
from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session


router = APIRouter()


def authenticate_user(username: str, password: str, db: Session = Depends(get_db)):
    user = get_user(username=username, db=db)
    print(user)
    if not user:
        return False
    if not Hasher.verify_password(password, user.hashed_password):
        return False
    return user