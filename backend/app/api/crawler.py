from fastapi import APIRouter

from pydantic import BaseModel

from app.retriever.service import crawl_service


router = APIRouter(
    prefix="/crawler",
    tags=["Crawler"]
)


class CrawlRequest(BaseModel):

    url: str


@router.post("/")
async def crawl(
    request: CrawlRequest,
):

    page = await crawl_service.crawl(
        request.url
    )

    return page