import sqlite3

conn = sqlite3.connect('testDB.db')
print("opened Database successfully")

tables = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='TESTUSER'")
if tables == NULL:
    conn.execute('''CREATE TABLE TESTUSER
            (ID INT PRIMARY KEY     NOT NULL,
            NAME            TEXT    NOT NULL,
            PLATENO         TEXT    NOT NULL,
            MAKE            TEXT    NOT NULL,
            MODEL           TEXT    NOT NULL);''')
    
    print ("Users table created successfully")

tables = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='TESTLOG'")
if tables == NULL:
    conn.execute('''CREATE TABLE TESTLOG
            (USERID                 KEY     NOT NULL,
            TIME                    TEXT    NOT NULL,
            PLATENO                 TEXT    NOT NULL,
            ACCESS                  BIT     NOT NULL);''')

#    conn.execute('''CREATE TABLE TESTLOG
#            (USERID INT PRIMARY     KEY     NOT NULL,
#            TIME                    TEXT    NOT NULL,
#            PLATENO                 TEXT    NOT NULL,
#            ACCESS                  BIT     NOT NULL);''')

    print("Log table created successfully")

conn.close()

