import logging

logging.basicConfig(
    level=logging.INFO,
    format="[ %(asctime)s ]  [%(levelname)s] %(message)s",
    datefmt="%y-%m-%d %H:%M:%S",
    filename="parsed_log.log"
)


try:
    file_path = "Z:/Python/day5/data.txt"
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
    logging.info("File has been read successfully")

except FileNotFoundError:
    logging.error("error during file parsing")
