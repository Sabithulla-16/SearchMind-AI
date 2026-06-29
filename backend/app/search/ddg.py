from ddgs import DDGS

from app.search.models import SearchResult


class DDGClient:

    def __init__(self):
        self.client = DDGS()

    def search(
        self,
        query: str,
        max_results: int = 5
    ):

        results = self.client.text(
            query,
            max_results=max_results
        )

        search_results = []

        for item in results:

            search_results.append(

                SearchResult(
                    title=item.get("title", ""),
                    url=item.get("href", ""),
                    snippet=item.get("body", "")
                )

            )

        return search_results


ddg_client = DDGClient()