import sqlite3

conn = sqlite3.connect('testDB.db')
print("opened Database successfully")

tables = conn.execute("DROP TABLE TESTLOG")

conn.close()
