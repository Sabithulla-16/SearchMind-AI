from app.sources.base import BaseSource
from app.sources.models import SourceDocument, SourceResult

from app.retriever.service import retriever_service


class WebSource(BaseSource):

    name = "web"

    async def retrieve(
        self,
        urls,
        target_documents=5,
    ):

        retrieved_documents, stats = await retriever_service.retrieve_many(
            urls,
            target_documents,
        )

        documents = []

        for doc in retrieved_documents:

            documents.append(

                SourceDocument(

                    title=doc.title,

                    url=doc.url,

                    text=doc.content,

                    source="web",

                )

            )

        return SourceResult(

            source="web",

            documents=documents,

            statistics={

                "attempted": stats.attempted,

                "successful": stats.successful,

                "failed": stats.failed,

                "skipped": stats.skipped,

            },

        )


web_source = WebSource()