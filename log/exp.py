import logging
import mod1

logging.basicConfig(filename="log2.txt",format="%(asctime)s->%(levelname)s->%(message)s,",
	level=logging.DEBUG)
print mod1.fun()
logging.info("------ program started...............")
a=raw_input("Enter a value:")
b=raw_input("Enter b value:")
if not a.isdigit() or not b.isdigit():
	logging.warn("got the alphanumeric values may raise an exception")
try:
	a=int(a)
	b=int(b)
	result = a/b
	logging.debug("result={0}".format(result))
except Exception as err:
	logging.exception("{0}".format(err))


