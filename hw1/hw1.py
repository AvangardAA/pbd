"""
kse pbd hw1
"""
import os
import time

from datetime import datetime

import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv


def create_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASS'),
            database=os.getenv('DB_DB')
        )
        if connection.is_connected(): return connection

    except Error as e: print(f"Error: {e}")
    return None


def read_uncommitted_demo():
    """
    https://github.com/AngelShynk/PracticalAssignment01/blob/main/read_uncommited_demo.py
    """
    connection1 = create_connection()
    connection2 = create_connection()

    try:
        cursor1 = connection1.cursor()
        cursor2 = connection2.cursor()

        # Transaction 1: Read Uncommitted
        print(f"Transaction 1 started: {datetime.now()}")
        connection1.start_transaction(isolation_level='READ UNCOMMITTED')
        cursor1.execute("UPDATE accounts SET balance = 9999 WHERE name = 'Alice'")

        # Transaction 2: Read Uncommitted
        print(f"Transaction 2 started: {datetime.now()}")
        connection2.start_transaction(isolation_level='READ UNCOMMITTED')
        cursor2.execute("SELECT balance FROM accounts WHERE name = 'Alice'")
        balance_dirty_read = cursor2.fetchone()[0]

        print(f"Dirty Read (READ UNCOMMITTED): Alice's balance = {balance_dirty_read}")

        print(f"Transaction 1 rollback(): {datetime.now()}")
        connection1.rollback()

        print(f"Transaction 2 commit(): {datetime.now()}")
        connection2.commit()

    except Error as e: print(f"Error: {e}")
    finally:
        if cursor1: cursor1.close()
        if connection1 and connection1.is_connected(): connection1.close()
        if cursor2: cursor2.close()
        if connection2 and connection2.is_connected(): connection2.close()


def read_commit():
    connection1 = create_connection()
    connection2 = create_connection()

    try:
        cursor1 = connection1.cursor()
        cursor2 = connection2.cursor()

        print(f"Transaction 1 started: {datetime.now()}")
        connection1.start_transaction(isolation_level='READ COMMITTED')
        cursor1.execute("SELECT balance FROM accounts WHERE name = 'Alice'")
        balance = cursor1.fetchone()[0]
        print(f"Transaction 1 Alice balance: {balance}")

        print(f"Transaction 2 started: {datetime.now()}")
        connection2.start_transaction(isolation_level='READ COMMITTED')
        cursor2.execute("UPDATE accounts SET balance = 1100 WHERE name = 'Alice'")
        connection2.commit()

        cursor1.execute("SELECT balance FROM accounts WHERE name = 'Alice'")
        balance = cursor1.fetchone()[0]
        print(f"Transaction 1 Alice balance: {balance}")

        print(f"Transaction 1 commit(): {datetime.now()}")
        connection1.commit()

    except Error as e: print(f"Error: {e}")
    finally:
        if cursor1: cursor1.close()
        if connection1 and connection1.is_connected(): connection1.close()
        if cursor2: cursor2.close()
        if connection2 and connection2.is_connected(): connection2.close()


def read_repeat():
    connection1 = create_connection()
    connection2 = create_connection()

    try:
        cursor1 = connection1.cursor()
        cursor2 = connection2.cursor()

        print(f"Transaction started: {datetime.now()}")
        connection1.start_transaction(isolation_level='REPEATABLE READ')
        cursor1.execute("SELECT balance FROM accounts WHERE name = 'Alice'")
        balance = cursor1.fetchone()[0]
        print(f"Start: {balance}")

        cursor2.execute("UPDATE accounts SET balance = 1200 WHERE name = 'Alice'")
        connection2.commit()

        cursor1.execute("SELECT balance FROM accounts WHERE name = 'Alice'")
        balance = cursor1.fetchone()[0]
        print(f"Final: {balance}")

        print(f"Transaction commit(): {datetime.now()}")
        connection1.commit()

    except Error as e: print(f"Error: {e}")
    finally:
        if cursor1: cursor1.close()
        if connection1 and connection1.is_connected(): connection1.close()
        if cursor2: cursor2.close()
        if connection2 and connection2.is_connected(): connection2.close()


def dlock():
    connection1 = create_connection()
    connection2 = create_connection()

    try:
        cursor1 = connection1.cursor()
        cursor2 = connection2.cursor()

        print(f"Transaction 1 started: {datetime.now()}")
        connection1.start_transaction()
        cursor1.execute("SELECT balance FROM accounts WHERE name = 'Alice' FOR UPDATE")

        time.sleep(2)

        print(f"Transaction 2 started: {datetime.now()}")
        connection2.start_transaction()
        cursor2.execute("SELECT balance FROM accounts WHERE name = 'Bob' FOR UPDATE")

        time.sleep(2)

        cursor1.execute("UPDATE accounts SET balance = balance + 100 WHERE name = 'Bob'")
        cursor2.execute("UPDATE accounts SET balance = balance + 100 WHERE name = 'Alice'")

        connection1.commit()
        connection2.commit()

    except Error as e:
        print(f"deadlock {e}")
        connection1.rollback()
        connection2.rollback()
    finally:
        if cursor1: cursor1.close()
        if connection1 and connection1.is_connected(): connection1.close()
        if cursor2: cursor2.close()
        if connection2 and connection2.is_connected(): connection2.close()


def read_no_repeat():
    connection1 = create_connection()
    connection2 = create_connection()

    try:
        cursor1 = connection1.cursor()
        cursor2 = connection2.cursor()

        print(f"Transaction 1 started: {datetime.now()}")
        connection1.start_transaction(isolation_level='READ COMMITTED')
        cursor1.execute("SELECT balance FROM accounts WHERE name = 'Alice'")
        balance = cursor1.fetchone()[0]
        print(f"Transaction 1 Alice balance: {balance}")

        print(f"Transaction 2 started: {datetime.now()}")
        connection2.start_transaction(isolation_level='READ COMMITTED')
        cursor2.execute("UPDATE accounts SET balance = 1200 WHERE name = 'Alice'")
        connection2.commit()

        cursor1.execute("SELECT balance FROM accounts WHERE name = 'Alice'")
        balance = cursor1.fetchone()[0]
        print(f"Transaction 1 Alice balance: {balance}")

        print(f"Transaction 1 commit(): {datetime.now()}")
        connection1.commit()

    except Error as e:
        print(f"Error: {e}")
        connection1.rollback()
        connection2.rollback()
    finally:
        if cursor1: cursor1.close()
        if connection1 and connection1.is_connected(): connection1.close()
        if cursor2: cursor2.close()
        if connection2 and connection2.is_connected(): connection2.close()


if __name__ == "__main__":
    load_dotenv()

    read_uncommitted_demo()
    read_commit()
    read_repeat()
    read_no_repeat()
    dlock()
