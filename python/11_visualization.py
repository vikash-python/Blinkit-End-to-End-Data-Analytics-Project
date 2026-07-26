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
    password="DB PASSWORD",
    port="5432"
)

project_folder = os.path.dirname(os.path.dirname(__file__))
images_folder = os.path.join(project_folder, "images")
os.makedirs(images_folder, exist_ok=True)

# =====================================
# 1 Monthly Sales Trend
# =====================================

sales = pd.read_sql("""
SELECT month,
SUM(total_sales) AS sales
FROM orders_full
GROUP BY month
ORDER BY month;
""", conn)

plt.figure(figsize=(8,5))
plt.plot(sales["month"], sales["sales"], marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig(os.path.join(images_folder, "dashboard_monthly_sales.png"))
plt.close()

# =====================================
# 2 Category Sales
# =====================================

category = pd.read_sql("""
SELECT category,
SUM(total_sales) AS sales
FROM product_dashboard
GROUP BY category
ORDER BY sales DESC;
""", conn)

plt.figure(figsize=(10,5))
plt.bar(category["category"], category["sales"])
plt.xticks(rotation=45)
plt.title("Category Wise Sales")
plt.tight_layout()
plt.savefig(os.path.join(images_folder, "dashboard_category_sales.png"))
plt.close()

# =====================================
# 3 Payment Method
# =====================================

payment = pd.read_sql("""
SELECT payment_method,
SUM(total_sales) AS sales
FROM sales_dashboard
GROUP BY payment_method;
""", conn)

plt.figure(figsize=(6,6))
plt.pie(
    payment["sales"],
    labels=payment["payment_method"],
    autopct="%1.1f%%"
)
plt.title("Payment Method Distribution")
plt.tight_layout()
plt.savefig(os.path.join(images_folder, "dashboard_payment.png"))
plt.close()

# =====================================
# 4 Delivery Status
# =====================================

delivery = pd.read_sql("""
SELECT delivery_status,
COUNT(*) AS orders
FROM sales_dashboard
GROUP BY delivery_status;
""", conn)

plt.figure(figsize=(7,5))
plt.bar(
    delivery["delivery_status"],
    delivery["orders"]
)
plt.title("Delivery Status")
plt.tight_layout()
plt.savefig(os.path.join(images_folder, "dashboard_delivery.png"))
plt.close()

# =====================================
# 5 Sentiment
# =====================================

feedback = pd.read_sql("""
SELECT sentiment,
COUNT(*) AS total
FROM customer_feedback_cleaned
GROUP BY sentiment;
""", conn)

plt.figure(figsize=(6,6))
plt.pie(
    feedback["total"],
    labels=feedback["sentiment"],
    autopct="%1.1f%%"
)
plt.title("Customer Sentiment")
plt.tight_layout()
plt.savefig(os.path.join(images_folder, "dashboard_sentiment.png"))
plt.close()

conn.close()

print("\nAll Dashboard Charts Created Successfully!")