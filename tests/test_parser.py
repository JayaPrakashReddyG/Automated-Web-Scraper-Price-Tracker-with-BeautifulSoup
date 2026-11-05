import pytest

from price_tracker.parser import (
    parse_price,
    parse_discount,
    clean_product_name
)

from price_tracker.exceptions import ParserException


def test_parse_price():

    assert parse_price("₹1,299") == 1299.0


def test_parse_price_without_currency():

    assert parse_price("5999") == 5999.0


def test_parse_decimal_price():

    assert parse_price("₹1,299.50") == 1299.50


def test_invalid_price():

    with pytest.raises(ParserException):
        parse_price("Price unavailable")


def test_empty_price():

    with pytest.raises(ParserException):
        parse_price(None)


def test_parse_discount():

    assert parse_discount(1000, 800) == 20.0


def test_zero_original_price():

    assert parse_discount(0, 500) == 0.0


def test_clean_product_name():

    assert clean_product_name(" Samsung   Galaxy S24 ") == "Samsung Galaxy S24"


def test_empty_product_name():

    assert clean_product_name("") == ""