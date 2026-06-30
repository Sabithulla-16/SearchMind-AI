from app.rag.reranking.loader import cross_encoder
from app.rag.reranking.models import RerankedChunk
from app.rag.reranking.utils import build_pairs
from app.rag.reranking.config import DEFAULT_TOP_K

class RerankingService:

    def rerank(
        self,
        query: str,
        chunks,
        top_k: int = DEFAULT_TOP_K,
    ):

        if not chunks:
            return []

        pairs = build_pairs(
            query,
            chunks,
        )

        scores = list(cross_encoder.predict(
            pairs
        ))

        ranked = []

        for chunk, score in zip(
            chunks,
            scores,
        ):

            ranked.append(
                RerankedChunk(
                    score=float(score),
                    chunk_id=chunk.chunk_id,
                    title=chunk.title,
                    url=chunk.url,
                    text=chunk.text,
                )
            )

        ranked.sort(
            key=lambda x: x.score,
            reverse=True,
        )

        print("\nCross Encoder Ranking")

        for chunk in ranked[:5]:
            print(f"{chunk.score:.4f} | {chunk.title}")

        return ranked[:top_k]


reranking_service = RerankingService()