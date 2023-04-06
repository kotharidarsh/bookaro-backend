from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from starlette.staticfiles import StaticFiles
from starlette_exporter import PrometheusMiddleware, handle_metrics

from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)

from app.core.config import settings
from app.api.utils.exception_handler import register_handlers
from app.api.api_v1.endpoints.health import health_api
from app.api.api_v1.api import api_router
# import app.setup.initial_data as initialize

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=settings.API_VERSION_STR + "/openapi.json",
    version=settings.VERSION,
    middleware=settings.MIDDLEWARES,
    docs_url=None,
    redoc_url=None,
)

# Register Custom Exception/Error Handlers
register_handlers(app)

# Prometheus Metrics
app.add_middleware(PrometheusMiddleware)
app.add_route(settings.API_VERSION_STR + "/metrics", handle_metrics)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


@app.on_event("startup")
async def startup():
    try:
        # initialize.init()
        pass
    except Exception as err:
        print("Exception encountered upon startup!!!")
        print(err)


@app.on_event("shutdown")
async def shutdown():
    pass


# mounting endpoints
app.include_router(api_router, prefix=settings.API_VERSION_STR)
app.mount(path="/health", app=health_api)

app.mount(
    settings.API_VERSION_STR + "/coverage",
    StaticFiles(directory="coverage", check_dir=False, html=True),
    name="coverage",
)

# Off load static file from CDN for Prod
app.mount(
    settings.API_VERSION_STR + "/static",
    StaticFiles(directory="static", check_dir=False),
    name="static",
)


@app.get(settings.API_VERSION_STR + "/docs", include_in_schema=False)
async def custom_swagger_ui_html():  # pragma: no cover
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=settings.AUTH_REDIRECT_URL,
        swagger_js_url=settings.API_VERSION_STR + "/static/swagger-ui-bundle.js",
        swagger_css_url=settings.API_VERSION_STR + "/static/swagger-ui.css",
    )


@app.get(settings.AUTH_REDIRECT_URL, include_in_schema=False)
async def swagger_ui_redirect():  # pragma: no cover
    return get_swagger_ui_oauth2_redirect_html()
