from pathlib import Path

from app.sources.ranking.extractor import (
    feature_extractor,
)

from app.sources.ranking.scorer import (
    document_scorer,
)

from app.sources.ranking.models import (
    RankedDocument,
)

from app.sources.ranking.config import (
    MAX_RESULTS,
    MINIMUM_SCORE,
)

from app.rag.embeddings.client import (
    embedding_client,
)


class RankingService:

    def rank(

        self,

        files: list[Path],

        query: str,

    ):

        ranked = []

        query_embedding = embedding_client.embed(
            query
        )

        for file in files:

            features = feature_extractor.extract(

                path=file,

                query=query,

                query_embedding=query_embedding,

            )

            score = document_scorer.score(

                features

            )

            ranked.append(

                RankedDocument(

                    path=file,

                    score=score,

                    features=features,

                )

            )

        ranked.sort(

            key=lambda item: item.score,

            reverse=True,

        )

        ranked = [

            item

            for item in ranked

            if item.score >= MINIMUM_SCORE

        ]

        

        return ranked[:MAX_RESULTS]


ranking_service = RankingService()