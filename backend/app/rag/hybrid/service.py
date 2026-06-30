from app.rag.hybrid.bm25 import bm25_index
from app.rag.hybrid.fusion import rrf

from app.rag.indexing.service import indexing_service

from app.rag.hybrid.config import (
    BM25_TOP_K,
    FAISS_TOP_K,
)


class HybridService:

    def index(
        self,
        chunks,
    ):

        bm25_index.build(
            chunks
        )

    def search(
        self,
        query: str,
    ):

        # -----------------------------
        # Dense Retrieval (FAISS)
        # -----------------------------

        dense_results = indexing_service.search(
            query=query,
            top_k=FAISS_TOP_K,
        )

        # -----------------------------
        # Sparse Retrieval (BM25)
        # -----------------------------

        sparse_results = bm25_index.search(
            query=query,
            top_k=BM25_TOP_K,
        )

        # -----------------------------
        # Hybrid Fusion
        # -----------------------------

        fused_results = rrf.fuse(
            dense_results=dense_results,
            sparse_results=sparse_results,
        )

        return fused_results


hybrid_service = HybridService()