from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# Database config
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "report"
}

# Paths
TEMPLATE_DIR = BASE_DIR / "templates"
REPORT_DIR = BASE_DIR / "reports"
CHART_DIR = BASE_DIR / "charts"

# Email config
EMAIL_CONFIG = {
    "sender": "mdabucse@gmail.com",
    "password": "pkxujlbdghyedfgj",
    "smtp_server": "smtp.gmail.com",
    "port": 587
}