import matplotlib.pyplot as plt
from config import CHART_DIR

def generate_bar_chart(region_data):
    path = CHART_DIR / "region_chart.png"

    plt.figure()
    plt.bar(region_data.keys(), region_data.values())
    plt.title("Revenue by Region")

    plt.savefig(path)
    plt.close()

    return path.resolve().as_uri()


def generate_line_chart(daily_sales):
    path = CHART_DIR / "daily_chart.png"

    plt.figure()
    plt.plot(list(daily_sales.keys()), list(daily_sales.values()))
    plt.xticks(rotation=45)
    plt.title("Daily Sales Trend")

    plt.savefig(path)
    plt.close()

    return path.resolve().as_uri()