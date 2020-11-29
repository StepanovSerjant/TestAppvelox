from typing import List

from fastapi import APIRouter

from core import services
from task_app.schemas import TaskCreate, TaskList, TaskSingle, TaskUpdate


tasks_router = APIRouter()


@tasks_router.post("/")
async def task_create(item: TaskCreate):
    """ Создание новой задачи """
    return await services.create_task(item)


@tasks_router.delete("/{id}")
async def task_delete(id: int):
    """ Удаление нужной задачи """
    return await services.delete_task(id)


@tasks_router.get("/{id}", response_model=TaskSingle)
async def task_single(id: int):
    """ Получение нужной задачи по айди """
    return await services.get_task(id)


@tasks_router.patch("/{id}", response_model=TaskSingle)
async def task_update(id: int, item: TaskUpdate):
    """ Обновление нужной задачи по айди """
    await services.update_task(id, item)
    return await services.get_task(id)


@tasks_router.get("/", response_model=List[TaskSingle])
async def task_all():
    """ Получение списка всех задач """
    return await services.get_task_list()
