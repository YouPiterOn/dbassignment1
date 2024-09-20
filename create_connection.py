import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

def create_connection():
    load_dotenv()
    try:
        connection = mysql.connector.connect(
            host = os.getenv('HOST'),
            port = os.getenv('PORT'),
            user = os.getenv('USER'),
            password = os.getenv('PASSWORD'),
            database = os.getenv('DATABASE')
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error: {e}")
    return None