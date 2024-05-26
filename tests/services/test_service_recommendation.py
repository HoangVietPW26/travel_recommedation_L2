import unittest
from unittest.mock import patch

from src.schemas.recommendation import RecommendationRequest
from src.services.recommendation.recommendation import process_get_recommendation


class TestProcessGetRecommendation(unittest.TestCase):

    @patch('src.models.recommendation.OpenAIRecommendator')
    @patch('src.services.utils.parsing_recommendation')
    async def test_process_get_recommendation(self, mock_parsing_recommendation, mock_openai_recommender):

        # Arrange
        mock_recommendation =  "1. Picnic\n2. Swimming\n3. Playing football"
        mock_parsed_recommendation = ['1. Picnic', '2. Swimming', '3. Playing football']
        mock_openai_recommender.return_value.give_recommendation.return_value = mock_recommendation
        mock_parsing_recommendation.return_value = mock_parsed_recommendation

        req = RecommendationRequest(country='USA', season='summer')
        expected_prompt = "Recommend three things to do in USA during Summer, just recommendations, no explaination."

        # Act
        recommendations = await process_get_recommendation(req)

        # Assert
        self.assertEqual(recommendations, mock_parsed_recommendation)
        mock_openai_recommender.return_value.give_recommendation.assert_called_once_with(prompt=expected_prompt)
        mock_parsing_recommendation.assert_called_once_with(mock_recommendation)
