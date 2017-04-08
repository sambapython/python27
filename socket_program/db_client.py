import socket
s=None
try:
	s=socket.socket()
	#print s.connect(("www.google.com",80))
	#print s.connect(("www.google.com",800))
	host=socket.gethostname()
	port=8889
	s.connect((host,port))
	ack =  s.recv(1024)
	print ack
	a=raw_input("Enter customerid: ")
	s.send(a)
	resp = s.recv(1024)
	print "respnse from the client: ", resp
except Exception as err:
	print err
finally:
	if s:
		s.close()
