SELECT
    (SELECT CONCAT(p.product_name, ": ", COUNT(o.order_id))
     FROM opt_orders o
     JOIN opt_products p ON o.product_id = p.product_id
     WHERE o.order_date > '2023-01-01'
     GROUP BY p.product_name
     ORDER BY COUNT(o.order_id) ASC
     LIMIT 1) AS min_order,

    (SELECT CONCAT(p.product_name, ": ", COUNT(o.order_id))
     FROM opt_orders o
     JOIN opt_products p ON o.product_id = p.product_id
     WHERE o.order_date > '2023-01-01'
     GROUP BY p.product_name
     ORDER BY COUNT(o.order_id) DESC
     LIMIT 1) AS max_order,

    (SELECT COUNT(*) 
     FROM opt_orders o 
     WHERE o.order_date > '2023-01-01') AS total_orders;