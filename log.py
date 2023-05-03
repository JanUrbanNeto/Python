import logging

LOG_FORMAT = "%(levelname)s, %(asctime)s - %(message)s"

logging.basicConfig(filename="teste.log", level=logging.DEBUG, filemode="w", format=LOG_FORMAT)

log = logging.getLogger()
log.info("info level")
log.debug("debug level")
log.warning("warning level")
log.error("error level")
log.critical("critical level")
log.level