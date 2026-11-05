import csv
import json

from price_tracker.exporter import PriceExporter


def test_export_to_csv(tmp_path, sample_price_record):

    exporter = PriceExporter()

    output_file = tmp_path / "price_report.csv"

    exporter.export_to_csv(
        [sample_price_record],
        output_file
    )

    assert output_file.exists()

    with open(output_file, newline="", encoding="utf-8") as file:

        data = list(csv.DictReader(file))

    assert len(data) == 1
    assert data[0]["product_id"] == "P001"


def test_export_to_json(tmp_path, sample_price_record):

    exporter = PriceExporter()

    output_file = tmp_path / "price_report.json"

    exporter.export_to_json(
        [sample_price_record],
        output_file
    )

    assert output_file.exists()

    with open(output_file, encoding="utf-8") as file:

        data = json.load(file)

    assert data[0]["product_id"] == "P001"


def test_export_empty_records(tmp_path):

    exporter = PriceExporter()

    output_file = tmp_path / "empty.csv"

    exporter.export_to_csv([], output_file)

    assert not output_file.exists()


def test_export_all(tmp_path, sample_price_record):

    exporter = PriceExporter()

    csv_file = tmp_path / "report.csv"
    json_file = tmp_path / "report.json"

    exporter.export_to_csv(
        [sample_price_record],
        csv_file
    )

    exporter.export_to_json(
        [sample_price_record],
        json_file
    )

    assert csv_file.exists()
    assert json_file.exists()