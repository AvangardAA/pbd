import uuid
import random

import mysql.connector
from faker import Faker

fake = Faker()
NUM_PROD = 100000
NUM_USERS = 10000
NUM_CATEGORIRES = 1000

CONF = {
    'host': 'localhost',
    'user': 'admin_e',
    'password': 'admindummy',
    'database': 'ecommerce',
}


def connect():
    try:
        conn = mysql.connector.connect(**CONF)
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")


def generate(conn):
    cursor = conn.cursor()

    insert_product_query = """
    INSERT INTO products (name, description, price, stock_quantity, created_at, updated_at)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    insert_user_query = """
    INSERT INTO users (username, password, email, role, created_at, updated_at)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    insert_order_query = """
    INSERT INTO orders (user_id, order_date, total_price, status)
    VALUES (%s, %s, %s, %s)
    """

    insert_order_item_query = """
    INSERT INTO order_items (order_id, product_id, quantity, price)
    VALUES (%s, %s, %s, %s)
    """

    insert_payment_query = """
    INSERT INTO payments (order_id, payment_method, payment_date, amount)
    VALUES (%s, %s, %s, %s)
    """

    insert_category_query = """
    INSERT INTO categories (name, description, created_at, updated_at)
    VALUES (%s, %s, %s, %s)
    """

    insert_product_category_query = """
    INSERT INTO product_categories (product_id, category_id)
    VALUES (%s, %s)
    """

    users = []
    for i in range(NUM_USERS):
        role = 'customer' if i < 9950 else 'sales'
        users.append((uuid.uuid4().hex, fake.password(), uuid.uuid4().hex + "@gmail.com", role, fake.date_this_decade(), fake.date_this_decade()))

    cursor.executemany(insert_user_query, users)
    conn.commit()

    cursor.execute("SELECT user_id FROM users")
    user_ids = [row[0] for row in cursor.fetchall()]

    categories = []
    for i in range(NUM_CATEGORIRES):
        categories.append((uuid.uuid4().hex, uuid.uuid4().hex, fake.date_this_decade(), fake.date_this_decade()))

    cursor.executemany(insert_category_query, categories)
    conn.commit()

    cursor.execute("SELECT category_id FROM categories")
    category_ids = [row[0] for row in cursor.fetchall()]

    product_counter = 0
    while product_counter < NUM_PROD:
        # if product_counter == 1000: exit(0) # temporary
        products = []
        for _ in range(1000):
            product_name = uuid.uuid4().hex
            product_description = fake.text(max_nb_chars=200)
            product_price = round(random.uniform(5.0, 500.0), 2)
            stock_quantity = random.randint(1, 1000)
            created_at = fake.date_this_decade()
            updated_at = fake.date_this_decade()
            products.append((product_name, product_description, product_price, stock_quantity, created_at, updated_at))

        cursor.executemany(insert_product_query, products)
        conn.commit()
        product_counter += 1000

        cursor.execute(f"SELECT product_id FROM products ORDER BY product_id LIMIT {product_counter - 1000}, 1000")  # add offset
        product_ids = [row[0] for row in cursor.fetchall()]

        # assign category
        pid_cid = [(pid, random.choice(category_ids)) for pid in product_ids]
        cursor.executemany(insert_product_category_query, pid_cid)
        conn.commit()

        # 50 orders per 1000 products added
        for _ in range(50):
            user_id = random.choice(user_ids)
            total_price = round(random.uniform(20.0, 1000.0), 2)
            status = random.choice(['pending', 'completed', 'shipped', 'cancelled'])

            cursor.execute(insert_order_query, (user_id, fake.date_this_decade(), total_price, status))
            order_id = cursor.lastrowid

            order_items = []
            for _ in range(random.randint(1, 5)):
                order_items.append((order_id, random.choice(product_ids), random.randint(1, 5), round(random.uniform(5.0, 100.0), 2)))

            cursor.executemany(insert_order_item_query, order_items)
            conn.commit()

            payment_method = random.choice(['credit_card', 'paypal', 'bank_transfer'])
            cursor.execute(insert_payment_query, (order_id, payment_method, fake.date_this_decade(), total_price))
            conn.commit()

        print(f"Current: {product_counter}")


if __name__ == "__main__":
    if conn := connect():
        generate(conn)
        conn.close()
