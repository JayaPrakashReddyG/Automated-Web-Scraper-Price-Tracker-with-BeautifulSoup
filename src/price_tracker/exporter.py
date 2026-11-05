import csv
import json

from pathlib import Path

from .config import PRICE_REPORT_CSV, PRICE_REPORT_JSON
from .exceptions import ExportException
from .logger import setup_logger

logger = setup_logger()


class PriceExporter:

    def export_to_csv(self, records, file_path=PRICE_REPORT_CSV):

        try:

            file_path = Path(file_path)
            file_path.parent.mkdir(parents=True, exist_ok=True)

            if not records:
                logger.warning("No records available for CSV export.")
                return

            fieldnames = list(records[0].keys())

            with open(
                file_path,
                "w",
                newline="",
                encoding="utf-8"
            ) as file:

                writer = csv.DictWriter(
                    file,
                    fieldnames=fieldnames
                )

                writer.writeheader()
                writer.writerows(records)

            logger.info("CSV report exported: %s", file_path)

        except (OSError, csv.Error, TypeError) as error:
            raise ExportException(str(error)) from error

    def export_to_json(self, records, file_path=PRICE_REPORT_JSON):

        try:

            file_path = Path(file_path)
            file_path.parent.mkdir(parents=True, exist_ok=True)

            with open(
                file_path,
                "w",
                encoding="utf-8"
            ) as file:

                json.dump(
                    records,
                    file,
                    indent=4,
                    ensure_ascii=False
                )

            logger.info("JSON report exported: %s", file_path)

        except (OSError, TypeError, ValueError) as error:
            raise ExportException(str(error)) from error

    def export_all(self, records):

        self.export_to_csv(records)
        self.export_to_json(records)

        logger.info("All reports exported successfully.")