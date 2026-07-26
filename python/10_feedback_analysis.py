import pandas as pd
import psycopg2
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv
load_dotenv()

# -------------------------
# Database Connection
# -------------------------

conn = psycopg2.connect(
    host="localhost",
    database="blinkit_db",
    user="postgres",
    password=os.getenv("DB_PASSWORD"),
    port="5432"
)
# -------------------------
# Load Data
# -------------------------

query = """
SELECT *
FROM customer_feedback_cleaned;
"""

df = pd.read_sql(query, conn)

print("\n========== FEEDBACK ANALYSIS ==========\n")

# -------------------------
# Average Rating
# -------------------------

print("Average Rating :")

print(df["rating"].mean())

# -------------------------
# Rating Count
# -------------------------

rating_count = df["rating"].value_counts().sort_index()

print("\n===== RATING DISTRIBUTION =====\n")

print(rating_count)

# -------------------------
# Sentiment Count
# -------------------------

sentiment_count = df["sentiment"].value_counts()

print("\n===== SENTIMENT DISTRIBUTION =====\n")

print(sentiment_count)

# -------------------------
# Images Folder
# -------------------------

project_folder = os.path.dirname(os.path.dirname(__file__))

images_folder = os.path.join(project_folder,"images")

os.makedirs(images_folder,exist_ok=True)

# -------------------------
# Rating Chart
# -------------------------

plt.figure(figsize=(8,5))

rating_count.plot(kind="bar")

plt.title("Customer Rating Distribution")

plt.xlabel("Rating")

plt.ylabel("Count")

plt.tight_layout()

plt.savefig(
    os.path.join(
        images_folder,
        "rating_distribution.png"
    )
)

plt.show()

# -------------------------
# Sentiment Pie Chart
# -------------------------

plt.figure(figsize=(6,6))

sentiment_count.plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.ylabel("")

plt.title("Customer Sentiment")

plt.tight_layout()

plt.savefig(
    os.path.join(
        images_folder,
        "sentiment_distribution.png"
    )
)

plt.show()

conn.close()