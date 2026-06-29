from app.llm.service import llm_service

from app.search.prompts import SEARCH_PLANNER_PROMPT

from app.search.schemas import SearchPlan


class SearchPlanner:

    async def plan(self, query: str) -> SearchPlan:

        result = await llm_service.generate_json(
            user_message=query,
            system_prompt=SEARCH_PLANNER_PROMPT
        )

        result["original_query"] = query

        return SearchPlan(**result)

planner = SearchPlanner()