import mysql.connector
from mysql.connector import Error
try:
    # Connect to the database
    conn = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="root",
        database="dbconnectivity"
    )

    if conn.is_connected():
        print("Connected to MySQL database")

    cursor = conn.cursor()

    cursor.execute("create table if not exists demo_data (id int primary key, name varchar(100))")

    cursor.execute("show databases")
    print("Databases in MySQL:")
    for database in cursor:
        print(database)

    conn.commit()

except Error as e:
    print(f"Error: {e}")

finally:
    # Close the connection
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("MySQL connection is closed")