from pydantic import BaseModel

from app.rag.indexing.models import SearchHit


class HybridSearchResult(BaseModel):
    results: list[SearchHit]