import mysql.connector
from mysql.connector import Error

def connect_database():
    db_name = "fitnesscenter"
    user = "root"
    password = "Luna2794"
    host = "localhost"

    try:
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password = password,
            host = host
        )

        if conn.is_connected():
            print("connected")
            return conn

    except Error as e:
        print(e)
        return None

    