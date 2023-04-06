from celery import Celery

from app.core.config import settings

celery_app = Celery(
    "app",
    backend=settings.CELERY_RESULT_BACKEND,
    broker=settings.CELERY_BROKER,
    include=["app.tasks"],
)
celery_app.conf.update(
    {
        "task_routes": {
            "app.tasks.register.register_organization": {
                "queue": settings.AUTH_SERVICE_QUEUE
            },
            "app.tasks.passwords.recover_password": {
                "queue": settings.AUTH_SERVICE_QUEUE
            }
        },
        "result_expires": 3600,
        "task_serializer": "json",
        "result_serializer": "json",
        "accept_content": ["json"]
    }
)


if __name__ == "__main__":
    celery_app.start()
