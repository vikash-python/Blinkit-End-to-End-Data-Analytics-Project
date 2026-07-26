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
FROM orders_full;
"""

df = pd.read_sql(query, conn)

print(df.head())

conn.close()