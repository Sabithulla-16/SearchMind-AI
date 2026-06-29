import asyncio

from app.retriever.fetchers.html import html_fetcher
from app.retriever.extractor import extractor
from app.retriever.cleaner import cleaner


class RetrieverService:

    async def retrieve(self, url: str):

        html = await html_fetcher.fetch(url)

        page = extractor.extract(url, html)

        if page is None:
            return None

        page.content = cleaner.clean(page.content)

        return page

    async def retrieve_many(self, urls: list[str]):

        tasks = [
            self.retrieve(url)
            for url in urls
        ]

        documents = await asyncio.gather(
            *tasks,
            return_exceptions=True
        )

        return [
            doc
            for doc in documents
            if doc is not None and not isinstance(doc, Exception)
        ]


retriever_service = RetrieverService()