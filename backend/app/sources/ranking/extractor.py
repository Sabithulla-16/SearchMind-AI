from pathlib import Path

from app.sources.ranking.models import DocumentFeatures

from app.sources.ranking.config import (
    DOCUMENTATION_KEYWORDS,
    CONFIGURATION_FILENAMES,
)

from app.sources.ranking.semantic import (
    semantic_ranker,
)


class FeatureExtractor:

    def extract(
        self,
        path: Path,
        query: str,
        query_embedding,
    ) -> DocumentFeatures:

        filename = path.name.lower()

        stem = path.stem.lower()

        directories = [

            part.lower()

            for part in path.parts

        ]

        query_words = {

            word.lower()

            for word in query.split()

        }

        query_matches = 0

        for word in query_words:

            if word in filename:

                query_matches += 1

        semantic_similarity = semantic_ranker.similarity(

            query_embedding=query_embedding,

            path=path,

        )

        return DocumentFeatures(

            path=path,

            filename=filename,

            extension=path.suffix.lower(),

            directories=directories,

            size=path.stat().st_size,

            query_matches=query_matches,

            semantic_similarity=semantic_similarity,

            is_documentation=any(

                key in stem

                for key in DOCUMENTATION_KEYWORDS

            ),

            is_configuration=(

                filename

                in CONFIGURATION_FILENAMES

            ),

            is_source_code=path.suffix.lower() != ".md",

        )


feature_extractor = FeatureExtractor()