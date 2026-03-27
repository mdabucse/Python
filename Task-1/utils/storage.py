import csv

def save_to_csv(data, filename=r"Task-1\utils\products.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["title", "price","new_price","change","old_price"])
        writer.writeheader()
        writer.writerows(data)

    print(f"Data saved to {filename}")

