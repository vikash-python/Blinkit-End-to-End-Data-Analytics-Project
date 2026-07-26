import pandas as pd
import psycopg2
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

# -------------------------
# Reports Folder
# -------------------------

project_folder = os.path.dirname(os.path.dirname(__file__))
reports_folder = os.path.join(project_folder, "reports")

os.makedirs(reports_folder, exist_ok=True)

report_path = os.path.join(reports_folder, "final_report.xlsx")

# -------------------------
# Sales Summary
# -------------------------

sales = pd.read_sql("""
SELECT
COUNT(order_id) AS total_orders,
SUM(total_sales) AS total_revenue,
AVG(total_sales) AS average_order_value
FROM sales_dashboard;
""", conn)

# -------------------------
# Category Summary
# -------------------------

category = pd.read_sql("""
SELECT
category,
SUM(total_sales) AS total_sales
FROM product_dashboard
GROUP BY category
ORDER BY total_sales DESC;
""", conn)

# -------------------------
# Payment Summary
# -------------------------

payment = pd.read_sql("""
SELECT
payment_method,
SUM(total_sales) AS total_sales
FROM sales_dashboard
GROUP BY payment_method;
""", conn)

# -------------------------
# Delivery Summary
# -------------------------

delivery = pd.read_sql("""
SELECT
delivery_status,
COUNT(*) AS total_orders
FROM sales_dashboard
GROUP BY delivery_status;
""", conn)

# -------------------------
# Customer Summary
# -------------------------

customer = pd.read_sql("""
SELECT
customer_segment,
COUNT(customer_id) AS total_customers
FROM orders_full
GROUP BY customer_segment;
""", conn)

# -------------------------
# Feedback Summary
# -------------------------

feedback = pd.read_sql("""
SELECT
sentiment,
COUNT(*) AS total_feedback
FROM customer_feedback_cleaned
GROUP BY sentiment;
""", conn)

# -------------------------
# Export Excel
# -------------------------

with pd.ExcelWriter(report_path) as writer:

    sales.to_excel(writer,
                   sheet_name="Sales Summary",
                   index=False)

    category.to_excel(writer,
                      sheet_name="Category Summary",
                      index=False)

    payment.to_excel(writer,
                     sheet_name="Payment Summary",
                     index=False)

    delivery.to_excel(writer,
                      sheet_name="Delivery Summary",
                      index=False)

    customer.to_excel(writer,
                      sheet_name="Customer Summary",
                      index=False)

    feedback.to_excel(writer,
                      sheet_name="Feedback Summary",
                      index=False)

conn.close()

print("\nFinal Excel Report Created Successfully!")
print(report_path)