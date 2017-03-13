from socket import *

HOST = '192.168.43.42'
PORT =  8000
s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT)) #connects to a host
while True:
	message = input("Your Message: ")
	bytes = str.encode(message)
	type(bytes)
	s.send(bytes)
	print("Awaiting reply: ")
	reply = s.recv(1024)
	print("Received: ", repr(reply))
s.close()
