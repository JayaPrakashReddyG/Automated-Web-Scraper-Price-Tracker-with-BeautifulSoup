import time
import requests

from bs4 import BeautifulSoup

from .config import (
    REQUEST_TIMEOUT,
    MAX_RETRIES,
    REQUEST_DELAY,
    USER_AGENT
)

from .exceptions import ScraperException
from .logger import setup_logger

logger = setup_logger()


class WebScraper:

    def __init__(self):

        self.session = requests.Session()

        self.session.headers.update({
            "User-Agent": USER_AGENT
        })

    def fetch_page(self, url):

        if not url.startswith(("http://", "https://")):
            raise ScraperException("Invalid product URL.")

        for attempt in range(MAX_RETRIES):

            try:

                response = self.session.get(
                    url,
                    timeout=REQUEST_TIMEOUT
                )

                response.raise_for_status()

                logger.info("Successfully fetched: %s", url)

                time.sleep(REQUEST_DELAY)

                return response.text

            except requests.RequestException as error:

                logger.warning(
                    "Attempt %s failed: %s",
                    attempt + 1,
                    error
                )

                if attempt == MAX_RETRIES - 1:
                    raise ScraperException(str(error)) from error

                time.sleep(REQUEST_DELAY)

    def parse_html(self, html):

        return BeautifulSoup(html, "html.parser")

    def close(self):

        self.session.close()