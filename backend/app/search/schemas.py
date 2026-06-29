from typing import List
from app.search.models import SearchResult
from pydantic import BaseModel


class SearchPlan(BaseModel):
    original_query: str
    intent: str
    language: str
    search_type: str
    time_sensitive: bool
    search_queries: List[str]

class SearchResponse(BaseModel):
    query: str
    results: List[SearchResult]