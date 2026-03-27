# Python Web Scraper with Price Tracking

A modular Python-based web scraping system that extracts product data, stores it in MySQL, and tracks price changes over time.

---

## Features

* Scrapes product data using Playwright (handles dynamic websites)
* Extracts structured data (title, price)
* Stores data in MySQL database
* Detects price changes between runs
* Generates formatted price change reports
* Exports results to CSV
* Modular and scalable architecture

---

## Project Structure

```
project/
│
├── main.py              # Entry point (controls full pipeline)
│
├── utils/
│   ├── scrapy.py        # Handles scraping logic (pagination, navigation)
│   ├── parser.py        # Extracts data from HTML elements
│   ├── database.py      # Database operations (insert, fetch)
│   ├── storage.py       # Saves data to CSV
│   ├── report.py        # Price comparison and report generation
│   ├── logger.py        # Logging utility
│   ├── config.py        # Configuration (URLs, settings)
│   └── utils.py         # Helper functions (data cleaning)
│
├── products.csv         # Output CSV (optional)
├── .gitignore
└── README.md
```

---

## How It Works

```
1. Fetch previous prices from database
2. Scrape new product data
3. Compare old and new prices
4. Store updated data in database
5. Generate report
6. Save report to CSV
```

---

## File Responsibilities

### main.py

* Controls the full workflow
* Orchestrates all modules

---

### utils/scrapy.py

* Navigates pages using Playwright
* Handles pagination
* Collects product elements

---

### utils/parser.py

* Extracts product title and price
* Converts raw HTML into structured data

---

### utils/database.py

* Connects to MySQL
* Inserts product data
* Fetches latest previous prices

---

### utils/report.py

* Compares old and new prices
* Calculates percentage change
* Formats and prints report

---

### utils/storage.py

* Saves report data into CSV format

---

### utils/logger.py

* Provides timestamp-based logging

---

### utils/config.py

* Stores configuration such as base URL and page count

---

### utils/utils.py

* Contains helper functions
* Example: cleaning and converting price values

---

## Database Schema (MySQL)

```sql
CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) UNIQUE,
    price FLOAT,
    scraped_at DATETIME
);
```

---

## Sample Output

```
[2026-03-27 22:51:58] Page 3/3 — 20 products extracted
Inserted/Updated 60 records into MySQL

=== Price Change Report ===
+-------------------------------+-----------+-----------+--------+
| Product                       | Old Price | New Price | Change |
+-------------------------------+-----------+-----------+--------+
| HP Laptop                    | 52990     | 49990     |  -5.6% |
| Dell Inspiron                | 61499     | 63499     |  +3.2% |
+-------------------------------+-----------+-----------+--------+
```

---

## Installation

```
pip install playwright mysql-connector-python
playwright install
```

---

## Running the Project

```
python main.py
```

---

## Notes

* Ensure MySQL server is running
* Update database credentials in `utils/database.py`
* Add delays if required to avoid blocking during scraping

