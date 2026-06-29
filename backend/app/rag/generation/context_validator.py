from app.rag.generation.models import ContextDocument
from app.rag.chunking.tokenizer import tokenizer


class ContextValidator:

    def validate(
        self,
        documents: list[ContextDocument],
        max_tokens: int = 3000,
        min_text_length: int = 50,
    ) -> list[ContextDocument]:
        """
        Validate and clean retrieved context before sending it to the LLM.

        - Removes empty documents
        - Removes duplicate text
        - Removes very short documents
        - Enforces a total token budget
        """

        validated = []

        seen_texts = set()

        current_tokens = 0

        for document in documents:

            text = document.text.strip()

            if not text:
                continue

            if len(text) < min_text_length:
                continue

            normalized = " ".join(text.split()).lower()

            if normalized in seen_texts:
                continue

            tokens = tokenizer.count_tokens(text)

            if current_tokens + tokens > max_tokens:
                break

            current_tokens += tokens

            seen_texts.add(normalized)

            validated.append(document)

        return validated


context_validator = ContextValidator()