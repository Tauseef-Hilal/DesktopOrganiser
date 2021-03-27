"""
    Automatic desktop cleaner

    Automatically cleans your desktop by
    moving the files to a folder
"""

import os
import time

from events import event_handler, observer
import extensions

observer.schedule(event_handler, extensions.target, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()

observer.join()
