--Total Orders
SELECT 
    COUNT(DISTINCT order_id) AS total_orders
FROM sales_dashboard;

--Total Revenue
SELECT 
    SUM(total_sales) AS total_revenue
FROM sales_dashboard;

--Average Order Value


SELECT 
    AVG(total_sales) AS average_order_value
FROM sales_dashboard;


--Category Wise Sales

SELECT
    category,
    SUM(total_sales) AS revenue
FROM sales_dashboard
GROUP BY category
ORDER BY revenue DESC;


--Top 10 Products

SELECT
    product_name,
    SUM(total_sales) AS revenue
FROM orders_full
GROUP BY product_name
ORDER BY revenue DESC
LIMIT 10;


-- Monthly Revenue Trend

SELECT
    "Year",
    "Month",
    SUM(total_sales) AS monthly_revenue
FROM sales_dashboard
GROUP BY "Year", "Month"
ORDER BY "Year", "Month";


-- Payment Method Performance

SELECT
    payment_method,
    COUNT(order_id) AS total_orders,
    SUM(total_sales) AS revenue
FROM sales_dashboard
GROUP BY payment_method
ORDER BY revenue DESC;



-- Delivery Status Analysis

SELECT
    delivery_status,
    COUNT(order_id) AS total_orders
FROM sales_dashboard
GROUP BY delivery_status
ORDER BY total_orders DESC;

-- Category Wise Quantity Sold

SELECT
    category,
    SUM(quantity) AS total_quantity
FROM sales_dashboard
GROUP BY category
ORDER BY total_quantity DESC;


-- Customer Segment Analysis

SELECT
    customer_segment,
    COUNT(customer_id) AS customers,
    AVG(order_total) AS avg_order_value,
    SUM(order_total) AS total_revenue
FROM orders_full
GROUP BY customer_segment
ORDER BY total_revenue DESC;

