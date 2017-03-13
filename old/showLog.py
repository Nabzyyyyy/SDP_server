import sqlite3

conn = sqlite3.connect('testDB.db')
print("Opened database successfully")

#conn.execute("UPDATE TESTUSER SET PLATENO = 'EDK6023' WHERE NAME = 'Nabil' AND MAKE LIKE '%honda%'")
cursor = conn.execute("SELECT USERID, TIME, PLATENO, ACCESS from TESTLOG")
for row in cursor:
    print("\nUSERID  = ", row[0])
    print("TIME    = ", row[1])
    print("PLATENO = ", row[2])
    print("ACCESS  = ", row[3])
    print()
    
print("Operation done successfully")
conn.close()
