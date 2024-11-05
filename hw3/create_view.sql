CREATE VIEW order_details AS
SELECT 
    o.order_id,
    o.order_date,
    o.status AS order_status,
    u.username AS customer_name,
    p.name AS product_name,
    oi.quantity,
    oi.price AS product_price_from_order_items,
    (oi.quantity * oi.price) AS total_product_price,
    p.price AS product_price_from_products,
    o.total_price,
    pay.payment_method,
    pay.amount AS payment_amount
FROM
    orders o
JOIN
    users u ON o.user_id = u.user_id
JOIN
    order_items oi ON o.order_id = oi.order_id
JOIN
    products p ON oi.product_id = p.product_id
LEFT JOIN
    payments pay ON o.order_id = pay.order_id
WHERE
    o.status = 'completed';

