from fastapi import APIRouter
from pydantic import BaseModel

from app.search.planner import planner
from app.search.schemas import SearchResponse
from app.search.service import search_service

router = APIRouter(
    prefix="/search",
    tags=["Search"]
)


class SearchRequest(BaseModel):
    query: str


@router.post("/", response_model=SearchResponse)
async def search(request: SearchRequest):

    plan = await planner.plan(request.query)

    results = await search_service.search(plan)

    return SearchResponse(
        query=request.query,
        results=results
    )