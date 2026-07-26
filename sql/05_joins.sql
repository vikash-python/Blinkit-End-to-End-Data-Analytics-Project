-- =========================================================
-- Blinkit End-to-End Data Analytics Project
-- File: 05_joins.sql
-- Description: SQL Joins Analysis
-- =========================================================




-- Orders with Customer Feedback

SELECT
    o.order_id,
    o.customer_id,
    o.order_total,
    f.rating,
    f.sentiment,
    f.feedback_category
FROM orders_full o
JOIN customer_feedback_cleaned f
ON o.order_id = f.order_id;



-- Order Product Analysis

SELECT
    o.order_id,
    o.product_id,
    o.product_name,
    o.category,
    o.quantity,
    o.total_sales
FROM orders_full o
JOIN product_dashboard p
ON o.product_id = p.product_id;


-- Delivery Performance Analysis

SELECT
    o.order_id,
    o.order_total,
    d.delivery_time_minutes,
    d.distance_km,
    d.delivery_status
FROM orders_full o
JOIN delivery_cleaned d
ON o.order_id = d.order_id;


-- Product Inventory Analysis

SELECT
    p.product_id,
    p.product_name,
    p.category,
    p.total_sales,
    i.available_stock,
    i.damage_percent
FROM product_dashboard p
JOIN inventory_cleaned i
ON p.product_id = i.product_id;


-- Marketing Campaign Analysis

SELECT
    campaign_name,
    channel,
    impressions,
    clicks,
    conversions,
    spend,
    revenue_generated,
    roas
FROM marketing_cleaned
ORDER BY roas DESC;



-- Orders without feedback analysis

SELECT
    o.order_id,
    o.customer_id,
    o.order_total,
    f.rating,
    f.sentiment
FROM orders_full o
LEFT JOIN customer_feedback_cleaned f
ON o.order_id = f.order_id;


-- Product Stock Analysis

SELECT
    p.product_id,
    p.product_name,
    p.category,
    p.total_sales,
    i.available_stock,
    i.damage_percent
FROM product_dashboard p
LEFT JOIN inventory_cleaned i
ON p.product_id = i.product_id;


-- Complete Customer Order Analysis

SELECT
    o.order_id,
    o.customer_name,
    p.product_name,
    p.category,
    o.order_total,
    f.rating,
    f.sentiment
FROM orders_full o

JOIN product_dashboard p
ON o.product_id = p.product_id

LEFT JOIN customer_feedback_cleaned f
ON o.order_id = f.order_id;

--Sales + Product Category Analysis
SELECT
    p.category,
    COUNT(s.order_id) AS total_orders,
    SUM(s.total_sales) AS revenue
FROM sales_dashboard s

JOIN product_dashboard p
ON s.product_id = p.product_id

GROUP BY p.category
ORDER BY revenue DESC;

--Delivery + Orders Analysis
SELECT
    d.delivery_status,
    COUNT(o.order_id) AS total_orders,
    AVG(o.order_total) AS avg_order_value
FROM orders_full o

JOIN delivery_cleaned d
ON o.order_id = d.order_id

GROUP BY d.delivery_status;