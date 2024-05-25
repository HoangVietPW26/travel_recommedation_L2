from typing import List
from pydantic import BaseModel, Field

from src.schemas.utils import Seasons


class RecommendationRequest(BaseModel):

    country: str = Field()
    season: Seasons = Field()


class RecommendationResponse(BaseModel):

    country: str = Field()
    season: str = Field()
    recommendations: List[str] = Field()
