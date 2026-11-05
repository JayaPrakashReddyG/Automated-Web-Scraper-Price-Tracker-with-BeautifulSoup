import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

sys.path.insert(0, str(PROJECT_ROOT / "src"))

from price_tracker.product_manager import ProductManager
from price_tracker.database import PriceDatabase


def main():

    manager = ProductManager()

    products = manager.load_from_json()

    if not products:

        products = manager.load_from_csv()

    if not products:

        print("No sample products found!")

        return

    database = PriceDatabase()

    count = 0

    for product in products:

        try:

            database.add_product(product)

            count += 1

            print(
                f"Added: {product['product_name']}"
            )

        except Exception as error:

            print(
                f"Failed: {product.get('product_name')} - {error}"
            )

    database.close()

    print("\n================================")
    print(" SAMPLE PRODUCT IMPORT")
    print("================================")
    print(f"Total products: {len(products)}")
    print(f"Successfully added: {count}")
    print("================================")


if __name__ == "__main__":
    main()