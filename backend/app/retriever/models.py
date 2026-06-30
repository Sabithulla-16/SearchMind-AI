from pydantic import BaseModel


class RetrievedDocument(BaseModel):
    title: str
    url: str
    content: str


class RetrievalStatistics(BaseModel):
    attempted: int = 0
    successful: int = 0
    failed: int = 0
    skipped: int = 0