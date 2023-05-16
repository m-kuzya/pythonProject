from typing import Optional

from fastapi_users import schemas


class ShowUser(schemas.BaseUser[int]):
    id: Optional[int]
    email: str
    username: str
    role_id: Optional[int]
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    username: str
    email: str
    password: str
    role_id: Optional[int] = 1
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False