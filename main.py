from fastapi import FastAPI

from core.db import database
from task_app.routes import tasks_router


app = FastAPI()
app.include_router(tasks_router, prefix="/task", tags=["task"])


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
