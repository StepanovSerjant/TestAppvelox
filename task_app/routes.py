from typing import List

from fastapi import APIRouter, Depends, HTTPException, Query
from starlette import status
from starlette.responses import Response

from task_app import services, schemas
from core.fast_users import fastusers
from user_auth.models import User 


tasks_router = APIRouter()


@tasks_router.post("/", status_code=201, response_model=schemas.TaskSingle)
async def task_create(
        item: schemas.TaskCreate,
        user: User = Depends(fastusers.get_current_active_user)
    ):
    """ Создание новой задачи для пользователя"""
    return await services.create_task(item, user)


@tasks_router.delete("/{id}")
async def task_delete(
        id: int,
        user: User = Depends(fastusers.get_current_active_user)
    ):
    """ Удаление конкретной задачи пользователя """
    is_deleted = await services.delete_task(id, user)
    if is_deleted:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(status_code=404, detail="Task not found")


@tasks_router.get("/{id}", response_model=schemas.TaskSingle) 
async def task_single(
        id: int,
        user: User = Depends(fastusers.get_current_active_user)
    ):
    """ Получение данных конкретной задачи пользователя  """
    task = await services.get_task(id, user.id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@tasks_router.patch("/completed/{id}")
async def task_completed(
        id: int,
        user: User = Depends(fastusers.get_current_active_user)
    ):
    """ Обновление нужной задачи по айди """
    task_exist = await services.get_task(id=id, user_id=user.id)
    if not task_exist:
        raise HTTPException(status_code=404, detail="Task not found")
    await services.set_task_complete(id=id)
    return {"is_completed": True}


@tasks_router.get("/", response_model=List[schemas.TaskList])
async def task_list(
        user: User = Depends(fastusers.get_current_active_user)
    ):
    """ Получение списка данных всех задач пользователя """
    task_list = await services.get_user_task_list(user)
    return task_list

