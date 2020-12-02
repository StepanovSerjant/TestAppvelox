import os

from dotenv import load_dotenv


load_dotenv()

# Секретный ключ для генерации токена и его время жизни в секундах
SECRET_KEY = str(os.getenv("SECRET_KEY"))
LIFETIME_SECONDS = 3600

# Настройки БД
DB_USERNAME = str(os.getenv("DB_USERNAME"))
DB_PASSWORD = str(os.getenv("DB_PASSWORD"))
DB_HOST = str(os.getenv("DB_HOST"))
DB_NAME = str(os.getenv("DB_NAME"))

