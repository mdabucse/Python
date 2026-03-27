def calculate_change(old_price, new_price):
    if old_price == 0:
        return 0.0
    return round(((new_price - old_price) / old_price) * 100, 1)

def compare_prices(old_data, new_data):
    changes = []

    for item in new_data:
        title = item["title"]
        new_price = item["price"]

        old_price = old_data.get(title)

        # skip if no previous data
        if old_price is None:
            continue

        if old_price != new_price:
            change = calculate_change(old_price, new_price)

            changes.append({
                "title": title,
                "old_price": old_price,
                "new_price": new_price,
                "change": change
            })

    return changes

def print_report(changes):
    print("\n=== Price Change Report ===")
    print("+-------------------------------+-----------+-----------+--------+")
    print("| Product                       | Old Price | New Price | Change |")
    print("+-------------------------------+-----------+-----------+--------+")

    for item in changes:
        print(f"| {item['title'][:29]:<29} | "
              f"{item['old_price']:<9} | "
              f"{item['new_price']:<9} | "
              f"{item['change']:+6}% |")

    print("+-------------------------------+-----------+-----------+--------+")
    print(f"{len(changes)} price changes detected.")