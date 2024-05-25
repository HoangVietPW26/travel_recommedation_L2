from fastapi import APIRouter, Depends

from schemas.recommendation import (
    RecommendationRequest,
    RecommendationResponse
)
from services.recommendation.recommendation import (
    process_get_recommendation
)

router = APIRouter()

@router.get("/recommendation", response_model=RecommendationResponse)
async def get_recommendations(req: RecommendationRequest = Depends()):

    recommendations = await process_get_recommendation(req)

    return RecommendationResponse(
        country=req.country,
        season=req.season,
        recommendations=recommendations
    )
