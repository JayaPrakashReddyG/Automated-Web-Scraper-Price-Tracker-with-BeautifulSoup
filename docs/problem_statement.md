# Problem Statement

## Project Title
Automated Web Scraper & Price Tracker

## 1. Introduction

Online shopping has become a popular way for customers to purchase products. However, the same product may be available at different prices across different online shopping platforms.

Manually visiting multiple websites to compare product prices is time-consuming and inconvenient. Customers may also miss price drops, discounts, and special offers.

The Automated Web Scraper & Price Tracker is a Python-based application designed to automate the process of collecting product prices from supported websites, comparing prices, maintaining historical price records, and generating reports.

## 2. Problem Description

Customers face several difficulties while comparing online product prices:

- Checking multiple websites manually takes time.
- Product prices frequently change.
- Discounts and offers may not be easy to identify.
- Customers may miss opportunities to purchase products at lower prices.
- Maintaining historical price records manually is difficult.
- Comparing current prices with target prices requires additional effort.

There is a need for an automated solution that collects available product information and presents price comparisons in a convenient format.

## 3. Proposed Solution

The proposed system uses Python, Requests, BeautifulSoup, SQLite, and Streamlit to automate product price tracking.

The application will:

1. Load product information from CSV or JSON files.
2. Visit configured product URLs.
3. Retrieve webpage HTML using HTTP requests.
4. Extract product names and prices using configured HTML selectors.
5. Compare current prices with user-defined target prices.
6. Store product details and price history in SQLite.
7. Identify price drops and target-price achievements.
8. Generate CSV and JSON reports.
9. Display results through an interactive Streamlit dashboard.

## 4. Project Objectives

- Automate product price collection from supported websites.
- Reduce manual price comparison effort.
- Track historical product prices.
- Identify products that reach their target prices.
- Generate downloadable price reports.
- Provide an interactive dashboard for analysis.
- Develop a modular and testable Python application.

## 5. Expected Outcome

The final application should provide:

- Automated product tracking.
- Current and previous price information.
- Target-price comparison.
- Discount calculations when original prices are available.
- Historical price records.
- CSV and JSON exports.
- Dashboard-based visualization.
- Logging and error handling.

## 6. Intended Users

- Online shoppers.
- Price-conscious customers.
- Students learning Python automation.
- Developers interested in web scraping and data analysis.
- Small businesses monitoring publicly available product prices.

## 7. Conclusion

The Automated Web Scraper & Price Tracker aims to simplify online price comparison through automation. It combines web scraping, data processing, database management, reporting, and visualization in a single Python-based project.