from pydantic import BaseModel

from app.rag.indexing.models import SearchHit


class CandidateSelectionResult(BaseModel):

    candidates: list[SearchHit]

    removed_duplicates: int

    unique_urls: int