from fastapi import APIRouter, Depends

from src.schemas.recommendation import (
    RecommendationRequest,
    RecommendationResponse
)
from src.services.recommendation.recommendation import (
    process_get_recommendation
)


router = APIRouter()

@router.get("/recommendation", response_model=RecommendationResponse)
async def get_recommendations(
            req: RecommendationRequest = Depends()
        ) -> RecommendationResponse:

    recommendations = await process_get_recommendation(req)

    return RecommendationResponse(
        country=req.country,
        season=req.season,
        recommendations=recommendations
    )
