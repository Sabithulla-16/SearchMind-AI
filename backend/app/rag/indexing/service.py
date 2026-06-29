from app.rag.embeddings.models import EmbeddedChunk

from app.rag.indexing.models import SearchHit

from app.rag.indexing.faiss_store import faiss_store

from app.rag.embeddings.client import embedding_client


class IndexingService:

    def index(
        self,
        chunks: list[EmbeddedChunk],
    ):

        faiss_store.add(chunks)

    def search(
        self,
        query: str,
        top_k: int = 5,
    ):

        embedding = embedding_client.embed(
            query
        )

        scores, indices = faiss_store.search(
            embedding,
            top_k,
        )

        results = []

        for score, idx in zip(scores, indices):

            if idx == -1:
                continue

            chunk = faiss_store.chunks[idx]

            results.append(

                SearchHit(

                    score=float(score),

                    chunk_id=chunk.chunk_id,

                    title=chunk.title,

                    url=chunk.url,

                    text=chunk.text,

                )

            )

        return results


indexing_service = IndexingService()