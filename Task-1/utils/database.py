import mysql.connector
from datetime import datetime

def insert_products(data):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="presidio"
    )

    cursor = conn.cursor()

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    values = [
        (item["title"], item["price"], now)
        for item in data
    ]

    cursor.executemany("""
        INSERT INTO products (title, price, scraped_at)
        VALUES (%s, %s, %s)
        ON DUPLICATE KEY UPDATE
            price = VALUES(price),
            scraped_at = VALUES(scraped_at)
    """, values)

    conn.commit()
    cursor.close()
    conn.close()

    print(f"✅ Inserted/Updated {len(data)} records into MySQL")

import mysql.connector

def get_previous_prices():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="presidio"
    )

    cursor = conn.cursor()

    # Get latest record BEFORE current run
    cursor.execute("""
        SELECT p1.title, p1.price
        FROM products p1
        INNER JOIN (
            SELECT title, MAX(scraped_at) AS max_date
            FROM products
            GROUP BY title
        ) p2
        ON p1.title = p2.title AND p1.scraped_at = p2.max_date
    """)

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    # Convert to dict → easy lookup
    return {row["title"]: row["price"] for row in rows}