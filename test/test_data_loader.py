import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from data_etl.data_loader import DataLoader
from sqlalchemy import MetaData, Table, Column, Integer, String
import pandas as pd
import tempfile


class TestDataLoader(unittest.TestCase):
    def setUp(self):
        # Create a temp database for testing. Don't worry this will get deleted
        self.db_file = tempfile.NamedTemporaryFile()
        self.engine = create_engine(f'sqlite:///{self.db_file.name}')
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

        # Create the posts table in the test database

        self.metadata = MetaData()
        self.posts = Table(
            'posts', self.metadata,
            Column('id', Integer, primary_key=True),
            Column('title', String),
            Column('body', String),
            Column('title_length', Integer)
        )
        self.metadata.create_all(self.engine)

    def test_load_data(self):
        # Define some test data
        test_data = {
            'id': [1],
            'title': '[Ed Sheeran]',
            'body': '[Thinking Out Loud]',
            'title_length': [10]
        }
        test_data = pd.DataFrame(test_data)
        # Instantiate DataLoader with the test temporary database and test data
        data_loader = DataLoader(self.db_file.name, test_data)

        # Call the load_data method
        new_data_points, old_data_points = data_loader.load_data()

        # Query the database to check if data is loaded correctly
        post = self.session.query(self.posts).filter_by(id=1).first()

        # Check if data points are correctly inserted
        self.assertEqual(new_data_points, 1)
        self.assertEqual(old_data_points, 0)
        # Check if data is correctly inserted into the database
        self.assertEqual(post.id, test_data['id'][0])
        self.assertEqual(post.title, test_data['title'][0])
        self.assertEqual(post.body, test_data['body'][0])
        self.assertEqual(post.title_length, test_data['title_length'][0])

    def tearDown(self):
        # Closing the session and dropping the tables after the test
        self.session.close()
        self.posts.drop(self.engine)
        # Closing and deleting the temporary database file
        self.db_file.close()


if __name__ == '__main__':
    unittest.main()
