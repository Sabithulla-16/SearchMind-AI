from pydantic import BaseModel


class SearchHit(BaseModel):

    score: float

    chunk_id: str

    title: str

    url: str

    text: str