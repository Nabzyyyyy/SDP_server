import sqlite3

conn = sqlite3.connect('testDB.db')
print("Opened database successfully")

conn.execute("DELETE FROM TESTLOG")
conn.commit()

print("Cleared log table successfully")
conn.close()
