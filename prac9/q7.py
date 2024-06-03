import sqlite3

# Create an in-memory SQLite database
connection = sqlite3.connect(':memory:')

# Create a cursor object using the cursor() method
cursor = connection.cursor()

# Create a table
create_table_query = '''
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT UNIQUE
)
'''
cursor.execute(create_table_query)

# Insert some data into the table
insert_data_query = '''
INSERT INTO users (name, age, email) VALUES
('Alice', 30, 'alice@example.com'),
('Bob', 25, 'bob@example.com'),
('Charlie', 35, 'charlie@example.com')
'''
cursor.execute(insert_data_query)

# Commit the changes
connection.commit()

# Query the table to verify the data
select_query = 'SELECT * FROM users'
cursor.execute(select_query)
rows = cursor.fetchall()

# Print the rows
for row in rows:
    print(row)

# Close the connection
connection.close()
