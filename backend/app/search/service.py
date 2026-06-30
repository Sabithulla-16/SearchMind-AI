from app.search.ddg import ddg_client
from app.search.models import SearchResult
from app.search.schemas import SearchPlan
from app.search.ranking.service import ranking_service


class SearchService:

    async def search(
        self,
        plan: SearchPlan,
        max_results_per_query: int = 5
    ):

        urls = set()

        results: list[SearchResult] = []

        for query in plan.search_queries:

            search_results = ddg_client.search(
                query,
                max_results=max_results_per_query
            )

            for result in search_results:

                if result.url in urls:
                    continue

                urls.add(result.url)

                results.append(result)

        results = ranking_service.rank(results)

        return results


search_service = SearchService()