import pandas as pd
import plotly.express as px
import streamlit as st


def render_price_comparison(records):

    if not records:
        st.info("No price data available.")
        return

    df = pd.DataFrame(records)

    required = ["product_name", "current_price", "target_price"]

    if not all(column in df.columns for column in required):
        st.warning("Required price columns are missing.")
        return

    st.subheader("Current Price vs Target Price")

    chart_data = df[
        ["product_name", "current_price", "target_price"]
    ].melt(
        id_vars="product_name",
        var_name="Price Type",
        value_name="Price"
    )

    fig = px.bar(
        chart_data,
        x="product_name",
        y="Price",
        color="Price Type",
        barmode="group",
        title="Product Price Comparison",
        template="plotly_dark"
    )

    fig.update_layout(
        xaxis_title="Products",
        yaxis_title="Price (INR)",
        xaxis_tickangle=-35
    )

    st.plotly_chart(fig, use_container_width=True)


def render_discount_chart(records):

    if not records:
        return

    df = pd.DataFrame(records)

    if "discount_percentage" not in df.columns:
        return

    st.subheader("Product Discount Analysis")

    fig = px.pie(
        df,
        names="product_name",
        values="discount_percentage",
        title="Discount Distribution",
        hole=0.45,
        template="plotly_dark"
    )

    st.plotly_chart(fig, use_container_width=True)


def render_price_history(history):

    if not history:
        st.info("No price history available.")
        return

    df = pd.DataFrame(history)

    required = ["last_checked", "current_price"]

    if not all(column in df.columns for column in required):
        return

    df["last_checked"] = pd.to_datetime(df["last_checked"])

    df = df.sort_values("last_checked")

    st.subheader("Price History Trend")

    fig = px.line(
        df,
        x="last_checked",
        y="current_price",
        markers=True,
        title="Product Price History",
        template="plotly_dark"
    )

    st.plotly_chart(fig, use_container_width=True)