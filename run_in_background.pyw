"""
    Automatic desktop cleaner

    Automatically cleans your desktop by
    moving the files to a folder
"""

import time

from events import event_handler, observer
import extensions

if __name__ == '__main__':
    observer.schedule(event_handler, extensions.target, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
