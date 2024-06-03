import mysql.connector
from mysql.connector import Error

try:

    conn = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="root",
        database="dbconnectivity"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM doctor_details")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

except Error as e:
    print(e)
finally:
    conn.close()
    print("Connection closed")
