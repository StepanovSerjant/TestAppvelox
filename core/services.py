from core.db import database
from task_app.models import tasks
from task_app.schemas import TaskCreate, TaskUpdate


async def get_task_list():
	""" Получение списка всех задач """
	return await database.fetch_all(query=tasks.select())


async def create_task(item: TaskCreate):
    """ Запись задачи в БД """
    task = tasks.insert().values(**item.dict())
    return await database.execute(task)


async def delete_task(id):
	""" Удаление задачи по айди из БД """
	query = tasks.delete().where(tasks.c.id==id)
	return await database.fetch_one(query=query)


async def get_task(id):
	query = tasks.select().where(tasks.c.id==id)
	return await database.fetch_one(query=query)


async def update_task(id, item: TaskUpdate):
	query = tasks.update().where(tasks.c.id==id).values(**item.dict())
	return await database.fetch_one(query=query)
