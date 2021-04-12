from os.path import join
from os import name
from log import usr_dir, target

destinations = {
    'others': join(target, "Others"),
    '.mp3': join(usr_dir, "Music"),
    '.mp4': join(usr_dir, "Videos") if name == "nt" else "Movies",
    '.jpg': join(usr_dir, "Pictures"),
    '.png': join(usr_dir, "Pictures"),
    '.txt': join(target, "TextFiles"),
    '.zip': join(target, "CompressedFiles"),
    '.rar': join(target, "CompressedFiles"),
    '.exe': join(target, "Executables"),
    '.msi': join(target, "Executables"),
    '.py': join(target, "PythonFiles")
}
