from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from functools import lru_cache
from pathlib import Path
import os


class Settings(BaseSettings):
    # 中间件 配置
    MIDDLEWARE_CORS: bool
    MIDDLEWARE_GZIP: bool
    MIDDLEWARE_ACCESS: bool

    # FastAPI 配置
    FASTAPI_API_PREFIX: str
    FASTAPI_TITLE: str
    FASTAPI_VERSION: str

    # uvicorn 配置
    UVICORN_HOST: str
    UVICORN_PORT: int
    UVICORN_RELOAD: str

    # MySQL 配置
    MYSQL_HOST: str
    MYSQL_PORT: int
    MYSQL_DB: str
    MYSQL_USER: str
    MYSQL_PASSWORD: str

    # MongoDB 配置
    MONGO_HOST: str
    MONGO_PORT: int
    MONGO_DB: str
    MONGO_USER: str
    MONGO_PASSWORD: str

    # redis 配置
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_DB: int
    REDIS_PASSWORD: str

    # JWT
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    # TOS
    TOS_REGION: str
    VOLCENGINE_ACCESS: str
    VOLCENGINE_SECRET: str
    TOS_ACCOUNT_ID: str
    TOS_ROLE_NAME: str
    TOS_ENDPOINT: str
    TOS_BUCKET_NAME: str


@lru_cache
def get_settings():
    # 读取环境变量
    app_env = os.environ.get("APP_ENV")

    # 如果有环境变量
    if not app_env:
        env_file = ".env.local"
    else:
        env_file = f".env.{app_env}"  # APP_ENV 可选 dev,prod 对应着 .env.dev    .env.prod

    parents = os.path.join(Path(__file__).resolve().parent.parent)

    # 加载配置
    load_dotenv(os.path.join(parents, env_file))

    return Settings()


settings = get_settings()
