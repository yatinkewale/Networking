from socket import *
serverPort = 12111
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('127.0.0.1',serverPort))
serverSocket.listen(1)
print ('The server is ready')
connectionSocket, a = serverSocket.accept()
print('Received connection from',a)

while True:
	x = connectionSocket.recv(512).decode('utf-8')
	y = connectionSocket.recv(512).decode('utf-8')
	g=(x+'-'+y)
	c=eval(g)
	z=str(c)
	b=bytes("\nSubtraction is "+z+"\n","ascii")
	connectionSocket.send(b)

