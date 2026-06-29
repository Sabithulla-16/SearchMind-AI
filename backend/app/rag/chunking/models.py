from pydantic import BaseModel


class RetrievedChunk(BaseModel):
    chunk_id: str
    url: str
    title: str

    text: str

    chunk_index: int
    total_chunks: int

    token_count: int