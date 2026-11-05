from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = PROJECT_ROOT / "data"
INPUT_DIR = DATA_DIR / "input"
OUTPUT_DIR = DATA_DIR / "output"
DATABASE_DIR = DATA_DIR / "database"

LOG_DIR = PROJECT_ROOT / "logs"

PRODUCTS_CSV = INPUT_DIR / "products.csv"
PRODUCTS_JSON = INPUT_DIR / "sample_products.json"

PRICE_REPORT_CSV = OUTPUT_DIR / "price_report.csv"
PRICE_REPORT_JSON = OUTPUT_DIR / "price_report.json"

DATABASE_PATH = DATABASE_DIR / "price_tracker.db"

REQUEST_TIMEOUT = 15

MAX_RETRIES = 3

REQUEST_DELAY = 2

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36"
)

CURRENCY = "INR"

PRICE_ALERT_ENABLED = True

DEFAULT_LOG_LEVEL = "INFO"