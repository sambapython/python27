import logging
logging.basicConfig(filename="log1.txt",format="%(asctime)s->%(levelname)s->%(message)s,",
	level=logging.DEBUG)
logging.info("information")
logging.debug("debug information")
logging.warn("warning information")
logging.error("error information")
logging.exception("Exception information")
