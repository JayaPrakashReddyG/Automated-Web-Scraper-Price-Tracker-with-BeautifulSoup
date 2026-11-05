"""
Automated Web Scraper & Price Tracker

Main application entry point.

This script:
1. Loads product information.
2. Tracks product prices.
3. Compares current and target prices.
4. Stores price history.
5. Generates CSV and JSON reports.
"""

import sys
from pathlib import Path

# Add project source directory
PROJECT_ROOT = Path(__file__).resolve().parent
SRC_PATH = PROJECT_ROOT / "src"

sys.path.insert(0, str(SRC_PATH))

from price_tracker.product_manager import ProductManager
from price_tracker.price_tracker import PriceTracker
from price_tracker.exporter import PriceExporter
from price_tracker.logger import setup_logger
from price_tracker.config import INPUT_DIR, OUTPUT_DIR


def main():
    """Run the price tracking application."""

    logger = setup_logger()

    print("\n" + "=" * 60)
    print(" AUTOMATED WEB SCRAPER & PRICE TRACKER ")
    print("=" * 60)

    tracker = None

    try:
        logger.info("Application started.")

        # Load product information
        product_manager = ProductManager()

        csv_file = INPUT_DIR / "products.csv"
        json_file = INPUT_DIR / "sample_products.json"

        if csv_file.exists():
            products = product_manager.load_from_csv(csv_file)
        elif json_file.exists():
            products = product_manager.load_from_json(json_file)
        else:
            logger.error("No product input file found.")
            print("Error: No product input file found.")
            return

        if not products:
            logger.warning("No products available for tracking.")
            print("No products available.")
            return

        print(f"\nProducts loaded: {len(products)}")

        # Initialize price tracker
        tracker = PriceTracker()

        # Track products
        print("\nStarting price tracking...\n")

        results = tracker.track_products(products)

        # Generate reports
        exporter = PriceExporter()

        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

        exporter.export_all(
            results,
            csv_path=OUTPUT_DIR / "price_report.csv",
            json_path=OUTPUT_DIR / "price_report.json"
        )

        # Display summary
        successful = sum(
            1 for result in results
            if result.get("current_price") is not None
        )

        print("\n" + "=" * 60)
        print(" TRACKING SUMMARY ")
        print("=" * 60)

        print(f"Total products : {len(products)}")
        print(f"Successful     : {successful}")
        print(f"Failed         : {len(products) - successful}")

        print("\nReports generated:")
        print(f"CSV  : {OUTPUT_DIR / 'price_report.csv'}")
        print(f"JSON : {OUTPUT_DIR / 'price_report.json'}")

        logger.info("Application completed successfully.")

    except KeyboardInterrupt:
        print("\nApplication interrupted by user.")
        logger.warning("Application interrupted.")

    except Exception as error:
        logger.exception("Application failed: %s", error)
        print(f"\nApplication error: {error}")

    finally:
        if tracker is not None:
            tracker.close()

        print("\nApplication finished.")


if __name__ == "__main__":
    main()