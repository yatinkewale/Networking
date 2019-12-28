
from socket import *
serverName = '127.0.0.1'
serverPort = 12111
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
while True:
	a=input('Enter first number = ')
	clientSocket.send(a.encode('utf-8'))
	b=input('Enter second number = ')
	clientSocket.send(b.encode('utf-8'))
	answer = clientSocket.recv(512).decode('utf-8')
	print (answer)

