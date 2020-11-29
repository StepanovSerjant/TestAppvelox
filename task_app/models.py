from sqlalchemy import Column, Boolean, Date, Integer, String

from core.db import Base


class Task(Base):
    """ Кортеж задачи """

    __tablename__ = "user_task"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, nullable=False)
    text = Column(String(275), nullable=False)
    completity_date = Column(Date, nullable=False)
    is_completed = Column(Boolean, default=False)


tasks = Task.__table__
