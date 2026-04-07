# PDF Report Generator

A Python-based system that generates automated monthly sales reports with charts, templates, and PDF export.

---

## Features

* MySQL data integration
* Jinja2 HTML templating
* Chart generation (Matplotlib)
* PDF export (WeasyPrint)
* Optional email delivery

---

## Project Structure

```
pdf-report-generator/
├── generate_report.py
├── config.py
├── db/
├── services/
├── templates/
├── charts/
├── reports/
```

---

## Setup

### 1. Install dependencies

```bash
pip install mysql-connector-python jinja2 matplotlib weasyprint
```

### 2. Configure database

Update `config.py`:

```
host = localhost
user = root
password = root
database = report
```

### 3. Run the project

```bash
python generate_report.py --month 2026-01 --template sales_monthly
```

---

## Output

* Generates PDF report in `reports/`
* Includes:

  * Summary metrics
  * Charts (region + daily sales)
  * Conditional alerts

---

## Notes

* Use absolute paths for charts (`.resolve().as_uri()`)
* SMTP may be blocked on some networks

---
