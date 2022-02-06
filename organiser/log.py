import os
import getpass
import logging
from logging.handlers import RotatingFileHandler
from datetime import date

usr_dir = os.path.join(os.getcwd().split(os.getlogin())[0], os.getlogin())
desktop = os.path.join(usr_dir, "Desktop")
target = os.path.join(desktop, "Target")
log_folder = os.path.join(target, "Log")
print(usr_dir)
if not os.path.isdir(target):
    os.mkdir(target)
if not os.path.isdir(log_folder):
    os.mkdir(log_folder)

logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
handler = RotatingFileHandler(os.path.join(log_folder, f"{date.today()}.log"))
logger.addHandler(handler)
logger.setLevel(logging.INFO)
handler.setFormatter(formatter)
