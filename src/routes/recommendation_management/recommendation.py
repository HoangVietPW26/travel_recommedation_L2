from fastapi import APIRouter, Depends, HTTPException

from schemas.recommendation import (
    RecommendationRequest,
    RecommendationResponse
)

router = APIRouter()

REC = [
    'Eat Vietnamese Pho',
    'Go camping in Ba Vi',
    'Have Picnic in Moc Chau'
]


@router.get("/recommendation", response_model=RecommendationResponse)
async def get_recommendation(req: RecommendationRequest = Depends()):
    return RecommendationResponse(
        country=req.country,
        season=req.season,
        recommendations=REC
    )