import unittest
from unittest.mock import patch

from src.schemas.recommendation import RecommendationRequest, RecommendationResponse
from src.routes.recommendation_management.recommendation import get_recommendations


class TestGetRecommendations(unittest.TestCase):

    @patch('src.routes.recommendation_management.recommendation.process_get_recommendation')
    def test_get_recommendation(self, mock_process_get_recommend):

        mock_recommendations =  [
            "1. Picnic",
            "2. Swimming",
            "3. Playing football"
        ]
        mock_process_get_recommend.return_value = mock_recommendations

        mock_req = RecommendationRequest(
            country="vietnam",
            season="summer"
        )

        expected_response = RecommendationResponse(
            country="vietnam",
            season="summer",
            recommendations=mock_recommendations
        )

        response = get_recommendations(req=mock_req)
        self.assertEqual(response, expected_response)
        mock_process_get_recommend.assert_called_once_with(mock_req)
