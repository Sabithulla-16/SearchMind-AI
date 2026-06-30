from rank_bm25 import BM25Okapi

from app.rag.chunking.models import RetrievedChunk
from app.rag.indexing.models import SearchHit


class BM25Index:

    def __init__(self):

        self.documents: list[RetrievedChunk] = []

        self.corpus = []

        self.index = None

    def build(
        self,
        chunks: list[RetrievedChunk],
    ):

        self.documents = chunks

        self.corpus = [
            chunk.text.lower().split()
            for chunk in chunks
        ]

        self.index = BM25Okapi(
            self.corpus
        )

    def search(
        self,
        query: str,
        top_k: int,
    ):

        if self.index is None:
            return []

        tokens = query.lower().split()

        scores = self.index.get_scores(
            tokens
        )

        ranked = sorted(
            enumerate(scores),
            key=lambda x: x[1],
            reverse=True,
        )

        results = []

        for index, score in ranked[:top_k]:

            chunk = self.documents[index]

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


bm25_index = BM25Index()