import unittest
from unittest.mock import patch
from fastapi.testclient import TestClient

from src.app import app
from src.schemas.recommendation import RecommendationRequest
from src.routes.recommendation_management.recommendation import get_recommendations


client = TestClient(app)

class TestGetRecommendations(unittest.TestCase):

    
    @patch('src.services.recommendation.recommendation.process_get_recommendation')
    async def test_get_recommendation(self, mock_process_get_recommend):

        mock_recommendations =  [
            "1. Picnic",
            "2. Swimming",
            "3. Playing football"
        ]
        mock_process_get_recommend.return_value = mock_recommendations

        mock_req = {
            "country": "vietnam",
            "seasom": "summer"
        }

        expected_response = {
            "country": "vietnam",
            "season": "summer",
            "recommendations": mock_recommendations
        }

        response = await get_recommendations(req=mock_req)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response, expected_response)
        mock_process_get_recommend.assert_called_once_with(RecommendationRequest(**mock_req))
