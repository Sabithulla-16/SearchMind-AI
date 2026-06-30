from collections import defaultdict

from app.rag.candidate_selection.config import (
    MAX_CHUNKS_PER_URL,
)

from app.rag.candidate_selection.models import (
    CandidateSelectionResult,
)


class CandidateSelector:

    def select(
        self,
        candidates,
    ):

        url_counter = defaultdict(int)

        selected = []

        removed = 0

        # -------------------------
        # PASS 1
        # One chunk per URL
        # -------------------------

        remaining = []

        for chunk in candidates:

            if url_counter[chunk.url] == 0:

                selected.append(chunk)

                url_counter[chunk.url] += 1

            else:

                remaining.append(chunk)

        # -------------------------
        # PASS 2
        # Fill remaining slots
        # -------------------------

        for chunk in remaining:

            if (
                url_counter[chunk.url]
                >= MAX_CHUNKS_PER_URL
            ):
                removed += 1
                continue

            selected.append(chunk)

            url_counter[chunk.url] += 1

        return CandidateSelectionResult(

            candidates=selected,

            removed_duplicates=removed,

            unique_urls=len(url_counter),

        )


candidate_selector = CandidateSelector()