DELIMITER $$

CREATE PROCEDURE PlaceOrder(
    IN p_user_id INT,
    IN p_total_price DECIMAL(10, 2),
    IN p_status ENUM('pending', 'completed', 'shipped', 'cancelled'),
    IN p_order_items JSON
)
BEGIN
    DECLARE new_order_id INT;
    DECLARE i INT DEFAULT 0;
    DECLARE num_items INT;

    INSERT INTO orders (user_id, total_price, status)
    VALUES (p_user_id, p_total_price, p_status);

    SET new_order_id = LAST_INSERT_ID();
    SET num_items = JSON_LENGTH(p_order_items);

    WHILE i < num_items DO
        INSERT INTO order_items (order_id, product_id, quantity, price)
        VALUES (
            new_order_id, 
            JSON_UNQUOTE(JSON_EXTRACT(p_order_items, CONCAT('$[', i, '].product_id'))),
            JSON_UNQUOTE(JSON_EXTRACT(p_order_items, CONCAT('$[', i, '].quantity'))),
            JSON_UNQUOTE(JSON_EXTRACT(p_order_items, CONCAT('$[', i, '].price')))
        );
        SET i = i + 1;
    END WHILE;

END $$

DELIMITER ;