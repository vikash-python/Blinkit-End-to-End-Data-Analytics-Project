import pandas as pd
import psycopg2
import matplotlib.pyplot as plt
import os

# -------------------------
# Database Connection
# -------------------------
conn = psycopg2.connect(
    host="localhost",
    database="blinkit_db",
    user="postgres",
    password="NewPassword123",
    port="5432"
)

# -------------------------
# Load Data
# -------------------------
query = """
SELECT *
FROM product_dashboard;
"""

df = pd.read_sql(query, conn)

print("\n===== PRODUCT DATA =====\n")
print(df.head())

# -------------------------
# Top 10 Products by Sales
# -------------------------
top_products = (
    df.sort_values(
        by="total_sales",
        ascending=False
    )
    .head(10)
)

print("\n===== TOP 10 PRODUCTS =====\n")
print(top_products[["product_name","total_sales"]])

# -------------------------
# Lowest 10 Products
# -------------------------
lowest_products = (
    df.sort_values(
        by="total_sales"
    )
    .head(10)
)

print("\n===== LOWEST 10 PRODUCTS =====\n")
print(lowest_products[["product_name","total_sales"]])

top_orders = (
    df.sort_values(
        by="total_orders",
        ascending=False
    )
    .head(10)
)

print("\n===== TOP PRODUCTS BY ORDERS =====\n")
print(top_orders[["product_name","total_orders"]])


# -------------------------
# Images Folder
# -------------------------
project_folder = os.path.dirname(os.path.dirname(__file__))
images_folder = os.path.join(project_folder, "images")

os.makedirs(images_folder, exist_ok=True)

# -------------------------
# Bar Chart
# -------------------------
plt.figure(figsize=(10,6))

plt.bar(
    top_products["product_name"],
    top_products["total_sales"]
)

plt.xticks(rotation=45)

plt.title("Top 10 Products by Sales")
plt.xlabel("Product")
plt.ylabel("Sales")

plt.tight_layout()

plt.savefig(
    os.path.join(
        images_folder,
        "top_products.png"
    )
)

plt.show()

conn.close()