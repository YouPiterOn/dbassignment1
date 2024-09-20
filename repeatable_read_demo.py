from datetime import datetime
from create_connection import *

def repeatable_read_demo():
    print("Repeatable read --------------------------------")

    connection1 = create_connection()
    connection2 = create_connection()

    try:
        cursor1 = connection1.cursor()
        cursor2 = connection2.cursor()

        # Transaction 1: Repeatable Read Before
        print(f"Transaction 1 started: {datetime.now()}")
        connection1.start_transaction(isolation_level='REPEATABLE READ')
        cursor1.execute("SELECT balance FROM accounts WHERE name = 'Alice'")
        balance_repeatable_read = cursor1.fetchone()[0]

        print(f"Repeatable read before update: Alice's balance = {balance_repeatable_read}")

        # Transaction 2: Modify Value
        print(f"Transaction 2 started: {datetime.now()}")
        connection2.start_transaction(isolation_level='READ COMMITTED')
        cursor2.execute("UPDATE accounts SET balance = 9999 WHERE name = 'Alice'")

        print(f"Transaction 2 commit(): {datetime.now()}")
        connection2.commit()

        # Transaction 1: Repeatable Read After
        cursor1.execute("SELECT balance FROM accounts WHERE name = 'Alice'")
        balance_repeatable_read = cursor1.fetchone()[0]

        print(f"Repeatable read after update: Alice's balance = {balance_repeatable_read}")

        # Transaction 1: Reverse Changes
        cursor1.execute("UPDATE accounts SET balance = 1000 WHERE name = 'Alice'")

        print(f"Transaction 1 commit(): {datetime.now()}")
        connection1.commit()

    except Error as e:
        print(f"Error: {e}")
    finally:
        print("\n")

        if cursor1:
            cursor1.close()
        if connection1 and connection1.is_connected():
            connection1.close()
        if cursor2:
            cursor2.close()
        if connection2 and connection2.is_connected():
            connection2.close()

if __name__ == "__main__":
    repeatable_read_demo()
