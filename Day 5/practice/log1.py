import logging

logging.basicConfig(
    level=logging.INFO,
    format="[ %(asctime)s ]  [%(levelname)s] %(message)s",
    datefmt="%y-%m-%d %H:%M:%S",
    filename="basic.log"
)
logging.debug("this is a debug message")
logging.info("this is a info message")
logging.warning("this is a warning message")
logging.error("this is a error message")
logging.critical("this is a critical message")
