from app.search.models import SearchResult


class Deduplicator:

    def deduplicate(
        self,
        results: list[SearchResult],
    ) -> list[SearchResult]:

        seen_urls = set()

        unique = []

        for result in results:

            url = result.url.strip()

            if url in seen_urls:
                continue

            seen_urls.add(url)

            unique.append(result)

        return unique


deduplicator = Deduplicator()