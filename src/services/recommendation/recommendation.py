from models.recommendation import OpenAIRecommendator
from schemas.recommendation import RecommendationRequest

def process_get_recommendation(req: RecommendationRequest):

    openai_recommendator = OpenAIRecommendator()
    rec = openai_recommendator.give_recommendation(
                                prompt='What is the result of 1+1'
                            )
    
    return rec