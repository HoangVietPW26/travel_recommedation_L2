import unittest

from src.services.utils import parsing_recommendation

class TestParsingRecommendation(unittest.TestCase):

    def test_parsing_recommendation(self):

        mock_recommendation =  "1. Picnic\n2. Swimming\n3. Playing football"
        excepted_result = ['1. Picnic', '2. Swimming', '3. Playing football']

        parsed_recommendation = parsing_recommendation(mock_recommendation)

        self.assertEqual(parsed_recommendation, excepted_result)
