# Automated Web Scraper & Price Tracker

A Python-based web scraping and price monitoring application that collects product prices from supported websites, compares them with target prices, stores historical records, and generates reports.

## Project Overview

Online product prices frequently change across shopping websites. Manually checking multiple websites is time-consuming.

This project automates product price collection and comparison using Python web scraping technologies.

Users can maintain product information, track available prices, compare prices against target values, and visualize results through an interactive dashboard.

## Features

- Automated product price scraping.
- CSV and JSON product input.
- HTML parsing using BeautifulSoup.
- Configurable website CSS selectors.
- Current and target price comparison.
- Discount calculation.
- Historical price tracking.
- SQLite database storage.
- Price-drop and target-price alerts.
- CSV and JSON report generation.
- Interactive Streamlit dashboard.
- Plotly visualizations.
- Application logging.
- Pytest-based automated testing.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core development |
| Requests | HTTP requests |
| BeautifulSoup | HTML parsing |
| Pandas | Data processing |
| SQLite | Database |
| Streamlit | Dashboard |
| Plotly | Visualization |
| Pytest | Testing |
| Python-dotenv | Configuration |

## Project Structure

```text
Automated-Web-Scraper-Price-Tracker/
│
├── data/
│   ├── input/
│   ├── output/
│   └── database/
│
├── src/
│   └── price_tracker/
│
├── dashboard/
├── tests/
├── config/
├── scripts/
├── logs/
├── docs/
├── evidence/
│
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
├── pytest.ini
├── main.py
├── README.md
└── LICENSE