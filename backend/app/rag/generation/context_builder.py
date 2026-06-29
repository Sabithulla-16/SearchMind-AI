from app.rag.indexing.models import SearchHit
from app.rag.generation.models import ContextDocument


class ContextBuilder:

    def build(
        self,
        hits: list[SearchHit],
        max_chunks: int = 5,
    ):

        documents = []

        seen_urls = set()

        for hit in sorted(
            hits,
            key=lambda x: x.score,
            reverse=True,
        ):

            if hit.url in seen_urls:
                continue

            seen_urls.add(hit.url)

            documents.append(

                ContextDocument(

                    title=hit.title,

                    url=hit.url,

                    score=hit.score,

                    text=hit.text,

                )

            )

            if len(documents) >= max_chunks:
                break

        return documents


context_builder = ContextBuilder()