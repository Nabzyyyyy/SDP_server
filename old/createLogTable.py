import sqlite3

conn = sqlite3.connect('testDB.db')
print("opened Database successfully")

tables = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='TESTLOG'")
conn.execute('''CREATE TABLE TESTLOG
            (USERID                 KEY     NOT NULL,
            TIME                    TEXT    NOT NULL,
            PLATENO                 TEXT    NOT NULL,
            ACCESS                  BIT     NOT NULL);''')

print("Added log table successfully")
