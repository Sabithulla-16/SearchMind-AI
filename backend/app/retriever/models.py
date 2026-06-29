from typing import List
from pydantic import BaseModel


class RetrievedDocument(BaseModel):
    title: str
    url: str
    content: str


class RetrievalResponse(BaseModel):
    documents: List[RetrievedDocument]