-- =========================================================
-- Blinkit End-to-End Data Analytics Project
-- File: 03_import_data.sql
-- Description: Data Import Process
-- =========================================================


/*
Data Loading Process:

The cleaned CSV files were imported into PostgreSQL
using Python Pandas and SQLAlchemy.

Workflow:

CSV Files
    |
    ↓
Pandas DataFrame (read_csv)
    |
    ↓
SQLAlchemy Engine Connection
    |
    ↓
PostgreSQL Database (blinkit_db)


Python Import Example:

orders_full.to_sql(
    "orders_full",
    engine,
    if_exists="replace",
    index=False
)


Imported Tables:

1. orders_full
2. sales_dashboard
3. product_dashboard
4. inventory_cleaned
5. delivery_cleaned
6. marketing_cleaned
7. customer_feedback_cleaned

*/