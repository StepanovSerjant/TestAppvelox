from fastapi_users.authentication import JWTAuthentication

from config import SECRET_KEY, LIFETIME_SECONDS


jwt_authentication = JWTAuthentication(secret=SECRET_KEY, lifetime_seconds=LIFETIME_SECONDS)

auth_backends = [
    jwt_authentication
]
