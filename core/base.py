# import for alembic that doesn't see the core module and models
from core.db import Base
from task_app.models import Task, tasks
from user_auth.models import User, users

