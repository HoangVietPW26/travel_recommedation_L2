from fastapi import APIRouter, Depends

from schemas.recommendation import (
    RecommendationRequest,
    RecommendationResponse
)
from services.recommendation.recommendation import (
    process_get_recommendation
)

router = APIRouter()

REC = [
    'Eat Vietnamese Pho',
    'Go camping in Ba Vi',
    'Have Picnic in Moc Chau'
]


@router.get("/recommendation", response_model=RecommendationResponse)
async def get_recommendation(req: RecommendationRequest = Depends()):

    rec = process_get_recommendation(req)

    return RecommendationResponse(
        country=req.country,
        season=req.season,
        recommendations=[str(rec)]
    )