import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger("lucifer11 logger")
logger.setLevel(logging.DEBUG)

handler = logging.FileHandler("mylog.log")
handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(levelname)s - %(asctime)s: %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)

logger.debug("this is a debug message!")
logger.info("this is important information!")