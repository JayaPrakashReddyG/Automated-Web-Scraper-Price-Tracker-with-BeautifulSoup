import logging
from pathlib import Path

from .config import LOG_DIR, DEFAULT_LOG_LEVEL


def setup_logger(name="price_tracker"):

    LOG_DIR.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(getattr(logging, DEFAULT_LOG_LEVEL.upper()))

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    file_handler = logging.FileHandler(
        LOG_DIR / "price_tracker.log",
        encoding="utf-8"
    )

    console_handler = logging.StreamHandler()

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger   