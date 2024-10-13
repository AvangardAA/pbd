"""
kse pbd hw2
run with python3 -m hw2.hw2 from proj root
"""

from mysql.connector import Error
from faker import Faker
from dotenv import load_dotenv

from hw1.hw1 import create_connection


def generate():
    fake = Faker()
    if (connection := create_connection()):
        cursor = connection.cursor()

        try:
            client_ids = []
            product_ids = []

            for _ in range(10000):
                client_id = fake.uuid4()
                name = fake.first_name()
                surname = fake.last_name()
                email = fake.email()
                phone = fake.phone_number()
                address = fake.address().replace('\n', ', ')
                status = fake.random_element(elements=('active', 'inactive'))

                cursor.execute(
                    "INSERT INTO opt_clients (id, name, surname, email, phone, address, status) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                    (client_id, name, surname, email, phone, address, status)
                )
                client_ids.append(client_id)

                product_name = fake.word().capitalize()
                product_category = fake.random_element(elements=('Category1', 'Category2', 'Category3', 'Category4', 'Category5'))
                description = fake.sentence()

                cursor.execute(
                    "INSERT INTO opt_products (product_name, product_category, description) VALUES (%s, %s, %s)",
                    (product_name, product_category, description)
                )
                product_ids.append(cursor.lastrowid)

                order_date = fake.date_between(start_date='-1y', end_date='today')

                order_client_id = client_id
                order_product_id = fake.random_element(elements=product_ids)

                cursor.execute(
                    "INSERT INTO opt_orders (order_date, client_id, product_id) VALUES (%s, %s, %s)",
                    (order_date, order_client_id, order_product_id)
                )

            connection.commit()

        except Error as e:
            print(f"Error: {e}")
            connection.rollback()

        finally:
            cursor.close()
            connection.close()


if __name__ == "__main__":
    load_dotenv()
    generate()
