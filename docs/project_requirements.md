# Project Requirements

## 1. Project Overview

The Automated Web Scraper & Price Tracker is a Python application that collects product prices from supported websites, compares them with target prices, stores price history, and generates reports.

## 2. Functional Requirements

### FR-01: Product Management
- Load products from CSV files.
- Load products from JSON files.
- Store product ID, name, URL, and target price.
- Retrieve products using their IDs.
- Add and remove products.

### FR-02: Web Scraping
- Send HTTP requests to configured product URLs.
- Retrieve webpage HTML.
- Parse HTML using BeautifulSoup.
- Support configurable CSS selectors.
- Handle request failures and timeouts.
- Retry failed requests where appropriate.

### FR-03: Price Extraction
- Extract product names.
- Extract current prices.
- Extract original prices when available.
- Extract discount information when available.
- Convert extracted price values into numeric values.

### FR-04: Price Comparison
- Compare current prices with target prices.
- Calculate discounts.
- Identify price drops.
- Find the lowest recorded price.
- Sort products by price.

### FR-05: Price Alerts
- Identify products that reach their target prices.
- Identify products with price reductions.
- Display alert information in the dashboard.
- Support optional notification integrations in future versions.

### FR-06: Database Management
- Store product information.
- Store historical price records.
- Retrieve price history.
- Maintain records using SQLite.

### FR-07: Report Generation
- Export price reports to CSV.
- Export price reports to JSON.
- Include product name, current price, target price, discount, and tracking status.
- Save generated reports in the output directory.

### FR-08: Dashboard
- Display total tracked products.
- Display products reaching target prices.
- Display price comparison charts.
- Display discount information.
- Display historical price trends.
- Provide an option to run price tracking.

## 3. Non-Functional Requirements

### Performance
- Avoid unnecessary HTTP requests.
- Use configurable request timeouts.
- Introduce delays between requests.
- Handle multiple products efficiently.

### Reliability
- Handle network failures.
- Handle missing HTML elements.
- Handle invalid price values.
- Record errors in log files.

### Maintainability
- Use a modular project structure.
- Separate scraping, parsing, database, and reporting logic.
- Maintain reusable functions and classes.

### Usability
- Provide CSV and JSON input support.
- Provide an interactive dashboard.
- Generate readable reports.
- Display meaningful error messages.

### Security
- Store sensitive configuration in environment variables.
- Never commit API keys or credentials.
- Validate input data.
- Avoid executing untrusted webpage content.

## 4. Software Requirements

| Software | Purpose |
|---|---|
| Python 3.10+ | Main programming language |
| VS Code | Development environment |
| Requests | HTTP requests |
| BeautifulSoup4 | HTML parsing |
| Pandas | Data processing |
| SQLite | Database |
| Streamlit | Dashboard |
| Plotly | Interactive charts |
| Pytest | Unit and integration testing |
| Python-dotenv | Environment configuration |

## 5. Hardware Requirements

Minimum recommended configuration:

- Processor: Dual-core processor.
- RAM: 4 GB or higher.
- Storage: 500 MB free space.
- Operating System: Windows, Linux, or macOS.
- Internet connection for live website scraping.

## 6. Input Requirements

Each product should contain:

| Field | Description |
|---|---|
| product_id | Unique product identifier |
| product_name | Product name |
| product_url | Product webpage URL |
| target_price | Desired purchase price |
| website | Website name (optional) |

## 7. Output Requirements

The application should generate:

- price_report.csv
- price_report.json
- SQLite database records
- Application logs
- Dashboard visualizations
- Test execution reports

## 8. Constraints

- Product webpages must be publicly accessible.
- Website HTML structures may change.
- CSS selectors must match the supported website.
- Some websites may block automated requests.
- Live scraping depends on network availability.
- Website terms and applicable scraping policies must be respected.

## 9. Acceptance Criteria

The project is considered functional when:

1. Products can be loaded from CSV or JSON.
2. The scraper can retrieve accessible webpages.
3. Prices can be extracted using valid selectors.
4. Prices can be compared against target prices.
5. Product and price-history records can be stored.
6. CSV and JSON reports can be generated.
7. The dashboard can display available tracking data.
8. Automated tests can execute successfully.