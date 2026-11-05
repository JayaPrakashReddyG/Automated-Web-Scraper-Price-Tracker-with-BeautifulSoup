import streamlit as st


def render_header():
    st.markdown(
        """
        <div style="
            background: linear-gradient(120deg, #101827, #1d4ed8);
            padding: 30px;
            border-radius: 15px;
            margin-bottom: 25px;
        ">
            <h1 style="color:white;margin:0;">
                PriceTracker Pro
            </h1>
            <p style="color:#dbeafe;margin-top:8px;">
                Smart Product Price Monitoring Dashboard
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


def render_metric_cards(total, tracked, reached, average_discount):

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Products", total)
    col2.metric("Successfully Tracked", tracked)
    col3.metric("Target Reached", reached)
    col4.metric("Average Discount", f"{average_discount:.2f}%")


def render_product_table(records):

    if not records:
        st.info("No product records available.")
        return

    st.subheader("Product Price Details")

    st.dataframe(
        records,
        use_container_width=True,
        hide_index=True
    )


def render_target_alerts(records):

    st.subheader("Price Target Alerts")

    alerts = [
        record for record in records
        if record.get("price_status") == "Target Reached"
    ]

    if alerts:
        for product in alerts:
            st.success(
                f"🎉 {product['product_name']} "
                f"reached target price: "
                f"₹{product['current_price']}"
            )
    else:
        st.info("No products have reached their target prices yet.")


def render_sidebar():

    st.sidebar.title("⚙️ Navigation")

    return st.sidebar.radio(
        "Choose Section",
        [
            "Overview",
            "Products",
            "Price Comparison",
            "Alerts",
            "Reports"
        ]
    )