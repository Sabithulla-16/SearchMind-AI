from collections import defaultdict

from app.rag.hybrid.config import RRF_K
from app.rag.indexing.models import SearchHit


class ReciprocalRankFusion:

    def fuse(
        self,
        dense_results: list[SearchHit],
        sparse_results: list[SearchHit],
    ) -> list[SearchHit]:

        scores = defaultdict(float)
        documents = {}

        # -------------------------
        # Dense Results (FAISS)
        # -------------------------

        for rank, hit in enumerate(dense_results, start=1):

            scores[hit.chunk_id] += 1 / (RRF_K + rank)

            documents[hit.chunk_id] = hit

        # -------------------------
        # Sparse Results (BM25)
        # -------------------------

        for rank, hit in enumerate(sparse_results, start=1):

            scores[hit.chunk_id] += 1 / (RRF_K + rank)

            documents[hit.chunk_id] = hit

        fused = sorted(
            scores.items(),
            key=lambda item: item[1],
            reverse=True,
        )

        results = []

        for chunk_id, score in fused:

            hit = documents[chunk_id]

            hit.score = score

            results.append(hit)

        return results


rrf = ReciprocalRankFusion()