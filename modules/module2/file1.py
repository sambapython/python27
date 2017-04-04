print "file1"
def fun():
	return "this is fun in file1.py modified"
def fun1():
	return "this is fun1 in file1.py modified"

if __name__ == "__main__":
	print "program started"
	print "__name__",__name__
	print fun()
	print fun1()
	print "program ended"