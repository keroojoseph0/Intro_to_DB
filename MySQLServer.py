import mysql.connector
from mysql.connector import Error

try:
    with connect(
    host = "localhost",
    user = "root",
    password = "SecureP@sw0rd!123"
    ) as connection:
        DB_name = "alx_book_store"
        create_db = f"CREATE DATABASE IF NOT EXISTS {DB_name}"
        
        with connection.cursor() as cursor:
            cursor.execute(create_db)
            print(f"Datebase '{DB_name}' created successfuly!")
except Error as e:
    print(e)
