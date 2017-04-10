a=10
b=20
c=30
print a,b,c
def fun(a1,b1):
	print a1
	print b1
	return a1+b1
for i in range(3):
	print i+c
res = fun(a,b)
print "program ended"