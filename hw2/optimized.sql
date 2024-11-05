WITH order_counts AS (
    SELECT 
        p.product_name,
        COUNT(o.order_id) AS order_count
    FROM 
        opt_orders o
    JOIN 
        opt_products p ON o.product_id = p.product_id
    WHERE 
        o.order_date > '2023-01-01'
    GROUP BY 
        p.product_name
)

SELECT
    (SELECT CONCAT(product_name, ": ", order_count)
     FROM order_counts
     ORDER BY order_count ASC
     LIMIT 1) AS min_order,

    (SELECT CONCAT(product_name, ": ", order_count)
     FROM order_counts
     ORDER BY order_count DESC
     LIMIT 1) AS max_order,

    (SELECT SUM(order_count) 
     FROM order_counts) AS total_orders;