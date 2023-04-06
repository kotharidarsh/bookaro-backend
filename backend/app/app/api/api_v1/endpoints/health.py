from __future__ import annotations
from fastapi import FastAPI, APIRouter, status
from fastapi.responses import JSONResponse

health_api = FastAPI(
    title="Service Endpoint Health Check",
    description="Health and liveness probe for Argon Service Endpoints..."
)
health_router = APIRouter()


@health_router.get('/', response_model=None)  # pragma: no cover
def health_and_liveness_probe_endpoint():  # pragma: no cover
    """ API Endpoint to check the application microservice health

    Attributes
    ----------
        None
    """
    return JSONResponse(
        content={
            'status': 'success'
        },
        status_code=status.HTTP_200_OK
    )


health_api.include_router(router=health_router)
