from fastapi import APIRouter

from pydantic import BaseModel

from app.llm.service import llm_service


router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


class ChatRequest(BaseModel):
    message: str


@router.post("/")
async def chat(request: ChatRequest):

    response = await llm_service.generate(
        request.message
    )

    return {
        "response": response
    }