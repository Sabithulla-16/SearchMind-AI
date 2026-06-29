import httpx

from app.retriever.fetchers.base import BaseFetcher


class HTMLFetcher(BaseFetcher):

    async def fetch(self, source: str) -> str:

        async with httpx.AsyncClient(
            timeout=20,
            follow_redirects=True
        ) as client:

            response = await client.get(source)

            response.raise_for_status()

            return response.text


html_fetcher = HTMLFetcher()