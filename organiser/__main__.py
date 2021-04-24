"""
    Automatic desktop cleaner

    Automatically cleans your desktop by
    moving the files to a folder
"""

import time

from organiser.events import event_handler, observer
from organiser import log


def main():
    """Start of the program"""

    observer.schedule(event_handler, log.desktop, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()


if __name__ == '__main__':
    main()
