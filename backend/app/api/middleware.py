import uuid
import time

from fastapi import Request


async def request_middleware(
    request: Request,
    call_next,
):

    request.state.request_id = str(
        uuid.uuid4()
    )

    start = time.perf_counter()

    response = await call_next(
        request
    )

    duration = (
        time.perf_counter() - start
    ) * 1000

    print(

        f"[{request.state.request_id}] "

        f"{request.method} "

        f"{request.url.path} "

        f"{duration:.2f} ms"

    )

    response.headers[
        "X-Request-ID"
    ] = request.state.request_id

    return response