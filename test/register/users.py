from routes.hashing import Hasher
from datetime import datetime
from auth.database import User
from auth.schemas import UserCreate
from sqlalchemy.orm import Session


def create_new_user(user: UserCreate, db: Session):
    user = User(
        username=user.username,
        email=user.email,
        password=Hasher.get_password_hash(user.password),
        is_active=True,
        is_verified=false,
        is_superuser=False,
        role_id=1,
        registered_at=datetime.utcnow,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user_by_email(email: str, db: Session):
    user = db.query(User).filter(User.email == email).first()
    return user
