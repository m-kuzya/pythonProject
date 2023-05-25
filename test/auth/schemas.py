from typing import Optional

from fastapi_users import schemas


class ShowUser(schemas.BaseUser[int]):
    id: Optional[int]
    email: str
    is_active: bool = True
    is_superuser: bool = False

    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    email: str
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False