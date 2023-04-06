from fastapi import APIRouter

from app.api.api_v1.endpoints import authentication

from app.core.config import settings
from app import schemas

api_router = APIRouter()

# The below check has been added to manage single code repo for different microservice development and deployments
if settings.APP_MODULE == schemas.Module.AUTHENTICATION.value:
    api_router.include_router(
        authentication.router,
        prefix=""
    )
else:
    raise Exception("Invalid Module...!")
