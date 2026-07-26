import pandas as pd
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="blinkit_db",
    user="postgres",
    password = ("NayaStrongPassword456"),
    port="5432"
)

query = """
SELECT *
FROM orders_full;
"""

df = pd.read_sql(query, conn)

print(df.head())

conn.close()