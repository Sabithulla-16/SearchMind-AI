from app.rag.chunking.service import chunking_service

from app.rag.embeddings.service import embedding_service

from app.rag.indexing.service import indexing_service

from app.rag.hybrid.service import hybrid_service

from app.rag.candidate_selection.service import (
    candidate_selection_service,
)

from app.rag.reranking.service import reranking_service

from app.rag.context.service import context_service

from app.rag.generation.service import generation_service

from app.observability.service import observability_service


class RagPipeline:

    async def run(
        self,
        query: str,
        documents,
    ):

        # -----------------------------
        # Chunking
        # -----------------------------

        observability_service.start(
            "Chunking"
        )

        chunks = chunking_service.chunk_documents(
            documents
        )

        observability_service.stop(
            "Chunking"
        )

        observability_service.counter(
            "Chunks",
            len(chunks),
        )

        # -----------------------------
        # Embeddings
        # -----------------------------

        observability_service.start(
            "Embedding"
        )

        embedded = embedding_service.embed_chunks(
            chunks
        )

        observability_service.stop(
            "Embedding"
        )

        observability_service.counter(
            "Embedded Chunks",
            len(embedded),
        )

        # -----------------------------
        # Indexing
        # -----------------------------

        observability_service.start(
            "Indexing"
        )

        indexing_service.clear()

        indexing_service.index(
            embedded
        )

        hybrid_service.index(
            chunks
        )

        observability_service.stop(
            "Indexing"
        )

        # -----------------------------
        # Hybrid Search
        # -----------------------------

        observability_service.start(
            "Hybrid Search"
        )

        hybrid_results = hybrid_service.search(
            query
        )

        observability_service.stop(
            "Hybrid Search"
        )

        observability_service.counter(
            "Hybrid Results",
            len(hybrid_results),
        )

        # -----------------------------
        # Candidate Selection
        # -----------------------------

        observability_service.start(
            "Candidate Selector"
        )

        selection = candidate_selection_service.select(
            hybrid_results
        )

        observability_service.stop(
            "Candidate Selector"
        )

        observability_service.counter(
            "Candidates",
            len(selection.candidates),
        )

        # -----------------------------
        # Cross Encoder
        # -----------------------------

        observability_service.start(
            "Cross Encoder"
        )

        reranked = reranking_service.rerank(
            query=query,
            chunks=selection.candidates,
        )

        observability_service.stop(
            "Cross Encoder"
        )

        observability_service.counter(
            "Reranked Results",
            len(reranked),
        )

        # -----------------------------
        # Context
        # -----------------------------

        context = context_service.build(
            reranked
        )

        # -----------------------------
        # Generation
        # -----------------------------

        observability_service.start(
            "Generation"
        )

        generation = await generation_service.generate(
            query=query,
            context=context,
        )

        observability_service.stop(
            "Generation"
        )

        return {
            "generation": generation,
            "documents": documents,
            "chunks": chunks,
            "embedded": embedded,
            "hybrid_results": hybrid_results,
            "candidate_selection": selection,
            "reranked": reranked,
            "context": context,
        }


rag_pipeline = RagPipeline()