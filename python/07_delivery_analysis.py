import pandas as pd
import psycopg2
import matplotlib.pyplot as plt
import os


conn = psycopg2.connect(
    host="localhost",
    database="blinkit_db",     
    user="postgres",
    password="DB PASSWORD",  
    port="5432"
)


query = """
SELECT *
FROM sales_dashboard;
"""

df = pd.read_sql(query, conn)


delivery_summary = (
    df.groupby("delivery_status")
      .agg(
          Total_Orders=("order_id", "count")
      )
)

delivery_summary["Percentage"] = (
    delivery_summary["Total_Orders"]
    / delivery_summary["Total_Orders"].sum()
    * 100
)

print("\n===== DELIVERY ANALYSIS =====\n")
print(delivery_summary)

project_folder = os.path.dirname(os.path.dirname(__file__))
images_folder = os.path.join(project_folder, "images")

os.makedirs(images_folder, exist_ok=True)


plt.figure(figsize=(7,5))

delivery_summary["Total_Orders"].plot(kind="bar")

plt.title("Orders by Delivery Status")
plt.xlabel("Delivery Status")
plt.ylabel("Orders")

plt.tight_layout()

plt.savefig(os.path.join(images_folder,
                         "delivery_bar_chart.png"))

plt.show()



plt.figure(figsize=(6,6))

delivery_summary["Total_Orders"].plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.ylabel("")
plt.title("Delivery Status Distribution")

plt.tight_layout()

plt.savefig(os.path.join(images_folder,
                         "delivery_pie_chart.png"))

plt.show()

conn.close()