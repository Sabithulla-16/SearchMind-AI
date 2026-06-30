import asyncio

from app.retriever.fetchers.html import html_fetcher
from app.retriever.extractor import extractor
from app.retriever.cleaner import cleaner
from app.retriever.validator import document_validator
from app.retriever.statistics import statistics_tracker


class RetrieverService:

    async def retrieve(self, url: str):

        html = await html_fetcher.fetch(url)

        page = extractor.extract(url, html)

        if page is None:
            return None

        page.content = cleaner.clean(page.content)

        return page

    async def retrieve_many(
        self,
        urls: list[str],
        target_documents: int = 5,
        batch_size: int = 5,
    ):

        documents = []

        statistics_tracker.reset()

        index = 0

        while (
            len(documents) < target_documents
            and index < len(urls)
        ):

            batch = urls[index:index + batch_size]

            tasks = [
                self.retrieve(url)
                for url in batch
            ]

            results = await asyncio.gather(
                *tasks,
                return_exceptions=True
            )

            for result in results:

                statistics_tracker.attempted()

                if isinstance(result, Exception):
                    statistics_tracker.failed()
                    continue

                if result is None:
                    statistics_tracker.failed()
                    continue

                if not document_validator.validate(result):
                    statistics_tracker.failed()
                    continue

                documents.append(result)

                statistics_tracker.success()

                if len(documents) >= target_documents:
                    break

            index += batch_size

        stats = statistics_tracker.summary()

        stats.skipped = max(
            0,
            len(urls) - stats.attempted
        )

        return documents, stats


retriever_service = RetrieverService()