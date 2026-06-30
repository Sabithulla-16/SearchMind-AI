from app.rag.context.builder import context_builder


class ContextService:

    def build(
        self,
        chunks,
    ):

        return context_builder.build(
            chunks
        )


context_service = ContextService()