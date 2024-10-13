CREATE INDEX idx_opt_orders_order_date_product_id 
ON opt_orders(order_date, product_id);

CREATE INDEX idx_opt_products_product_id 
ON opt_products(product_id);