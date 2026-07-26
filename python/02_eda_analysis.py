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




print("First 5 Rows:")
print(df.head())


print("\nDataset Shape:")
print(df.shape)


print("\nColumn Names:")
print(df.columns)


print("\nData Types:")
print(df.dtypes)


print("\nMissing Values:")
print(df.isnull().sum())


print("\nDuplicate Rows:")
print(df.duplicated().sum())


conn.close()