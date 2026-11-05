from datetime import datetime

from .scraper import WebScraper
from .parser import parse_price, parse_discount
from .price_comparator import PriceComparator
from .database import PriceDatabase
from .logger import setup_logger

logger = setup_logger()


class PriceTracker:

    def __init__(self):

        self.scraper = WebScraper()
        self.database = PriceDatabase()
        self.comparator = PriceComparator()

    def track_product(self, product):

        logger.info(
            "Tracking product: %s",
            product["product_name"]
        )

        html = self.scraper.fetch_page(
            product["product_url"]
        )

        soup = self.scraper.parse_html(html)

        # Generic selectors for basic demo websites.
        price_element = (
            soup.select_one('[itemprop="price"]')
            or soup.select_one(".price")
            or soup.select_one(".product-price")
        )

        if not price_element:
            logger.warning(
                "Price element not found: %s",
                product["product_name"]
            )
            return None

        price_text = (
            price_element.get("content")
            or price_element.get_text(strip=True)
        )

        current_price = parse_price(price_text)

        original_price = current_price

        original_element = (
            soup.select_one(".original-price")
            or soup.select_one(".old-price")
        )

        if original_element:

            try:
                original_price = parse_price(
                    original_element.get_text(strip=True)
                )
            except Exception:
                original_price = current_price

        discount = parse_discount(
            original_price,
            current_price
        )

        comparison = self.comparator.compare_price(
            current_price,
            float(product["target_price"])
        )

        record = {
            "product_id": product["product_id"],
            "product_name": product["product_name"],
            "website": product["website"],
            "product_url": product["product_url"],
            "original_price": original_price,
            "current_price": current_price,
            "target_price": float(product["target_price"]),
            "price_difference": comparison["price_difference"],
            "discount_percentage": discount,
            "price_status": comparison["price_status"],
            "last_checked": datetime.now().isoformat(
                timespec="seconds"
            )
        }

        self.database.add_product(product)

        self.database.save_price_history(record)

        logger.info(
            "Price tracked successfully: %s",
            product["product_name"]
        )

        return record

    def track_products(self, products):

        results = []

        for product in products:

            try:

                result = self.track_product(product)

                if result:
                    results.append(result)

            except Exception as error:

                logger.error(
                    "Failed to track %s: %s",
                    product.get("product_name", "Unknown"),
                    error
                )

        return results

    def close(self):

        self.scraper.close()
        self.database.close()