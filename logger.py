import logging
from datetime import datetime

class Logger:
    def __init__(self):
        logging.basicConfig(filename='phonebook.log', level=logging.INFO)

    def log(self, message):
        logging.info(f"{datetime.now()}: {message}")
