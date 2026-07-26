import pandas as pd
import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()

conn = psycopg2.connect(
    host="localhost",
    database="blinkit_db",
    user="postgres",
    password=os.getenv("DB_PASSWORD"),
    port="5432"
)


query = """
SELECT *
FROM sales_dashboard;
"""


df = pd.read_sql(query, conn)




total_orders = df['order_id'].nunique()

print("Total Orders:", total_orders)




total_revenue = df['total_sales'].sum()

print("Total Revenue:", total_revenue)




total_quantity = df['quantity'].sum()

print("Total Quantity Sold:", total_quantity)



avg_order_value = df.groupby('order_id')['total_sales'].sum().mean()

print("Average Order Value:", avg_order_value)



category_sales = (
    df.groupby('category')['total_sales']
    .sum()
    .sort_values(ascending=False)
)

print("\nCategory Wise Sales:")
print(category_sales)


conn.close()


