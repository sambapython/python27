import logging
def fun():
	logging.info("function started")
	result=20
	logging.warn("warniog message")
	logging.debug("result:{0}".format(result))
	return result