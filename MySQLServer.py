import getpass
import mysql.connector
from mysql.connector import Error

def main():
    host = input("Host [localhost]: ") or "localhost"
    user = input("User [root]: ") or "root"
    password = getpass.getpass("Password: ")

    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(host=host, user=user, password=password)
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None and conn.is_connected():
            conn.close()

if __name__ == "__main__":
    main()
