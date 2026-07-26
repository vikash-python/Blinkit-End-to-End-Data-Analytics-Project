-- =========================================================
-- Blinkit End-to-End Data Analytics Project
-- File: 06_window_functions.sql
-- Description: Advanced SQL Window Functions
-- =========================================================



-- Product Sales Ranking

SELECT
    product_name,
    category,
    total_sales,
    RANK() OVER(
        ORDER BY total_sales DESC
    ) AS sales_rank
FROM product_dashboard;


-- Top Products by Category

SELECT
    product_name,
    category,
    total_sales,

    RANK() OVER(
        PARTITION BY category
        ORDER BY total_sales DESC
    ) AS category_rank

FROM product_dashboard;



-- Running Revenue

SELECT
    order_date,
    total_sales,

    SUM(total_sales) OVER(
        ORDER BY order_date
    ) AS running_revenue

FROM sales_dashboard;



-- Customer Spending Rank

SELECT
    customer_id,
    customer_name,
    SUM(order_total) AS total_spent,

    RANK() OVER(
        ORDER BY SUM(order_total) DESC
    ) AS customer_rank

FROM orders_full

GROUP BY
    customer_id,
    customer_name;



-- Previous Order Value

SELECT
    customer_id,
    order_date,
    order_total,

    LAG(order_total) OVER(
        PARTITION BY customer_id
        ORDER BY order_date
    ) AS previous_order_value

FROM orders_full;


-- Product Numbering by Category

SELECT
    product_name,
    category,
    total_sales,

    ROW_NUMBER() OVER(
        PARTITION BY category
        ORDER BY total_sales DESC
    ) AS product_number

FROM product_dashboard;


-- Dense Rank Product Analysis

SELECT
    product_name,
    category,
    total_sales,

    DENSE_RANK() OVER(
        PARTITION BY category
        ORDER BY total_sales DESC
    ) AS dense_rank

FROM product_dashboard;



-- Next Order Analysis

SELECT
    customer_id,
    order_date,
    order_total,

    LEAD(order_total) OVER(
        PARTITION BY customer_id
        ORDER BY order_date
    ) AS next_order_value

FROM orders_full;



-- Monthly Revenue Growth Percentage

WITH monthly_sales AS
(
    SELECT
        "Year",
        "Month",
        SUM(total_sales) AS revenue

    FROM sales_dashboard

    GROUP BY "Year", "Month"
)

SELECT
    "Year",
    "Month",
    revenue,

    LAG(revenue) OVER(
        ORDER BY "Year", "Month"
    ) AS previous_month_revenue,

    ROUND(
        (
            (
                revenue - LAG(revenue) OVER(
                    ORDER BY "Year", "Month"
                )
            )
            /
            NULLIF(
                LAG(revenue) OVER(
                    ORDER BY "Year", "Month"
                ),
                0
            ) * 100
        )::numeric
    ,2) AS growth_percentage

FROM monthly_sales;