from app.search.models import SearchResult


class SearchRanker:

    def rank(
        self,
        results: list[SearchResult],
    ) -> list[SearchResult]:

        return results


search_ranker = SearchRanker()