import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

sys.path.insert(0, str(PROJECT_ROOT / "src"))

from price_tracker.product_manager import ProductManager
from price_tracker.price_tracker import PriceTracker
from price_tracker.exporter import PriceExporter
from price_tracker.logger import setup_logger


logger = setup_logger("scraper_runner")


def main():

    print("\n====================================")
    print(" AUTOMATED PRICE TRACKER")
    print("====================================")

    manager = ProductManager()

    products = manager.load_from_csv()

    if not products:

        products = manager.load_from_json()

    if not products:

        print("No products available for tracking!")

        return

    print(f"Products loaded: {len(products)}")

    tracker = PriceTracker()

    try:

        print("\nStarting price tracking...\n")

        results = tracker.track_products(products)

        if results:

            exporter = PriceExporter()

            exporter.export_all(results)

            print("\nPrice tracking completed!")

            print(f"Successfully tracked: {len(results)}")

            for result in results:

                print(
                    f"{result['product_name']} | "
                    f"₹{result['current_price']} | "
                    f"{result['price_status']}"
                )

            print("\nReports generated:")
            print(" - data/output/price_report.csv")
            print(" - data/output/price_report.json")

        else:

            print("No prices could be extracted.")

            print("Check product URLs and website selectors.")

    except Exception as error:

        logger.exception("Price tracking failed: %s", error)

        print("Error:", error)

    finally:

        tracker.close()

    print("\n====================================")
    print(" PROCESS FINISHED")
    print("====================================")


if __name__ == "__main__":
    main()