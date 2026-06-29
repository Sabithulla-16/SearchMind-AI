from pydantic import BaseModel

from app.search.schemas import SearchPlan
from app.search.models import SearchResult

from app.retriever.models import RetrievedDocument

from app.rag.chunking.models import RetrievedChunk

from app.rag.embeddings.models import EmbeddedChunk

from app.rag.indexing.models import SearchHit


class PipelineResult(BaseModel):

    plan: SearchPlan

    search_results: list[SearchResult]

    documents: list[RetrievedDocument]

    chunks: list[RetrievedChunk]

    embedded_chunks: list[EmbeddedChunk]

    semantic_results: list[SearchHit]