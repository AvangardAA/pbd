CREATE USER 'admin_e'@'localhost' IDENTIFIED BY 'admindummy';
CREATE USER 'sales_e'@'localhost' IDENTIFIED BY 'salesdummy';
CREATE USER 'customer_e'@'localhost' IDENTIFIED BY 'customerdummy';

GRANT ALL PRIVILEGES ON ecommerce.* TO 'admin_e'@'localhost';
GRANT SELECT, INSERT, UPDATE, DELETE ON ecommerce.orders TO 'sales_e'@'localhost';
GRANT SELECT, INSERT ON ecommerce.orders TO 'customer_e'@'localhost';
GRANT SELECT, INSERT ON ecommerce.products TO 'customer_e'@'localhost';

FLUSH PRIVILEGES;