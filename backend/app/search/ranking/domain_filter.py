from urllib.parse import urlparse

from app.search.models import SearchResult


class DomainFilter:

    def filter(
        self,
        results: list[SearchResult],
        max_per_domain: int = 2,
    ) -> list[SearchResult]:

        filtered = []

        domains = {}

        for result in results:

            domain = urlparse(result.url).netloc.lower()

            count = domains.get(domain, 0)

            if count >= max_per_domain:
                continue

            domains[domain] = count + 1

            filtered.append(result)

        return filtered


domain_filter = DomainFilter()