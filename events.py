import os
import time
from datetime import date

import extensions

try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
except ModuleNotFoundError:
    print("[Error] The program has unmet dependencies:")
    print("Depends on:")
    print("==========================================")

    try:
        with open('Requirements.txt') as _file:
            print(_file.read())
        print("==========================================")
        print("Please run install.py first")
        time.sleep(2)
        exit()
    except FileNotFoundError:
        print("[Error] Requirements.txt not found")
        print("Please run install.py first")
        time.sleep(2)
        exit()
    time.sleep(2)
    exit()

class My_Handler(FileSystemEventHandler):

    def on_modified(self, event):

        for _file in os.listdir(extensions.target):
            i = 0
            path = extensions.target + _file

            if _file != "Target":
                file_ext = os.path.splitext(path)[1]

                if file_ext not in extensions.destinations.keys():
                    file_ext = "others"

                folder_destination = extensions.destinations[file_ext]
                folder_destination = folder_destination.format(os.getlogin())

                try:
                    while os.path.isfile(folder_destination + _file):
                        i += 1
                        _file = os.path.splitext(path)[0] \
                                + str(i) + \
                                os.path.splitext(path)[1]
                        _file = _file.split('\\')[4]
                    
                    new_path = folder_destination + _file
                    log_dir = extensions.destinations['log']
                    log_file = log_dir + str(date.today()) + '.txt'

                    os.rename(path, new_path)

                    with open(log_file, 'a') as log:
                        log.write(path + ' --> ' + new_path + '\n')

                except FileNotFoundError:
                    main = extensions.destinations['main_folder']
                    if not os.path.isdir(main):
                        os.mkdir(main)
                    if not os.path.isdir(log_dir):
                        os.mkdir(log_dir)
                    if not os.path.isfile(log_file):
                        with open(log_file, 'w') as log:
                            pass
                    if not os.path.isdir(folder_destination):
                        os.mkdir(folder_destination)
                except:
                    pass



event_handler = My_Handler()
observer = Observer()
