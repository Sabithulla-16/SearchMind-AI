from nltk.tokenize import sent_tokenize

from app.rag.chunking.tokenizer import tokenizer


class TokenSplitter:

    def split(
        self,
        text: str,
        chunk_size: int = 512,
        overlap: int = 50,
    ):

        sentences = sent_tokenize(text)

        chunks = []

        current_sentences = []
        current_tokens = 0

        for sentence in sentences:

            token_count = tokenizer.count_tokens(sentence)

            # If adding this sentence would exceed the chunk size,
            # finalize the current chunk.
            if current_sentences and current_tokens + token_count > chunk_size:

                chunk_text = " ".join(current_sentences)
                chunks.append(chunk_text)

                # Create overlap using the last sentences
                overlap_sentences = []
                overlap_tokens = 0

                for s in reversed(current_sentences):
                    s_tokens = tokenizer.count_tokens(s)

                    if overlap_tokens + s_tokens > overlap:
                        break

                    overlap_sentences.insert(0, s)
                    overlap_tokens += s_tokens

                current_sentences = overlap_sentences
                current_tokens = overlap_tokens

            current_sentences.append(sentence)
            current_tokens += token_count

        if current_sentences:
            chunks.append(" ".join(current_sentences))

        return chunks


splitter = TokenSplitter()