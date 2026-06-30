from fastapi import FastAPI

from app.api.router import router

from app.api.middleware import (
    request_middleware,
)

app = FastAPI(

    title="SearchMind AI",

    description="Intelligent Multi-Source Search Engine API",

    version="1.0.0",

)

app.middleware("http")(
    request_middleware
)

app.include_router(
    router
)