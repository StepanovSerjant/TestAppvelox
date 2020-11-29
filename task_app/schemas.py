from datetime import date
from typing import Optional

from pydantic import BaseModel


class TaskBase(BaseModel):
    """ Базовая схема для задачи """
    title: str
    text: str


class TaskUpdate(TaskBase):
    """ Схема для списка задач """

    title: Optional[str]
    text: Optional[str]
    completity_date: Optional[date]
    is_completed: Optional[bool]


class TaskSingle(TaskBase):
    """ Схема для списка задач """

    id: int
    completity_date: date


class TaskList(TaskSingle):
    """ Схема для списка задач """
    pass


class TaskCreate(TaskBase):
    """ Схема создания задачи """

    completity_date: date
    is_completed: bool = False

    class Config:
        orm_mode = True
