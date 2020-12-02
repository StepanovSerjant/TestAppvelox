from typing import Optional

import pydantic
import uuid
from fastapi_users import models


# Классы необходимые для авторизации с помощью fastapi_users
class User(models.BaseUser):
    pass


class UserCreate(User, models.BaseUserCreate):
    name: str


class UserUpdate(User, models.BaseUserUpdate):
    pass


class UserDB(User, models.BaseUserDB):
    name: str


class UserInTask(pydantic.BaseModel):
    """ Схема для отображения данных пользователя в информации о задачах """
    id: uuid.UUID
    name: Optional[str] = None

    @pydantic.validator("id", pre=True, always=True)
    def default_id(cls, v):
        return v or str(uuid.uuid4())

    class Config:
        orm_mode = True

