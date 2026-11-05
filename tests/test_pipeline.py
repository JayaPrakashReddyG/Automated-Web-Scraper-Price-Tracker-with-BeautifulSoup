from unittest.mock import patch

from price_tracker.price_tracker import PriceTracker


def test_complete_price_tracking_pipeline(
    sample_product,
    temp_database
):

    mock_html = """
    <html>
        <body>
            <h1>Samsung Galaxy S24</h1>
            <span class="price">₹49,999</span>
            <span class="original-price">₹59,999</span>
        </body>
    </html>
    """

    class MockScraper:

        def fetch_page(self, url):
            return mock_html

        def parse_html(self, html):

            from bs4 import BeautifulSoup

            return BeautifulSoup(html, "html.parser")

        def close(self):
            pass

    with patch(
        "price_tracker.price_tracker.WebScraper",
        return_value=MockScraper()
    ), patch(
        "price_tracker.price_tracker.PriceDatabase",
        return_value=temp_database
    ):

        tracker = PriceTracker()

        try:

            result = tracker.track_product(sample_product)

            assert result is not None

            assert result["product_id"] == "P001"

            assert result["current_price"] == 49999.0

            assert result["original_price"] == 59999.0

            assert result["price_status"] == "Target Reached"

            history = temp_database.get_price_history("P001")

            assert len(history) == 1

        finally:

            tracker.close()


def test_pipeline_handles_scraping_failure(sample_product):

    class FailedScraper:

        def fetch_page(self, url):
            raise Exception("Scraping failed")

        def close(self):
            pass

    with patch(
        "price_tracker.price_tracker.WebScraper",
        return_value=FailedScraper()
    ):

        tracker = PriceTracker()

        try:

            results = tracker.track_products([sample_product])

            assert results == []

        finally:

            tracker.close()