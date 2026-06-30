import asyncio
import time

from app.sources.models import (
    SourceRequest,
    SourceResult,
    MergedSourceResult,
)

from app.sources.registry import source_registry


class SourceManager:

    async def retrieve(
        self,
        request: SourceRequest,
    ):

        tasks = []

        # -------------------------
        # Web
        # -------------------------

        if request.web_urls:

            web = source_registry.get("web")

            tasks.append(

                web.retrieve(

                    urls=request.web_urls,

                    target_documents=request.target_documents,

                )

            )

        # -------------------------
        # PDF
        # -------------------------

        for path in request.pdf_paths:

            pdf = source_registry.get("pdf")

            tasks.append(

                pdf.retrieve(
                    path=path
                )

            )

        # -------------------------
        # Filesystem
        # -------------------------

        for folder in request.folders:

            filesystem = source_registry.get(
                "filesystem"
            )

            tasks.append(

                filesystem.retrieve(
                    folder=folder,
                )

            )

        # -------------------------
        # GitHub
        # -------------------------

        for repository in request.github_repositories:

            github = source_registry.get(
                "github"
            )

            tasks.append(

                github.retrieve(
                    repository_url=repository,
                )

            )

        results: list[SourceResult] = await asyncio.gather(
            *tasks
        )

        documents = []

        for result in results:

            documents.extend(
                result.documents
            )

        return MergedSourceResult(

            documents=documents,

            source_results=results,

        )


source_manager = SourceManager()