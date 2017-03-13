import sqlite3

conn = sqlite3.connect('testDB.db')
print("Opened database successfully")

#conn.execute("UPDATE TESTUSER SET PLATENO = 'EDK6023' WHERE NAME = 'Nabil' AND MAKE LIKE '%honda%'")
cursor = conn.execute("SELECT ID, NAME, PLATENO, MAKE, MODEL from TESTUSER")
for row in cursor:
    print("ID = ", row[0])
    print("Name = ", row[1])
    print("PlateNo = ", row[2])
    print("Make = ", row[3])
    print("Model = ", row[4])


print("Operation done successfully")
conn.close()

    
    
