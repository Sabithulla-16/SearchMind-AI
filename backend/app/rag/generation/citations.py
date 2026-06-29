from app.rag.generation.models import ContextDocument


class CitationBuilder:

    def build(
        self,
        documents: list[ContextDocument],
    ):

        citations = []

        for doc in documents:

            citations.append(
                {
                    "title": doc.title,
                    "url": doc.url,
                }
            )

        return citations


citation_builder = CitationBuilder()