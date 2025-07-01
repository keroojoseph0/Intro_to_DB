import mysql.connector

try:
    with mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "SecureP@sw0rd!123"
    ) as connection:
        create_db = f"CREATE DATABASE IF NOT EXISTS alx_book_store"
        
        with connection.cursor() as cursor:
            cursor.execute(create_db)
            print("Datebase 'alx_book_store' created successfuly!")
except mysql.connector.Error as e:
    print(e)
