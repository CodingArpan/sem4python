import sqlite3 
con = sqlite3.connect('demodata.sqlite')
cursor = con.cursor()
# cursor.execute("CREATE TABLE hospital (id INTEGER, name TEXT, bed_count INTEGER)")
cursor.execute("INSERT INTO hospital VALUES (1, 'Prabhat Clinic', 200)")
for i in range(10):
    cursor.execute("INSERT INTO hospital VALUES (?, ?, ?)", (i, 'Hospital'+str(i), i*10))
# cursor.execute("drop table hospital")
con.commit()
val = cursor.execute("SELECT * FROM hospital")

for row in val:
    print(row)




















