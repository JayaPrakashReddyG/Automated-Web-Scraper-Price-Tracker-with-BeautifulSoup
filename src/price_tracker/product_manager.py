import csv
import json

from pathlib import Path

from .config import PRODUCTS_CSV, PRODUCTS_JSON
from .exceptions import ProductNotFoundException
from .logger import setup_logger

logger = setup_logger()


class ProductManager:

    def __init__(self):
        self.products = []

    def load_from_csv(self, file_path=PRODUCTS_CSV):

        file_path = Path(file_path)

        if not file_path.exists():
            logger.error("Products CSV file not found.")
            return []

        with open(file_path, "r", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)
            self.products = list(reader)

        logger.info("Loaded %s products from CSV.", len(self.products))

        return self.products

    def load_from_json(self, file_path=PRODUCTS_JSON):

        file_path = Path(file_path)

        if not file_path.exists():
            logger.error("Products JSON file not found.")
            return []

        with open(file_path, "r", encoding="utf-8") as file:
            self.products = json.load(file)

        logger.info("Loaded %s products from JSON.", len(self.products))

        return self.products

    def get_all_products(self):
        return self.products

    def get_product_by_id(self, product_id):

        for product in self.products:
            if product.get("product_id") == product_id:
                return product

        raise ProductNotFoundException(
            f"Product {product_id} not found."
        )

    def add_product(self, product):

        required_fields = [
            "product_id",
            "product_name",
            "product_url",
            "target_price",
            "website",
            "category"
        ]

        for field in required_fields:
            if field not in product:
                raise ValueError(f"Missing field: {field}")

        if any(
            p.get("product_id") == product["product_id"]
            for p in self.products
        ):
            raise ValueError("Product ID already exists.")

        self.products.append(product)

        logger.info("Product added: %s", product["product_name"])

        return product

    def remove_product(self, product_id):

        original_count = len(self.products)

        self.products = [
            p for p in self.products
            if p.get("product_id") != product_id
        ]

        if len(self.products) == original_count:
            raise ProductNotFoundException(
                f"Product {product_id} not found."
            )

        logger.info("Product removed: %s", product_id)

    def save_to_json(self, file_path=PRODUCTS_JSON):

        file_path = Path(file_path)
        file_path.parent.mkdir(parents=True, exist_ok=True)

        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(self.products, file, indent=4)

        logger.info("Products saved to JSON.")