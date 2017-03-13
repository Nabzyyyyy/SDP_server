from socket import *
import datetime
import json
import sqlite3

def recv_data():
        data = conn.recv(1024)
        #print("Received: ", repr(data))
        reply = "Received data"
        reply_enc = str.encode(reply)
        type(reply_enc)
        conn.sendall(reply_enc)
        return data

def log_data(logEntry):
        if (logEntry): #put in while loop for testing until broken pipe is fixed?
                conn = sqlite3.connect('testDB.db')
                #save plate to iterate SQLite tablef or user's ID 
                plate = logEntry[1]
                #print(plate)
                cursor = conn.execute("SELECT ID FROM TESTUSER WHERE PLATENO=?", (plate,))
                userid = 0
                #create user id var and assign it to the ID found
                for row in cursor:
                        userid = int(row[0])

                print("Opened database successfully")
                #create object for logEntry including ID to insert into SQLite testlog table
                logEntryID = [userid, logEntry[0], logEntry[1], logEntry[2]]
                
                conn.execute("INSERT INTO TESTLOG (USERID,TIME,PLATENO,ACCESS) \
                    VALUES (?, ?, ?, ?)", logEntryID);

                conn.commit()
                print("Log added successfully")
                #conn.close()


HOST = ''
PORT= 8000
s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print('Connected by: ', addr)

try:
        while True:
                raw = recv_data()
                val = raw.decode()
                if len(val) != 0:
                        logEntry = json.loads(val)
                        print("Log Time: ", logEntry[0])
                        print("PlateNo : ", logEntry[1])
                        print("Entry   : ", logEntry[2])
                        log_data(logEntry)

except socket.error:
        print("Socket error")
        conn.close()
        
except IOError:
        if e.errno == errno.EPIPE:
                print("Connection closed")
                conn.close()
        else:
                print("Error Error Error Error")
                conn.close()

#while True:
        #data = conn.recv(1024)
        #print("Received: ", repr(data))
        #reply = "Received data"
        #reply_enc = str.encode(reply)
        #type(reply_enc)
        #conn.sendall(reply_enc)

conn.close()
