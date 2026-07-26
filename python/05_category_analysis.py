import pandas as pd
import psycopg2
import matplotlib.pyplot as plt

# Database Connection
conn = psycopg2.connect(
    host="localhost",
    database="blinkit_db",
    user="postgres",
    password="DB PASSWORD",
    port="5432"
)

# Load Data
query = """
SELECT *
FROM sales_dashboard;
"""

df = pd.read_sql(query, conn)

# -----------------------------
# Category Wise Sales
# -----------------------------
category_sales = (
    df.groupby("category")["total_sales"]
      .sum()
      .sort_values(ascending=False)
)

print("\n===== CATEGORY WISE SALES =====")
print(category_sales)

# -----------------------------
# Category Wise Quantity
# -----------------------------
category_quantity = (
    df.groupby("category")["quantity"]
      .sum()
      .sort_values(ascending=False)
)

print("\n===== CATEGORY WISE QUANTITY =====")
print(category_quantity)

# -----------------------------
# Highest & Lowest Category
# -----------------------------
print("\nHighest Selling Category:")
print(category_sales.idxmax(), "=", round(category_sales.max(), 2))

print("\nLowest Selling Category:")
print(category_sales.idxmin(), "=", round(category_sales.min(), 2))

# -----------------------------
# BAR CHART
# -----------------------------
plt.figure(figsize=(10,6))

category_sales.plot(kind="bar")

plt.title("Category Wise Sales")
plt.xlabel("Category")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)

plt.tight_layout()

import os

project_folder = os.path.dirname(os.path.dirname(__file__))
image_path = os.path.join(project_folder, "images", "category_sales.png")

plt.savefig(image_path)
plt.show()

conn.close()