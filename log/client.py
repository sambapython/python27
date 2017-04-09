import socket
s=None
try:
	s=socket.socket()
	print s.connect(("www.google.com",80))
except Exception as err:
	print err
finally:
	if s:
		s.close()
