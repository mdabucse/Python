from collections import defaultdict

def process_sales_data(data):
    total_revenue = 0
    total_units = 0
    region_data = defaultdict(float)
    daily_sales = defaultdict(float)

    for row in data:
        total_revenue += row["revenue"]
        total_units += row["units_sold"]

        region_data[row["region"]] += row["revenue"]
        daily_sales[row["date"]] += row["revenue"]

    avg_order_value = total_revenue / total_units if total_units else 0

    return {
        "total_revenue": total_revenue,
        "total_units": total_units,
        "avg_order_value": avg_order_value,
        "region_data": dict(region_data),
        "daily_sales": dict(daily_sales)
    }