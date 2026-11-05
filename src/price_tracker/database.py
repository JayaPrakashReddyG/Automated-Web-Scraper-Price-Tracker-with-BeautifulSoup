import sqlite3

from pathlib import Path

from .config import DATABASE_PATH
from .logger import setup_logger

logger = setup_logger()


class PriceDatabase:

    def __init__(self, db_path=DATABASE_PATH):

        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)

        self.initialize_database()

    def get_connection(self):

        return sqlite3.connect(self.db_path)

    def initialize_database(self):

        with self.get_connection() as connection:

            cursor = connection.cursor()

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS products (
                    product_id TEXT PRIMARY KEY,
                    product_name TEXT NOT NULL,
                    product_url TEXT NOT NULL,
                    target_price REAL,
                    website TEXT,
                    category TEXT
                )
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS price_history (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    product_id TEXT NOT NULL,
                    original_price REAL,
                    current_price REAL NOT NULL,
                    target_price REAL,
                    discount_percentage REAL,
                    price_status TEXT,
                    last_checked TEXT,
                    FOREIGN KEY(product_id)
                    REFERENCES products(product_id)
                )
            """)

            connection.commit()

        logger.info("Database initialized successfully.")

    def add_product(self, product):

        with self.get_connection() as connection:

            connection.execute("""
                INSERT OR REPLACE INTO products
                (product_id, product_name, product_url,
                 target_price, website, category)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                product["product_id"],
                product["product_name"],
                product["product_url"],
                float(product["target_price"]),
                product["website"],
                product["category"]
            ))

        logger.info("Product saved: %s", product["product_id"])

    def get_all_products(self):

        with self.get_connection() as connection:

            cursor = connection.execute(
                "SELECT * FROM products"
            )

            columns = [column[0] for column in cursor.description]

            return [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]

    def save_price_history(self, record):

        with self.get_connection() as connection:

            connection.execute("""
                INSERT INTO price_history (
                    product_id,
                    original_price,
                    current_price,
                    target_price,
                    discount_percentage,
                    price_status,
                    last_checked
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                record["product_id"],
                record.get("original_price"),
                record["current_price"],
                record.get("target_price"),
                record.get("discount_percentage"),
                record.get("price_status"),
                record.get("last_checked")
            ))

        logger.info(
            "Price history saved for %s",
            record["product_id"]
        )

    def get_price_history(self, product_id):

        with self.get_connection() as connection:

            cursor = connection.execute("""
                SELECT * FROM price_history
                WHERE product_id = ?
                ORDER BY last_checked DESC
            """, (product_id,))

            columns = [column[0] for column in cursor.description]

            return [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]

    def close(self):
        pass