from pathlib import Path


class EmbeddingCache:

    def __init__(self):

        self.cache = {}

    def get(
        self,
        path: Path,
        modified: float,
    ):

        key = (str(path), modified)

        return self.cache.get(key)

    def set(
        self,
        path: Path,
        modified: float,
        embedding,
    ):

        key = (str(path), modified)

        self.cache[key] = embedding


embedding_cache = EmbeddingCache()