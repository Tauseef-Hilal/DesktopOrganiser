import os

target = "C:\\Users\\{}\\Desktop\\".format(os.getlogin())

destinations = {
    'main_folder': "C:\\Users\\{}\\Desktop\\Target\\".format(os.getlogin()),
    'log': "C:\\Users\\{}\\Desktop\\Target\\Log\\".format(os.getlogin()),
    'others': "C:\\Users\\{}\\Desktop\\Target\\Others\\".format(os.getlogin()),
    '.mp3': "C:\\Users\\{}\\Music\\",
    '.mp4': "C:\\Users\\{}\\Videos\\",
    '.jpg': "C:\\Users\\{}\\Pictures\\",
    '.png': "C:\\Users\\{}\\Pictures\\",
    '.txt': "C:\\Users\\{}\\Desktop\\Target\\Text-Files\\",
    '.zip': "C:\\Users\\{}\\Desktop\\Target\\Compressed-Files\\",
    '.rar': "C:\\Users\\{}\\Desktop\\Target\\Compressed-Files\\",
    '.exe': "C:\\Users\\{}\\Desktop\\Target\\Executables\\",
    '.msi': "C:\\Users\\{}\\Desktop\\Target\\Executables\\",
    '.py': "C:\\Users\\{}\\Desktop\\Target\\Python-Files\\",
}
