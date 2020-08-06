import logging

logging.basicConfig(filename="mylog.log", level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
#logging.disable(logging.CRITICAL) #DEBUG, INFO, WARNING, ERROR, CRITICAL

logging.debug("Start of program")
#logging.info, logging.warning, logging.error, logging.critical

def factorial(n):
    logging.debug("Start of factorial(%s)" % (n))
    total = 1
    for i in range(1,n+1):
        total *= i
        logging.debug("count is %s, total is %s" % (i, total))

    logging.debug("return is %s" % (total))
    return total

print(factorial(5))
logging.debug("End of program")
