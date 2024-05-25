class DataTransformer:
    def __init__(self, data, min_title_length=5):
        self.data = data
        self.min_title_length = min_title_length

    def transform_data(self):
        # Filtering out posts that have less than 5 characters in the title
        transformed_data = self.data[self.data['title'].str.len() >= self.min_title_length]

        # Adding a new column called title_length
        transformed_data['title_length'] = transformed_data['title'].apply(len)

        return transformed_data
