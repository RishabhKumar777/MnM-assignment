import requests
import pandas as pd
from retrying import retry
import structlog

# Define logger
logger = structlog.get_logger('Extracting Data through API call')


class PostDataExtractor:
    SUCCESS_CODE = 200  # Success code
    MAX_RETRIES = 5  # number of retries
    BASE_WAIT_TIME = 1000  # in milliseconds

    # setting defaults here but can be used to extract other data too based on inputs
    def __init__(self, base_url,
                 posts_endpoint):
        self.base_url = base_url
        self.posts_endpoint = posts_endpoint

    # retries being handled here with wait time
    @retry(stop_max_attempt_number=MAX_RETRIES, wait_fixed=BASE_WAIT_TIME)
    def make_request(self):
        logger.info('making Request for', request=self.base_url + self.posts_endpoint)
        response = requests.get(self.base_url + self.posts_endpoint)
        response.raise_for_status()  # Raises exception for non-200 status codes
        return response

    # class for extracting data and returning data. This also handles errors
    def extract_data(self):
        try:
            response = self.make_request()
            if response.status_code == self.SUCCESS_CODE:
                logger.info('Successfully extracting data from API')
                posts_data = response.json()
                logger.info('Extraction complete')
                data = pd.DataFrame(posts_data)
                count = len(data)
                logger.info(f'Successfully extracted {count} data points from API')
                return data, count
            else:
                logger.info("Error:", response.status_code)
                return None, None
        except Exception:
            logger.error("Error during request:", exc_info=True)
            return None, None
