import unittest
import pandas as pd
from data_etl.data_transformation import DataTransformer


# Trying to test data transformer class here
class TestDataTransformer(unittest.TestCase):
    def setUp(self):
        # Sample data
        self.sample_data = pd.DataFrame({'title': ['Spider Man', 'Thor', 'Iron Man', 'Hulk']})
        self.transformer = DataTransformer(self.sample_data, min_title_length=5)

    def test_transform_data(self):
        transformed_data = self.transformer.transform_data()
        # Check if the length of the title is greater than or equal to 5. Thor and Hulk should not be there.
        self.assertTrue(all(len(title) >= 5 for title in transformed_data['title']))
        # Check if the 'title_length' column is added
        self.assertTrue('title_length' in transformed_data.columns)
        # Check if the length of 'title_length' column matches the length of the corresponding title
        self.assertTrue(all(len(title) == length for title, length in zip(transformed_data['title'],
                                                                          transformed_data['title_length'])))


if __name__ == '__main__':
    unittest.main()