import socket
s=None
try:
	s=socket.socket()
	host=socket.gethostname()
	port=8889
	s.bind((host,port))
	s.listen(6)
	print "waiting for the request......"
	co,ci = s.accept()
	co.send("connected successfully")
	data_clinet = co.recv(1024)
	data_clinet = int(data_clinet)
	res  = "EVEN" if data_clinet%2==0 else "ODD"
	co.send(res)

	#co.send("connected")
	#co.send("<html><body><h1>connected</h1></body></html>")

except Exception as err:
	print err
finally:
	if s:
		s.close()
