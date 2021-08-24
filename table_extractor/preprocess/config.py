import logging
import os
import sys
from pathlib import Path

LOGGING_FORMAT = "[%(asctime)s] - [%(name)s] - [%(levelname)s] - %(message)s"
LOGGING_LEVEL = logging.INFO


def config_logger():
    formatter = logging.Formatter(fmt=LOGGING_FORMAT, datefmt='%d-%m-%Y %H:%M:%S')
    logging.root.setLevel(LOGGING_LEVEL)

    console_handler = logging.StreamHandler(stream=sys.stdout)
    console_handler.setFormatter(formatter)
    logging.root.addHandler(console_handler)

    if log_filename := os.environ.get("PREPROCESSING_LOG_FILE_PATH"):
        file_handler = logging.FileHandler(Path(log_filename).absolute())
        logging.root.addHandler(file_handler)
    else:
        logging.warning("A log file doesn't define")

