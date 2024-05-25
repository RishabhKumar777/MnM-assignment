import structlog

# Define logger
logger = structlog.get_logger()


class DataTransformer:
    # Setting default length here but can be changed based on needs
    def __init__(self, data, min_title_length):
        self.data = data
        self.min_title_length = min_title_length

    def transform_data(self):
        # Filtering out posts that have less than 5 characters in the title
        logger.info('Removing posts that have less than {} in title'.format(self.min_title_length))
        transformed_data = self.data[self.data['title'].str.len() >= self.min_title_length]

        # Adding a new column called title_length
        logger.info('Adding new column called title length in data')
        transformed_data['title_length'] = transformed_data['title'].apply(len)
        return transformed_data
