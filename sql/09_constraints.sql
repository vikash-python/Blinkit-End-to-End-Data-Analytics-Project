-- ==========================================
-- PRIMARY KEYS
-- ==========================================

ALTER TABLE orders_full
ADD CONSTRAINT orders_full_pkey
PRIMARY KEY (order_id);


ALTER TABLE delivery_cleaned
ADD CONSTRAINT delivery_pkey
PRIMARY KEY (order_id);


ALTER TABLE customer_feedback_cleaned
ADD CONSTRAINT feedback_pkey
PRIMARY KEY (feedback_id);


ALTER TABLE product_dashboard
ADD CONSTRAINT product_pkey
PRIMARY KEY (product_id);


ALTER TABLE marketing_cleaned
ADD CONSTRAINT marketing_pkey
PRIMARY KEY (campaign_id);



-- ==========================================
-- FOREIGN KEYS
-- ==========================================

ALTER TABLE delivery_cleaned
ADD CONSTRAINT fk_delivery_order
FOREIGN KEY (order_id)
REFERENCES orders_full(order_id);


ALTER TABLE customer_feedback_cleaned
ADD CONSTRAINT fk_feedback_order
FOREIGN KEY (order_id)
REFERENCES orders_full(order_id);


ALTER TABLE inventory_cleaned
ADD CONSTRAINT fk_inventory_product
FOREIGN KEY (product_id)
REFERENCES product_dashboard(product_id);


ALTER TABLE sales_dashboard
ADD CONSTRAINT fk_sales_product
FOREIGN KEY (product_id)
REFERENCES product_dashboard(product_id);