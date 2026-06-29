from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def root():
    return {
        "message": "SearchMind AI Backend Running"
    }


@router.get("/health")
async def health():
    return {
        "status": "healthy"
    }