import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="127.0.0.1:3306",
        user="ryan",
        password="aa0934019769",
        database="olist_ecommerce"
    )
