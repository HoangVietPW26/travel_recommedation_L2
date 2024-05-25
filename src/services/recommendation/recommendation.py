from models.recommendation import OpenAIRecommendator
from schemas.recommendation import RecommendationRequest
from services.utils import parsing_recommendation
def process_get_recommendation(req: RecommendationRequest):

    prompt = f"Recommend three things to do in {req.country} during {req.season}, just recommendations, no explaination."
    openai_recommendator = OpenAIRecommendator()
    rec = openai_recommendator.give_recommendation(
                                prompt=prompt,
                            )
    rec = parsing_recommendation(rec)

    return rec
