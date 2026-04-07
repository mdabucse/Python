import argparse
from db.db import fetch_sales_data
from services.data_service import process_sales_data
from services.chart_service import generate_bar_chart, generate_line_chart
from services.template_service import render_template
from services.pdf_service import generate_pdf
from services.email_service import send_email


def main(month, template_name):
    print("[1/5] Connecting to database... OK")

    data = fetch_sales_data(month)
    print(f"[2/5] Querying {month} sales data... OK ({len(data)} records)")

    processed = process_sales_data(data)

    bar_chart = generate_bar_chart(processed["region_data"])
    line_chart = generate_line_chart(processed["daily_sales"])

    context = {
        **processed,
        "month": month,
        "bar_chart": bar_chart,
        "line_chart": line_chart
    }

    print("[3/5] Rendering template...")
    html = render_template(template_name, context)

    print("[4/5] Generating PDF...")
    pdf_path = generate_pdf(html, f"sales_report_{month}.pdf")

    print("[5/5] Sending email...")
    send_email(
        ["exec-team@company.com"],
        f"{month} Sales Report",
        "Attached is the report",
        pdf_path
    )

    print(f"\nOutput: {pdf_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--month", required=True)
    parser.add_argument("--template", required=True)

    args = parser.parse_args()

    main(args.month, args.template)