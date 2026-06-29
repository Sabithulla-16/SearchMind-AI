import json

from app.llm.client import client
from app.core.config import settings


class LLMService:

    @staticmethod
    async def generate(
        user_message: str,
        system_prompt: str,
        temperature: float = 0.2,
    ):
        completion = client.chat.completions.create(
            model=settings.GROQ_MODEL,
            temperature=temperature,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ]
        )

        return completion.choices[0].message.content

    @staticmethod
    async def generate_json(
        user_message: str,
        system_prompt: str,
    ):
        response = await LLMService.generate(
            user_message=user_message,
            system_prompt=system_prompt,
            temperature=0
        )

        return json.loads(response)


llm_service = LLMService()