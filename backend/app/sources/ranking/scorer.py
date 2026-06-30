from app.sources.ranking.config import (
    SOURCE_DIRECTORIES,
    LOW_PRIORITY_DIRECTORIES,
    WEIGHTS,
)

from app.sources.ranking.models import (
    DocumentFeatures,
)


class DocumentScorer:

    def score(
        self,
        features: DocumentFeatures,
    ):

        score = (

            features.semantic_similarity

            * WEIGHTS["semantic"]

        )

        if features.query_matches:

            score += (
                features.query_matches
                * WEIGHTS["query"]
            )

        if features.is_documentation:

            score += WEIGHTS["documentation"]

        if features.is_configuration:

            score += WEIGHTS["configuration"]

        if features.is_source_code:

            score += WEIGHTS["source_code"]

        if any(

            directory in SOURCE_DIRECTORIES

            for directory in features.directories

        ):

            score += WEIGHTS["directory"]

        if any(

            directory in LOW_PRIORITY_DIRECTORIES

            for directory in features.directories

        ):

            score -= 10

        if 1024 <= features.size <= 500000:

            score += WEIGHTS["size"]

        return float(score)


document_scorer = DocumentScorer()