import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

sys.path.insert(0, str(PROJECT_ROOT / "src"))

from price_tracker.database import PriceDatabase
from price_tracker.logger import setup_logger

logger = setup_logger("database_initializer")


def main():

    try:

        database = PriceDatabase()

        logger.info("Database initialized successfully!")

        print("\n================================")
        print(" DATABASE INITIALIZATION")
        print("================================")
        print("Status: SUCCESS")
        print("Database: price_tracker.db")
        print("================================\n")

        database.close()

    except Exception as error:

        logger.error("Database initialization failed: %s", error)

        print("Database initialization failed:", error)


if __name__ == "__main__":
    main()