"""Day 8: safe, local SQLite parameterized-query demonstration."""

import sqlite3


PRODUCTS = [
    ("Gift Card", "Gifts", 1),
    ("Prototype Gift", "Gifts", 0),
    ("T-Shirt", "Clothing", 1),
]


def main() -> None:
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()
    cursor.execute(
        "CREATE TABLE products (name TEXT, category TEXT, released INTEGER)"
    )
    cursor.executemany("INSERT INTO products VALUES (?, ?, ?)", PRODUCTS)

    category = input("Category (Gifts/Clothing/Unknown): ").strip()
    query = "SELECT name FROM products WHERE category = ? AND released = ?"
    parameters = (category, 1)

    print(f"SQL template: {query}")
    print(f"Parameters: {parameters}")
    cursor.execute(query, parameters)

    rows = cursor.fetchall()
    print("Results:")
    if not rows:
        print("(no rows)")
    for (name,) in rows:
        print(f"- {name}")

    connection.close()


if __name__ == "__main__":
    main()

