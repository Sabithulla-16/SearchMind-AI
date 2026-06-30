from pydantic import BaseModel

from app.search.models import SearchResult


class RankedSearchResults(BaseModel):
    results: list[SearchResult]