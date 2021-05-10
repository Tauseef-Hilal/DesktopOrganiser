from os import rename, listdir, mkdir
from os.path import join, isfile, splitext, exists, basename
import time

try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
    from organiser.extensions import destinations
    from organiser import log
except ModuleNotFoundError:
    print("[Error] The program has unmet dependencies:")
    print("Depends on:")
    print("==========================================")

    try:
        with open('Requirements.txt') as _file:
            print(_file.read())
        print("==========================================")
        print("Please run install.py first")
    except FileNotFoundError:
        print("[Error] Requirements.txt not found")
        print("Please run install.py first")
    finally:
        time.sleep(2)
        exit()


class My_Handler(FileSystemEventHandler):

    def on_modified(self, event):

        for _file in listdir(log.desktop):
            i = 0
            path = join(log.desktop, _file)

            if _file != "Target":
                file_ext = splitext(path)[1]
                others_dir = destinations['others']

                if file_ext not in destinations.keys():
                    new_dir = file_ext[1:].title() + "-Files"
                    destinations[file_ext] = join(others_dir, new_dir)

                folder_destination = destinations[file_ext]
                folder_destination = folder_destination

                try:
                    while isfile(join(folder_destination, _file)):
                        i += 1
                        _file = splitext(path)[0] \
                            + '-' + str(i) + \
                            splitext(path)[1]
                        _file = basename(_file)

                    new_path = join(folder_destination, _file)

                    rename(path, new_path)

                    log.logger.info(path + ' --> ' + new_path + '\n')

                except FileNotFoundError:
                    if not exists(others_dir):
                        mkdir(others_dir)
                    if not exists(folder_destination):
                        mkdir(folder_destination)
                except:
                    pass


event_handler = My_Handler()
observer = Observer()
