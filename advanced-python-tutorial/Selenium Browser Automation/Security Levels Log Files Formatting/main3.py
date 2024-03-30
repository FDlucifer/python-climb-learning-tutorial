import logging
import datetime as dt

today = dt.datetime.today()
filename = f"{today.month:02d}-{today.day:02d}-{today.year}.log"

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("lucilogger")

file_handler = logging.FileHandler(filename)
file_handler.setLevel(logging.WARNING)
formatter = logging.Formatter("%(asctime)s: %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

logger.debug("hey i am debug")
logger.info("hey i am info")
logger.warning("hey i am warning")
logger.error("hey i am error")
logger.critical("hey i am critical")