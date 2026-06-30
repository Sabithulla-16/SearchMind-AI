from fastapi import APIRouter

from app.api.routes.health import (
    router as health_router,
)

from app.api.routes.search import (
    router as search_router,
)

router = APIRouter()

router.include_router(
    health_router,
    tags=["Health"],
)

router.include_router(
    search_router,
    tags=["Search"],
)