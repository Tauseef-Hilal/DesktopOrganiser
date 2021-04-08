import os
import logging
from logging.handlers import RotatingFileHandler
from datetime import date

path = "C:\\Users\\{}\\Desktop\\Target\\".format(os.getlogin())
if not os.path.isdir(path):
    os.mkdir(path)
if not os.path.isdir(path + "Log\\"):
    os.mkdir(path + "Log\\")

logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
handler = RotatingFileHandler(path + f"Log\\{date.today()}.log")
logger.addHandler(handler)

logger.setLevel(logging.INFO)
handler.setFormatter(formatter)
