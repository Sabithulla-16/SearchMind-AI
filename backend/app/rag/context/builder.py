from collections import defaultdict

from app.rag.context.config import (
    MAX_CONTEXT_CHUNKS,
    MAX_CHUNKS_PER_SOURCE,
    MAX_CONTEXT_TOKENS,
)

from app.rag.context.models import ContextResult

from app.rag.generation.models import ContextDocument

from app.rag.context.utils import estimate_tokens


class ContextBuilder:

    def build(
        self,
        chunks,
    ) -> ContextResult:

        selected = []

        source_counter = defaultdict(int)

        total_tokens = 0

        skipped_duplicates = 0

        remaining = []

        # ----------------------------
        # PASS 1
        # One chunk per source
        # ----------------------------

        for chunk in chunks:

            if len(selected) >= MAX_CONTEXT_CHUNKS:
                break

            chunk_tokens = estimate_tokens(chunk.text)

            if (
                total_tokens + chunk_tokens
                > MAX_CONTEXT_TOKENS
            ):
                continue

            if source_counter[chunk.url] == 0:

                selected.append(

                    ContextDocument(

                        title=chunk.title,

                        url=chunk.url,

                        text=chunk.text,

                        score=chunk.score,

                    )

                )

                source_counter[chunk.url] += 1

                total_tokens += chunk_tokens

            else:

                remaining.append(chunk)

        # ----------------------------
        # PASS 2
        # Fill remaining capacity
        # ----------------------------

        for chunk in remaining:

            if len(selected) >= MAX_CONTEXT_CHUNKS:
                break

            if (
                source_counter[chunk.url]
                >= MAX_CHUNKS_PER_SOURCE
            ):
                skipped_duplicates += 1
                continue

            chunk_tokens = estimate_tokens(chunk.text)

            if (
                total_tokens + chunk_tokens
                > MAX_CONTEXT_TOKENS
            ):
                continue

            selected.append(

                ContextDocument(

                    title=chunk.title,

                    url=chunk.url,

                    text=chunk.text,

                    score=chunk.score,

                )

            )

            source_counter[chunk.url] += 1

            total_tokens += chunk_tokens

        return ContextResult(
            chunks=selected,
            total_tokens=total_tokens,
            unique_sources=len(source_counter),
            skipped_duplicates=skipped_duplicates,
        )


context_builder = ContextBuilder()