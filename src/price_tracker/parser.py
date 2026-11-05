import re

from .exceptions import ParserException


def parse_price(price_text):

    if price_text is None:
        raise ParserException("Price value is empty.")

    try:
        cleaned = str(price_text).replace(",", "")

        match = re.search(r"\d+(?:\.\d{1,2})?", cleaned)

        if not match:
            raise ParserException(
                f"Unable to extract price from: {price_text}"
            )

        price = float(match.group())

        if price <= 0:
            raise ParserException("Price must be greater than zero.")

        return round(price, 2)

    except (ValueError, TypeError) as error:
        raise ParserException(str(error)) from error


def parse_discount(original_price, current_price):

    if original_price <= 0:
        return 0.0

    discount = (
        (original_price - current_price) / original_price
    ) * 100

    return round(discount, 2)


def clean_product_name(name):

    if not name:
        return ""

    return " ".join(str(name).split())