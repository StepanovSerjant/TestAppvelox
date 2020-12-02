from fastapi_users import FastAPIUsers

from user_auth.schemas import User, UserCreate, UserUpdate, UserDB
from user_auth.models import user_db
from user_auth.jwt_config import auth_backends


fastusers = FastAPIUsers(
    user_db,
    auth_backends,
    User,
    UserCreate,
    UserUpdate,
    UserDB,
)

