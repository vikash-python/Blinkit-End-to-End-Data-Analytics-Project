-- =========================================================
-- Blinkit End-to-End Data Analytics Project
-- File: 07_views.sql
-- Description: SQL Views for Reporting
-- =========================================================

--Sales Performance View
CREATE OR REPLACE VIEW vw_sales_performance AS

SELECT
    order_id,
    product_id,
    category,
    quantity,
    total_sales,
    payment_method,
    delivery_status,
    "Year",
    "Month"
FROM sales_dashboard;


--Product Performance View
CREATE OR REPLACE VIEW vw_product_performance AS

SELECT
    product_id,
    product_name,
    category,
    brand,
    total_quantity,
    total_sales,
    total_orders
FROM product_dashboard;


--Delivery Performance View
CREATE OR REPLACE VIEW vw_delivery_performance AS

SELECT
    order_id,
    delivery_partner_id,
    delivery_status,
    delivery_time_minutes,
    distance_km,
    reasons_if_delayed
FROM delivery_cleaned;


--Customer Feedback View
CREATE OR REPLACE VIEW vw_customer_feedback AS

SELECT
    feedback_id,
    order_id,
    customer_id,
    rating,
    sentiment,
    feedback_category,
    feedback_date
FROM customer_feedback_cleaned;



--Marketing Performance View
CREATE OR REPLACE VIEW vw_marketing_performance AS

SELECT
    campaign_id,
    campaign_name,
    channel,
    impressions,
    clicks,
    conversions,
    spend,
    revenue_generated,
    roas
FROM marketing_cleaned;




--Inventory View
CREATE OR REPLACE VIEW vw_inventory_status AS

SELECT
    product_id,
    date,
    stock_received,
    available_stock,
    damaged_stock,
    damage_percent
FROM inventory_cleaned;


--Complete Order Report View 
CREATE OR REPLACE VIEW vw_complete_order_report AS

SELECT
    o.order_id,
    o.customer_name,
    o.product_name,
    o.category,
    o.order_total,
    d.delivery_status,
    d.delivery_time_minutes,
    f.rating,
    f.sentiment

FROM orders_full o

LEFT JOIN delivery_cleaned d
ON o.order_id = d.order_id

LEFT JOIN customer_feedback_cleaned f
ON o.order_id = f.order_id;


