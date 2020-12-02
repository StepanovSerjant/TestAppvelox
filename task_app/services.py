from sqlalchemy import select

from core.db import database
from user_auth.models import User, users
from task_app.models import Task, tasks
from task_app.schemas import TaskCreate


async def get_user_task_list(user: User):
    """ Получение списка всех задач пользователя + """
    task_list = await database.fetch_all(query=tasks.select(). \
        where(tasks.c.user == user.id))
    return [dict(task) for task in task_list]


async def create_task(item: TaskCreate, user: User):
    """ Запись задачи в БД """
    task = tasks.insert().values(**item.dict(), user=user.id)
    id = await database.execute(task)
    return await get_task(id, user.id)


async def delete_task(id, user):
    """ Удаление задачи по айди из БД + """
    task = await get_task(id, user.id)
    if task:
        await database.execute(tasks.delete().where((tasks.c.id == id) & \
            (tasks.c.user == user.id)))
        return True
    return False


async def get_task(id, user_id):
    """ Получение задачи по идентификатору """
    u = users.alias('user')
    t = tasks.alias('task')
    q = select([u.c.id.label("userId"), u.c.name.label("userName"), t]) \
        .select_from(t.join(u)) \
        .where((t.c.id == id) & (u.c.id == t.c.user) & (t.c.user == user_id))
    task = await database.fetch_one(q)
    if task is not None:
        task = dict(task)
        return {**task}
    return task


async def set_task_complete(id: int):
    """ Пометка конкретной задачи пользователя как выполненная """
    task = tasks.update().where(tasks.c.id == id).values(is_completed=True)
    return await database.execute(task)


