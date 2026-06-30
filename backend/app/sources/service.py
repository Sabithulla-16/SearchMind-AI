from app.sources.manager import source_manager

from app.sources.models import SourceRequest


class SourceService:

    async def retrieve(
        self,
        request: SourceRequest,
    ):

        return await source_manager.retrieve(
            request
        )


source_service = SourceService()