from app.search.models import SearchResult

from app.search.ranking.deduplicator import deduplicator
from app.search.ranking.domain_filter import domain_filter
from app.search.ranking.ranker import search_ranker


class RankingService:

    def rank(
        self,
        results: list[SearchResult],
    ) -> list[SearchResult]:

        results = deduplicator.deduplicate(results)

        results = domain_filter.filter(results)

        results = search_ranker.rank(results)

        return results


ranking_service = RankingService()