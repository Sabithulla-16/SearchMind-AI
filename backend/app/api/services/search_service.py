from app.pipeline.search_pipeline import (
    search_pipeline,
)

from app.pipeline.pdf_pipeline import (
    pdf_pipeline,
)

from app.pipeline.filesystem_pipeline import (
    filesystem_pipeline,
)

from app.pipeline.github_pipeline import (
    github_pipeline,
)

from app.pipeline.multisource_pipeline import (
    multisource_pipeline,
)

from app.api.models import SearchRequest


class APISearchService:

        async def search(
            self,
            request: SearchRequest,
        ):

            # -------------------------
            # Validation
            # -------------------------

            if request.type == "pdf":

                if not request.pdf_paths:

                    raise ValueError(
                        "No PDF path provided."
                    )

            elif request.type == "filesystem":

                if not request.folders:

                    raise ValueError(
                        "No folder path provided."
                    )

            elif request.type == "github":

                if not request.github_repositories:

                    raise ValueError(
                        "No GitHub repository provided."
                    )

            elif request.type == "multisource":

                if (
                    not request.pdf_paths
                    and not request.folders
                    and not request.github_repositories
                ):

                    raise ValueError(
                        "At least one source is required."
                    )

            # -------------------------
            # Pipeline Dispatch
            # -------------------------

            match request.type:

                case "web":

                    return await search_pipeline.run(
                        request.query
                    )

                case "pdf":

                    return await pdf_pipeline.run(

                        pdf_path=request.pdf_paths[0],

                        query=request.query,

                    )

                case "filesystem":

                    return await filesystem_pipeline.run(

                        folder=request.folders[0],

                        query=request.query,

                    )

                case "github":

                    return await github_pipeline.run(

                        repository=request.github_repositories[0],

                        query=request.query,

                    )

                case "multisource":

                    return await multisource_pipeline.run(

                        query=request.query,

                        pdf_paths=request.pdf_paths,

                        folders=request.folders,

                        github_repositories=request.github_repositories,

                    )

            raise ValueError(
                f"Unsupported search type: {request.type}"
            )

api_search_service = APISearchService()