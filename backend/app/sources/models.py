from pathlib import Path

from pydantic import BaseModel, Field

from typing import Any


class SourceDocument(BaseModel):

    title: str

    url: str

    text: str

    source: str

    metadata: dict[str, Any] = Field(
        default_factory=dict
    )


class SourceRequest(BaseModel):

    query: str

    web_urls: list[str] = Field(
        default_factory=list
    )

    pdf_paths: list[str] = Field(
        default_factory=list
    )

    folders: list[str] = Field(
        default_factory=list
    )

    github_repositories: list[str] = Field(
        default_factory=list
    )

    target_documents: int = 5

class SourceResult(BaseModel):

    source: str

    documents: list[SourceDocument]

    statistics: dict[str, int] = Field(
        default_factory=dict
    )

    duration_ms: float = 0

class MergedSourceResult(BaseModel):

    documents: list[SourceDocument]

    source_results: list[SourceResult]

    @property
    def total_documents(self):

        return len(self.documents)

    @property
    def total_sources(self):

        return len(self.source_results)