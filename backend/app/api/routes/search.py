from fastapi import APIRouter

from app.api.models import SearchRequest

from fastapi import Request

from fastapi.responses import (
    JSONResponse,
)

from app.api.responses import (
    response_builder,
)

from app.api.services.search_service import (
    api_search_service,
)

router = APIRouter()


@router.post("/search")
async def search(

    http_request: Request,

    request: SearchRequest,
):

    try:

        result = await api_search_service.search(
            request
        )

        response = response_builder.success(

            request=http_request,

            pipeline_type=request.type,

            query=request.query,

            result=result,

        )

        return JSONResponse(

            status_code=200,

            content=response.model_dump(),

        )

    except ValueError as error:

        response = response_builder.error(

            request=http_request,

            error=error,

        )

        return JSONResponse(

            status_code=400,

            content=response.model_dump(),

        )

    except Exception as error:

        response = response_builder.error(

            request=http_request,

            error=error,

        )

        return JSONResponse(

            status_code=500,

            content=response.model_dump(),

        )