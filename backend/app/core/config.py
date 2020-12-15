from os import getenv


PROJECT_NAME = "debito_automatico"

SECRET_KEY = getenv("SECRET_KEY")

SQLALCHEMY_DATABASE_URI = getenv("DATABASE_URL")

API_V1_STR = "/api/v1"

FIRST_SUPERUSER = getenv("FIRST_SUPERUSER")
FIRST_SUPERUSER_PASSWORD = getenv("FIRST_SUPERUSER_PASSWORD")

ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7

EMAIL_TEST_USER = "test@example.com"
