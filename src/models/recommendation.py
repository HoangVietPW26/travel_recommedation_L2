from openai import OpenAI
from config import Configuration

OPENAI_API_KEY = Configuration.OPENAI_API_KEY

class OpenAIRecommendator:

    def __init__(self, api_key=OPENAI_API_KEY) -> None:
        self.client = OpenAI(api_key=api_key)

    def give_recommendation(self, prompt):
        
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        recommendations = completion.choices[0].message.content
        
        return recommendations
