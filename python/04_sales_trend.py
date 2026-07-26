import pandas as pd
import psycopg2


conn = psycopg2.connect(
    host="localhost",
    database="blinkit_db",
    user="postgres",
    password="NewPassword123",
    port="5432"
)


query = """
SELECT *
FROM sales_dashboard;
"""


df = pd.read_sql(query, conn)


monthly_sales = (
    df.groupby(['Year','Month'])['total_sales']
    .sum()
    .reset_index()
)


print(monthly_sales)


conn.close()



month_order = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

monthly_sales["Month"] = pd.Categorical(
    monthly_sales["Month"],
    categories=month_order,
    ordered=True
)

monthly_sales = monthly_sales.sort_values("Month")

import matplotlib.pyplot as plt
plt.figure(figsize=(10,5))
plt.plot(monthly_sales["Month"], monthly_sales["total_sales"], marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
