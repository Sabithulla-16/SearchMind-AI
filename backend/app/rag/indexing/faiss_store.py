import faiss
import numpy as np

from app.rag.embeddings.models import EmbeddedChunk


class FAISSStore:

    def __init__(self):

        self.dimension = 384

        self.index = faiss.IndexFlatIP(
            self.dimension
        )

        self.chunks: list[EmbeddedChunk] = []

    def add(
        self,
        chunks: list[EmbeddedChunk],
    ):

        vectors = np.array(
            [c.embedding for c in chunks],
            dtype="float32",
        )

        self.index.add(vectors)

        self.chunks.extend(chunks)

    def search(
        self,
        query_embedding,
        top_k=5,
    ):

        query = np.array(
            [query_embedding],
            dtype="float32",
        )

        scores, indices = self.index.search(
            query,
            top_k,
        )

        return scores[0], indices[0]


faiss_store = FAISSStore()