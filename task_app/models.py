# from fastapi_users.db import sqlalchemy
from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from core.db import Base


class Task(Base):
    """ Таблица для хранения задач пользователей в БД """

    __tablename__ = "user_task"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, nullable=False)
    text = Column(String(275), nullable=False)
    completity_date = Column(Date, nullable=False)
    is_completed = Column(Boolean, default=False)

    user = Column(String, ForeignKey("user.id"))
    user_id = relationship("User")


tasks = Task.__table__
