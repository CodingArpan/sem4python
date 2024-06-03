import mysql.connector
try:
    # Establish a connection to the MySQL database
    conn = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="root",
        database="dbconnectivity"
    )

    cursor = conn.cursor()

    # Create hospital_details table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS hospital_details (
        Hospital_Id INT PRIMARY KEY,
        Hospital_Name VARCHAR(255) NOT NULL,
        Bed_count INT NOT NULL
    )
    ''')

    # Create doctor_details table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS doctor_details (
        Doctor_Id INT PRIMARY KEY,
        Doctor_Name VARCHAR(255) NOT NULL,
        Hospital_Id INT NOT NULL,
        Speciality VARCHAR(255) NOT NULL,
        Salary INT NOT NULL,
        Experience INT NOT NULL,
        FOREIGN KEY (Hospital_Id) REFERENCES hospital_details (Hospital_Id)
    )
    ''')

    # Insert values into hospital_details table
    hospital_details = [
        (1, 'Janta', 200),
        (2, 'Zydus', 500),
        (3, 'Sal', 1000),
        (4, 'Stirling', 1500)
    ]

    cursor.executemany('''
    INSERT INTO hospital_details (Hospital_Id, Hospital_Name, Bed_count)
    VALUES (%s, %s, %s)
    ''', hospital_details)

    # Insert values into doctor_details table
    doctor_details = [
        (101, 'Karan', 1, 'Pediatric', 40000, 0),
        (102, 'Naresh', 1, 'Oncologist', 80000, 5),
        (103, 'Hardik', 2, 'Surgeon', 60000, 2),
        (104, 'Vishal', 2, 'Homeopathy', 50000, 1),
        (105, 'Jay', 3, 'Ayurvedic', 40000, 0),
        (106, 'Deep', 3, 'Physiotherapist', 70000, 4),
        (107, 'Divyesh', 4, 'Pediatric', 55000, 3),
        (108, 'Arjun', 4, 'Skin', 55000, 3)
    ]

    cursor.executemany('''
    INSERT INTO doctor_details (Doctor_Id, Doctor_Name, Hospital_Id, Speciality, Salary, Experience)
    VALUES (%s, %s, %s, %s, %s, %s)
    ''', doctor_details)

    # Commit the transaction
    conn.commit()

except mysql.connector.Error as e:
    print(f"Error: {e}")

finally:

    # Close the connection
    conn.close()

    print("Tables created and values inserted successfully.")
