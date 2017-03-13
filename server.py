from socket import *
import datetime
import json
import sqlite3

def recv_data(conn):
        raw = conn.recv(2048)
        return raw.decode() 
        #data = conn.recv(1024)
        ##print("Received: ", repr(data))
        #reply = "Received data"
        #reply_enc = str.encode(reply)
        #type(reply_enc)
        #conn.sendall(reply_enc)
        #return data

def receive(conn):
        while True:
                request = recv_data(conn)
                if len(request) == 0:
                        continue
                message = 'Received data'
                bytes = str.encode(message)
                conn.sendall(bytes)
                data = json.loads(request)
                
                if 'log' in data:
                        log_data(data['log'])

                if 'end' in data and data['end'] == True:
                        return


def log_data(logEntry):
        if (logEntry): #put in while loop for testing until broken pipe is fixed?
                conn = sqlite3.connect('testDB.db')
                #save plate to iterate SQLite tablef or user's ID 
                plate = logEntry['plate']
                #print(plate)
                cursor = conn.execute("SELECT ID FROM TESTUSER WHERE PLATENO=?", (plate,))
                userid = 0
                #create user id var and assign it to the ID found
                for row in cursor:
                        userid = int(row[0])
                
                #create object for logEntry including ID to insert into SQLite testlog table
                logEntryID = [userid, logEntry['timestamp'], logEntry['plate'], logEntry['access']]
                
                cursor = conn.execute("INSERT INTO TESTLOG (USERID,TIME,PLATENO,ACCESS) \
                    VALUES (?, ?, ?, ?)", logEntryID);

                conn.commit()
                print("Log added successfully: ")
                print(cursor.rowcount)
                
def listen():
        s.listen(1)
        conn, addr = s.accept()

        try:
                receive(conn)
                #receive(conn)

        except:
                print("Exception Error")
                raise
                

# default host is the ip address
HOST = ''

# Uses a port that's not in use
PORT= 8000

# create socket
s = socket(AF_INET, SOCK_STREAM)

# allows reuse of a socket in case of crash close from previous run
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

#binds to hose and port
s.bind((HOST, PORT))

while True:
        listen()

conn.close()
