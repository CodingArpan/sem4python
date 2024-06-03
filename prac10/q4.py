import tkinter as tk
from tkinter import messagebox
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


# Function to insert data into the database

    def insert_data(enrollment, name, gender, address, branch, mobile, email):
        # Insert a row of data
        table = """CREATE TABLE if not exists students (
        enrollment VARCHAR(20) NOT NULL,
        name VARCHAR(100) NOT NULL,
        gender VARCHAR(20) NOT NULL,
        address VARCHAR(255),
        branch VARCHAR(50) NOT NULL,
        mobile VARCHAR(15),
        email VARCHAR(100),
        PRIMARY KEY (enrollment)
    )"""
        cursor.execute(table)
        insert_query = """INSERT INTO students (enrollment, name, gender, address, branch, mobile, email)
                              VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(insert_query, (enrollment, name,
                       gender, address, branch, mobile, email))

        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Data saved successfully")

    # Function to clear the form fields after submission
    def clear_fields():
        enrollment_var.set("")
        name_var.set("")
        gender_var.set("Select Gender")
        address_var.set("")
        branch_var.set("")
        mobile_var.set("")
        email_var.set("")

    # Function to submit the form
    def submit():
        insert_data(enrollment_var.get(), name_var.get(), gender_var.get(
        ), address_var.get(), branch_var.get(), mobile_var.get(), email_var.get())
        clear_fields()

    # Create the main window
    root = tk.Tk()
    root.title("Student Registration")
    root.geometry('500x250')

    # Define StringVar for form fields
    enrollment_var = tk.StringVar()
    name_var = tk.StringVar()
    gender_var = tk.StringVar(value="Select Gender")
    address_var = tk.StringVar()
    branch_var = tk.StringVar()
    mobile_var = tk.StringVar()
    email_var = tk.StringVar()

    # Create and place form fields
    tk.Label(root, text="Enrollment No.").grid(row=0, column=0)
    tk.Entry(root, textvariable=enrollment_var).grid(row=0, column=1)

    tk.Label(root, text="Name").grid(row=1, column=0)
    tk.Entry(root, textvariable=name_var).grid(row=1, column=1)

    tk.Label(root, text="Gender").grid(row=2, column=0)
    tk.OptionMenu(root, gender_var, "Male", "Female",
                  "Other").grid(row=2, column=1)

    tk.Label(root, text="Address").grid(row=3, column=0)
    tk.Entry(root, textvariable=address_var).grid(row=3, column=1)

    tk.Label(root, text="Branch").grid(row=4, column=0)
    tk.Entry(root, textvariable=branch_var).grid(row=4, column=1)

    tk.Label(root, text="Mobile No.").grid(row=5, column=0)
    tk.Entry(root, textvariable=mobile_var).grid(row=5, column=1)

    tk.Label(root, text="Email Address").grid(row=6, column=0)
    tk.Entry(root, textvariable=email_var).grid(row=6, column=1)

    # Submit button
    tk.Button(root, text="Submit", command=submit).grid(row=7, columnspan=2)

    # Start the GUI event loop
    root.mainloop()


except Error as e:
    print(f"Error: {e}")
