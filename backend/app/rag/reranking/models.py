from pydantic import BaseModel


class RerankedChunk(BaseModel):
    score: float
    chunk_id: str
    title: str
    url: str
    text: str