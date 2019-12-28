#!/usr/bin/python
import sys
import socket
import os


ip1=sys.argv[1]
ip2=sys.argv[2]

print('IP address =',ip1)
try:
	socket.inet_aton(ip1)
	try:
		adress1=socket.gethostbyaddr(ip1)
		adress1=adress1[0]
		print('Hostname = ',adress1)
	except socket.herror:
		print('Exception raised')
		pass
except socket.error:
	print('Exception raised')

	

print('IP address =',ip2)
try:
	socket.inet_aton(ip2)
	response =os.system("ping -c 1 " + ip2 +">/dev/null")
	if response == 0:
		print ('Status = Up')
	else:
		print ('Status = Down')
except socket.error:
	print('Exception raised')

