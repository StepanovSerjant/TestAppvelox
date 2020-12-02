from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy import Column, String

from core.db import Base, database
from user_auth.schemas import UserDB


class User(Base, SQLAlchemyBaseUserTable):
    """ Кортеж пользователя """

    name = Column(String, unique=True)


users = User.__table__
user_db = SQLAlchemyUserDatabase(UserDB, database, users)
