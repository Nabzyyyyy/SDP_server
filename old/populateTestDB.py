import sqlite3

conn = sqlite3.connect('testDB.db')
print("Opened database successfully")

conn.execute("INSERT INTO TESTUSER (ID,NAME,PLATENO,MAKE,MODEL) \
            VALUES (1, 'Tyler', 'GJH9885', 'Dodge', 'Dart')");


conn.execute("INSERT INTO TESTUSER (ID,NAME,PLATENO,MAKE,MODEL) \
            VALUES (2, 'Nabil', 'EDK6023', 'Honda', 'Civic')");

conn.commit()
print("Tyler and Nabil added successfully")
conn.close()
