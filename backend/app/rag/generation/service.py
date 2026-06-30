from app.rag.generation.context_validator import context_validator
from app.rag.generation.answer_generator import answer_generator
from app.rag.generation.response_parser import response_parser
from app.rag.generation.citations import citation_builder
from app.rag.generation.models import GeneratedAnswer

class GenerationService:

    async def generate(
        self,
        query: str,
        context,
    ):

        context = context_validator.validate(
            context.chunks
        )

        answer = await answer_generator.generate(
            query=query,
            documents=context,
        )

        answer = response_parser.parse(answer)

        citations = citation_builder.build(
            context
        )

        return GeneratedAnswer(
            answer=answer,
            sources=citations,
        )


generation_service = GenerationService()