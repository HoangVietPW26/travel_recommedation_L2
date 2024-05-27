from src.models.recommendation import OpenAIRecommendator
from src.schemas.recommendation import RecommendationRequest
from src.services.utils import parsing_recommendation


def process_get_recommendation(req: RecommendationRequest) -> list:

    prompt = f"Recommend three things to do in {req.country} during {req.season}, just recommendations, no explaination."
    openai_recommendator = OpenAIRecommendator()
    pre_parsed_recommendation = openai_recommendator.give_recommendation(
                                prompt=prompt,
                            )
    recommendations = parsing_recommendation(pre_parsed_recommendation)

    return recommendations
