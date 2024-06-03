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
    # drop table ‘hospital_details’.
    cursor.execute("drop table hospital_details")


except Error as e:
    print(e)
finally:
    conn.close()
    print("Connection closed")
