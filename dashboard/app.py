
"""
Automated Web Scraper & Price Tracker
Streamlit Dashboard
"""

import json
import sys
from pathlib import Path

import streamlit as st

# --------------------------------------------------
# PROJECT PATH CONFIGURATION
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SRC_PATH = PROJECT_ROOT / "src"

# Add project root and src folder to Python import path
for path in (PROJECT_ROOT, SRC_PATH):
    path_str = str(path)

    if path_str not in sys.path:
        sys.path.insert(0, path_str)


# --------------------------------------------------
# PROJECT IMPORTS
# --------------------------------------------------

from price_tracker.config import (
    PRICE_REPORT_CSV,
    PRICE_REPORT_JSON,
    PRODUCTS_CSV
)

from price_tracker.product_manager import ProductManager
from price_tracker.price_tracker import PriceTracker

from dashboard.components import (
    render_header,
    render_metric_cards,
    render_product_table,
    render_target_alerts,
    render_sidebar
)

from dashboard.charts import (
    render_price_comparison,
    render_discount_chart,
    render_price_history
)


# --------------------------------------------------
# STREAMLIT PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="PriceTracker Pro",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)


# --------------------------------------------------
# LOAD REPORTS
# --------------------------------------------------

def load_reports():

    if PRICE_REPORT_JSON.exists():

        try:
            with open(
                PRICE_REPORT_JSON,
                "r",
                encoding="utf-8"
            ) as file:

                data = json.load(file)

                if isinstance(data, list):
                    return data

                return []

        except (json.JSONDecodeError, OSError) as error:

            st.error(f"Unable to read price report: {error}")

    return []


# --------------------------------------------------
# RUN PRICE TRACKING
# --------------------------------------------------

def run_price_tracking():

    manager = ProductManager()

    try:
        products = manager.load_from_csv(PRODUCTS_CSV)

        if not products:
            st.warning("No products found in input CSV.")
            return

        tracker = PriceTracker()

        try:

            with st.spinner("Scraping product prices..."):

                records = tracker.track_products(products)

            if records:

                from price_tracker.exporter import PriceExporter

                exporter = PriceExporter()

                exporter.export_all(
                    records,
                    csv_path=PRICE_REPORT_CSV,
                    json_path=PRICE_REPORT_JSON
                )

                successful = sum(
                    1 for item in records
                    if item.get("current_price") is not None
                )

                st.success(
                    f"Tracking completed! "
                    f"{successful}/{len(records)} products scraped successfully."
                )

                if successful == 0:
                    st.warning(
                        "No live prices were extracted. "
                        "Check product URLs and website selectors."
                    )

            else:

                st.warning(
                    "No tracking records returned. "
                    "Check your input products and scraper configuration."
                )

        finally:
            tracker.close()

    except Exception as error:

        st.error(f"Price tracking failed: {error}")


# --------------------------------------------------
# DASHBOARD MAIN FUNCTION
# --------------------------------------------------

def main():

    render_header()

    selected_page = render_sidebar()

    st.sidebar.markdown("---")

    if st.sidebar.button(
        "🔄 Run Price Tracker",
        use_container_width=True
    ):

        run_price_tracking()
        st.rerun()

    # Load latest reports
    records = load_reports()

    total = len(records)

    tracked = sum(
        1 for item in records
        if item.get("current_price") is not None
    )

    reached = sum(
        1 for item in records
        if item.get("price_status") == "Target Reached"
    )

    average_discount = (
        sum(
            float(item.get("discount_percentage") or 0)
            for item in records
        ) / total
        if total else 0
    )

    # --------------------------------------------------
    # OVERVIEW PAGE
    # --------------------------------------------------

    if selected_page == "Overview":

        st.title("📊 Dashboard Overview")

        render_metric_cards(
            total,
            tracked,
            reached,
            average_discount
        )

        st.divider()

        render_price_comparison(records)

        render_discount_chart(records)

        render_target_alerts(records)

    # --------------------------------------------------
    # PRODUCTS PAGE
    # --------------------------------------------------

    elif selected_page == "Products":

        st.title("🛍️ Tracked Products")

        render_product_table(records)

    # --------------------------------------------------
    # PRICE COMPARISON PAGE
    # --------------------------------------------------

    elif selected_page == "Price Comparison":

        st.title("📈 Price Comparison")

        render_price_comparison(records)

        render_discount_chart(records)

        render_price_history(records)

    # --------------------------------------------------
    # ALERTS PAGE
    # --------------------------------------------------

    elif selected_page == "Alerts":

        st.title("🔔 Price Alerts")

        render_target_alerts(records)

    # --------------------------------------------------
    # REPORTS PAGE
    # --------------------------------------------------

    elif selected_page == "Reports":

        st.title("📁 Download Reports")

        if PRICE_REPORT_CSV.exists():

            st.download_button(
                label="⬇️ Download CSV Report",
                data=PRICE_REPORT_CSV.read_bytes(),
                file_name="price_report.csv",
                mime="text/csv"
            )

        if PRICE_REPORT_JSON.exists():

            st.download_button(
                label="⬇️ Download JSON Report",
                data=PRICE_REPORT_JSON.read_bytes(),
                file_name="price_report.json",
                mime="application/json"
            )

        if (
            not PRICE_REPORT_CSV.exists()
            and not PRICE_REPORT_JSON.exists()
        ):

            st.info("Reports are not available yet.")

    # --------------------------------------------------
    # SIDEBAR FOOTER
    # --------------------------------------------------

    st.sidebar.markdown("---")

    st.sidebar.caption(
        "Automated Web Scraper & Price Tracker v1.0"
    )


# --------------------------------------------------
# APPLICATION ENTRY POINT
# --------------------------------------------------

if __name__ == "__main__":
    main()
