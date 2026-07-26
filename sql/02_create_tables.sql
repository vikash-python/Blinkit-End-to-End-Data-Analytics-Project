-- =========================================================
-- File: 02_create_tables.sql
-- Project: Blinkit End-to-End Data Analytics
-- =========================================================

-- Tables are automatically created using Python
-- pandas.DataFrame.to_sql() with SQLAlchemy

-- Tables Created:
-- 1. orders_full
-- 2. sales_dashboard
-- 3. product_dashboard
-- 4. inventory_cleaned
-- 5. delivery_cleaned
-- 6. marketing_cleaned
-- 7. customer_feedback_cleaned



    order_id INT PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date DATE,
    promised_delivery_time TIMESTAMP,
    actual_delivery_time TIMESTAMP,
    delivery_status VARCHAR(30),
    order_total DECIMAL(10,2),
    payment_method VARCHAR(30),
    delivery_partner_id INT,
    store_id INT,
    year INT,
    month VARCHAR(20),
    day INT,
    weekday VARCHAR(20),
    quarter INT,
    delivery_delay_minutes DECIMAL(10,2),

    customer_name VARCHAR(100),
    email VARCHAR(150),
    phone BIGINT,
    address TEXT,
    area VARCHAR(100),
    pincode INT,
    registration_date DATE,
    customer_segment VARCHAR(50),
    total_orders INT,
    avg_order_value DECIMAL(10,2),

    Year_y INT,
    Month_y VARCHAR(20),
    Day_y INT,
    Weekday_y VARCHAR(20),

    product_id INT,
    quantity INT,
    unit_price DECIMAL(10,2),
    total_sales DECIMAL(10,2),

    product_name VARCHAR(100),
    category VARCHAR(100),
    brand VARCHAR(100),

    price DECIMAL(10,2),
    mrp DECIMAL(10,2),
    margin_percentage DECIMAL(5,2),

    shelf_life_days INT,
    min_stock_level INT,
    max_stock_level INT
);




-- =========================================================
-- Table: sales_dashboard
-- =========================================================

CREATE TABLE sales_dashboard (

    order_id INT,
    order_date DATE,
    customer_id INT,
    product_id INT,

    category VARCHAR(100),

    quantity INT,

    total_sales DECIMAL(10,2),

    payment_method VARCHAR(30),

    delivery_status VARCHAR(30),

    Year INT,
    Month VARCHAR(20),
    Day INT

);



-- =========================================================
-- Table: product_dashboard
-- =========================================================

CREATE TABLE product_dashboard (

    product_id INT PRIMARY KEY,

    product_name VARCHAR(100) NOT NULL,

    category VARCHAR(100),

    brand VARCHAR(100),

    total_quantity INT,

    total_sales DECIMAL(10,2),

    total_orders INT

);


-- =========================================================
-- Table: inventory_cleaned
-- =========================================================

CREATE TABLE inventory_cleaned (

    product_id INT,

    date DATE,

    stock_received INT,

    damaged_stock INT,

    Day INT,

    available_stock INT,

    damage_percent DECIMAL(10,2),

    Month VARCHAR(20)

);



-- =========================================================
-- Table: delivery_cleaned
-- =========================================================

CREATE TABLE delivery_cleaned (

    order_id INT,

    delivery_partner_id INT,

    promised_time TIMESTAMP,

    actual_time TIMESTAMP,

    delivery_time_minutes DECIMAL(10,2),

    distance_km DECIMAL(10,2),

    delivery_status VARCHAR(50),

    reasons_if_delayed TEXT

);



-- =========================================================
-- Table: marketing_cleaned
-- =========================================================

CREATE TABLE marketing_cleaned (

    campaign_id INT PRIMARY KEY,

    campaign_name VARCHAR(100),

    date DATE,

    target_audience VARCHAR(100),

    channel VARCHAR(50),

    impressions INT,

    clicks INT,

    conversions INT,

    spend DECIMAL(10,2),

    revenue_generated DECIMAL(10,2),

    roas DECIMAL(10,2),

    Year INT,

    Month VARCHAR(20),

    Day INT,

    Weekday VARCHAR(20)

);


-- =========================================================
-- Table: customer_feedback_cleaned
-- =========================================================

CREATE TABLE customer_feedback_cleaned (

    feedback_id INT PRIMARY KEY,

    order_id INT,

    customer_id INT,

    rating INT,

    feedback_text TEXT,

    feedback_category VARCHAR(100),

    sentiment VARCHAR(50),

    feedback_date DATE

);



