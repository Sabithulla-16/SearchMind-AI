from app.rag.generation.models import ContextDocument


class CitationBuilder:

    def build(
        self,
        documents: list[ContextDocument],
    ) -> list[ContextDocument]:

        return documents


citation_builder = CitationBuilder()