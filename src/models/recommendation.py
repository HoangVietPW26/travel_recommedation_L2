from openai import OpenAI
from config import Configuration


OPENAI_API_KEY = Configuration.OPENAI_API_KEY
OPENAI_MODEL = Configuration.OPENAI_MODEL


class OpenAIRecommendator:

    def __init__(self, api_key=OPENAI_API_KEY) -> None:
        self.client = OpenAI(api_key=api_key)

    async def give_recommendation(self, prompt: str) -> str:
        
        response = self.client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {"role": "user", "content": prompt}
            ],
            n=1,
            timeout=10
        )

        recommendations = response.choices[0].message.content

        return recommendations
