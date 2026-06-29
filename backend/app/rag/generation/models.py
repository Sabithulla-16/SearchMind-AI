from pydantic import BaseModel
from typing import List


class ContextDocument(BaseModel):
    title: str
    url: str
    score: float
    text: str


class GeneratedAnswer(BaseModel):
    answer: str
    sources: List[ContextDocument]