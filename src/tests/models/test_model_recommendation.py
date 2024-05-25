import unittest
from unittest.mock import patch, Mock

from src.config import Configuration
from src.models.recommendation import OpenAIRecommendator


class TestOpenAIRecommendator(unittest.TestCase):

    @patch('openai.OpenAI')
    async def test_give_recommendation(self, mock_openai):
        # Arrange
        mock_response = Mock()
        mock_response.choices = [Mock(message=Mock(content='Recommendations: Hiking, Camping, Fishing'))]
        mock_openai.return_value.chat.completions.create.return_value = mock_response

        prompt = "I want to go on a trip to the USA during the summer. Can you recommend some outdoor activities?"
        expected_recommendations = "Recommendations: Hiking, Camping, Fishing"

        # Act
        recommender = OpenAIRecommendator()
        recommendations = await recommender.give_recommendation(prompt)

        # Assert
        self.assertEqual(recommendations, expected_recommendations)
        mock_openai.return_value.chat.completions.create.assert_called_once_with(
            model=Configuration.OPENAI_MODEL,
            messages=[{"role": "user", "content": prompt}],
            n=1,
            timeout=10
        )
