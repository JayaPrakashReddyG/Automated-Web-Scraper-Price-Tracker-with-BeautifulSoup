from unittest.mock import Mock, patch

import pytest
import requests

from price_tracker.scraper import WebScraper
from price_tracker.exceptions import ScraperException


def test_fetch_page_success():

    scraper = WebScraper()

    mock_response = Mock()
    mock_response.text = "<html><body>Test Product</body></html>"
    mock_response.raise_for_status.return_value = None

    with patch.object(scraper.session, "get", return_value=mock_response):
        with patch("price_tracker.scraper.time.sleep"):
            result = scraper.fetch_page("https://example.com")

    assert "Test Product" in result

    scraper.close()


def test_invalid_url():

    scraper = WebScraper()

    with pytest.raises(ScraperException):
        scraper.fetch_page("invalid-url")

    scraper.close()


def test_fetch_page_failure():

    scraper = WebScraper()

    with patch.object(
        scraper.session,
        "get",
        side_effect=requests.RequestException("Connection failed")
    ):
        with patch("price_tracker.scraper.time.sleep"):
            with pytest.raises(ScraperException):
                scraper.fetch_page("https://example.com")

    scraper.close()


def test_parse_html():

    scraper = WebScraper()

    soup = scraper.parse_html(
        "<html><body><h1>Samsung Galaxy</h1></body></html>"
    )

    assert soup.find("h1").text == "Samsung Galaxy"

    scraper.close()