def test_database_initialization(temp_database):

    products = temp_database.get_all_products()

    assert products == []


def test_add_product(temp_database, sample_product):

    temp_database.add_product(sample_product)

    products = temp_database.get_all_products()

    assert len(products) == 1

    assert products[0]["product_id"] == "P001"


def test_save_price_history(
    temp_database,
    sample_product,
    sample_price_record
):

    temp_database.add_product(sample_product)

    temp_database.save_price_history(sample_price_record)

    history = temp_database.get_price_history("P001")

    assert len(history) == 1

    assert history[0]["current_price"] == 69999


def test_multiple_price_history(
    temp_database,
    sample_product,
    sample_price_record
):

    temp_database.add_product(sample_product)

    temp_database.save_price_history(sample_price_record)

    second_record = sample_price_record.copy()
    second_record["current_price"] = 65000

    temp_database.save_price_history(second_record)

    history = temp_database.get_price_history("P001")

    assert len(history) == 2


def test_update_existing_product(temp_database, sample_product):

    temp_database.add_product(sample_product)

    updated_product = sample_product.copy()
    updated_product["target_price"] = 50000

    temp_database.add_product(updated_product)

    products = temp_database.get_all_products()

    assert len(products) == 1
    assert products[0]["target_price"] == 50000