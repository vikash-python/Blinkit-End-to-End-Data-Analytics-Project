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
FROM sales_dashboard;
"""

df = pd.read_sql(query, conn)

# -------------------------
# Payment Summary
# -------------------------
payment_summary = df.groupby("payment_method").agg(
    Total_Orders=("order_id", "count"),
    Total_Revenue=("total_sales", "sum")
)

payment_summary = payment_summary.sort_values(
    by="Total_Revenue",
    ascending=False
)

print("\n===== PAYMENT METHOD ANALYSIS =====\n")
print(payment_summary)

# -------------------------
# Revenue Percentage
# -------------------------
payment_summary["Revenue %"] = (
    payment_summary["Total_Revenue"]
    / payment_summary["Total_Revenue"].sum()
    * 100
)

print("\n===== PAYMENT PERCENTAGE =====\n")
print(payment_summary)

# -------------------------
# Image Folder
# -------------------------
project_folder = os.path.dirname(os.path.dirname(__file__))
images_folder = os.path.join(project_folder, "images")

os.makedirs(images_folder, exist_ok=True)

# -------------------------
# Bar Chart
# -------------------------
plt.figure(figsize=(8,5))

payment_summary["Total_Revenue"].plot(kind="bar")

plt.title("Revenue by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Revenue")

plt.tight_layout()

plt.savefig(os.path.join(images_folder,
                         "payment_bar_chart.png"))

plt.show()

# -------------------------
# Pie Chart
# -------------------------
plt.figure(figsize=(6,6))

payment_summary["Total_Revenue"].plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.ylabel("")
plt.title("Revenue Share by Payment Method")

plt.tight_layout()

plt.savefig(os.path.join(images_folder,
                         "payment_pie_chart.png"))

plt.show()

conn.close()