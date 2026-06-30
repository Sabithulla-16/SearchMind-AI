from app.sources.models import SourceRequest

from app.sources.service import source_service

from app.pipeline.rag_pipeline import rag_pipeline

from app.observability.service import observability_service


class FilesystemPipeline:

    async def run(
        self,
        folder: str,
        query: str,
    ):

        observability_service.reset()

        observability_service.start(
            "Sources"
        )

        request = SourceRequest(

            query=query,

            folders=[folder],

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


filesystem_pipeline = FilesystemPipeline()