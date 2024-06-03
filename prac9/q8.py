import sqlite3

# Establish a connection to the SQLite database file named 'demo.db'
connection = sqlite3.connect('demo.db')

# Create a cursor object using the cursor() method
cursor = connection.cursor()

# Define a script with multiple SQL queries
sql_script = '''
-- Drop the table if it already exists
DROP TABLE IF EXISTS users;

-- Create the users table
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT UNIQUE
);

-- Insert some data into the users table
INSERT INTO users (name, age, email) VALUES
('Alice', 30, 'alice@example.com'),
('Bob', 25, 'bob@example.com'),
('Charlie', 35, 'charlie@example.com');
'''

# Execute the script with multiple SQL queries
cursor.executescript(sql_script)

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
