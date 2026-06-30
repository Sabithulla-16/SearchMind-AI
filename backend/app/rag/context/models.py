from pydantic import BaseModel

from app.rag.generation.models import ContextDocument

class ContextResult(BaseModel):

    chunks: list[ContextDocument]

    total_tokens: int

    unique_sources: int

    skipped_duplicates: int