import argparse
from data_extraction import PostDataExtractor
from data_transformation import DataTransformer
from data_loader import DataLoader


def main(base_url: str, posts_endpoint: str, min_title_length: str, db_path):
    """
    This is the class which calls all 3 classes for extraction, transformation and loading of data
    :param base_url:
    :param posts_endpoint:
    :param min_title_length:
    :param db_path:
    :return:
    """
    # Step 1: Extract data
    extractor = PostDataExtractor(base_url, posts_endpoint)
    extracted_data = extractor.extract_data()

    # Step 2: Transform data
    transformer = DataTransformer(extracted_data, min_title_length=min_title_length)
    transformed_data = transformer.transform_data()

    # Step 3: Load data
    loader = DataLoader(db_path, transformed_data)
    loader.load_data()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extract, Transform, and Load Data')
    parser.add_argument('--base-url',
                        type=str,
                        help='URL for extraction of data',
                        default='https://jsonplaceholder.typicode.com')
    parser.add_argument('--posts-endpoint',
                        type=str,
                        help='Endpoint for data extraction',
                        default='/posts')
    parser.add_argument('--min-title-length',
                        type=int,
                        help='Minimum title length for data transformation',
                        default=5)
    parser.add_argument('--db-path',
                        type=str, help='Path to SQLite database for data loading',
                        default='posts.db')
    args = parser.parse_args()
    main(base_url=args.base_url,
         posts_endpoint=args.posts_endpoint,
         min_title_length=args.min_title_length,
         db_path=args.db_path)
