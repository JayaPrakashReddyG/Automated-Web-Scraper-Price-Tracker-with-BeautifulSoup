import pytest
import tempfile

from pathlib import Path

from price_tracker.database import PriceDatabase
from price_tracker.product_manager import ProductManager


@pytest.fixture
def sample_product():

    return {
        "product_id": "P001",
        "product_name": "Samsung Galaxy S24",
        "product_url": "https://example.com/samsung-s24",
        "target_price": 55000,
        "website": "ExampleStore",
        "category": "Electronics"
    }


@pytest.fixture
def sample_products():

    return [
        {
            "product_id": "P001",
            "product_name": "Samsung Galaxy S24",
            "product_url": "https://example.com/samsung-s24",
            "target_price": 55000,
            "website": "ExampleStore",
            "category": "Electronics"
        },
        {
            "product_id": "P002",
            "product_name": "iPhone 16",
            "product_url": "https://example.com/iphone-16",
            "target_price": 65000,
            "website": "ExampleStore",
            "category": "Electronics"
        }
    ]


@pytest.fixture
def temp_database(tmp_path):

    db_path = tmp_path / "test_price_tracker.db"

    database = PriceDatabase(db_path)

    yield database

    database.close()


@pytest.fixture
def product_manager():

    manager = ProductManager()

    return manager


@pytest.fixture
def sample_price_record():

    return {
        "product_id": "P001",
        "product_name": "Samsung Galaxy S24",
        "website": "ExampleStore",
        "product_url": "https://example.com/samsung-s24",
        "original_price": 74999,
        "current_price": 69999,
        "target_price": 55000,
        "price_difference": 14999,
        "discount_percentage": 6.67,
        "price_status": "Above Target",
        "last_checked": "2026-11-05 19:00:00"
    }