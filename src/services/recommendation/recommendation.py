from src.models.recommendation import OpenAIRecommendator
from src.schemas.recommendation import RecommendationRequest
from src.services.utils import parsing_recommendation


async def process_get_recommendation(req: RecommendationRequest):

    prompt = f"Recommend three things to do in {req.country} during {req.season}, just recommendations, no explaination."
    openai_recommendator = OpenAIRecommendator()
    rec = await openai_recommendator.give_recommendation(
                                prompt=prompt,
                            )
    rec = parsing_recommendation(rec)

    return rec
