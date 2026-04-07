import mysql.connector
from config import DB_CONFIG

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)


def fetch_sales_data(month):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT date, region, revenue, units_sold
    FROM sales
    WHERE DATE_FORMAT(date, '%Y-%m') = %s
    """

    cursor.execute(query, (month,))
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data