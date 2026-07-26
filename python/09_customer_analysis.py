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
FROM orders_full;
"""

df = pd.read_sql(query, conn)

print("\n========== CUSTOMER ANALYSIS ==========\n")

# -------------------------
# Total Customers
# -------------------------
print("Total Customers :", df["customer_id"].nunique())

# -------------------------
# Top Customers by Sales
# -------------------------
top_sales = (
    df.groupby("customer_name")
      .agg(
          Total_Sales=("total_sales","sum")
      )
      .sort_values(
          by="Total_Sales",
          ascending=False
      )
      .head(10)
)

print("\n===== TOP 10 CUSTOMERS BY SALES =====\n")
print(top_sales)

# -------------------------
# Top Customers by Orders
# -------------------------
top_orders = (
    df.groupby("customer_name")
      .agg(
          Orders=("order_id","count")
      )
      .sort_values(
          by="Orders",
          ascending=False
      )
      .head(10)
)

print("\n===== TOP 10 CUSTOMERS BY ORDERS =====\n")
print(top_orders)

# -------------------------
# Customer Segment
# -------------------------
segment = (
    df.groupby("customer_segment")
      .agg(
          Customers=("customer_id","nunique")
      )
)

print("\n===== CUSTOMER SEGMENT =====\n")
print(segment)

# -------------------------
# Images Folder
# -------------------------
project_folder = os.path.dirname(os.path.dirname(__file__))
images_folder = os.path.join(project_folder,"images")

os.makedirs(images_folder,exist_ok=True)

# -------------------------
# Sales Chart
# -------------------------
plt.figure(figsize=(10,6))

top_sales["Total_Sales"].plot(kind="bar")

plt.title("Top 10 Customers by Sales")

plt.xlabel("Customer")

plt.ylabel("Sales")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    os.path.join(
        images_folder,
        "top_customer_sales.png"
    )
)

plt.show()

# -------------------------
# Orders Chart
# -------------------------
plt.figure(figsize=(10,6))

top_orders["Orders"].plot(kind="bar")

plt.title("Top 10 Customers by Orders")

plt.xlabel("Customer")

plt.ylabel("Orders")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    os.path.join(
        images_folder,
        "top_customer_orders.png"
    )
)

plt.show()

conn.close()