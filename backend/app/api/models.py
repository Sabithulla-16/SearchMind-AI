from typing import Literal

from pydantic import BaseModel, Field


class SearchRequest(BaseModel):

    type: Literal[
        "web",
        "pdf",
        "filesystem",
        "github",
        "multisource",
    ]

    query: str

    pdf_paths: list[str] = Field(
        default_factory=list
    )

    folders: list[str] = Field(
        default_factory=list
    )

    github_repositories: list[str] = Field(
        default_factory=list
    )