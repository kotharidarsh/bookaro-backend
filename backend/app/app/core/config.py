import logging
import secrets
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyUrl, AnyHttpUrl, BaseSettings, EmailStr, HttpUrl, PostgresDsn, validator
from starlette.middleware import Middleware
from starlette_context.middleware import ContextMiddleware
from starlette_context import plugins
from functools import lru_cache


@lru_cache()
def get_settings():
    return Settings()


class Settings(BaseSettings):

    class Config:
        case_sensitive = True
        env_file = ".env"

    # project and endpoint accessibility related configurations
    DOMAIN: str = "0.0.0.0"
    VERSION: str = "1.0.0"
    API_VERSION: str = "v1"
    API_NAME: str = "api"
    APP_MODULE: str
    API_VERSION_STR: str = f"/{API_NAME}/{API_VERSION}"
    PROJECT_NAME: str
    APP_ENV: str = "LOCAL"
    SERVER_HOST: str = "http://127.0.0.1:8001"

    SECRET_KEY: str = secrets.token_urlsafe(32)
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    EMAIL_RESET_TOKEN_EXPIRE_HOURS: int = 10

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
        "http://localhost",
        "http://localhost:4200",
        "http://localhost:3000",
        "http://localhost:8080",
        "http://localhost:8001",
        "https://localhost",
        "https://localhost:4200",
        "https://localhost:3000",
        "https://localhost:8080",
        "https://localhost:8001",
    ]
    AUTH_AUTHORIZATION_URL: AnyHttpUrl
    AUTH_TOKEN_URL: AnyHttpUrl
    AUTH_REDIRECT_URL: str = "/docs"

    MIDDLEWARES: list = [
        Middleware(
            ContextMiddleware,
            plugins=(plugins.RequestIdPlugin(), plugins.CorrelationIdPlugin()),
        )
    ]

    # database creds and indices
    DB_HOST: str
    DB_PORT: int
    DB_USERNAME: str
    DB_PASSWORD: str
    DB_NAME: str

    # redis cache and celery worker config
    CELERY_BROKER = "amqp://guest:guest@localhost:5672//"
    # CELERY_BACKEND = "amqp://guest:guest@localhost:5672//"
    CELERY_RESULT_BACKEND = "rpc://"
    AUTH_SERVICE_QUEUE: str
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_PASSWORD: str

    # smtp configs
    EMAILS_ENABLED: bool = True
    EMAILS_FROM_NAME: str = "Darshit Kothari"
    EMAILS_FROM_EMAIL: str = "kotharidarsh104@gmail.com"
    EMAIL_TEMPLATES_DIR: str = "app/email_templates/build"
    SMTP_HOST: str = "smtp.gmail.com"
    SMTP_PORT: int = 587
    SMTP_TLS: bool = True
    SMTP_USER: str = "kotharidarsh104@gmail.com"
    SMTP_PASSWORD: str = "kgarayamwnqdoqlq"

    # additional configs
    TRIAL_PERIOD: int = 2592000  # 30 days in seconds
    DATE_FORMAT = "%Y-%m-%dT%H:%M:%S"
    EPOCH_DATE: str = "1970-01-01T00:00:00"


settings = get_settings()
