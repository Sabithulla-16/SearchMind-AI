from app.sources.models import SourceRequest

from app.sources.service import source_service

from app.pipeline.rag_pipeline import rag_pipeline

from app.observability.service import observability_service


class MultiPipeline:

    async def run(
        self,
        query: str,
        web_urls: list[str] | None = None,
        pdf_paths: list[str] | None = None,
        folders: list[str] | None = None,
        github_repositories: list[str] | None = None,
    ):

        observability_service.reset()

        observability_service.start(
            "Sources"
        )

        request = SourceRequest(

            query=query,

            web_urls=web_urls or [],

            pdf_paths=pdf_paths or [],

            folders=folders or [],

            github_repositories=github_repositories or [],

        )

        result = await source_service.retrieve(
            request
        )

        observability_service.stop(
            "Sources"
        )

        documents = result.documents

        observability_service.counter(
            "Retrieved Documents",
            len(documents),
        )

        generation = await rag_pipeline.run(

            query=query,

            documents=documents,

        )

        observability_service.summary()

        return generation


multisource_pipeline = MultiPipeline()