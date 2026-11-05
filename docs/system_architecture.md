# System Architecture

## 1. Introduction

The Automated Web Scraper & Price Tracker follows a modular architecture. Each component performs a specific responsibility, making the application easier to develop, test, maintain, and extend.

## 2. Architecture Overview

The system consists of the following major layers:

1. Input Layer
2. Product Management Layer
3. Web Scraping Layer
4. Data Parsing Layer
5. Price Processing Layer
6. Database Layer
7. Alert Management Layer
8. Reporting Layer
9. Presentation Layer

## 3. Architecture Diagram

```mermaid
flowchart TD
    A[CSV / JSON Product Input] --> B[Product Manager]
    B --> C[Price Tracker]
    C --> D[Web Scraper]
    D --> E[Online Product Webpage]
    E --> F[HTML Response]
    F --> G[HTML Parser]
    G --> H[Price Comparator]
    H --> I[Alert Manager]
    H --> J[Database]
    J --> K[Price History]
    H --> L[Report Exporter]
    L --> M[CSV / JSON Reports]
    J --> N[Streamlit Dashboard]
    M --> N