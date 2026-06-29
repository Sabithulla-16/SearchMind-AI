from app.rag.generation.service import generation_service
from app.search.planner import planner

from app.search.service import search_service

from app.retriever.service import retriever_service

from app.rag.chunking.service import chunking_service

from app.rag.embeddings.service import embedding_service

from app.rag.indexing.service import indexing_service

from app.rag.generation.service import generation_service

from app.pipeline.models import PipelineResult


class SearchPipeline:

    async def run(
        self,
        query: str,
    ):

        print("\n========== PIPELINE ==========\n")

        # Step 1
        print("Planning search...")
        plan = await planner.plan(query)

        # Step 2
        print("Searching DDGS...")
        search_results = await search_service.search(plan)

        urls = [
            result.url
            for result in search_results[:5]
        ]

        # Step 3
        print(f"Retrieving {len(urls)} pages...")
        documents = await retriever_service.retrieve_many(
            urls
        )

        # Step 4
        print("Chunking...")

        chunks = chunking_service.chunk_documents(
            documents
        )

        # Step 5
        print("Embedding...")

        embedded = embedding_service.embed_chunks(
            chunks
        )

        # Step 6
        print("Indexing...")

        indexing_service.index(
            embedded
        )

        # Step 7
        print("Semantic Search...")

        semantic = indexing_service.search(
            query
        )

        print("Generating answer...")

        generation = await generation_service.generate(
            query=query,
            search_hits=semantic,
        )

        print("\n========== DONE ==========\n")

        return generation


search_pipeline = SearchPipeline()