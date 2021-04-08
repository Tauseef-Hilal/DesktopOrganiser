import os
import time

try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
    import extensions
    import log
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

        for _file in os.listdir(extensions.target):
            i = 0
            path = extensions.target + _file

            if _file != "Target":
                file_ext = os.path.splitext(path)[1]
                others_dir = extensions.destinations['others']

                if file_ext not in extensions.destinations.keys():
                    new_dir =  file_ext[1:].title() + '-Files\\'
                    extensions.destinations[file_ext] = others_dir + new_dir

                folder_destination = extensions.destinations[file_ext]
                folder_destination = folder_destination.format(os.getlogin())

                try:
                    while os.path.isfile(folder_destination + _file):
                        i += 1
                        _file = os.path.splitext(path)[0] \
                                + '-' + str(i) + \
                                os.path.splitext(path)[1]
                        _file = _file.split('\\')[4]
                    
                    new_path = folder_destination + _file

                    os.rename(path, new_path)

                    log.logger.info(path + ' --> ' + new_path + '\n')

                except FileNotFoundError:
                    if not os.path.isdir(others_dir):
                        os.mkdir(others_dir)
                    if not os.path.isdir(folder_destination):
                        os.mkdir(folder_destination)
                except:
                    pass


event_handler = My_Handler()
observer = Observer()
