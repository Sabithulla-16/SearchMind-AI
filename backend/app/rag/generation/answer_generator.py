from app.llm.service import llm_service
from app.llm.prompts import GENERATION_SYSTEM_PROMPT

from app.rag.generation.prompt_builder import prompt_builder
from app.rag.generation.models import ContextDocument


class AnswerGenerator:

    async def generate(
        self,
        query: str,
        documents: list[ContextDocument],
    ) -> str:

        prompt = prompt_builder.build(
            query=query,
            documents=documents,
        )

        response = await llm_service.generate(
            user_message=prompt,
            system_prompt=GENERATION_SYSTEM_PROMPT,
            temperature=0.2,
        )

        return response


answer_generator = AnswerGenerator()