from app.rag.generation.models import ContextDocument


class PromptBuilder:

    def build(
        self,
        query: str,
        documents: list[ContextDocument],
    ) -> str:

        context_sections = []

        for index, document in enumerate(documents, start=1):

            context_sections.append(
                f"""
Source {index}

Title:
{document.title}

URL:
{document.url}

Relevance Score:
{document.score:.3f}

Content:
{document.text}
"""
            )

        context = "\n\n=========================\n\n".join(
            context_sections
        )

        prompt = f"""
Answer the user's question using ONLY the provided context.

If the answer cannot be determined from the context,
clearly state that the available sources do not contain enough information.

Do not make up facts.

Question:
{query}

=====================================================

CONTEXT

{context}

=====================================================

Instructions:

- Answer only using the retrieved context.
- Do not use outside knowledge.
- If multiple sources provide the same information, combine them naturally.
- If the context is insufficient, explicitly say that the available sources do not contain enough information.
- Do not mention that you were given context.
- Do not mention "Source 1" or "Source 2" in the answer.
- Write the answer in clear Markdown.
"""

        return prompt.strip()


prompt_builder = PromptBuilder()