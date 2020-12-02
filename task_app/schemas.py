from datetime import date
from typing import Optional

from pydantic import BaseModel, Field

from user_auth.schemas import UserInTask


class TaskBase(BaseModel):
    """ Базовая схема для задачи """
    title: str = Field(
        ...,
        max_length=50,
        min_length=2,
        example="Title of the task"
    )

    text: str = Field(
        ...,
        max_length=150,
        min_length=2,
        example="Some text for the task"
    )
    completity_date: date = Field(
        ...,
        example="2020-12-01"
    )


class TaskCreate(TaskBase):
    """ Схема создания задачи """
    is_completed: bool = False

    class Config:
        orm_mode = True


class TaskSingle(TaskCreate):
    """ Схема для списка задач """
    id: int

    class Config:
        orm_mode = True


class TaskList(TaskSingle):
    """ Схема для списка задач """
    pass



