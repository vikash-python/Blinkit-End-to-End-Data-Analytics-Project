CREATE INDEX idx_orders_orderid
ON orders_full(order_id);

CREATE INDEX idx_orders_customer
ON orders_full(customer_id);

CREATE INDEX idx_orders_product
ON orders_full(product_id);

CREATE INDEX idx_sales_product
ON sales_dashboard(product_id);

CREATE INDEX idx_feedback_order
ON customer_feedback_cleaned(order_id);