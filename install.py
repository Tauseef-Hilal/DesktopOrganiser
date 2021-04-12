from os import system

try:
    with open('Requirements.txt') as _file:
        print("Installing...")
        print(_file.read())
        system('python -m pip install -r Requirements.txt')
except FileNotFoundError:
    print("Installing...")
    system('python -m pip install watchdog==2.0.2')
finally:
    print("Installation Successful!")
    input("Press a key to exit...")
