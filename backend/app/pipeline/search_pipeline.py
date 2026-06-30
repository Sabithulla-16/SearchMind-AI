from app.search.planner import planner

from app.search.service import search_service

from app.sources.service import source_service

from app.sources.models import SourceRequest

from app.pipeline.rag_pipeline import rag_pipeline

from app.observability.service import observability_service


class SearchPipeline:

    async def run(
        self,
        query: str,
    ):

        observability_service.reset()

        # -----------------------------
        # Planner
        # -----------------------------

        observability_service.start(
            "Planner"
        )

        plan = await planner.plan(
            query
        )

        observability_service.stop(
            "Planner"
        )

        # -----------------------------
        # Search
        # -----------------------------

        observability_service.start(
            "Search"
        )

        search_results = await search_service.search(
            plan
        )

        observability_service.stop(
            "Search"
        )

        observability_service.counter(
            "Search Results",
            len(search_results),
        )

        request = SourceRequest(

            query=query,

            web_urls=[
                result.url
                for result in search_results
            ],

            target_documents=5,

        )

        source_result = await source_service.retrieve(
            request
        )

        documents = source_result.documents

        result = await rag_pipeline.run(
            query=query,
            documents=documents,
        )

        result["plan"] = plan

        result["search_results"] = search_results

        result["source_result"] = source_result

        observability_service.summary()

        return result


search_pipeline = SearchPipeline()