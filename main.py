import fastapi_users
from fastapi import FastAPI
from starlette.requests import Request

from config import SECRET_KEY
from core.db import database
from core.fast_users import fastusers
from task_app.routes import tasks_router
from user_auth.jwt_config import jwt_authentication 
from user_auth.schemas import User


app = FastAPI()
app.include_router(
    fastusers.get_auth_router(jwt_authentication),
    prefix="/users",
    tags=["users"],
)
app.include_router(
    fastusers.get_register_router(),
    prefix="/users",
    tags=["users"],
)
app.include_router(
    fastusers.get_reset_password_router(SECRET_KEY),
    prefix="/users",
    tags=["users"],
)
app.include_router(
    fastusers.get_users_router(),
    prefix="/users",
    tags=["users"],
)
app.include_router(tasks_router, prefix="/tasks", tags=["tasks"])


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


# @fastusers.on_after_register()
# def on_after_register(user: User, request: Request):
#     print(f"User {user.id} has registered.")


# @fastusers.on_after_forgot_password()
# def on_after_forgot_password(user: User, token: str, request: Request):
#     print(f"User {user.id} has forgot their password. Reset token: {token}")


