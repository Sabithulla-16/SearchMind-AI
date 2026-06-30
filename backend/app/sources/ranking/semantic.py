from pathlib import Path

import numpy as np

from app.rag.embeddings.client import (
    embedding_client,
)

from app.sources.ranking.cache import (
    embedding_cache,
)

from app.sources.ranking.preview import (
    preview_reader,
)


class SemanticRanker:

    def similarity(

        self,

        query_embedding,

        path: Path,

    ) -> float:

        modified = path.stat().st_mtime

        file_embedding = embedding_cache.get(
            path,
            modified,
        )

        if file_embedding is None:

            preview = preview_reader.read(
                path
            )

            text = (
                f"Filename: {path.name}\n"
                f"Extension: {path.suffix}\n\n"
                f"{preview}"
            )

            file_embedding = embedding_client.embed(
                text
            )

            embedding_cache.set(

                path,

                modified,

                file_embedding,

            )

        similarity = np.dot(

            query_embedding,

            file_embedding,

        )

        return float(similarity)


semantic_ranker = SemanticRanker()