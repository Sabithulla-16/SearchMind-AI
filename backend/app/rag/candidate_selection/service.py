from app.rag.candidate_selection.selector import (
    candidate_selector,
)


class CandidateSelectionService:

    def select(
        self,
        candidates,
    ):

        return candidate_selector.select(
            candidates
        )


candidate_selection_service = (
    CandidateSelectionService()
)