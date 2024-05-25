import requests
import pandas as pd
from retrying import retry
import structlog

logger = structlog.get_logger('Extracting Data through API call')


class PostDataExtractor:
    SUCCESS_CODE = 200  # Success code
    MAX_RETRIES = 5  # number of retries
    BASE_WAIT_TIME = 1000  # in milliseconds

    def __init__(self, base_url: str, posts_endpoint: str):
        self.base_url = base_url
        self.posts_endpoint = posts_endpoint

    # retries being handled here with wait time
    @retry(stop_max_attempt_number=MAX_RETRIES, wait_fixed=BASE_WAIT_TIME)
    def make_request(self):
        response = requests.get(self.base_url + self.posts_endpoint)
        response.raise_for_status()  # Raise exception for non-200 status codes
        return response

    # class for extracting data and returning data. This also handles errors
    def extract_data(self):
        try:
            response = self.make_request()
            if response.status_code == self.SUCCESS_CODE:
                posts_data = response.json()
                data = pd.DataFrame(posts_data)
                return data
            else:
                logger.info("Error:", response.status_code)
                return None
        except Exception:
            logger.error("Error during request:", exc_info=True)
            return None
