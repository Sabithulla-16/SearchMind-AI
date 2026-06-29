from pydantic import BaseModel
from typing import List


class EmbeddedChunk(BaseModel):
    chunk_id: str

    url: str

    title: str

    text: str

    embedding: List[float]

    chunk_index: int

    total_chunks: int