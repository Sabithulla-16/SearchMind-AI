from fastapi import FastAPI

from app.api.routes import router as root_router
from app.api.chat import router as chat_router
from app.api.search import router as search_router
from app.api.crawler import router as crawler_router

from app.core.config import settings
from app.core.logger import app_logger

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
)

app.include_router(root_router, prefix="/api/v1")
app.include_router(chat_router, prefix="/api/v1")
app.include_router(search_router, prefix="/api/v1")
app.include_router(crawler_router, prefix="/api/v1")

app_logger.info("SearchMind AI Started")