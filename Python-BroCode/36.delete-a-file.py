import os
import shutil

path = "empty_folder"

try:
    shutil.rmtree(path)
    # os.remove(path)
    # os.rmdir(path)
except FileNotFoundError:
    print("This file was not found")
except PermissionError:
    print("You do not have permission to delete that")
else:
    print(path+" was delete")