from socket import *
serverName = 'localhost'
serverPort = 8888
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
income = clientSocket.recv(1024).decode('utf-8')
print(income)
himsg=('HELLO kewale.y\n')
clientSocket.send(himsg.encode('utf-8'))

while True:
	query = clientSocket.recv(1024).decode('utf-8')
	c=query[0:4]
	print (query)
	if c=='DONE':
		break
	z=query.lstrip('MATH ')
	y=z[:-1]
	d=eval(y)
	x=int(d)
	e=str(x)
	a=('ANSWER '+e+'\n')
	print(a)
	clientSocket.send(a.encode('utf-8'))
clientSocket.close()
		

