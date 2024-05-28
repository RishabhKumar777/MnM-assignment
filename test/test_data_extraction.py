import unittest
from unittest.mock import patch, MagicMock
from requests.exceptions import HTTPError
import pandas as pd
from data_etl.data_extraction import PostDataExtractor


class TestPostDataExtractor(unittest.TestCase):
    @patch('data_etl.data_extraction.requests.get')
    def test_extract_data_success(self, mock_get):
        # Mock successful API response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [{'id': 1, 'title': 'MethodsNMastery'}, {'id': 2, 'title': 'Innovision'}]
        mock_get.return_value = mock_response

        # Initialize PostDataExtractor with mock URL and endpoint
        extractor = PostDataExtractor('https://example.com', '/posts')

        # Call extract_data method
        extracted_data, input_count = extractor.extract_data()

        # Assert that extract_data returns the expected DataFrame and count. We have 2 rows above
        self.assertIsInstance(extracted_data, pd.DataFrame)
        self.assertEqual(input_count, 2)
        self.assertEqual(extracted_data.iloc[0]['title'], 'MethodsNMastery')

    @patch('data_etl.data_extraction.requests.get')
    def test_extract_data_failure(self, mock_get):
        # Mock unsuccessful API response
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        # Initialize PostDataExtractor with mock URL and endpoint
        extractor = PostDataExtractor('https://example.com', '/posts')

        # Call extract_data method
        extracted_data, input_count = extractor.extract_data()

        # Assert that extract_data returns None for data and count since the response is not 200 anymore
        self.assertIsNone(extracted_data)
        self.assertIsNone(input_count)

    @patch('data_etl.data_extraction.requests.get')
    def test_extract_data_exception(self, mock_get):
        # Mock exception during API request
        mock_get.side_effect = HTTPError('Mock HTTPError')

        # Initialize PostDataExtractor with mock URL and endpoint
        extractor = PostDataExtractor('https://example.com', '/posts')

        # Extract Mock Data
        extracted_data, input_count = extractor.extract_data()

        # Assert that extract_data returns None for data and count
        self.assertIsNone(extracted_data)
        self.assertIsNone(input_count)


if __name__ == '__main__':
    unittest.main()