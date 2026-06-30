from pathlib import Path

from pydantic import BaseModel


class DocumentFeatures(BaseModel):

    path: Path

    extension: str

    filename: str

    directories: list[str]

    size: int

    query_matches: int

    semantic_similarity: float = 0.0

    is_documentation: bool

    is_configuration: bool

    is_source_code: bool

class RankedDocument(BaseModel):

    path: Path

    score: float

    features: DocumentFeatures
