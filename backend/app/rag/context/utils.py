from app.rag.chunking.tokenizer import tokenizer


def estimate_tokens(text: str) -> int:
    return tokenizer.count_tokens(text)