from price_tracker.price_comparator import PriceComparator


def test_calculate_discount():

    result = PriceComparator.calculate_discount(1000, 800)

    assert result == 20.0


def test_zero_original_price():

    result = PriceComparator.calculate_discount(0, 500)

    assert result == 0.0


def test_compare_price_target_reached():

    result = PriceComparator.compare_price(500, 600)

    assert result["price_status"] == "Target Reached"


def test_compare_price_above_target():

    result = PriceComparator.compare_price(800, 600)

    assert result["price_status"] == "Above Target"


def test_find_lowest_price(sample_products):

    products = [
        {"product_name": "Product A", "current_price": 1000},
        {"product_name": "Product B", "current_price": 500},
        {"product_name": "Product C", "current_price": 1500}
    ]

    result = PriceComparator.find_lowest_price(products)

    assert result["product_name"] == "Product B"


def test_find_lowest_price_empty():

    assert PriceComparator.find_lowest_price([]) is None


def test_compare_products():

    products = [
        {"product_name": "A", "current_price": 3000},
        {"product_name": "B", "current_price": 1000},
        {"product_name": "C", "current_price": 2000}
    ]

    result = PriceComparator.compare_products(products)

    assert result[0]["product_name"] == "B"


def test_price_savings():

    result = PriceComparator.get_price_savings(1000, 750)

    assert result == 250