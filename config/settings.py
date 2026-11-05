import os
from pathlib import Path
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[1]

load_dotenv(PROJECT_ROOT / ".env")

# Application settings
APP_NAME = "Automated Web Scraper & Price Tracker"
APP_VERSION = "1.0.0"
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

# Currency settings
CURRENCY = os.getenv("CURRENCY", "INR")
CURRENCY_SYMBOL = "₹"

# Scraper settings
REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", "15"))
MAX_RETRIES = int(os.getenv("MAX_RETRIES", "3"))
REQUEST_DELAY = float(os.getenv("REQUEST_DELAY", "2"))

USER_AGENT = os.getenv(
    "USER_AGENT",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"
)

# Directory settings
DATA_DIR = PROJECT_ROOT / "data"
INPUT_DIR = DATA_DIR / "input"
OUTPUT_DIR = DATA_DIR / "output"
DATABASE_DIR = DATA_DIR / "database"

LOG_DIR = PROJECT_ROOT / "logs"

# File settings
PRODUCTS_CSV = INPUT_DIR / "products.csv"
PRODUCTS_JSON = INPUT_DIR / "sample_products.json"

PRICE_REPORT_CSV = OUTPUT_DIR / "price_report.csv"
PRICE_REPORT_JSON = OUTPUT_DIR / "price_report.json"

DATABASE_PATH = DATABASE_DIR / "price_tracker.db"

# Alert settings
PRICE_ALERT_ENABLED = True

# Dashboard settings
DASHBOARD_TITLE = "PriceTracker Pro"
DASHBOARD_LAYOUT = "wide"

# Create required directories
for directory in [
    INPUT_DIR,
    OUTPUT_DIR,
    DATABASE_DIR,
    LOG_DIR
]:
    directory.mkdir(parents=True, exist_ok=True)