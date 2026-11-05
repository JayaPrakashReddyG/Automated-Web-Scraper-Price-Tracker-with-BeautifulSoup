import json
import pytest

from price_tracker.product_manager import ProductManager
from price_tracker.exceptions import ProductNotFoundException


def test_add_product(product_manager, sample_product):

    product_manager.add_product(sample_product)

    assert len(product_manager.get_all_products()) == 1


def test_get_product_by_id(product_manager, sample_product):

    product_manager.add_product(sample_product)

    product = product_manager.get_product_by_id("P001")

    assert product["product_name"] == "Samsung Galaxy S24"


def test_product_not_found(product_manager):

    with pytest.raises(ProductNotFoundException):
        product_manager.get_product_by_id("P999")


def test_duplicate_product(product_manager, sample_product):

    product_manager.add_product(sample_product)

    with pytest.raises(ValueError):
        product_manager.add_product(sample_product)


def test_remove_product(product_manager, sample_product):

    product_manager.add_product(sample_product)

    product_manager.remove_product("P001")

    assert len(product_manager.get_all_products()) == 0


def test_load_from_csv(tmp_path, sample_product):

    csv_file = tmp_path / "products.csv"

    csv_file.write_text(
        "product_id,product_name,product_url,target_price,website,category\n"
        "P001,Samsung Galaxy S24,https://example.com,55000,ExampleStore,Electronics\n",
        encoding="utf-8"
    )

    manager = ProductManager()

    products = manager.load_from_csv(csv_file)

    assert len(products) == 1
    assert products[0]["product_id"] == "P001"


def test_save_to_json(tmp_path, sample_product):

    manager = ProductManager()

    manager.add_product(sample_product)

    json_file = tmp_path / "products.json"

    manager.save_to_json(json_file)

    with open(json_file, encoding="utf-8") as file:
        data = json.load(file)

    assert data[0]["product_id"] == "P001"


def test_add_product_missing_field(product_manager):

    with pytest.raises(ValueError):
        product_manager.add_product({
            "product_id": "P001"
        })