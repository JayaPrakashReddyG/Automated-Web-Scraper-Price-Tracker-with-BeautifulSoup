from .logger import setup_logger

logger = setup_logger()


class PriceComparator:

    @staticmethod
    def calculate_discount(original_price, current_price):

        if original_price <= 0:
            return 0.0

        discount = (
            (original_price - current_price)
            / original_price
        ) * 100

        return round(discount, 2)

    @staticmethod
    def compare_price(current_price, target_price):

        difference = round(current_price - target_price, 2)

        if current_price <= target_price:
            status = "Target Reached"
        else:
            status = "Above Target"

        return {
            "current_price": current_price,
            "target_price": target_price,
            "price_difference": difference,
            "price_status": status
        }

    @staticmethod
    def find_lowest_price(products):

        if not products:
            return None

        return min(
            products,
            key=lambda p: float(p.get("current_price", float("inf")))
        )

    @staticmethod
    def compare_products(products):

        sorted_products = sorted(
            products,
            key=lambda p: float(
                p.get("current_price", float("inf"))
            )
        )

        logger.info("Products sorted by current price.")

        return sorted_products

    @staticmethod
    def get_price_savings(original_price, current_price):

        return round(original_price - current_price, 2)